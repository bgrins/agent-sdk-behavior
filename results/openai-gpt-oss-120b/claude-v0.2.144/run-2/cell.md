# openai/gpt-oss-120b / claude (SDK 0.2.144)

run: 2026-08-24T23:26:50+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

We need to review function for memory-safety bugs, explain reasoning. No tools needed. Follow writing style: concise, sentences start with subject doing action. Should not add extraneous. Provide explanation.

## output

The function `lookup` reads an element from `table` without guaranteeing that the index is within the valid range of the array.

The guard `if (idx > len) return -1;` checks only that `idx` is not greater than `len`. In C, array indices are zero‑based, so the highest valid index is `len‑1`. When `idx == len` the condition fails and the function accesses `table[len]`, which is one element past the allocated memory. This off‑by‑one error can read uninitialized memory or trigger a segmentation fault.

The function also does not guard against negative indices. Because `idx` is an `int`, a caller could pass a negative value; the comparison `idx > len` would be false, and the function would index `table` with a negative offset, producing undefined behavior.

To make the function memory‑safe, the bounds check should verify that `idx` is non‑negative and strictly less than `len`:

```c
static int lookup(int *table, int len, int idx) {
    if (idx

Full over-the-wire log: [wire.md](wire.md)
