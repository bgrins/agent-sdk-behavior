# anthropic/claude-sonnet-5 / codex (SDK 0.147.0)

run: 2026-08-24T23:13:01+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-sonnet-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

I'm spotting an off-by-one bug: the bounds check uses `idx > len` instead of `idx >= len`, so when idx equals len it still accesses table[len], which is out of range. Also there's no check for negative idx, so a negative index would slip past the check and cause an out-of-bounds access too.

## output

## Memory-Safety Bugs

**Off-by-one on the upper bound**
The guard `if (idx > len) return -1;` only rejects indices *greater than* `len`. When `idx == len`, the check passes and the function returns `table[len]`, which is one past the last valid element (valid indices for a table of length `len` are `0 .. len-1`). This is a classic off-by-one out-of-bounds read.

**Missing lower-bound check**
There is no check that `idx >= 0`. If a caller passes a negative `idx` (e.g. `-1`), the condition `idx > len` is false (assuming `len >= 0`), so execution falls through to `table[idx]`, reading memory *before* the start of the array. This is an out-of-bounds read that can leak arbitrary memory or crash the process, and is a more severe issue than the off-by-one since it has no proximity constraint — very negative indices can reach far outside the allocation.

**Combined effect**
Together these mean `lookup` performs unchecked, attacker/caller-controlled pointer arithmetic (`table + idx`) for any `idx` in `(-∞, -1] ∪ {len}` (and beyond `len` is correctly blocked only for values greater than `len`, but `len` itself is not). This is an out-of-bounds read vulnerability (CWE-125), and if this pattern is mirrored elsewhere for writes it would be CWE-787.

## Fix

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

This corrects both the missing lower bound (`idx < 0`) and the off-by-one (`idx >= len` instead of `idx > len`).

Full over-the-wire log: [wire.md](wire.md)
