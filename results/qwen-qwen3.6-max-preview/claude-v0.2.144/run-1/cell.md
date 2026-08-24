# qwen/qwen3.6-max-preview / claude (SDK 0.2.144)

run: 2026-08-24T22:45:50+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user wants me to review a C function for memory-safety bugs. Let me analyze it carefully.

## output

## Off-by-one bounds check

The boundary condition uses `>` instead of `>=`, which allows an out-of-bounds read when `idx == len`.

```c
if (idx > len) return -1;  // BUG: should be idx >= len
```

In C, a valid index into an array of length `len` is `0` through `len - 1`. When `idx == len`, the check passes but `table[len]` reads one element past the end of the array — undefined behavior.

**Fixed:**

```c
if (idx < 0 || idx >= len) return -1;
return table[idx];
```

## Negative index

There is no check for `idx < 0`. A negative index reads before the start of the array — also undefined behavior. The fix above adds this check.

## Summary

| Bug | Trigger | Consequence |
|---|---|---|
| Off-by-one | `idx == len` | OOB read past end |
| No negative check | `idx < 0` | OOB read before start |

Both are classic memory-safety violations (CWE-125: Out-of-bounds Read).

Full over-the-wire log: [wire.md](wire.md)
