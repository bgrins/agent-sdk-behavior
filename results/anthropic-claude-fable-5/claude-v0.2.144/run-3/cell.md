# anthropic/claude-fable-5 / claude (SDK 0.2.144)

run: 2026-08-24T23:14:23+00:00 · prompt: `default.md` (sha256 071ebc17e17f)

wire settings: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`

wire settings: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`

## thinking

I'm spotting two real bugs: the bounds check should use `>=` instead of `>`, since `idx == len` already reads past the end, and since `idx` is signed, negative values slip through the check and cause an out-of-bounds read before the array starts. There's also a design concern with the sentinel value -1 potentially colliding with legitimate table entries.

## output

Two out-of-bounds reads, both in the bounds check.

**1. Off-by-one: `idx == len` passes the check**

Valid indices for a `len`-element array are `0` through `len - 1`. The check `idx > len` lets `idx == len` through, so `table[len]` reads one element past the end. The comparison must be `idx >= len`.

**2. Negative `idx` passes the check**

`idx` is a signed `int`, and the check has no lower bound. A call like `lookup(table, 10, -4)` satisfies `-4 > 10 == false`, falls through, and reads `table[-4]` — an out-of-bounds read before the array. Depending on what precedes the buffer, this can leak adjacent memory (heap metadata, other objects) or crash. The check needs `idx < 0` as well.

Corrected:

```c
static int lookup(int *table, int len, int idx) {
    if (idx < 0 || idx >= len) return -1;
    return table[idx];
}
```

Two secondary issues worth noting:

- **The error sentinel is ambiguous.** `-1` is also a valid table value, so callers cannot distinguish "index rejected" from "table holds -1". If callers branch on that, a caller-side bug can follow. A safer signature returns status separately: `bool lookup(const int *table, int len, int idx, int *out)`.
- **No NULL check on `table`, and a negative `len` is accepted.** If callers guarantee both, fine — but if `len` can ever be negative, every `idx >= 0` passes `idx >= len` is false only when `idx < len`, so the corrected check already handles it (`idx >= len` rejects everything when `len <= 0`). The NULL case still dereferences unless callers guarantee otherwise.

The reasoning pattern: for any index check, verify both edges (lower and upper) and verify the upper edge uses `>=`, not `>`. Signed index types make the missing lower bound exploitable, not just theoretical — attacker-controlled negative indices are a classic primitive for reading (or with a write, corrupting) memory at controlled negative offsets.

Full over-the-wire log: [wire.md](wire.md)
