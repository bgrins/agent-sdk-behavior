# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "claude-agent-sdk>=0.2.128",
#     "openai-codex>=0.144.4",
# ]
# ///
"""Run a models x harnesses grid and report surfaced thinking + output.

Each cell drives one model through one agent harness (the Codex SDK or the
Claude Agent SDK) via OpenRouter, with every SDK request relayed through a
local logging proxy. Cells land under
results/<model>/<harness>-v<sdk>/run-N/ (cell.md + wire.md); reruns retry
only failed or empty cells. Both harnesses run isolated from user config
(fresh CODEX_HOME / CLAUDE_CONFIG_DIR).

Usage:
  uv run run_grid.py --models stealth/ox-alpha,z-ai/glm-5.2:free
  uv run run_grid.py --legs codex --repeats 3 --force
"""

import argparse
import asyncio
import datetime
import hashlib
import http.server
import importlib.metadata
import json
import os
import re
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

OPENROUTER_HOST = "https://openrouter.ai"
INSTRUCTIONS = (
    "You are a security code reviewer. Reason carefully before answering."
)
DEFAULT_PROMPT = Path(__file__).parent / "prompts" / "default.md"

SETTINGS_KEYS = (
    "model",
    "temperature",
    "top_p",
    "top_k",
    "max_tokens",
    "max_output_tokens",
    "max_completion_tokens",
    "reasoning",
    "reasoning_effort",
    "thinking",
    "output_config",
    "stream",
    "parallel_tool_calls",
    "include",
    "store",
)


def settings_of(body: dict) -> dict:
    settings = {k: body[k] for k in SETTINGS_KEYS if k in body}
    settings["tools_count"] = len(body.get("tools") or [])
    sys_field = body.get("system") or body.get("instructions") or ""
    settings["system_chars"] = len(json.dumps(sys_field))
    return settings


def start_wire_relay(log_path: Path, captured: list[dict]) -> str:
    """Local proxy to OpenRouter logging every request to *log_path*."""

    class Relay(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            raw = self.rfile.read(int(self.headers.get("content-length", 0)))
            try:
                body = json.loads(raw)
            except json.JSONDecodeError:
                body = {"_raw": raw.decode(errors="replace")[:2000]}
            headers = {
                k: ("<redacted>" if k.lower() in ("authorization", "x-api-key") else v)
                for k, v in self.headers.items()
            }
            entry = settings_of(body)

            fwd = {
                k: v
                for k, v in self.headers.items()
                if k.lower() not in ("host", "content-length", "accept-encoding")
            }
            fwd["content-length"] = str(len(raw))
            # Retry free-tier load shedding so a blip doesn't read as a
            # harness difference.
            started = time.monotonic()
            resp_headers: dict = {}
            for attempt in range(4):
                req = urllib.request.Request(
                    f"{OPENROUTER_HOST}{self.path}", data=raw, headers=fwd
                )
                try:
                    resp = urllib.request.urlopen(req, timeout=300)
                    status, payload, resp_headers = (
                        resp.status, resp.read(), resp.headers)
                except urllib.error.HTTPError as err:
                    status, payload, resp_headers = err.code, err.read(), err.headers
                except Exception as err:  # connection-level: never hang the SDK
                    status = 502
                    payload = json.dumps(
                        {"error": {"message": f"relay transport error: {err!r}"}}
                    ).encode()
                    resp_headers = {"content-type": "application/json"}
                if status not in (429, 502, 503) or attempt == 3:
                    break
                delay = min(float(dict(resp_headers).get("Retry-After") or 5), 15)
                print(f"    [relay] HTTP {status}, retrying in {delay:.0f}s")
                time.sleep(delay)
            entry["response_status"] = status
            captured.append(entry)
            print(f"    [relay] {self.path} -> {status}"
                  f" ({time.monotonic() - started:.0f}s, {len(payload)}b)")
            with log_path.open("a") as fh:
                fh.write(f"## POST {self.path}\n\n")
                fh.write(f"settings: `{json.dumps(entry)}`\n\n")
                fh.write("<details><summary>request headers (auth redacted)"
                         "</summary>\n\n```json\n")
                fh.write(json.dumps(headers, indent=2))
                fh.write("\n```\n</details>\n\nrequest body:\n\n```json\n")
                fh.write(json.dumps(body, indent=2))
                fh.write(f"\n```\n\n<details><summary>response: HTTP {status}"
                         f" ({len(payload)} bytes)</summary>\n\n```\n")
                fh.write(payload.decode(errors="replace"))
                fh.write("\n```\n</details>\n\n")
            self.send_response(status)
            for k, v in dict(resp_headers).items():
                if k.lower() not in (
                    "transfer-encoding",
                    "content-length",
                    "content-encoding",
                ):
                    self.send_header(k, v)
            self.send_header("content-length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, *args):
            pass

    relay = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Relay)
    threading.Thread(target=relay.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{relay.server_port}"


async def claude_leg(model: str, prompt: str, relay: str) -> list[tuple[str, str]]:
    from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, query

    out: list[tuple[str, str]] = []
    options = ClaudeAgentOptions(
        model=model,
        system_prompt=INSTRUCTIONS,
        effort="high",
        max_turns=1,
        allowed_tools=[],
        # The default (None) loads the operator's CLAUDE.md and skills, which
        # the codex leg never sees. Checked by ablation/probe_isolation.py.
        setting_sources=[],
        skills=[],
        env={
            "ANTHROPIC_BASE_URL": f"{relay}/api",
            "ANTHROPIC_API_KEY": os.environ["OPENROUTER_API_KEY"],
            "CLAUDE_CONFIG_DIR": tempfile.mkdtemp(prefix="grid-claude-"),
        },
    )
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                kind = type(block).__name__
                text = getattr(block, "thinking", None) or getattr(block, "text", "")
                out.append(("thinking" if kind == "ThinkingBlock" else "output", text))
    return out


async def codex_leg(model: str, prompt: str, relay: str) -> list[tuple[str, str]]:
    from openai_codex import ApprovalMode, AsyncCodex, CodexConfig, Sandbox

    os.environ["CODEX_HOME"] = tempfile.mkdtemp(prefix="grid-codex-")
    overrides = [
        'model_provider="openrouter"',
        'model_providers.openrouter.name="OpenRouter"',
        f'model_providers.openrouter.base_url="{relay}/api/v1"',
        'model_providers.openrouter.wire_api="responses"',
        'model_providers.openrouter.env_key="OPENROUTER_API_KEY"',
        "model_providers.openrouter.requires_openai_auth=false",
        'web_search="disabled"',
    ]
    out: list[tuple[str, str]] = []
    async with AsyncCodex(config=CodexConfig(config_overrides=overrides)) as codex:
        thread = await codex.thread_start(
            model=model,
            developer_instructions=INSTRUCTIONS,
            approval_mode=ApprovalMode.deny_all,
            sandbox=Sandbox("read-only"),
        )
        turn = await thread.turn(prompt, effort="high")
        async for notif in turn.stream():
            if (getattr(notif, "method", "") or "") != "item/completed":
                continue
            item = getattr(getattr(notif, "payload", None), "item", None)
            root = getattr(item, "root", item)
            kind = getattr(root, "type", type(root).__name__)
            if kind == "userMessage":
                continue
            text = (
                getattr(root, "text", None)
                or getattr(root, "reasoning", None)
                or getattr(root, "summary", None)
                or repr(root)[:800]
            )
            if kind == "reasoning":
                content = getattr(root, "content", None)
                if content:
                    text = "\n".join(str(c) for c in content)
            out.append(("thinking" if kind == "reasoning" else "output", str(text)))
    return out


LEGS = {"codex": codex_leg, "claude": claude_leg}
LEG_PACKAGES = {"codex": "openai-codex", "claude": "claude-agent-sdk"}
LEG_TIMEOUT_SECONDS = 900


def leg_version(leg: str) -> str:
    return importlib.metadata.version(LEG_PACKAGES[leg])


def slug(model: str) -> str:
    return re.sub(r"[^a-z0-9.-]+", "-", model.lower())


def write_cell(cell_dir: Path, model: str, leg: str, prompt_name: str,
               prompt_hash: str, blocks: list[tuple[str, str]],
               wire: list[dict], error: str | None) -> None:
    stamp = datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds")
    lines = [
        f"# {model} / {leg} (SDK {leg_version(leg)})",
        "",
        f"run: {stamp} · prompt: `{prompt_name}` (sha256 {prompt_hash})",
        "",
    ]
    if error:
        lines += ["**LEG FAILED:**", "", "```", error, "```", ""]
    # One line per unique request shape: harness retries and side requests
    # (e.g. the claude CLI's title generation) collapse into counts.
    shapes: dict[str, list] = {}
    for request in wire:
        status = request.get("response_status")
        shape = json.dumps(
            {k: v for k, v in request.items() if k != "response_status"}
        )
        shapes.setdefault(shape, []).append(status)
    for shape, statuses in shapes.items():
        note = f" (x{len(statuses)}, statuses {statuses})" if (
            len(statuses) > 1 or any(st and st >= 400 for st in statuses)
        ) else ""
        lines += [f"wire settings{note}: `{shape}`", ""]
    for kind, text in blocks:
        lines += [f"## {kind}", "", text.strip(), ""]
    if not blocks and not error:
        lines += ["(no thinking or output surfaced; see wire.md)", ""]
    lines += ["Full over-the-wire log: [wire.md](wire.md)", ""]
    (cell_dir / "cell.md").write_text("\n".join(lines))


def cell_succeeded(cell_dir: Path) -> bool:
    """A cell counts as done when it produced blocks and did not fail.

    Failed, empty, or missing cells rerun on the next invocation, so
    "rerun the failures" is just running the same command again.
    """
    cell_md = cell_dir / "cell.md"
    if not cell_md.exists():
        return False
    text = cell_md.read_text()
    return "**LEG FAILED:**" not in text and "\n## " in text


def load_dotenv() -> None:
    """Load OPENROUTER_API_KEY from a .env beside this script if unset."""
    env_file = Path(__file__).parent / ".env"
    if "OPENROUTER_API_KEY" in os.environ or not env_file.exists():
        return
    for line in env_file.read_text().splitlines():
        key, _, value = line.partition("=")
        if key.strip() == "OPENROUTER_API_KEY" and value:
            os.environ[key.strip()] = value.strip()


async def main() -> None:
    load_dotenv()
    if "OPENROUTER_API_KEY" not in os.environ:
        raise SystemExit("set OPENROUTER_API_KEY (env or .env beside run_grid.py)")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--models", default="stealth/ox-alpha",
                        help="comma-separated OpenRouter model ids")
    parser.add_argument("--legs", default="codex,claude",
                        help="comma-separated subset of: codex,claude")
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT,
                        help="path to the user prompt")
    parser.add_argument("--repeats", type=int, default=3,
                        help="runs per model x harness cell")
    parser.add_argument("--force", action="store_true",
                        help="rerun cells that already succeeded")
    parser.add_argument("--results-root", type=Path,
                        default=Path(__file__).parent / "results",
                        help="results tree root (cells accumulate per"
                             " model/harness-version)")
    args = parser.parse_args()

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    legs = [leg.strip() for leg in args.legs.split(",") if leg.strip()]
    prompt = args.prompt.read_text()
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()[:12]
    results_root = args.results_root
    results_root.mkdir(parents=True, exist_ok=True)

    for model in models:
        for leg in legs:
            for n in range(1, args.repeats + 1):
                cell_dir = (results_root / slug(model)
                            / f"{leg}-v{leg_version(leg)}" / f"run-{n}")
                if not args.force and cell_succeeded(cell_dir):
                    print(f"=== {model} / {leg} run-{n}: already succeeded"
                          " (skip; --force to rerun)", flush=True)
                    continue
                cell_dir.mkdir(parents=True, exist_ok=True)
                (cell_dir / "wire.md").write_text("")
                print(f"=== {model} / {leg} run-{n}"
                      f" (SDK {leg_version(leg)})", flush=True)
                captured: list[dict] = []
                relay = start_wire_relay(cell_dir / "wire.md", captured)
                blocks, error = [], None
                try:
                    blocks = await asyncio.wait_for(
                        LEGS[leg](model, prompt, relay),
                        timeout=LEG_TIMEOUT_SECONDS,
                    )
                except Exception as err:
                    error = repr(err)
                    print(f"    LEG FAILED: {error}", flush=True)
                write_cell(cell_dir, model, leg, args.prompt.name,
                           prompt_hash, blocks, captured, error)

    build_report(results_root)
    print(f"\nreport: {results_root / 'REPORT.md'}")


def build_report(results_root: Path) -> None:
    """Regenerate REPORT.md by scanning the whole results tree.

    Cells accumulate across runs (keyed model x harness x SDK version); the
    report always reflects everything present, not just the last invocation.
    """
    cells: dict[str, dict[str, dict]] = {}
    columns: set[str] = set()
    for cell_md in sorted(results_root.glob("*/*/run-*/cell.md")):
        run = cell_md.parent.name             # run-N
        column = cell_md.parent.parent.name    # e.g. codex-v0.147.0
        model_dir = cell_md.parent.parent.parent.name
        text = cell_md.read_text()
        title = text.splitlines()[0].lstrip("# ")
        model = title.split(" / ")[0]
        failed = "**LEG FAILED:**" in text
        thinking = re.findall(r"## thinking\n\n(.*?)(?=\n## |\Z)", text, re.S)
        thinking_chars = sum(len(t.strip()) for t in thinking)
        statuses = [int(m) for m in re.findall(r'"response_status": (\d+)', text)]
        bad_http = any(st >= 400 for st in statuses)
        mark = "❌" if failed else ("⚠️" if bad_http or not thinking_chars else "✅")
        excerpt = " ".join(" ".join(thinking).split())[:160]
        settings = re.findall(r"wire settings: `(.*)`", text)
        cells.setdefault(model, {})[f"{column}/{run}"] = {
            "mark": mark,
            "thinking_chars": thinking_chars,
            "excerpt": excerpt,
            "settings": settings,
            "path": f"{model_dir}/{column}/{run}/cell.md",
        }
        columns.add(f"{column}/{run}")
    ordered_columns = sorted(columns)

    report = ["# Agent SDK behavior grid", "",
              "Cells accumulate per model x harness x SDK version; rerunning"
              " a cell refreshes it. Harness isolation: fresh `CODEX_HOME` /"
              " `CLAUDE_CONFIG_DIR` · gateway: OpenRouter · effort high.", "",
              "| model | " + " | ".join(ordered_columns) + " |",
              "|---|" + "---|" * len(ordered_columns)]
    for model in sorted(cells):
        row = [f"`{model}`"]
        for column in ordered_columns:
            cell = cells[model].get(column)
            row.append(
                f"{cell['mark']} [cell]({cell['path']})"
                f" · {cell['thinking_chars']} thinking chars" if cell else ""
            )
        report.append("| " + " | ".join(row) + " |")
    report += ["", "## Thinking excerpts", ""]
    for model in sorted(cells):
        for column in ordered_columns:
            if cell := cells[model].get(column):
                report += [f"**{model} / {column}**: {cell['excerpt'] or '(none)'}", ""]
    report += ["## Wire settings per cell", ""]
    for model in sorted(cells):
        for column in ordered_columns:
            for setting in (cells[model].get(column) or {}).get("settings", []):
                report += [f"- **{model} / {column}**: `{setting}`"]
    report += ["", "Full request/response logs live next to each cell as"
               " `wire.md`; every request body is fenced JSON and can"
               " be replayed with curl against openrouter.ai.", ""]
    (results_root / "REPORT.md").write_text("\n".join(report))


asyncio.run(main())
