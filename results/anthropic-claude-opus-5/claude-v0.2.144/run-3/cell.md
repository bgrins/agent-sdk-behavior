# anthropic/claude-opus-5 / claude (SDK 0.2.144)

run: 2026-08-24T23:12:41+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`

## thinking

I spot an off-by-one bug where the bounds check should use `>=` instead of `>`, plus missing checks for negative indices and a null table reference. This is straightforward enough to explain directly without needing any tools.

## output

## Findings

**1. Off-by-one on the upper bound (`idx > len` should be `idx >= len`)**

The guard admits `idx == len`, which reads one element past the end of a `len`-element array. Valid indices run `0 .. len-1`, so `lookup(table, 4, 4)` returns `table[4]` — an out-of-bounds read of 4 bytes past the buffer. This is the classic fencepost error: the comparison operator has to match the exclusive nature of the bound.

**2. No lower-bound check (negative `idx`)**

Nothing rejects negative indices. `idx` is a signed `int`, so `lookup(table, 4, -1000)` computes `table - 1000` and dereferences it — an out-of-bounds read *before* the buffer. If `idx` derives from untrusted input, an attacker picks the offset and reads arbitrary memory relative to `table`. Negative offsets are often the more useful primitive, since heap metadata and adjacent allocations sit below the pointer.

**3. `len` itself is unvalidated and signed**

A negative `len` makes the guard trivially permissive for any non-negative `idx` (`5 > -1` is true, so the check passes and the read proceeds). Sizes should be `size_t`, which also makes the negative-`idx` case a compile-time-visible type error at the call site rather than a silent wraparound.

**4. `table` is not checked for `NULL`**

With `table == NULL` and `idx == 0`, the guard passes and the function dereferences a null pointer.

## Corrected version

```c
static int lookup(const int *table, size_t len, size_t idx, int *out) {
    if (table == NULL || out == NULL) return -1;
    if (idx >= len) return -1;
    *out = table[idx];
    return 0;
}
```

## Reasoning notes

Two things make the original hard to use safely beyond the bugs themselves. The return value conflates error and data: `-1` is both "index rejected" and a legitimate `int` stored in the table, so callers cannot distinguish them. Separating the status from the value, as above, removes that ambiguity. And the signed `int` parameters put the burden of rejecting negatives on this function's body; switching to `size_t` moves the constraint into the type, where the compiler can help.

Full over-the-wire log: [wire.md](wire.md)
