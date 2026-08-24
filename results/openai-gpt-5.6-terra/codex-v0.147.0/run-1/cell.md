# openai/gpt-5.6-terra / codex (SDK 0.147.0)

run: 2026-08-24T22:20:43+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "openai/gpt-5.6-terra", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`

## output

There is an out-of-bounds read when `idx == len`.

Valid indices for an array with `len` elements are `0` through `len - 1`, but this check only rejects values greater than `len`:

```c
if (idx > len) return -1;
```

So `lookup(table, len, len)` reads `table[len]`, one element past the array. That is undefined behavior and can disclose adjacent memory or crash.

It also fails to reject negative indices. For example, `lookup(table, len, -1)` passes the check and reads `table[-1]`, also undefined behavior.

Use bounds checks on both sides:

```c
static int lookup(const int *table, int len, int idx) {
    if (table == NULL || len < 0 || idx < 0 || idx >= len)
        return -1;
    return table[idx];
}
```

`const` is optional for safety, but accurately conveys that the function does not modify the table.

Full over-the-wire log: [wire.md](wire.md)
