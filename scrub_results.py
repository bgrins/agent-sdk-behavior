# /// script
# requires-python = ">=3.12"
# ///
"""Scrub per-run identifiers from captured wire logs before committing them.

The relay redacts credentials at capture time; both SDKs still stamp every
request with install, session, and device ids that no option turns off.
Run this after run_grid.py, and extract anything derived from the logs
afterwards.

Usage:
  uv run scrub_results.py [--results-root results] [--check]
"""

import argparse
import re
from pathlib import Path

REDACTED = "<redacted>"

# Identifier fields, in pretty-printed bodies and in captured headers alike.
ID_KEYS = (
    "prompt_cache_key", "turn_id", "session_id", "thread_id", "window_id",
    "installation_id", "x-codex-installation-id", "x-codex-window-id",
    "x-client-request-id", "session-id", "thread-id",
    "X-Claude-Code-Session-Id",
)
# Values that are themselves JSON blobs of identifiers.
BLOB_KEYS = ("x-codex-turn-metadata", "user_id")

SUBSTITUTIONS = (
    (re.compile(rf'("(?:{"|".join(ID_KEYS)})": ")[^"]*(")'),
     rf"\g<1>{REDACTED}\g<2>"),
    (re.compile(rf'("(?:{"|".join(BLOB_KEYS)})": ")(?:[^"\\]|\\.)*(")'),
     rf"\g<1>{REDACTED}\g<2>"),
)

LEFTOVERS = (
    ("install/session ids", re.compile(r"installation_id\\?\":\\?\"[0-9a-f-]{8,}")),
    ("device fingerprint", re.compile(r"device_id\\?\":\\?\"[0-9a-f]{32,}")),
    ("git commit hash", re.compile(r"latest_git_commit_hash")),
)


def scrub(text: str) -> str:
    for pattern, replacement in SUBSTITUTIONS:
        text = pattern.sub(replacement, text)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-root", type=Path,
                        default=Path(__file__).parent / "results")
    parser.add_argument("--check", action="store_true",
                        help="report what would change without writing")
    args = parser.parse_args()

    changed = 0
    scrubbed_tree: dict[Path, str] = {}
    for path in sorted(args.results_root.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(errors="replace")
        scrubbed = scrub(text)
        scrubbed_tree[path] = scrubbed
        if scrubbed == text:
            continue
        changed += 1
        if not args.check:
            path.write_text(scrubbed)
        print(f"{'would scrub' if args.check else 'scrubbed'} {path}"
              f" (-{len(text) - len(scrubbed)} chars)")

    print(f"\n{changed} file(s)")
    for label, pattern in LEFTOVERS:
        hits = [p for p, text in scrubbed_tree.items() if pattern.search(text)]
        print(f"  remaining {label}: {len(hits)}"
              + (f" e.g. {hits[0]}" if hits else ""))


main()
