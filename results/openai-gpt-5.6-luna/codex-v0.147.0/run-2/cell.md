# openai/gpt-5.6-luna / codex (SDK 0.147.0)

run: 2026-08-24T23:09:01+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "openai/gpt-5.6-luna", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`

## thinking

ReasoningThreadItem(content=[], id='rs_09c1a3d1c71c3a49016a8ccf09365087d1ae462b0bb0c25200', summary=[], type='reasoning')

## output

The function has an out-of-bounds read:

```c
if (idx > len) return -1;
return table[idx];
```

Valid indices for a table of length `len` are `0` through `len - 1`, but `idx == len` is accepted and reads one element past the table.

Negative indices are also accepted because `idx > len` is false for them:

```c
lookup(table, 10, -1); // reads table[-1]
```

A safer bounds check is:

```c
static int lookup(const int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

This assumes `table` points to at least `len` valid `int` elements and that `len` is nonnegative. If `table` may be `NULL`, that should also be checked before dereferencing.

Full over-the-wire log: [wire.md](wire.md)
