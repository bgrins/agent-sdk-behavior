# z-ai/glm-5.2:free / claude (SDK 0.2.144)

run: 2026-08-24T23:07:36+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings (x2, statuses [429, 200]): `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings (x5, statuses [429, 429, 429, 429, 200]): `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants a memory-safety review of this C function. Let me analyze it.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

Bugs:

1. **Negative index not checked.** `idx` is a signed `int`. If `idx` is negative, the `idx > len` check passes (assuming len >= 0), and `table[idx]` reads memory before the buffer — out-of-bounds read.

2. **Off-by-one on the upper bound.** The check is `idx > len`, but valid indices for a buffer of length `len` are `0..len-1`. When `idx == len`, the check passes and `table[len]` reads one element past the end — out-of-bounds read. Should be `idx >= len`.

3. **No null-pointer check on `table`.** If `table` is NULL and the bounds check passes, dereferencing crashes. This may or may not be in scope but worth noting.

4. **`len` could be negative.** If `len` is negative, `idx > len` is likely true for most positive idx, but a negative idx with negative len could pass... actually if both negative, idx > len could be false. Edge case. The function assumes len >= 0 but doesn't validate.

Let me write up the reasoning clearly.

## output

## Memory-safety review

Two definite bugs, one likely bug, and one assumption worth flagging.

### Bug 1 — negative index reads before the buffer (definite)

`idx` is a signed `int`, but the guard only checks the upper bound. A negative `idx` passes `idx > len` (for any non-negative `len`) and reaches `table[idx]`, which dereferences memory *before* the buffer. This is an out-of-bounds read; in a security context it can leak neighboring stack/heap data, and with a large-magnitude negative value it can fault.

```c
lookup(table, 4, -1);   // reads table[-1] — UB, OOB read
```

The fix is to bound `idx` from below as well:

```c
if (idx < 0 || idx >= len) return -1;
```

### Bug 2 — off-by-one allows `table[len]` (definite)

The upper-bound check is `idx > len`, but valid indices for a buffer of length `len` are `0..len-1`. When `idx == len` the guard passes and `table[idx]` reads exactly one element past the end — another out-of-bounds read. The comparison must be `>=`, not `>`:

```c
lookup(table, 4, 4);   // reads table[4], one past the end — UB, OOB read
```

### Bug 3 — no null check on `table` (likely)

If a caller passes `NULL` for `table` with any in-range `idx`, the bounds check passes and `table[idx]` dereferences a null pointer. Whether this is the function's responsibility or the caller's is a design choice, but the current bounds check creates a false sense of safety — it validates the index and then dereferences an unchecked pointer. If the intent of the guard is "make this safe to call with arbitrary inputs," `table` needs a check too.

### Assumption worth flagging — `len` is trusted to be non-negative

Nothing validates `len`. If `len` is negative, the guard `idx > len` is trivially true for most `idx` (so the function returns -1, accidentally safe), but a negative `idx` paired with a more-negative `len` can slip through: `idx = -1, len = -2` gives `-1 > -2` → false, so it proceeds to `table[-1]`. The robust form treats `len` as unsigned or rejects negative `len`:

```c
if (len <= 0 || idx < 0 || idx >= len) return -1;
return table[idx];
```

### Corrected version

```c
static int lookup(int *table, int len, int idx) {
    if (table == NULL || len <= 0) return -1;
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

The original's central defect is that `idx > len` does the wrong comparison in two directions at once: it lets negatives through (no lower bound) and lets `len` itself through (`>` instead of `>=`). Both produce out-of-bounds reads from caller-controlled input, which is the memory-safety failure.

Full over-the-wire log: [wire.md](wire.md)
