# anthropic/claude-fable-5 / codex (SDK 0.147.0)

run: 2026-08-24T23:13:50+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-fable-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

This is a straightforward code review question, so I can just answer it directly.

## output

**Memory-Safety Bugs**

- **Off-by-one (out-of-bounds read):** The check `idx > len` allows `idx == len`, but valid indices for an array of length `len` are `0 … len-1`. `lookup(table, len, len)` passes the check and reads `table[len]`, one element past the end — undefined behavior (CWE-193/CWE-125).
- **No lower-bound check:** Negative `idx` is never rejected. `lookup(table, len, -5)` reads `table[-5]`, an out-of-bounds read before the buffer. This is a classic signed-index bug attackers exploit to leak or address adjacent memory.
- **No NULL check (minor/defensive):** If `table` can be NULL, dereferencing it crashes. Whether this matters depends on the caller contract.

**Design Smell**

- The error sentinel `-1` is ambiguous: a table can legitimately contain `-1`, so callers can't distinguish "invalid index" from "value is -1". Not a memory-safety issue, but it can mask the bounds failures above.

**Fixed Version**

```c
static int lookup(const int *table, int len, int idx) {
    if (table == NULL || idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Key changes: `idx >= len` instead of `idx > len`, and rejecting `idx < 0`. Using `size_t` for `len`/`idx` (with `idx >= len`) is another way to eliminate the negative-index case entirely, as long as callers can't accidentally pass a negative value that wraps to a huge unsigned number.

Full over-the-wire log: [wire.md](wire.md)
