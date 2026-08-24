# anthropic/claude-fable-5 / claude (SDK 0.2.144)

run: 2026-08-24T23:14:08+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`

## thinking

This is a simple inline review, no tools needed. I'm spotting an off-by-one bug where the bounds check should use >= instead of >, allowing an out-of-bounds read one past the array end, and also noting there's no check for negative index values.

Also worth flagging: table could be NULL depending on the contract, the -1 sentinel conflates error with a legitimate value, and len itself could theoretically be negative, though the index checks matter most. I'll write up the fixed version now.

## output

Two out-of-bounds reads survive the bounds check, one on each side of the table.

**1. Off-by-one: `idx == len` passes the check.**
The check rejects `idx > len`, so `idx == len` falls through to `table[len]` — one element past the end. Valid indices for a `len`-element array are `0` through `len - 1`, so the comparison must be `idx >= len`.

Failure scenario: `lookup(table, 4, 4)` reads `table[4]` on a 4-element array. That read is undefined behavior — in practice it returns adjacent stack or heap memory, and it can leak secrets or crash if the array sits at the end of a page.

**2. Negative `idx` is never checked.**
`idx` is a signed `int`, and the check `idx > len` accepts every negative value. `lookup(table, 4, -1000)` reads 4000 bytes before the array. An attacker who controls `idx` gets a relative read into whatever precedes the table.

**Lesser issues worth noting:**

- **Negative or garbage `len`.** If a caller passes `len = -1`, even the corrected `idx >= len` check rejects everything, which is safe — but mixing signed comparisons here is fragile. Using `size_t` for `len` (and validating `idx` against it after checking `idx >= 0`) removes the class of bug.
- **`table` may be NULL.** The function dereferences it unconditionally. Whether that needs a check depends on the documented contract with callers; for a `static` helper with audited call sites it may be acceptable.
- **In-band error value.** Returning `-1` for "out of range" is indistinguishable from a stored value of `-1`. Not a memory-safety bug, but callers who treat `-1` as "not found" will misbehave on legitimate data. Return the value through an out-parameter and use the return code purely for status.

Corrected version:

```c
static int lookup(const int *table, size_t len, int idx, int *out) {
    if (table == NULL || idx < 0 || (size_t)idx >= len)
        return -1;
    *out = table[idx];
    return 0;
}
```

The core pattern to remember: a bounds check on a signed index needs both ends (`idx < 0 || idx >= len`), and `>` vs `>=` against `len` is the classic off-by-one that turns a guard into a one-element leak.

Full over-the-wire log: [wire.md](wire.md)
