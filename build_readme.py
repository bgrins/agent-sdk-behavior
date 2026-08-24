# /// script
# requires-python = ">=3.12"
# ///
"""Inject the current results into README.md.

Reads every cell.md and judge.json under results/ and rewrites the
per-model comparison table between the results markers in README.md:

  uv run build_readme.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
START = "<!-- results:start -->"
END = "<!-- results:end -->"


def bug_mark(location: dict | None) -> str:
    if not location:
        return "?"
    marks = {
        (True, True): "thinking+output",
        (False, True): "output only",
        (True, False): "thinking only",
        (False, False): "missed",
    }
    return marks[bool(location.get("in_thinking")), bool(location.get("in_output"))]


def cell_row(cell_md: Path) -> dict:
    text = cell_md.read_text()
    cell_dir = cell_md.parent
    sections = re.findall(
        r"^## (thinking|output)\n\n(.*?)(?=^## (?:thinking|output)$|^Full over)",
        text, re.S | re.M)
    title = text.splitlines()[0].lstrip("# ")
    model_id = title.split(" / ")[0]
    row = {
        "model": cell_dir.parent.parent.name,
        "run": cell_dir.name,
        "display": model_id.split("/", 1)[-1],
        "harness": cell_dir.parent.name,
        "failed": "**LEG FAILED:**" in text,
        "thinking_chars": sum(
            len(t.strip()) for k, t in sections if k == "thinking"
        ),
        "thinking_text": "\n\n".join(
            t.strip() for k, t in sections if k == "thinking"
        ),
        "output_text": "\n\n".join(
            t.strip() for k, t in sections if k == "output"
        ),
    }
    judge_json = cell_dir / "judge.json"
    if judge_json.exists():
        verdict = json.loads(judge_json.read_text())["verdict"]
        row.update(
            register=verdict.get("register"),
            relation=verdict.get("thinking_output_relation"),
            hypotheses=len(verdict.get("hypotheses_explored") or []),
            self_corrections=len(verdict.get("self_corrections") or []),
            bugs_in_thinking=sum(
                bool((verdict.get(bug) or {}).get("in_thinking"))
                for bug in ("off_by_one", "negative_index")
            ),
        )
    return row


def bar(chars: int, max_chars: int) -> str:
    if not chars:
        return "·"
    return "▇" * max(1, round(chars / max_chars * 8))


def channel(row: dict) -> str:
    """How much of the model's reasoning the provider actually exposes.

    The closed providers all return derived thinking, not the raw chain of
    thought: OpenAI surfaces only summaries, Anthropic summarizes extended
    thinking for Claude 4+ (brief thinking may pass through verbatim), and
    Google returns thought summaries for Gemini. Open-weight models ship
    reasoning_content verbatim. Ox is presumed raw (it uses the open-model
    chat channel) but, being a stealth model, that is unverifiable.
    """
    if not row.get("thinking_chars"):
        return "hidden"
    display = row["display"]
    if display.startswith("gpt-oss"):
        return "raw"  # OpenAI's open-weight family exposes raw CoT
    if display.startswith(("gpt-", "claude-", "gemini-")):
        return "summary"
    return "raw"


def hover(row: dict) -> str:
    """A tooltip-sized excerpt of the leg's thinking for a link title."""
    text = " ".join(row.get("thinking_text", "").split())[:240]
    if not text:
        return "no thinking surfaced"
    return text.replace('"', "'")


STYLE_NAMES = {"draft": "drafting", "deliberation": "deliberating"}
# Display names only; judge.json keeps the schema's terms.
REGISTER_NAMES = {"telegraphic": "telegram"}


def style(row: dict) -> str:
    relation = row.get("relation", "?")
    return STYLE_NAMES.get(relation, relation)


def register(row: dict) -> str:
    value = str(row.get("register", "?"))
    for schema_name, display in REGISTER_NAMES.items():
        value = value.replace(schema_name, display)
    return value


def delta(a: object, b: object) -> str:
    text = f"{a} → {b}"
    return f"**{text}**" if a != b else text


def main() -> None:
    rows = [cell_row(c) for c in sorted(ROOT.glob("results/*/*/run-*/cell.md"))]
    by_model: dict[str, dict[str, list[dict]]] = {}
    for row in rows:
        leg = row["harness"].split("-v")[0]
        by_model.setdefault(row["model"], {}).setdefault(leg, []).append(row)
    max_chars = max((r["thinking_chars"] for r in rows), default=1) or 1
    versions = sorted({r["harness"] for r in rows})

    lines = [START, ""]

    def fmt(value: object, other: object, mark: bool) -> str:
        text = str(value)
        return f"**{text}**" if mark and value != other else text

    def ok_runs(runs: list[dict]) -> list[dict]:
        # empty runs (no thinking, no output — e.g. rate-limited out) are
        # rerunnable, not data
        return [r for r in runs if not r["failed"]
                and (r["thinking_text"] or r["output_text"])]

    def dist(runs: list[dict], key: str) -> str:
        """Bare label when runs agree, distribution when they split."""
        values = [str(r.get(key, "?")) for r in runs]
        counts: dict[str, int] = {}
        for value in values:
            counts[value] = counts.get(value, 0) + 1
        if len(counts) == 1:
            return values[0]
        total = len(values)
        parts = sorted(counts.items(), key=lambda kv: -kv[1])
        return " · ".join(f"{v} {n}/{total}" for v, n in parts)

    def majority(runs: list[dict], key: str) -> str:
        values = [str(r.get(key, "?")) for r in runs]
        return max(set(values), key=values.count) if values else "?"

    def median(runs: list[dict], key: str) -> int:
        values = sorted(r.get(key, 0) or 0 for r in runs)
        return values[len(values) // 2] if values else 0

    def span(runs: list[dict], key: str) -> str:
        values = sorted(r.get(key, 0) or 0 for r in runs)
        if not values:
            return "?"
        lo, hi = values[0], values[-1]
        return str(lo) if lo == hi else f"{lo}–{hi}"

    def model_rows(model: str) -> list[str]:
        claude = ok_runs(by_model[model].get("claude", []))
        codex = ok_runs(by_model[model].get("codex", []))
        display = next(
            r["display"] for runs in by_model[model].values() for r in runs
        )
        if not claude or not codex:
            state = f"only {'claude' if claude else 'codex'} succeeded" if (
                claude or codex) else "failed"
            return [f"| `{display}` | ({state}) | | | | | |"]
        rows = [f"| **[`{display}`](results/{model})** | | | | | | |"]
        expected = max(len(claude), len(codex))
        for label, runs, other in (("claude", claude, codex),
                                   ("codex", codex, claude)):
            first = runs[0]
            cell_link = f"results/{model}/{first['harness']}/{first['run']}/cell.md"
            mark = label == "codex"
            med = median(runs, "thinking_chars")
            short = (f" ({len(runs)} run{'s' if len(runs) != 1 else ''})"
                     if len(runs) < expected else "")
            tip = f"{span(runs, 'thinking_chars')} chars · {hover(first)}"
            rows.append(
                f"| | {label}{short} "
                f"| [{bar(med, max_chars)}&nbsp;{med}]({cell_link} \"{tip}\") "
                f"| {fmt(dist_register(runs), dist_register(other), mark)} "
                f"| {fmt(dist_style(runs), dist_style(other), mark)} "
                f"| {fmt(span(runs, 'hypotheses'), span(other, 'hypotheses'), mark)} "
                f"| {fmt(span(runs, 'self_corrections'), span(other, 'self_corrections'), mark)} |"
            )
        return rows

    def dist_style(runs: list[dict]) -> str:
        styled = [dict(r, relation=style(r)) for r in runs]
        return dist(styled, "relation")

    def dist_register(runs: list[dict]) -> str:
        named = [dict(r, register=register(r)) for r in runs]
        return dist(named, "register")

    def model_channel(model: str) -> str:
        legs = [r for runs in by_model[model].values()
                for r in runs if not r["failed"]]
        channels = {channel(r) for r in legs} - {"hidden"}
        return channels.pop() if len(channels) == 1 else (
            "raw" if "raw" in channels else "summary")

    header = ("| model | harness | thinking | register | style |"
              " hypotheses | self-correct |\n"
              "|---|---|---|---|---|---|---|")
    raw_models = [m for m in sorted(by_model) if model_channel(m) == "raw"]
    summary_models = [m for m in sorted(by_model) if m not in raw_models]

    lines += [
        "### Raw thinking",
        "",
        "These providers return the model's chain of thought verbatim, so"
        " thinking volume and register are directly comparable.",
        "",
        header,
    ]
    for model in raw_models:
        lines += model_rows(model)
    lines += [
        "",
        "### Summarized or hidden thinking",
        "",
        "These providers return a summary of the reasoning (OpenAI,"
        " Anthropic, Google) or nothing at all — the rows describe the"
        " summaries, not the underlying chain of thought.",
        "",
        header,
    ]
    for model in summary_models:
        lines += model_rows(model)
    lines += ["", "Hover a bar for a thinking excerpt; expand below for the"
              " full surfaced thinking.", ""]
    for model in sorted(by_model):
        claude_runs = [r for r in by_model[model].get("claude", [])
                       if not r["failed"]]
        codex_runs = [r for r in by_model[model].get("codex", [])
                      if not r["failed"]]
        if not claude_runs or not codex_runs:
            continue
        claude, codex = claude_runs[0], codex_runs[0]
        display = claude["display"]
        parts = [f"<details><summary><code>{display}</code> — claude:"
                 f" {register(claude)} {style(claude)}"
                 f" ({claude['thinking_chars']}) · codex:"
                 f" {register(codex)} {style(codex)}"
                 f" ({codex['thinking_chars']}) — run-1 shown</summary>", ""]
        for leg, row in (("claude", claude), ("codex", codex)):
            cell_path = f"results/{model}/{row['harness']}/{row['run']}/cell.md"
            text = row.get("thinking_text") or "(no thinking surfaced)"
            if len(text) > 1600:
                text = (f"{text[:1600]}\n[... truncated;"
                        f" full text in {cell_path}]")
            answer = row.get("output_text") or "(none)"
            if len(answer) > 1600:
                answer = (f"{answer[:1600]}\n[... truncated;"
                          f" full text in {cell_path}]")
            # blockquote levels: leg at one, thinking at two
            parts += [
                f"> **{leg}** ({row['harness']}):",
                ">",
                "> > " + text.replace("\n", "\n> > "),
                ">",
                f"> <details><summary>{leg} answer</summary>",
                ">",
                "> " + answer.replace("\n", "\n> "),
                ">",
                "> </details>",
                "",
            ]
        parts.append("</details>")
        lines += parts + [""]
    lines += [
        "",
        f"Harness versions: {', '.join(f'`{v}`' for v in versions)}."
        " Per-cell details: [results/REPORT.md](results/REPORT.md) and"
        " [results/JUDGING.md](results/JUDGING.md); every cell links its"
        " full wire log.",
        END,
    ]

    readme = ROOT / "README.md"
    text = readme.read_text()
    if START not in text or END not in text:
        raise SystemExit(f"README.md is missing the {START} / {END} markers")
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    readme.write_text(pattern.sub("\n".join(lines), text))
    print(f"README.md updated with {len(by_model)} models")


main()
