# z-ai/glm-5.2:free / claude (SDK 0.2.144)

run: 2026-08-24T21:05:18+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants a review of this C function for memory-safety bugs. Let me analyze it carefully.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

The bounds check is `idx > len`. This is wrong in two ways:

1. Off-by-one: valid indices are 0..len-1. The check allows `idx == len`, which reads `table[len]` — one past the end. Out-of-bounds read. The check should be `idx >= len`.

2. Negative indices: `idx` is a signed `int`. If `idx` is negative, `idx > len` is false (since len is presumably non-negative), so the function proceeds to `table[idx]` with a negative index — out-of-bounds read before the start of the buffer. The check should also be `idx < 0`.

Both are memory-safety bugs (out-of-bounds reads). Let me explain clearly.

## output

## Bugs

The bounds check `if (idx > len) return -1;` is wrong in two ways. Both produce out-of-bounds reads of `table`.

**1. Off-by-one: it allows `idx == len`.**

Valid indices for a buffer of length `len` are `0` through `len-1`. The guard rejects only values *strictly greater* than `len`, so `idx == len` passes and the function reads `table[len]` — one element past the end. The condition must be `idx >= len`.

**2. It never rejects negative indices.**

`idx` is a signed `int`. A negative `idx` makes `idx > len` false (assuming `len >= 0`), so execution falls through to `table[idx]`, reading memory before the start of the buffer. The guard must also check `idx < 0`.

### Why each matters

- `idx == len`: the read lands exactly one `int` past the allocation. On a heap buffer this is a classic heap over-read (potential info leak / adjacent-metadata corruption if later written); on a stack array it is a stack over-read. Fuzzers and sanitizers (ASan) flag it immediately.
- Negative `idx`: `table[-5]` reads `*(int*)((char*)table - 20)`, i.e. memory before the buffer. Same out-of-bounds-read class, and trivially reachable from any caller that passes an attacker-controlled or untrusted `idx`.

### Also worth noting

`len` is a signed `int`, so a caller passing a negative `len` makes the guard `idx > len` *more* permissive rather than rejecting the call — a subtle second-order hole if `len` is ever computed from untrusted input. A length that must be non-negative should be `size_t` (or at least `unsigned`), which also sidesteps the sign-comparison issues below.

There is also a signed/unsigned comparison smell once you fix the types: if `len` becomes `size_t` and `idx` stays `int`, `idx >= len` promotes `idx` to unsigned and a negative `idx` wraps to a huge value — so you must keep the `idx < 0` check *before* any unsigned comparison, or cast carefully.

### Fixed version

```c
static int lookup(const int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

This rejects negatives, rejects the one-past-the-end case, and the `idx >= len` comparison stays signed-on-signed so no promotion surprise occurs. Marking `table` `const` is incidental but reflects that the function only reads.

Full over-the-wire log: [wire.md](wire.md)
