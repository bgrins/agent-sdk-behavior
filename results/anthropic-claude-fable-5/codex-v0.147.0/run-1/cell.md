# anthropic/claude-fable-5 / codex (SDK 0.147.0)

run: 2026-08-24T22:25:13+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-fable-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

This is a simple review question, no tools needed here.

## output

**Memory-Safety Bugs**

- **Off-by-one bound check**: `if (idx > len)` allows `idx == len`, but valid indices are `0` to `len - 1`. Calling `lookup(table, len, len)` reads one element past the end of the array — a classic out-of-bounds read. The check must be `idx >= len`.
- **No lower-bound check**: `idx` is a signed `int`, so a negative value (e.g., `-1`) passes the check and `table[idx]` reads memory *before* the array. The check should also reject `idx < 0`.
- **No NULL check**: if `table` is `NULL`, the function dereferences it. Depending on the calling contract this may be acceptable, but a defensive `if (!table) return -1;` is cheap.
- **Ambiguous error sentinel** (design, not memory safety): returning `-1` for errors is indistinguishable from a stored value of `-1`, which can push callers into skipping validation or misinterpreting results.

**Corrected version**

```c
static int lookup(const int *table, int len, int idx) {
    if (table == NULL || idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

**Reasoning summary**

The two exploitable issues are the inclusive upper bound (`>` instead of `>=`) and the missing negative check. Together they permit reads at `table[len]` and at arbitrary negative offsets — both undefined behavior that can leak adjacent memory (an info-disclosure primitive similar in spirit to Heartbleed-style over-reads) or crash. If `len` could ever be attacker-influenced or negative itself, also consider using `size_t` for `len`/`idx` to eliminate the signedness hazard entirely.

Full over-the-wire log: [wire.md](wire.md)
