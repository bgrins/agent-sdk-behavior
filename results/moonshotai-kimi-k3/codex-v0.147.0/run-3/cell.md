# moonshotai/kimi-k3 / codex (SDK 0.147.0)

run: 2026-08-24T23:17:12+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "moonshotai/kimi-k3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

Classic off-by-one + negative index issues. idx > len should be idx >= len; negative idx passes check; len could be negative; table could be NULL. Concise review.

## output

This function has two memory-safety bugs.

**Bug 1: Off-by-one (heap/stack buffer over-read)**
- Valid indices for an array of length `len` are `0..len-1`. The check `idx > len` allows `idx == len` through, and `table[len]` reads one element past the end of the buffer — an out-of-bounds read.
- Fix: `if (idx >= len) return -1;`

**Bug 2: Negative index (buffer under-read)**
- `idx` is a signed `int`. Any negative value passes the `idx > len` check, so `table[-5]` reads memory *before* the buffer. On little-endian systems this can also enable reading attacker-influenced memory if `idx` comes from user input (a classic info-leak primitive).
- Fix: `if (idx < 0 || idx >= len) return -1;`

**Secondary concerns**
- If `len` can be negative (bad caller), `table[0]` would pass the check. Defensive code should also validate `len >= 0` or take `size_t` and let the caller guarantee validity.
- `table` is never NULL-checked; fine if the contract guarantees a non-NULL pointer, but worth documenting.
- Using `int` for a length is fragile; `size_t len` (and comparing `idx` carefully, or also taking `size_t idx` and only checking `idx >= len`, which automatically rejects "negative" values since they'd wrap to huge) is the idiomatic C fix.

Corrected version:

```c
static int lookup(const int *table, size_t len, size_t idx) {
    if (idx >= len) return -1;
    return table[idx];
}
```

Note that the signedness change closes the under-read for free: a negative `idx` passed as `size_t` becomes a huge value that fails `idx >= len`.

Full over-the-wire log: [wire.md](wire.md)
