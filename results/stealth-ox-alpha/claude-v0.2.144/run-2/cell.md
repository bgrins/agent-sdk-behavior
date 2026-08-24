# stealth/ox-alpha / claude (SDK 0.2.144)

run: 2026-08-24T23:03:24+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`

## thinking

Let me look at this function carefully.

```c
static int lookup(int *table, int len, int idx) {
    if (idx > len) return -1;
    return table[idx];
}
```

The intent: bounds check `idx` against `len`, then index into `table`.

Bugs:

1. **Off-by-one / boundary check is wrong direction of inequality**: Valid indices are 0..len-1. The check rejects only `idx > len`, so `idx == len` passes and reads `table[len]` — out of bounds read (one past the end). Should be `if (idx >= len)`.

2. **Missing lower bound check / signedness**: `idx` is `int`. If negative, `idx > len` is false (assuming len >= 0), so the function returns `table[idx]` with a negative index — out-of-bounds read before the buffer. This is a classic OOB read that can leak memory or crash. Fix: `if (idx < 0 || idx >= len) return -1;` or make idx unsigned... but making it unsigned has its own trap: if a caller passes a negative int converted to huge unsigned, then comparison with unsigned len would catch it, but if len stays int and idx unsigned, usual arithmetic conversions convert len to unsigned too — actually if idx is size_t and len is int, len converts to size_t; negative idx as size_t becomes huge; `idx > (size_t)len` catches negatives. But careful with `len <= 0` cases.

3. **`table` NULL not checked** — arguably out of scope for memory-safety within the function contract, but worth noting: if table can be NULL when len==0... Actually if len == 0 and idx == 0, current code: idx(0) > len(0)? No → returns table[0], reading through possibly-NULL pointer even though table has zero elements. So even the "empty table" case reads out of bounds. Good to mention.

4. **Return value collision**: `-1` sentinel vs legitimate table values of -1. Not memory safety but correctness/robustness. Maybe mention briefly.

5. Also note `len` could be negative — then any non-negative idx passes? If len = -1, idx = 0: 0 > -1 → return -1. OK that's fine actually. Negative idx with negative len still passes to table[idx] if idx <= len... e.g., idx=-5, len=-3: -5 > -3 false → table[-5] OOB.

Also mention exploitability: negative index OOB read → information disclosure; idx == len one-past-end read.

Fix:

```c
static int lookup(const int *table, size_t len, size_t idx) {
    if (idx >= len) return -1;
    return table[idx];
}
```

Using size_t makes negative indices impossible at the type level, but callers passing int must be checked at call sites. Alternatively keep ints: `if (idx < 0 || idx >= len) return -1;`

Note the subtlety about mixing signed/unsigned in comparisons.

Format: concise prose per writing style rules, exact identifiers. Use headers or just short paragraphs plus a fix block. Keep it tight. The user asked "review this function for memory-safety bugs and explain your reasoning."

I should structure: two real memory-safety bugs (upper-bound off-by-one, missing negative check), plus the empty-table/NULL interaction, plus brief notes on non-memory-safety issues (-1 collision), then fixed version.

Writing style: begin paragraphs with point, subject does action. Keep identifiers exact.

## output

Two bugs let this function read outside `table`: the upper bound is off by one, and nothing rejects negative indexes.

## Bug 1: `idx == len` passes the check

Valid indexes run from `0` to `len - 1`. The guard `idx > len` only rejects values past `len`, so `lookup(t, 4, 4)` reaches `table[4]` — one element past the end. That is an out-of-bounds read on every call where the caller passes the length itself, which is a natural thing to do when probing for the end of the table. The condition needs to be `idx >= len`.

## Bug 2: negative `idx` bypasses the guard entirely

`idx` is `int`. For any negative `idx` and non-negative `len`, the comparison `idx > len` is false, so control falls straight through to `table[idx]` with a negative offset. `lookup(t, 10, -3)` reads three ints below the array. Unlike the off-by-one, this one is attacker-relevant whenever `idx` comes from external input: a negative value turns the bounds check into a no-op while reading arbitrary memory before the allocation, which is an information-disclosure primitive, not just a crash.

The same hole appears with a negative `len`: `lookup(t, -3, -5)` also indexes out of bounds, since `-5 > -3` is false.

## Bug 3: the empty-table case reads anyway

With `len == 0` the table has no elements, yet `lookup(t, 0, 0)` skips the guard (`0 > 0` is false) and dereferences `table[0]`. If callers represent "no table" as `{NULL, 0}` — a common convention — this is a null-pointer dereference rather than a mere over-read. Bug 1's fix covers this case automatically, which is worth knowing when you weigh whether the `NULL` check matters here.

## Non-memory-safety notes

Returning `-1` as the error sentinel collides with any table element equal to `-1`; callers cannot distinguish a miss from a hit. That is a correctness issue, not a safety one, but it will surface once the bounds check works. `table` should also be `const int *` since the function only reads.

## Fixed version

Keeping `int` parameters, one compound test closes all three holes:

```c
static int lookup(const int *table, int len, int idx) {
    if (idx < 0 || idx >= len)
        return -1;
    return table[idx];
}
```

Switching `idx` and `len` to `size_t` removes the negative-input problem at the type level, but only if every caller already validated its own inputs before the conversion — a negative `int` silently becomes a huge `size_t` at the call boundary, and mixed signed/unsigned comparisons in this function would convert `len` instead of catching `idx`. Prefer the explicit `idx < 0` test unless you change the signature everywhere at once.

Full over-the-wire log: [wire.md](wire.md)
