# anthropic/claude-fable-5 / codex (SDK 0.147.0)

run: 2026-08-24T23:13:42+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-fable-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

This is a simple review question, no tools needed here.

## output

**Memory-Safety Bugs**

- **Off-by-one bound check**: `if (idx > len)` allows `idx == len`, but valid indices are `0 .. len-1`. `table[len]` reads one element past the end of the array — a classic off-by-one out-of-bounds read (CWE-193 / CWE-125).
- **No lower-bound check**: `idx` is signed and never checked for negativity. A negative `idx` passes the `idx > len` test and `table[idx]` reads memory *before* the array, another out-of-bounds read that can leak adjacent data or crash.
- **No NULL check** (defensive, depends on contract): if callers can pass `table == NULL`, this dereferences a null pointer.

**Reasoning**

- C array indexing is zero-based, so the exclusive upper bound is `len`, not `len + 1`. The check must reject equality.
- Signed comparison means all negative values are "less than" `len`, so they sail through. Attackers who control `idx` can read arbitrary offsets below the array base — a potential info-leak primitive.
- Note also that `-1` is ambiguous as an error sentinel if the table can legitimately contain `-1`; not a memory-safety bug, but an API smell.

**Fixed Version**

```c
static int lookup(const int *table, int len, int idx) {
    if (table == NULL || idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Alternatively, use an unsigned index type (`size_t`) to eliminate the negative case, keeping the `idx >= len` exclusive check.

Full over-the-wire log: [wire.md](wire.md)
