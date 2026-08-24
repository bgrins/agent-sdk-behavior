# moonshotai/kimi-k3 / codex (SDK 0.147.0)

run: 2026-08-24T23:16:47+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "moonshotai/kimi-k3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

Review: off-by-one — idx > len should be idx >= len. Valid indices 0..len-1. Also negative idx passes the check — if idx is negative, idx > len is false, and table[idx] is out of bounds. So two bugs: off-by-one upper bound, and no negative check. Also table could be NULL, len negative, etc.

This is a read-only Q, no tools needed. Just answer.

## output

This function has two memory-safety bugs.

**Bug 1: Off-by-one upper bound**

The guard `if (idx > len) return -1;` allows `idx == len` to pass through. Valid indices for a `len`-element array are `0` through `len - 1`, so `table[len]` reads one element past the end of the buffer (out-of-bounds read).

```c
// Passing table of length 4, idx == 4:
// check: 4 > 4 is false, so we read table[4] — one past the end
```

Fix: the comparison should be `idx >= len`.

**Bug 2: No lower-bound check**

`idx` is a signed `int`. If a caller passes a negative index (e.g., `-1`), the check `idx > len` is false, and `table[-1]` reads *before* the buffer — another out-of-bounds read.

Fix: also reject `idx < 0`.

**Corrected version**

```c
static int lookup(int *table, int len, int idx) {
    if (table == NULL) return -1;
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

I also added a `NULL` check for `table` — strictly speaking a contract violation rather than something the caller can always guarantee, but cheap insurance since the function already returns an error sentinel.

**Why it matters:** an out-of-bounds read here leaks adjacent memory contents to the caller (a potential info disclosure primitive), and on an attacker-controlled `idx` it's a classic building block for exploitation. The `(idx < 0 || idx >= len)` pattern — or better, taking `idx`/`len` as `size_t` so negatives are impossible — is the idiomatic safe bounds check in C.

Full over-the-wire log: [wire.md](wire.md)
