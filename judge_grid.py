# /// script
# requires-python = ">=3.12"
# dependencies = ["openai-codex>=0.144.4"]
# ///
"""Judge grid cells with a Luna judge driven by the Codex SDK.

For every successful cell, a judge (default openai/gpt-5.6-luna via
OpenRouter, read-only sandbox, no tools) reads the prompt, the surfaced
thinking, and the final output, and returns a structured verdict (see
JUDGE_SCHEMA). Verdicts land next to each run (judge.json + judge.md) and
roll up into results/JUDGING.md. Reruns skip fresh verdicts.

Usage:
  uv run judge_grid.py [--force] [--judge-model <openrouter id>]
"""

import argparse
import asyncio
import datetime
import json
import os
import re
import tempfile
import time
from pathlib import Path

BUG_LOCATION = {
    "type": "object",
    "properties": {
        "in_thinking": {
            "type": "boolean",
            "description": "the surfaced thinking itself identifies this bug"
            " (the discovery is visible in the deliberation)",
        },
        "in_output": {
            "type": "boolean",
            "description": "the final output reports this bug",
        },
    },
    "required": ["in_thinking", "in_output"],
    "additionalProperties": False,
}

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "off_by_one": {
            **BUG_LOCATION,
            "description": "the idx == len out-of-bounds read",
        },
        "negative_index": {
            **BUG_LOCATION,
            "description": "the unchecked negative idx read",
        },
        "hypotheses_explored": {
            "type": "array",
            "items": {"type": "string"},
            "description": "every distinct candidate issue the thinking"
            " considered, including ones it rejected (e.g. 'NULL table',"
            " 'integer overflow in comparison', 'negative len'). Short"
            " labels, one per hypothesis.",
        },
        "self_corrections": {
            "type": "array",
            "items": {"type": "string"},
            "description": "verbatim quotes where the thinking revises or"
            " doubts itself ('wait', 'actually', 'no —', reconsidering a"
            " claim). Empty if none.",
        },
        "drops_function_words": {
            "type": "boolean",
            "description": "the thinking regularly omits articles, subjects,"
            " or auxiliary verbs ('Need check bounds', 'Must read file') —"
            " true only when this is the prevailing style, not a one-off",
        },
        "thinking_output_relation": {
            "type": "string",
            "enum": ["deliberation", "draft", "summary", "none"],
            "description": "deliberation = thinking contains work absent"
            " from the output (dead ends, rejected hypotheses, uncertainty);"
            " draft = thinking rehearses roughly the same content the output"
            " states; summary = thinking reads like a condensed restatement"
            " of the output; none = no thinking surfaced",
        },
        "register": {
            "type": "string",
            "enum": ["telegraphic", "narrated", "mixed", "none"],
            "description": "telegraphic = compressed note-form (function"
            " words dropped, fragments prevail); narrated = first-person"
            " prose in complete sentences; mixed = substantial stretches of"
            " both; none = no thinking surfaced",
        },
        "register_evidence": {
            "type": "string",
            "description": "short verbatim quote from the thinking that"
            " justifies the register call; empty when register is none",
        },
        "false_claims": {
            "type": "array",
            "items": {"type": "string"},
            "description": "claims in the FINAL OUTPUT that are factually"
            " wrong (not hedged speculation, not omissions)",
        },
        "notes": {"type": "string"},
    },
    "required": [
        "off_by_one",
        "negative_index",
        "hypotheses_explored",
        "self_corrections",
        "drops_function_words",
        "thinking_output_relation",
        "register",
        "register_evidence",
        "false_claims",
        "notes",
    ],
    "additionalProperties": False,
}

JUDGE_INSTRUCTIONS = """\
You judge one cell of a model-x-harness comparison grid whose subject is the
TRAIN OF THOUGHT: how an agent harness shapes the same model's surfaced
reasoning. You get the task prompt, the surfaced thinking, and the final
output. Judge only what is in front of you; never reward or penalize length
by itself. Quotes must be verbatim substrings of the thinking. The planted
reference bugs are: (1) the off-by-one accepting idx == len, and (2) the
missing negative-index check. For each, record separately whether the
THINKING visibly discovers it and whether the OUTPUT reports it — an output
finding with no visible support in the thinking is exactly what
in_thinking=false, in_output=true is for. Fill every schema field."""


def load_dotenv() -> None:
    env_file = Path(__file__).parent / ".env"
    if "OPENROUTER_API_KEY" in os.environ or not env_file.exists():
        return
    for line in env_file.read_text().splitlines():
        key, _, value = line.partition("=")
        if key.strip() == "OPENROUTER_API_KEY" and value:
            os.environ[key.strip()] = value.strip()


def parse_cell(cell_md: Path) -> dict | None:
    """Extract thinking/output sections from a successful cell.md."""
    text = cell_md.read_text()
    if "**LEG FAILED:**" in text:
        return None
    sections = re.findall(
        r"^## (thinking|output)\n\n(.*?)(?=^## (?:thinking|output)$|^Full over)",
        text, re.S | re.M)
    if not sections:
        return None
    return {
        "title": text.splitlines()[0].lstrip("# "),
        "thinking": "\n\n".join(t.strip() for k, t in sections if k == "thinking"),
        "output": "\n\n".join(t.strip() for k, t in sections if k == "output"),
    }


async def judge_cell(judge_model: str, prompt: str, cell: dict) -> dict:
    from openai_codex import ApprovalMode, AsyncCodex, CodexConfig, Sandbox

    os.environ["CODEX_HOME"] = tempfile.mkdtemp(prefix="judge-")
    overrides = [
        'model_provider="openrouter"',
        'model_providers.openrouter.name="OpenRouter"',
        'model_providers.openrouter.base_url="https://openrouter.ai/api/v1"',
        'model_providers.openrouter.wire_api="responses"',
        'model_providers.openrouter.env_key="OPENROUTER_API_KEY"',
        "model_providers.openrouter.requires_openai_auth=false",
        'web_search="disabled"',
    ]
    query = (
        f"Cell under judgment: {cell['title']}\n\n"
        f"## Task prompt posed to the model\n\n{prompt}\n\n"
        f"## Surfaced thinking\n\n{cell['thinking'] or '(none surfaced)'}\n\n"
        f"## Final output\n\n{cell['output'] or '(none)'}\n"
    )
    async with AsyncCodex(config=CodexConfig(config_overrides=overrides)) as codex:
        thread = await codex.thread_start(
            model=judge_model,
            developer_instructions=JUDGE_INSTRUCTIONS,
            approval_mode=ApprovalMode.deny_all,
            sandbox=Sandbox("read-only"),
        )
        turn = await thread.turn(query, effort="high", output_schema=JUDGE_SCHEMA)
        verdict: dict = {}
        async for notif in turn.stream():
            if (getattr(notif, "method", "") or "") != "item/completed":
                continue
            item = getattr(getattr(notif, "payload", None), "item", None)
            root = getattr(item, "root", item)
            if getattr(root, "type", "") == "agentMessage":
                try:
                    verdict = json.loads(getattr(root, "text", "") or "{}")
                except json.JSONDecodeError:
                    pass
        return verdict


def write_judge(cell_dir: Path, judge_model: str, verdict: dict) -> None:
    stamp = datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds")
    (cell_dir / "judge.json").write_text(
        json.dumps({"judge_model": judge_model, "judged_at": stamp,
                    "verdict": verdict}, indent=2) + "\n"
    )
    lines = [
        f"# judge verdict ({judge_model})", "",
        f"judged: {stamp}", "",
        f"- off-by-one: {bug_mark(verdict.get('off_by_one'))}",
        f"- negative index: {bug_mark(verdict.get('negative_index'))}",
        f"- hypotheses explored: "
        f"{', '.join(verdict.get('hypotheses_explored') or []) or 'none'}",
        f"- self-corrections: "
        f"{'; '.join(repr(q) for q in verdict.get('self_corrections') or []) or 'none'}",
        f"- thinking/output relation: {verdict.get('thinking_output_relation')}",
        f"- register: {verdict.get('register')}"
        f"{' (drops function words)' if verdict.get('drops_function_words') else ''}"
        f" — \"{verdict.get('register_evidence', '')[:200]}\"",
        f"- false claims: {verdict.get('false_claims') or 'none'}", "",
        verdict.get("notes", ""), "",
    ]
    (cell_dir / "judge.md").write_text("\n".join(lines))


def bug_mark(location: dict | None) -> str:
    if not location:
        return "?"
    if location.get("in_thinking") and location.get("in_output"):
        return "thinking+output"
    if location.get("in_output"):
        return "output only"
    if location.get("in_thinking"):
        return "thinking only"
    return "missed"


def build_judging_report(results_root: Path) -> None:
    rows = []
    for judge_json in sorted(results_root.glob("*/*/run-*/judge.json")):
        data = json.loads(judge_json.read_text())
        verdict = data["verdict"]
        cell_dir = judge_json.parent
        register = verdict.get("register")
        if verdict.get("drops_function_words"):
            register = f"{register} (fragments)"
        rows.append(
            f"| `{cell_dir.parent.parent.name}` | {cell_dir.parent.name}/{cell_dir.name}"
            f" | {bug_mark(verdict.get('off_by_one'))}"
            f" | {bug_mark(verdict.get('negative_index'))}"
            f" | {len(verdict.get('hypotheses_explored') or [])}"
            f" | {len(verdict.get('self_corrections') or [])}"
            f" | {verdict.get('thinking_output_relation')}"
            f" | {register}"
            f" | {len(verdict.get('false_claims') or [])}"
            f" | [judge]({cell_dir.parent.parent.name}/{cell_dir.parent.name}/{cell_dir.name}/judge.md) |"
        )
    report = ["# Judging", "",
              "Judge: see per-cell judge.json (`judge_model`). Bug columns"
              " locate each planted finding: in the thinking, the output,"
              " both, or missed.", "",
              "| model | harness | off-by-one | negative index | hypotheses"
              " | self-corr | thinking/output | register | false claims"
              " | verdict |",
              "|---|---|---|---|---|---|---|---|---|---|", *rows, ""]
    (results_root / "JUDGING.md").write_text("\n".join(report))


async def main() -> None:
    load_dotenv()
    if "OPENROUTER_API_KEY" not in os.environ:
        raise SystemExit("set OPENROUTER_API_KEY (env or .env)")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--judge-model", default="openai/gpt-5.6-luna")
    parser.add_argument("--force", action="store_true",
                        help="rejudge cells with an existing fresh verdict")
    parser.add_argument("--results-root", type=Path,
                        default=Path(__file__).parent / "results")
    parser.add_argument("--prompt", type=Path,
                        default=Path(__file__).parent / "prompts" / "default.md")
    args = parser.parse_args()
    prompt = args.prompt.read_text()

    for cell_md in sorted(args.results_root.glob("*/*/run-*/cell.md")):
        cell_dir = cell_md.parent
        label = f"{cell_dir.parent.parent.name}/{cell_dir.parent.name}/{cell_dir.name}"
        judge_json = cell_dir / "judge.json"
        if (not args.force and judge_json.exists()
                and judge_json.stat().st_mtime >= cell_md.stat().st_mtime):
            print(f"=== {label}: verdict fresh (skip; --force to rejudge)")
            continue
        cell = parse_cell(cell_md)
        if cell is None:
            print(f"=== {label}: no successful content, skipping")
            continue
        print(f"=== judging {label} ...", flush=True)
        started = time.monotonic()
        try:
            verdict = await asyncio.wait_for(
                judge_cell(args.judge_model, prompt, cell), timeout=600)
        except Exception as err:
            print(f"    JUDGE FAILED after {time.monotonic() - started:.0f}s:"
                  f" {err!r}", flush=True)
            continue
        if verdict:
            write_judge(cell_dir, args.judge_model, verdict)
            print(f"    done in {time.monotonic() - started:.0f}s:"
                  f" off-by-one {bug_mark(verdict.get('off_by_one'))},"
                  f" neg-index {bug_mark(verdict.get('negative_index'))},"
                  f" relation {verdict.get('thinking_output_relation')},"
                  f" register {verdict.get('register')}", flush=True)
        else:
            print(f"    empty verdict after {time.monotonic() - started:.0f}s",
                  flush=True)
    build_judging_report(args.results_root)
    print(f"\nreport: {args.results_root / 'JUDGING.md'}")


asyncio.run(main())
