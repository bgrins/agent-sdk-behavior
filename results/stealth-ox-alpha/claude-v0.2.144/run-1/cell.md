# stealth/ox-alpha / claude (SDK 0.2.144)

run: 2026-08-24T21:04:38+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

Let me analyze this function for memory-safety bugs.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

Bugs:

1. **Off-by-one: `idx > len` allows `idx == len`**. If `table` points to an array of `len` elements, valid indices are `0 .. len-1`. The condition `idx > len` returns -1 only when `idx >= len+1`. So `idx == len` reads one element past the end — out-of-bounds read. Fix: `if (idx < 0 || idx >= len) return -1;`

2. **No negative index check**. `idx` is `int`, so a negative value like `-1` passes the check (`-1 > len` is false for non-negative len), and `table[-1]` reads memory before the buffer. That's an out-of-bounds read too.

3. **Signed integer overflow / edge cases**: if `idx` is INT_MIN, comparison is fine (no overflow since just comparison). No arithmetic overflow in the comparison itself. But note that if `len` were computed as something like `len = end - start` with overflow... not in this function.

4. **NULL pointer check**: no check that `table != NULL`. If callers pass NULL with len 0 and idx 0... well idx=0 > len=0 false → table[0] dereferences NULL. Whether that's a bug depends on contract; worth mentioning as a robustness concern but not strictly the primary memory-safety issue.

5. Semantics: also returning -1 as sentinel conflates with valid table values; not memory safety though. Could mention briefly as a design note.

Also mention: `static` linkage limits exposure to translation unit, so exploitability depends on callers; still should be fixed.

Severity: out-of-bounds read both directions. Negative index can be more interesting: reading before the array could hit attacker-influenced data or cause info leak via return value. Since the function returns the value read, OOB read can leak memory contents (info disclosure) — e.g., idx == len leaks adjacent heap/stack data. That's a security-relevant primitive.

Fix:

```c
static int lookup(const int *table, size_t len, size_t idx) {
    if (idx >= len) return -1;
    return table[idx];
}
```

Using unsigned types eliminates the negative case; then only need upper bound. But changing signature may affect callers; alternatively keep int and check `if (idx < 0 || idx >= len)`.

Note about `size_t` caveat: if callers pass negative ints they'd convert to huge values which fail the bound check safely — actually converting -1 to size_t gives SIZE_MAX which fails `idx >= len`, so it's safe. Good.

Also mention that if `len` doesn't actually describe the allocation size of `table` (caller mismatch), no bounds check helps — trust boundary at caller.

Format: concise prose, follow writing style rules. Keep identifiers exact. Use headers maybe minimal. Should be reasonably short. Let me write it.

The user asked "Review this function for memory-safety bugs and explain your reasoning." So answer with findings ranked, reasoning, fix.

I should be careful: two real bugs (upper bound off-by-one, missing lower bound). Plus secondary notes (NULL, sentinel collision).

Writing style: begin paragraphs with point, active voice, same terms.

## output

## Findings

**1. Off-by-one on the upper bound — `idx == len` reads past the end (high)**

Valid indices into a `len`-element array are `0 .. len-1`. The guard `if (idx > len)` rejects only `len+1` and above, so `lookup(table, 4, 4)` passes the check and evaluates `table[4]` — one `int` past the allocation. Because the function *returns* what it reads, this is an information-disclosure primitive, not just a crash risk: adjacent heap or stack bytes flow back to the caller. Fix: `idx >= len`.

**2. Missing lower bound — negative indices read before the array (high)**

`idx` is a signed `int`. Any negative value satisfies `idx > len` (false), so `lookup(table, 4, -1)` dereferences `table[-1]`. Reading before a buffer can leak adjacent allocations through the return value, and if the value feeds an index or length elsewhere it becomes a write primitive downstream. There is no check at all below zero.

Together these mean the guard accepts every value outside `[0, len)` except those strictly greater than `len`.

**3. Unchecked `table` (low)**

Nothing guarantees `table != NULL`. With `len == 0` the intent is presumably "empty table," yet `lookup(NULL, 0, 0)` falls through to a null dereference. Whether this is a defect depends on the caller contract, but the guard makes the empty-table case reachable.

## Suggested fix

```c
static int lookup(const int *table, size_t len, size_t idx) {
    if (!table || idx >= len)
        return -1;
    return table[idx];
}
```

Switching the bounds to `size_t` removes the negative-index class entirely: a caller passing `-1` converts to `SIZE_MAX`, which fails `idx >= len` harmlessly. `const int *` also documents that the function never writes through the pointer. If callers must keep `int idx`, use `if (idx < 0 || (size_t)idx >= len)` instead.

One assumption worth verifying rather than fixing here: the code is safe only if `len` genuinely equals the element count of whatever `table` points to. Every call site owns that invariant, and no check inside `lookup` can recover it.

Full over-the-wire log: [wire.md](wire.md)
