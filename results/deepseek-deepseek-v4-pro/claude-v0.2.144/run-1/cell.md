# deepseek/deepseek-v4-pro / claude (SDK 0.2.144)

run: 2026-08-24T21:05:37+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants me to review a C function for memory-safety bugs.

## output

## Memory-safety review of `lookup`

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

### Off-by-one bounds check (the main bug)

The check is `if (idx > len) return -1;` — but it should be `if (idx >= len)`.

In C, an array of length `len` has valid indices `0` through `len - 1`. With the current check, `idx == len` passes through and accesses `table[len]`, which is one past the end of the array. This is a classic off-by-one out-of-bounds read.

### No negative-index guard

`idx` is an `int` (signed). If `idx` is negative (e.g., `-1`), the check `idx > len` is false (assuming `len >= 0`), so `table[-1]` is accessed — reading memory *before* the array. This is an out-of-bounds read on the other side.

### Summary

Two paths to out-of-bounds access:

| Input | Condition passes? | Access | 
|---|---|---|
| `idx == len` | yes (bug) | `table[len]` — one past the end |
| `idx < 0` | yes (bug) | `table[idx]` — before the array |

The correct guard:

```c
if (idx < 0 || idx >= len) return -1;
```

Or equivalently, with `size_t`/`unsigned` casting, but the signed check is clearest for an `int` parameter.

Full over-the-wire log: [wire.md](wire.md)
