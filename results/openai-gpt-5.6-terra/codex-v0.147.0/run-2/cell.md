# openai/gpt-5.6-terra / codex (SDK 0.147.0)

run: 2026-08-24T23:10:19+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "openai/gpt-5.6-terra", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`

## output

The bounds check has an off-by-one bug.

`len` is typically the number of elements, so valid indices are `0` through `len - 1`. This code accepts `idx == len`:

```c
if (idx > len) return -1;
```

and then reads `table[len]`, which is one element past the allocation—an out-of-bounds read and undefined behavior. It could disclose adjacent memory or crash.

It also fails to reject negative indices. For `idx < 0`, the check passes and `table[idx]` reads before the array, another out-of-bounds read.

Use:

```c
static int lookup(const int *table, int len, int idx) {
    if (table == NULL || len < 0 || idx < 0 || idx >= len)
        return -1;
    return table[idx];
}
```

Whether `NULL` needs handling depends on the function’s contract, but validating it makes this standalone helper safer.

Full over-the-wire log: [wire.md](wire.md)
