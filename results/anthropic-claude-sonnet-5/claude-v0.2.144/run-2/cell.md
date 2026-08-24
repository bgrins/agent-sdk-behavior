# anthropic/claude-sonnet-5 / claude (SDK 0.2.144)

run: 2026-08-24T23:13:18+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`

## thinking

I'm reviewing a simple table lookup function for bugs. There's an off-by-one error since the bounds check allows idx equal to len, which is out of range, and it also fails to guard against negative indices.

## output

## Bugs

**1. Off-by-one on the upper bound (out-of-bounds read).**
The check `idx > len` allows `idx == len` through, but valid indices for an array of length `len` run from `0` to `len - 1`. When `idx == len`, `table[idx]` reads one element past the end of the buffer. The condition should be `idx >= len`.

**2. No lower-bound check (out-of-bounds read, more severe).**
The function never rejects negative `idx`. If `idx` is negative, `idx > len` is false (assuming `len >= 0`), so execution falls through to `table[idx]`, which reads memory *before* the start of the array. This is the more dangerous of the two, since a negative index can be pushed arbitrarily far back by the caller, turning this into a controllable out-of-bounds read rather than a one-element overrun.

**3. No validation that `table` is non-null or that `len` is non-negative.**
If `table` is `NULL`, any non-zero `idx` dereferences a null/near-null pointer (likely a crash, and on some platforms/architectures a security-relevant condition if that low memory is mapped). If `len` is negative (e.g., derived from an unchecked size calculation upstream), the `idx > len` check becomes even less meaningful, since almost any `idx >= 0` will satisfy `idx > len` and be rejected — but a negative `idx` combined with negative `len` can still slip through as described in bug 2.

## Why this matters

The function is a raw pointer-indexed accessor with no bounds enforcement beyond a single, incorrect comparison. Because it returns `table[idx]` directly (not writing), the exploitation impact is an out-of-bounds *read* — information disclosure or a crash — rather than memory corruption. But if `idx` is attacker-influenced (directly or indirectly, e.g., from parsed input, an index computed from a length field, etc.), this is a classic OOB-read primitive: it can leak adjacent heap/stack/global data through whatever channel eventually surfaces the returned `int`, or crash the process (DoS) if it reads unmapped memory.

## Fix

```c
static int lookup(int *table, int len, int idx) {
    if (!table || len < 0 || idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

This closes both the upper-bound off-by-one and the missing lower-bound check, and guards against a null table or a nonsensical negative length.

Full over-the-wire log: [wire.md](wire.md)
