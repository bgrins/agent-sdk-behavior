# z-ai/glm-5.2:free / claude (SDK 0.2.144)

run: 2026-08-24T23:05:43+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings (x3, statuses [429, 429, 429]): `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings (x4, statuses [429, 429, 429, 200]): `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants a memory-safety review of a C function. Let me reason carefully.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

The bounds check `if (idx > len) return -1;` has two bugs:

1. **Off-by-one**: It should be `idx >= len`, not `idx > len`. When `idx == len`, the check passes but `table[len]` is one past the end — out-of-bounds read. Valid indices are 0..len-1.

2. **Negative index**: `idx` is a signed `int`. A negative `idx` passes the `idx > len` check (negative is not greater than len), and then `table[idx]` with a negative index reads memory before the array buffer — out-of-bounds read. In C, array indexing with a negative value is defined as pointer arithmetic from the array base, so `table[-5]` reads `*(table - 5)`, which is memory before the buffer. This is undefined behavior / out-of-bounds read.

Also worth noting: if `len` could be negative (passed in), `idx > len` with a negative len... but the main issues are the two above.

Let me also consider: what if `table` is NULL? Not the main focus but could mention. The primary memory-safety bugs are the off-by-one and the negative index.

Let me write a clear explanation following the writing style guidelines.

## output

Two memory-safety bugs, both in the bounds check.

**1. Off-by-one: `idx == len` reads one past the end.** Valid indices for a `len`-element array run from `0` to `len - 1`. The guard rejects values *greater than* `len`, so `idx == len` slips through and `table[len]` reads the element just past the buffer. The condition must be `idx >= len`.

**2. Negative `idx` reads before the buffer.** `idx` is a signed `int`, and the check only compares against an upper bound. A negative index satisfies `idx > len` (it is not greater than `len`), then `table[idx]` becomes pointer arithmetic `*(table + idx)` — memory *before* the array. That is an out-of-bounds read and undefined behavior. The guard needs a lower bound too: `idx < 0`.

The second bug is the more dangerous of the two, because a negative `idx` reads attacker-influenced memory relative to the buffer with no crash, leaking whatever happens to sit before `table` on the stack or heap.

A correct version:

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Note also that `len` itself is signed; a caller passing a negative `len` makes `idx >= len` true for any non-negative `idx`, which is the safe direction, so that case degrades to "nothing found" rather than a memory bug — acceptable, though using `size_t` for `len` and `idx` would make the contract harder to violate.

Secondary, non-memory-safety concern: returning `-1` as a sentinel collides with any legitimate table entry whose value is `-1`. The caller cannot distinguish "out of bounds" from "the element is -1." A separate error channel (out-parameter, `ssize_t`, or returning a bool and taking an `int *out`) avoids that ambiguity — but that is an API design issue, not the memory-safety defect you asked about.

Full over-the-wire log: [wire.md](wire.md)
