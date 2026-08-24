# z-ai/glm-5.2:free / codex (SDK 0.147.0)

run: 2026-08-24T21:09:40+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "z-ai/glm-5.2:free", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

The bug: `idx > len` should be `idx >= len` or `idx < 0`. Off-by-one allows out-of-bounds read at idx==len, and no negative check.

## output

**Off-by-one out-of-bounds read**

The guard `idx > len` is wrong in two ways:

- It allows `idx == len`, which reads one element past the end of `table` (valid indices are `0` … `len-1`). With a 0-length array it even allows `idx == 0`. This is an out-of-bounds read: undefined behavior, and a potential info leak if the adjacent memory holds secrets.
- It never rejects negative `idx`. Since `idx` is a signed `int`, a caller can pass a negative value; `idx > len` is false, so `table[idx]` dereferences a pointer *before* the buffer — another out-of-bounds read (and, on platforms where negative offsets are meaningful, a more serious primitive).

**Fix**

Validate the full range before indexing:

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

`>=` closes the off-by-one, and the `idx < 0` check closes the signed-negatives hole. If `len` can ever be negative (e.g., from unchecked input), also guard `len < 0` or use a `size_t` for `len` to avoid the comparison itself being signed/unsigned problematic.

Full over-the-wire log: [wire.md](wire.md)
