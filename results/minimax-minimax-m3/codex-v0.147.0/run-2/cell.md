# minimax/minimax-m3 / codex (SDK 0.147.0)

run: 2026-08-24T23:20:46+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "minimax/minimax-m3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

## thinking

The user is asking me to review a C function for memory-safety bugs. This is a code review task, not a coding task. Let me analyze the function carefully.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

Let me identify the memory-safety bugs:

1. **Off-by-one error in bounds check**: The condition `idx > len` allows `idx == len`, which is out of bounds. Valid indices are `0` to `len-1`. So when `idx == len`, `table[idx]` reads past the end of the array. This is a classic off-by-one error.

2. **No lower bound check**: Negative indices are not checked. `idx` could be negative, leading to `table[idx]` reading memory before the start of the array. This is an arbitrary read vulnerability.

3. **No NULL check on `table`**: If `table` is NULL and idx happens to be... well, if idx is 0 or negative and table is NULL, it would crash. But more importantly, there's no defensive check.

4. **Possible signed integer issue**: `idx` is `int`, which is signed. If someone passes a very large value (like `INT_MAX`), the comparison might work but accessing `table[idx]` with such an index could read way past the buffer.

5. **`len` should also be checked for negative values**: If `len` is negative, the comparison `idx > len` would be true for most reasonable `idx` values, returning -1, which would mask the issue. But it's still a sign issue.

The most critical bugs are:
- Off-by-one: `idx > len` should be `idx >= len` (or `idx < 0 || idx >= len`)
- No negative index check: allows arbitrary memory read
- No NULL pointer check on `table`

This is a security-sensitive code review. I should be precise and explain each bug clearly.

Let me format my response according to the final answer guidelines. Since this is a focused code review with multiple distinct issues, I'll use headers to organize them. Keep it concise but thorough.

The user wants me to explain my reasoning, so I should be clear about each bug and why it's a problem.

## output

**Memory-Safety Bugs**

- **Off-by-one in upper bound (most critical)** — `idx > len` should be `idx >= len`. Valid indices are `0..len-1`, but this check permits `idx == len`, causing `table[idx]` to read one element past the end of the buffer.

- **Missing lower-bound check** — Nothing rejects a negative `idx`. With a negative index, `table[idx]` reads memory before the array (arbitrary out-of-bounds read). A signed comparison is the only thing standing between attacker-controlled input and an out-of-bounds access.

- **Unsigned/signed length confusion** — `len` is `int`. A negative `len` makes `idx > len` true for almost any index, so the function silently returns `-1` instead of validating that the array actually exists. Use `size_t` for lengths and `ssize_t` (or check explicitly) for indices.

- **No NULL check on `table`** — If `table` is NULL and the bounds check passes (e.g., `idx == 0`), this is a null-pointer dereference. Typically you assert or return early before the dereference.

**Corrected Version**

```c
static int lookup(const int *table, size_t len, ssize_t idx) {
    if (table == NULL || idx < 0 || (size_t)idx >= len) return -1;
    return table[idx];
}
```

**Severity**
The off-by-one plus missing lower-bound check combine into an arbitrary read primitive if `idx` ever comes from untrusted input (a parsed message, network packet, file, etc.) — a common source of CVEs in C parsers.

Full over-the-wire log: [wire.md](wire.md)
