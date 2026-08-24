# minimax/minimax-m3 / codex (SDK 0.147.0)

run: 2026-08-24T22:44:49+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "minimax/minimax-m3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

The user is asking me to review a C function for memory-safety bugs. This is a straightforward code review question, not a code modification task. I should just analyze it and explain my reasoning.

Let me analyze the function:

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

Issues I can spot:

1. **Missing lower bound check**: The function checks `idx > len` but doesn't check `idx < 0`. If `idx` is negative, the function returns `table[idx]`, which accesses memory before the start of the array — undefined behavior and an out-of-bounds read.

2. **Off-by-one on upper bound**: The check `idx > len` allows `idx == len`, but valid indices are `0` to `len - 1`. When `idx == len`, this reads one past the end of the array (off-by-one / buffer over-read by one element).

3. **Signed comparison pitfall**: `idx` and `len` are both `int`. If `len` could ever be negative, the semantics get weird, but since `len` is passed by the caller, the main concern is the negative `idx` case.

4. **No NULL check on `table`**: If `table` is NULL, dereferencing it is UB. Not strictly a memory-safety bug in the array-bounds sense, but worth mentioning.

The two primary memory-safety bugs are:
- Negative `idx` not rejected
- `idx == len` not rejected (off-by-one)

Let me write a clear, concise response. Since this is a casual review question, I should be conversational but use structured formatting where helpful. The user wants the bugs explained with reasoning, so I'll use bullets.

I don't need to use any tools — this is purely an analysis task. No file reading, no commands, no plan needed.

## output

**Memory-Safety Bugs**

- **No lower-bound check on `idx`** — `idx > len` only rejects indices that are *larger* than `len`. If `idx` is negative, the guard passes and the function dereferences `table[idx]`, which lands before the start of the array. That's a classic out-of-bounds read (heap or stack, depending on where `table` lives) and undefined behavior. The fix is `idx < 0` in the condition (or `idx >= len` flipped correctly).

- **Off-by-one on the upper bound** — even ignoring negatives, valid indices for an array of length `len` are `0 … len - 1`. The check `idx > len` lets `idx == len` through, so `return table[len]` reads one element past the end of the buffer. The guard should be `idx >= len` (i.e. reject when `idx` is *not strictly less than* `len`).

**Other Smells (not strictly OOB, but worth flagging)**

- **Signed-typed length/index** — `len` and `idx` are both `int`. If a caller ever passes a negative `len`, the `idx > len` comparison can return true for *every* non-negative `idx`, so the guard does nothing meaningful. For a bounds-checked API, `size_t` (or at least unsigned) is the conventional choice and removes the ambiguity.
- **No NULL check on `table`** — passing `NULL` reaches `return table[idx]` and dereferences it. Adding `if (!table) return -1;` (or asserting in debug builds) closes that hole.
- **Return-value collision** — `-1` doubles as both "index out of range" and a legitimate element value the caller may have stored. Not memory-safety, but it makes the contract ambiguous; using `INT_MIN` or returning via an out-parameter is safer.

**Corrected Core Guard**

```c
if (idx < 0 || idx >= len) return -1;
return table[idx];
```

That single change eliminates both OOB reads.

Full over-the-wire log: [wire.md](wire.md)
