# anthropic/claude-fable-5 / claude (SDK 0.2.144)

run: 2026-08-24T22:25:28+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`

## thinking

This is a simple review question—the bug is that the bounds check uses `>` instead of `>=`, and negative indices and a null table aren't being checked either. I can answer directly without needing any tools.

## output

Two memory-safety bugs, both in the bounds check.

**Off-by-one: `idx > len` admits `idx == len`.** A table of length `len` has valid indices `0` through `len - 1`. The check rejects only indices strictly greater than `len`, so `lookup(table, len, len)` passes the guard and reads `table[len]` — one element past the end. That is an out-of-bounds read and undefined behavior. The check must be `idx >= len`.

**No lower bound: negative `idx` is accepted.** `idx` is a signed `int`, and any negative value satisfies `idx > len` being false (e.g. `-1 > 10` is false), so `lookup(table, 10, -5)` reads `table[-5]` — memory before the array. The guard needs `idx < 0` as well.

Corrected:

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Two further points worth weighing, depending on the call sites:

- **`table` is never checked for NULL.** If any caller can pass NULL, `table[idx]` dereferences it. Whether to guard here or document the precondition is a design choice, but the function silently assumes non-NULL today.
- **A negative `len` also passes.** With `len = -1`, every non-negative `idx` fails `idx >= len`... actually with the corrected code, `idx >= len` catches it since any `idx >= 0 > -1`. In the *original* code, though, `len = -1` combined with the missing lower bound makes the guard nearly useless. Using `size_t` for `len` (and matching the check accordingly) removes the negative-length state entirely.
- **The `-1` sentinel is ambiguous.** `-1` is also a valid table value, so callers cannot distinguish "index out of range" from "stored value is -1." Not a memory-safety issue, but it invites callers to skip their own validation and lean on a signal this function cannot reliably deliver.

The core fix is the exclusive upper bound plus the lower bound: `idx < 0 || idx >= len`.

Full over-the-wire log: [wire.md](wire.md)
