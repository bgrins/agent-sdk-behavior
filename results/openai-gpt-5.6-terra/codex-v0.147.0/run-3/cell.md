# openai/gpt-5.6-terra / codex (SDK 0.147.0)

run: 2026-08-24T23:10:23+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "openai/gpt-5.6-terra", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`

## output

The bounds check has an off-by-one bug.

Valid indices for a table of `len` elements are `0` through `len - 1`. This code permits `idx == len`, then reads `table[len]`, which is one element past the allocation—undefined behavior and potentially an out-of-bounds read.

It also does not reject negative `idx`, so `table[-1]` reads before the array, another out-of-bounds access.

A safe version should validate both bounds (and, if applicable, the pointer and length):

```c
static int lookup(const int *table, int len, int idx) {
    if (table == NULL || len < 0 || idx < 0 || idx >= len) {
        return -1;
    }
    return table[idx];
}
```

If `-1` may be a legitimate table value, use a separate success/failure return value and an output parameter instead.

Full over-the-wire log: [wire.md](wire.md)
