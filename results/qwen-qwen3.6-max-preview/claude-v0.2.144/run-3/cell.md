# qwen/qwen3.6-max-preview / claude (SDK 0.2.144)

run: 2026-08-24T23:25:06+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants me to review a C function for memory-safety bugs. Let me analyze the code carefully.

## output

**Off-by-one bounds check bug.**

```c
if (idx > len) return -1;
```

This should be `idx >= len`. Valid indices for an array of length `len` are `0` through `len - 1`. When `idx == len`, the condition `idx > len` is false, so the function proceeds to `table[idx]` — an out-of-bounds read one element past the end of the array.

Additionally, there's **no check for negative `idx`**. If `idx` is negative, `table[idx]` reads before the start of the array.

**Fixed version:**

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Full over-the-wire log: [wire.md](wire.md)
