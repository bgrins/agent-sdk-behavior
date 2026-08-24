# anthropic/claude-opus-5 / claude (SDK 0.2.144)

run: 2026-08-24T23:12:26+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`

## thinking

I found two bugs: the check `idx > len` should be `idx >= len` since valid indices only run 0 to len-1, and there's also no guard against negative indices, so `idx < 0` slips through and reads before the buffer.

I'll fix it by adding both bounds checks (and a null check on table) before indexing, returning an error code if any fail. I'll write up the corrected function and explain the fixes.

## output

## Two memory-safety bugs

**1. Off-by-one in the bounds check (`>` should be `>=`)**

Valid indices for a `len`-element array run `0` through `len-1`. The guard rejects only `idx > len`, so `idx == len` passes and `table[len]` reads one element past the end of the buffer. That is a 4-byte out-of-bounds read on typical platforms — undefined behavior, and in practice it leaks whatever adjacent heap or stack data follows the array. Classic off-by-one, and the most likely one to survive testing, since `lookup(t, n, n)` looks superficially in range.

**2. No lower-bound check**

Nothing rejects negative `idx`. Because `idx` is a signed `int`, `-1` passes the guard (`-1 > len` is false) and `table[-1]` reads *before* the buffer. This is the more dangerous of the two: the offset is attacker-scaled, not fixed. An `idx` of `-1000000` computes the address `table + (-1000000 * sizeof(int))`, reading roughly 4 MB below the array. If `idx` derives from untrusted input — a parsed protocol field, a JSON number, an ID from a request — the caller gets an arbitrary-offset read primitive, usable to leak pointers or defeat ASLR.

**Secondary concern:** `-1` is both the error code and a legitimate `int` value a table can hold, so callers cannot distinguish "out of range" from "the stored value is -1". Not a memory-safety bug in this function, but it invites one in callers who treat a real `-1` payload as an error and then proceed with uninitialized state.

## Fix

```c
static int lookup(const int *table, size_t len, size_t idx, int *out) {
    if (!table || !out || idx >= len) return -1;
    *out = table[idx];
    return 0;
}
```

Switching `idx` and `len` to `size_t` collapses both bugs into the single check `idx >= len`: a negative value passed by a caller converts to a huge unsigned value, which that comparison rejects. This only works if *both* operands are unsigned — mixing a signed `idx` with an unsigned `len` makes the compiler convert `idx` to unsigned anyway, which happens to be safe here but is fragile and warns under `-Wsign-compare`. Keep them the same type.

Separating the value from the status via `out` removes the `-1` ambiguity. The `const` on `table` documents that `lookup` only reads.

If the signature must stay as written, the minimal correct guard is:

```c
if (idx < 0 || idx >= len) return -1;
```

Order matters for readability, not correctness, here — but check both ends, always.

Full over-the-wire log: [wire.md](wire.md)
