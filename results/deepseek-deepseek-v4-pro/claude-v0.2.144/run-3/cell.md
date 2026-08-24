# deepseek/deepseek-v4-pro / claude (SDK 0.2.144)

run: 2026-08-24T23:08:16+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants me to review a C function for memory-safety bugs.

## output

## Review of `lookup`

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

**Bug: off-by-one in the bounds check (`idx > len` instead of `idx >= len`).**

If `len` is the number of elements in `table`, the valid indices are `0` through `len - 1`. The condition `idx > len` passes `idx == len`, which is one past the end of the array. So `table[len]` is an out-of-bounds read.

**Bug: no negative-index check.**

Signed `int idx` can be negative. The condition `idx > len` passes all negative values (since any negative number is ≤ any non-negative `len`). So `table[-1]`, `table[-2]`, etc. all pass the guard and read memory before the array — a classic out-of-bounds read.

**Fix:**

```c
if (idx < 0 || idx >= len) return -1;
```

Or, if the table genuinely should never be empty and `len` is the count, an unsigned `size_t` for both `len` and `idx` would eliminate the negative case at the type level — but then you'd still need `idx >= len`.

Full over-the-wire log: [wire.md](wire.md)
