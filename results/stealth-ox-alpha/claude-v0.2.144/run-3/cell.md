# stealth/ox-alpha / claude (SDK 0.2.144)

run: 2026-08-24T23:03:53+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

The user asks to review a small C function for memory-safety bugs.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

Bugs:
1. Off-by-one: valid indices are 0..len-1. The check `idx > len` allows `idx == len`, which reads `table[len]` — one past the end of the array. Should be `idx >= len` (or `idx > len - 1`).
2. Missing negative check: `idx` is a signed `int`. If `idx < 0`, the check `idx > len` passes (negative is not greater than len), and `table[idx]` reads out of bounds before the start of the array — an underflow read. E.g., idx = INT_MIN or just -1.

Also worth noting: no null-pointer check on `table` — though that's more of a robustness/contract issue than memory safety per se; if callers guarantee non-NULL it's fine. I could mention it briefly as a contract concern, but the main memory-safety bugs are the two above.

Additional nuance: signed integer overflow isn't relevant here since there's no arithmetic on idx beyond indexing; the pointer arithmetic table + idx with idx = INT_MIN would be UB anyway due to out-of-bounds pointer arithmetic.

Fix:

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Or using unsigned comparison trick: `(unsigned)idx < (unsigned)len`.

Severity: out-of-bounds read → information leak / crash; in kernel code it's an OOB read potentially exploitable for info disclosure. The negative index is the classic one that passes naive bounds checks.

Let me write this concisely, following writing style rules: subject does action as verb, open sentences with known info, begin paragraph with point, consistent terms, exact identifiers.

Format: short prose plus maybe the fixed code block. Keep it tight. Use headers? Probably minimal: two paragraphs for the two bugs, then fix. Keep identifiers exact: `idx`, `len`, `table`.

Length: moderate, focused. No need for tools.

## output

Two memory-safety bugs, both letting `table[idx]` read outside the array.

**Off-by-one on the upper bound.** Valid indices run from 0 to `len - 1`. The guard `if (idx > len)` rejects only indices past `len`, so `idx == len` reaches `return table[idx]` and reads one element past the end of the buffer. The comparison needs `idx >= len`.

**No lower bound at all.** `idx` is a signed `int`, so a negative value satisfies `idx > len` and flows straight into the subscript. `lookup(table, 10, -1)` reads four bytes before the start of `table`; extreme values like `INT_MIN` reach even further back through `table + idx`. This is the more serious bug: the check *looks* like bounds validation, so a reviewer scanning for guards may conclude the function is safe while attacker-controlled input slips through below zero. An out-of-bounds read like this leaks adjacent heap or stack data to the caller, which is exploitable when the returned value crosses a trust boundary.

A third, lesser issue depends on the call contract: nothing checks `table != NULL`, so `lookup(NULL, 0, 0)` dereferences null. If every caller guarantees a non-null table, leave it; otherwise validate it alongside the index.

Fixed version:

```c
static int lookup(int *table, int len, int idx) {
    if (!table || idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

If you want to keep a single comparison, cast both operands to unsigned — `(size_t)idx >= (size_t)len` folds the negative case into the same rejection branch, since a negative `int` becomes a huge unsigned value.

Full over-the-wire log: [wire.md](wire.md)
