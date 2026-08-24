# Agent SDK behavior grid

Cells accumulate per model x harness x SDK version; rerunning a cell refreshes it. Harness isolation: fresh `CODEX_HOME` / `CLAUDE_CONFIG_DIR` · gateway: OpenRouter · effort high.

| model | claude-v0.2.144/run-1 | claude-v0.2.144/run-2 | claude-v0.2.144/run-3 | codex-v0.147.0/run-1 | codex-v0.147.0/run-2 | codex-v0.147.0/run-3 |
|---|---|---|---|---|---|---|
| `anthropic/claude-fable-5` | ✅ [cell](anthropic-claude-fable-5/claude-v0.2.144/run-1/cell.md) · 207 thinking chars | ✅ [cell](anthropic-claude-fable-5/claude-v0.2.144/run-2/cell.md) · 493 thinking chars | ✅ [cell](anthropic-claude-fable-5/claude-v0.2.144/run-3/cell.md) · 356 thinking chars | ✅ [cell](anthropic-claude-fable-5/codex-v0.147.0/run-1/cell.md) · 55 thinking chars | ✅ [cell](anthropic-claude-fable-5/codex-v0.147.0/run-2/cell.md) · 55 thinking chars | ✅ [cell](anthropic-claude-fable-5/codex-v0.147.0/run-3/cell.md) · 81 thinking chars |
| `anthropic/claude-haiku-4.5` | ✅ [cell](anthropic-claude-haiku-4.5/claude-v0.2.144/run-1/cell.md) · 1156 thinking chars | ✅ [cell](anthropic-claude-haiku-4.5/claude-v0.2.144/run-2/cell.md) · 1477 thinking chars | ✅ [cell](anthropic-claude-haiku-4.5/claude-v0.2.144/run-3/cell.md) · 1795 thinking chars | ✅ [cell](anthropic-claude-haiku-4.5/codex-v0.147.0/run-1/cell.md) · 1254 thinking chars | ✅ [cell](anthropic-claude-haiku-4.5/codex-v0.147.0/run-2/cell.md) · 1319 thinking chars | ✅ [cell](anthropic-claude-haiku-4.5/codex-v0.147.0/run-3/cell.md) · 1906 thinking chars |
| `anthropic/claude-opus-5` | ✅ [cell](anthropic-claude-opus-5/claude-v0.2.144/run-1/cell.md) · 196 thinking chars | ✅ [cell](anthropic-claude-opus-5/claude-v0.2.144/run-2/cell.md) · 395 thinking chars | ✅ [cell](anthropic-claude-opus-5/claude-v0.2.144/run-3/cell.md) · 226 thinking chars | ✅ [cell](anthropic-claude-opus-5/codex-v0.147.0/run-1/cell.md) · 153 thinking chars | ✅ [cell](anthropic-claude-opus-5/codex-v0.147.0/run-2/cell.md) · 913 thinking chars | ✅ [cell](anthropic-claude-opus-5/codex-v0.147.0/run-3/cell.md) · 680 thinking chars |
| `anthropic/claude-sonnet-5` | ✅ [cell](anthropic-claude-sonnet-5/claude-v0.2.144/run-1/cell.md) · 299 thinking chars | ✅ [cell](anthropic-claude-sonnet-5/claude-v0.2.144/run-2/cell.md) · 206 thinking chars | ✅ [cell](anthropic-claude-sonnet-5/claude-v0.2.144/run-3/cell.md) · 309 thinking chars | ✅ [cell](anthropic-claude-sonnet-5/codex-v0.147.0/run-1/cell.md) · 499 thinking chars | ✅ [cell](anthropic-claude-sonnet-5/codex-v0.147.0/run-2/cell.md) · 210 thinking chars | ✅ [cell](anthropic-claude-sonnet-5/codex-v0.147.0/run-3/cell.md) · 291 thinking chars |
| `deepseek/deepseek-v4-flash` | ✅ [cell](deepseek-deepseek-v4-flash/claude-v0.2.144/run-1/cell.md) · 2010 thinking chars | ✅ [cell](deepseek-deepseek-v4-flash/claude-v0.2.144/run-2/cell.md) · 1292 thinking chars | ✅ [cell](deepseek-deepseek-v4-flash/claude-v0.2.144/run-3/cell.md) · 582 thinking chars | ✅ [cell](deepseek-deepseek-v4-flash/codex-v0.147.0/run-1/cell.md) · 904 thinking chars | ✅ [cell](deepseek-deepseek-v4-flash/codex-v0.147.0/run-2/cell.md) · 2611 thinking chars | ✅ [cell](deepseek-deepseek-v4-flash/codex-v0.147.0/run-3/cell.md) · 962 thinking chars |
| `deepseek/deepseek-v4-pro` | ✅ [cell](deepseek-deepseek-v4-pro/claude-v0.2.144/run-1/cell.md) · 64 thinking chars | ✅ [cell](deepseek-deepseek-v4-pro/claude-v0.2.144/run-2/cell.md) · 999 thinking chars | ✅ [cell](deepseek-deepseek-v4-pro/claude-v0.2.144/run-3/cell.md) · 64 thinking chars | ✅ [cell](deepseek-deepseek-v4-pro/codex-v0.147.0/run-1/cell.md) · 1050 thinking chars | ✅ [cell](deepseek-deepseek-v4-pro/codex-v0.147.0/run-2/cell.md) · 1131 thinking chars | ✅ [cell](deepseek-deepseek-v4-pro/codex-v0.147.0/run-3/cell.md) · 1029 thinking chars |
| `google/gemini-3.1-pro-preview` | ✅ [cell](google-gemini-3.1-pro-preview/claude-v0.2.144/run-1/cell.md) · 828 thinking chars | ✅ [cell](google-gemini-3.1-pro-preview/claude-v0.2.144/run-2/cell.md) · 937 thinking chars | ✅ [cell](google-gemini-3.1-pro-preview/claude-v0.2.144/run-3/cell.md) · 1016 thinking chars | ✅ [cell](google-gemini-3.1-pro-preview/codex-v0.147.0/run-1/cell.md) · 1334 thinking chars | ✅ [cell](google-gemini-3.1-pro-preview/codex-v0.147.0/run-2/cell.md) · 857 thinking chars | ✅ [cell](google-gemini-3.1-pro-preview/codex-v0.147.0/run-3/cell.md) · 893 thinking chars |
| `google/gemini-3.7-flash` | ✅ [cell](google-gemini-3.7-flash/claude-v0.2.144/run-1/cell.md) · 1877 thinking chars | ✅ [cell](google-gemini-3.7-flash/claude-v0.2.144/run-2/cell.md) · 1578 thinking chars | ✅ [cell](google-gemini-3.7-flash/claude-v0.2.144/run-3/cell.md) · 1938 thinking chars | ✅ [cell](google-gemini-3.7-flash/codex-v0.147.0/run-1/cell.md) · 936 thinking chars | ✅ [cell](google-gemini-3.7-flash/codex-v0.147.0/run-2/cell.md) · 1374 thinking chars | ✅ [cell](google-gemini-3.7-flash/codex-v0.147.0/run-3/cell.md) · 811 thinking chars |
| `minimax/minimax-m3` | ✅ [cell](minimax-minimax-m3/claude-v0.2.144/run-1/cell.md) · 4545 thinking chars | ✅ [cell](minimax-minimax-m3/claude-v0.2.144/run-2/cell.md) · 1725 thinking chars | ✅ [cell](minimax-minimax-m3/claude-v0.2.144/run-3/cell.md) · 3437 thinking chars | ✅ [cell](minimax-minimax-m3/codex-v0.147.0/run-1/cell.md) · 1660 thinking chars | ✅ [cell](minimax-minimax-m3/codex-v0.147.0/run-2/cell.md) · 2007 thinking chars | ✅ [cell](minimax-minimax-m3/codex-v0.147.0/run-3/cell.md) · 2830 thinking chars |
| `moonshotai/kimi-k3` | ✅ [cell](moonshotai-kimi-k3/claude-v0.2.144/run-1/cell.md) · 6006 thinking chars | ✅ [cell](moonshotai-kimi-k3/claude-v0.2.144/run-2/cell.md) · 6191 thinking chars | ✅ [cell](moonshotai-kimi-k3/claude-v0.2.144/run-3/cell.md) · 2137 thinking chars | ✅ [cell](moonshotai-kimi-k3/codex-v0.147.0/run-1/cell.md) · 684 thinking chars | ✅ [cell](moonshotai-kimi-k3/codex-v0.147.0/run-2/cell.md) · 345 thinking chars | ✅ [cell](moonshotai-kimi-k3/codex-v0.147.0/run-3/cell.md) · 162 thinking chars |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | ✅ [cell](nvidia-nemotron-3-ultra-550b-a55b-free/claude-v0.2.144/run-1/cell.md) · 824 thinking chars | ✅ [cell](nvidia-nemotron-3-ultra-550b-a55b-free/claude-v0.2.144/run-2/cell.md) · 1002 thinking chars | ✅ [cell](nvidia-nemotron-3-ultra-550b-a55b-free/claude-v0.2.144/run-3/cell.md) · 785 thinking chars | ✅ [cell](nvidia-nemotron-3-ultra-550b-a55b-free/codex-v0.147.0/run-1/cell.md) · 574 thinking chars | ✅ [cell](nvidia-nemotron-3-ultra-550b-a55b-free/codex-v0.147.0/run-2/cell.md) · 736 thinking chars | ✅ [cell](nvidia-nemotron-3-ultra-550b-a55b-free/codex-v0.147.0/run-3/cell.md) · 833 thinking chars |
| `openai/gpt-5.6-luna` | ✅ [cell](openai-gpt-5.6-luna/claude-v0.2.144/run-1/cell.md) · 499 thinking chars | ✅ [cell](openai-gpt-5.6-luna/claude-v0.2.144/run-2/cell.md) · 1011 thinking chars | ✅ [cell](openai-gpt-5.6-luna/claude-v0.2.144/run-3/cell.md) · 533 thinking chars | ✅ [cell](openai-gpt-5.6-luna/codex-v0.147.0/run-1/cell.md) · 121 thinking chars | ✅ [cell](openai-gpt-5.6-luna/codex-v0.147.0/run-2/cell.md) · 121 thinking chars | ✅ [cell](openai-gpt-5.6-luna/codex-v0.147.0/run-3/cell.md) · 121 thinking chars |
| `openai/gpt-5.6-sol` | ⚠️ [cell](openai-gpt-5.6-sol/claude-v0.2.144/run-1/cell.md) · 0 thinking chars | ✅ [cell](openai-gpt-5.6-sol/claude-v0.2.144/run-2/cell.md) · 554 thinking chars | ⚠️ [cell](openai-gpt-5.6-sol/claude-v0.2.144/run-3/cell.md) · 0 thinking chars | ✅ [cell](openai-gpt-5.6-sol/codex-v0.147.0/run-1/cell.md) · 121 thinking chars | ✅ [cell](openai-gpt-5.6-sol/codex-v0.147.0/run-2/cell.md) · 121 thinking chars | ✅ [cell](openai-gpt-5.6-sol/codex-v0.147.0/run-3/cell.md) · 121 thinking chars |
| `openai/gpt-5.6-terra` | ⚠️ [cell](openai-gpt-5.6-terra/claude-v0.2.144/run-1/cell.md) · 0 thinking chars | ⚠️ [cell](openai-gpt-5.6-terra/claude-v0.2.144/run-2/cell.md) · 0 thinking chars | ⚠️ [cell](openai-gpt-5.6-terra/claude-v0.2.144/run-3/cell.md) · 0 thinking chars | ⚠️ [cell](openai-gpt-5.6-terra/codex-v0.147.0/run-1/cell.md) · 0 thinking chars | ⚠️ [cell](openai-gpt-5.6-terra/codex-v0.147.0/run-2/cell.md) · 0 thinking chars | ⚠️ [cell](openai-gpt-5.6-terra/codex-v0.147.0/run-3/cell.md) · 0 thinking chars |
| `openai/gpt-oss-120b` | ✅ [cell](openai-gpt-oss-120b/claude-v0.2.144/run-1/cell.md) · 523 thinking chars | ✅ [cell](openai-gpt-oss-120b/claude-v0.2.144/run-2/cell.md) · 208 thinking chars | ✅ [cell](openai-gpt-oss-120b/claude-v0.2.144/run-3/cell.md) · 872 thinking chars | ✅ [cell](openai-gpt-oss-120b/codex-v0.147.0/run-1/cell.md) · 2896 thinking chars | ✅ [cell](openai-gpt-oss-120b/codex-v0.147.0/run-2/cell.md) · 1975 thinking chars | ✅ [cell](openai-gpt-oss-120b/codex-v0.147.0/run-3/cell.md) · 2657 thinking chars |
| `qwen/qwen3.6-max-preview` | ✅ [cell](qwen-qwen3.6-max-preview/claude-v0.2.144/run-1/cell.md) · 93 thinking chars | ✅ [cell](qwen-qwen3.6-max-preview/claude-v0.2.144/run-2/cell.md) · 103 thinking chars | ✅ [cell](qwen-qwen3.6-max-preview/claude-v0.2.144/run-3/cell.md) · 99 thinking chars | ✅ [cell](qwen-qwen3.6-max-preview/codex-v0.147.0/run-1/cell.md) · 1449 thinking chars | ✅ [cell](qwen-qwen3.6-max-preview/codex-v0.147.0/run-2/cell.md) · 1312 thinking chars | ✅ [cell](qwen-qwen3.6-max-preview/codex-v0.147.0/run-3/cell.md) · 1237 thinking chars |
| `stealth/ox-alpha` | ✅ [cell](stealth-ox-alpha/claude-v0.2.144/run-1/cell.md) · 3111 thinking chars | ✅ [cell](stealth-ox-alpha/claude-v0.2.144/run-2/cell.md) · 3096 thinking chars | ✅ [cell](stealth-ox-alpha/claude-v0.2.144/run-3/cell.md) · 1965 thinking chars | ✅ [cell](stealth-ox-alpha/codex-v0.147.0/run-1/cell.md) · 684 thinking chars | ⚠️ [cell](stealth-ox-alpha/codex-v0.147.0/run-2/cell.md) · 0 thinking chars | ✅ [cell](stealth-ox-alpha/codex-v0.147.0/run-3/cell.md) · 869 thinking chars |
| `z-ai/glm-5.2:free` | ✅ [cell](z-ai-glm-5.2-free/claude-v0.2.144/run-1/cell.md) · 803 thinking chars | ✅ [cell](z-ai-glm-5.2-free/claude-v0.2.144/run-2/cell.md) · 1261 thinking chars | ✅ [cell](z-ai-glm-5.2-free/claude-v0.2.144/run-3/cell.md) · 1134 thinking chars | ✅ [cell](z-ai-glm-5.2-free/codex-v0.147.0/run-1/cell.md) · 130 thinking chars | ⚠️ [cell](z-ai-glm-5.2-free/codex-v0.147.0/run-2/cell.md) · 0 thinking chars | ⚠️ [cell](z-ai-glm-5.2-free/codex-v0.147.0/run-3/cell.md) · 0 thinking chars |

## Thinking excerpts

**anthropic/claude-fable-5 / claude-v0.2.144/run-1**: This is a simple review question—the bug is that the bounds check uses `>` instead of `>=`, and negative indices and a null table aren't being checked either. I

**anthropic/claude-fable-5 / claude-v0.2.144/run-2**: This is a simple inline review, no tools needed. I'm spotting an off-by-one bug where the bounds check should use >= instead of >, allowing an out-of-bounds rea

**anthropic/claude-fable-5 / claude-v0.2.144/run-3**: I'm spotting two real bugs: the bounds check should use `>=` instead of `>`, since `idx == len` already reads past the end, and since `idx` is signed, negative 

**anthropic/claude-fable-5 / codex-v0.147.0/run-1**: This is a simple review question, no tools needed here.

**anthropic/claude-fable-5 / codex-v0.147.0/run-2**: This is a simple review question, no tools needed here.

**anthropic/claude-fable-5 / codex-v0.147.0/run-3**: This is a straightforward code review question, so I can just answer it directly.

**anthropic/claude-haiku-4.5 / claude-v0.2.144/run-1**: The user is asking me to review a C function for memory-safety bugs. Let me analyze this carefully. The function is: ```c static int lookup(int *table, int len,

**anthropic/claude-haiku-4.5 / claude-v0.2.144/run-2**: The user is asking me to review a C function for memory-safety bugs. This is a security code review task. Let me analyze this function carefully. The function i

**anthropic/claude-haiku-4.5 / claude-v0.2.144/run-3**: The user is asking me to review this C function for memory-safety bugs. Let me analyze it carefully. The function is: ```c static int lookup(int *table, int len

**anthropic/claude-haiku-4.5 / codex-v0.147.0/run-1**: This is a code review task where I need to analyze a C function for memory-safety bugs. Let me examine the code carefully: ```c static int lookup(int *table, in

**anthropic/claude-haiku-4.5 / codex-v0.147.0/run-2**: The user is asking me to review a C function for memory-safety bugs. Let me analyze the code: ```c static int lookup(int *table, int len, int idx) { if (idx > l

**anthropic/claude-haiku-4.5 / codex-v0.147.0/run-3**: The user is asking me to review a C function for memory-safety bugs. Let me analyze this carefully. The function is: ```c static int lookup(int *table, int len,

**anthropic/claude-opus-5 / claude-v0.2.144/run-1**: I spot the bug: the boundary check should use `>=` instead of `>`, and there's no guard against negative indices either. This is a straightforward fix I can jus

**anthropic/claude-opus-5 / claude-v0.2.144/run-2**: I found two bugs: the check `idx > len` should be `idx >= len` since valid indices only run 0 to len-1, and there's also no guard against negative indices, so `

**anthropic/claude-opus-5 / claude-v0.2.144/run-3**: I spot an off-by-one bug where the bounds check should use `>=` instead of `>`, plus missing checks for negative indices and a null table reference. This is str

**anthropic/claude-opus-5 / codex-v0.147.0/run-1**: This looks like a straightforward code review task—I should flag the off-by-one error in the loop bounds and the risk of a negative index causing issues.

**anthropic/claude-opus-5 / codex-v0.147.0/run-2**: This is a simple code review task, no tools needed. I'm spotting the boundary bug where the comparison should reject the index equal to the length too, plus the

**anthropic/claude-opus-5 / codex-v0.147.0/run-3**: This is a simple security review of a C function, no tools needed. I'm spotting several bugs: an off-by-one allowing idx == len to read past the buffer, a missi

**anthropic/claude-sonnet-5 / claude-v0.2.144/run-1**: I'm reviewing this table lookup function for bounds-checking bugs. There's no check for negative indices, allowing an out-of-bounds underflow read, and the uppe

**anthropic/claude-sonnet-5 / claude-v0.2.144/run-2**: I'm reviewing a simple table lookup function for bugs. There's an off-by-one error since the bounds check allows idx equal to len, which is out of range, and it

**anthropic/claude-sonnet-5 / claude-v0.2.144/run-3**: This is a direct question about a code snippet, so I can just analyze it. I'm spotting two bugs: there's no check for a negative index, so it could read out of 

**anthropic/claude-sonnet-5 / codex-v0.147.0/run-1**: I'm spotting two bugs: the bounds check allows idx equal to len, causing an out-of-bounds read one past the array's end, and there's no check for negative idx, 

**anthropic/claude-sonnet-5 / codex-v0.147.0/run-2**: I'm spotting a bug: the check should be `idx >= len` not `idx > len`, since valid indices run from 0 to len-1, and there's also no check for negative indices. L

**anthropic/claude-sonnet-5 / codex-v0.147.0/run-3**: I'm spotting an off-by-one bug: the bounds check uses `idx > len` instead of `idx >= len`, so when idx equals len it still accesses table[len], which is out of 

**deepseek/deepseek-v4-flash / claude-v0.2.144/run-1**: The user is asking me to review a C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx

**deepseek/deepseek-v4-flash / claude-v0.2.144/run-2**: The user is asking me to review a C function for memory-safety bugs and explain my reasoning. Let me analyze the code carefully. ```c static int lookup(int *tab

**deepseek/deepseek-v4-flash / claude-v0.2.144/run-3**: The function has a clear memory-safety bug. Let me analyze it: ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; return table[idx

**deepseek/deepseek-v4-flash / codex-v0.147.0/run-1**: The user wants me to review this C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx 

**deepseek/deepseek-v4-flash / codex-v0.147.0/run-2**: The user wants me to review a C function for memory-safety bugs. Let me analyze the `lookup` function: ```c static int lookup(int *table, int len, int idx) { if

**deepseek/deepseek-v4-flash / codex-v0.147.0/run-3**: The user wants me to review a C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > l

**deepseek/deepseek-v4-pro / claude-v0.2.144/run-1**: The user wants me to review a C function for memory-safety bugs.

**deepseek/deepseek-v4-pro / claude-v0.2.144/run-2**: The user wants me to review a C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > l

**deepseek/deepseek-v4-pro / claude-v0.2.144/run-3**: The user wants me to review a C function for memory-safety bugs.

**deepseek/deepseek-v4-pro / codex-v0.147.0/run-1**: Let me analyze this C function for memory-safety bugs. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; return table[idx]; } ```

**deepseek/deepseek-v4-pro / codex-v0.147.0/run-2**: Let me analyze this C function for memory-safety bugs. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; return table[idx]; } ```

**deepseek/deepseek-v4-pro / codex-v0.147.0/run-3**: The user wants me to review a C function for memory-safety bugs. Let me analyze it. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return

**google/gemini-3.1-pro-preview / claude-v0.2.144/run-1**: **Reviewing Code Functionality** I'm currently scrutinizing the `lookup` function, specifically focusing on its boundary checks. My primary concern is ensuring 

**google/gemini-3.1-pro-preview / claude-v0.2.144/run-2**: **Reviewing Function Code** I'm currently examining a small C function, `lookup`, which takes an integer array, its length, and an index as input. My focus is o

**google/gemini-3.1-pro-preview / claude-v0.2.144/run-3**: **Reviewing Lookup Function** I'm currently analyzing this C function. My focus is on identifying potential memory safety vulnerabilities. I've noted a conditio

**google/gemini-3.1-pro-preview / codex-v0.147.0/run-1**: **Reviewing for Bugs** I'm currently examining a C function designed for table lookups, specifically looking for memory safety vulnerabilities. My immediate foc

**google/gemini-3.1-pro-preview / codex-v0.147.0/run-2**: **Reviewing Memory Access** I'm currently scrutinizing the provided C snippet, specifically focusing on potential memory access issues. My attention is drawn to

**google/gemini-3.1-pro-preview / codex-v0.147.0/run-3**: **Reviewing Memory Safety** I'm currently deep in analyzing the provided C code, specifically the `lookup` function, to identify any potential memory safety vul

**google/gemini-3.7-flash / claude-v0.2.144/run-1**: **Reviewing Memory Access** I'm currently examining a C function for potential memory-safety vulnerabilities. My focus is on the `lookup` function, specifically

**google/gemini-3.7-flash / claude-v0.2.144/run-2**: **Analyzing Code Snippet** I'm currently examining a C function `lookup` for security vulnerabilities. My focus is on potential issues related to index bounds c

**google/gemini-3.7-flash / claude-v0.2.144/run-3**: **Analyzing Code Vulnerabilities** I'm currently scrutinizing this C function for potential memory-safety flaws. My immediate focus is on the index validation a

**google/gemini-3.7-flash / codex-v0.147.0/run-1**: **Analyzing C Function Security** I'm currently scrutinizing a C function designed for table lookups, with a keen eye on potential memory-safety vulnerabilities

**google/gemini-3.7-flash / codex-v0.147.0/run-2**: **Analyzing C Function Security** I'm reviewing the provided C function, `lookup`, focusing on potential memory safety vulnerabilities. My initial assessment in

**google/gemini-3.7-flash / codex-v0.147.0/run-3**: **Analyzing Code Snippet** I'm currently scrutinizing a C function, `lookup`, for potential security vulnerabilities. My focus is on ensuring memory safety and 

**minimax/minimax-m3 / claude-v0.2.144/run-1**: We need answer review memory safety. Need carefully reason. Function int lookup(int *table, int len, int idx). Checks idx > len, misses idx < 0, and equality id

**minimax/minimax-m3 / claude-v0.2.144/run-2**: The user wants a security/memory-safety review of a C function. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > le

**minimax/minimax-m3 / claude-v0.2.144/run-3**: The user wants me to review a C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > l

**minimax/minimax-m3 / codex-v0.147.0/run-1**: The user is asking me to review a C function for memory-safety bugs. This is a straightforward code review question, not a code modification task. I should just

**minimax/minimax-m3 / codex-v0.147.0/run-2**: The user is asking me to review a C function for memory-safety bugs. This is a code review task, not a coding task. Let me analyze the function carefully. ```c 

**minimax/minimax-m3 / codex-v0.147.0/run-3**: The user is asking me to review a C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx

**moonshotai/kimi-k3 / claude-v0.2.144/run-1**: The user asks me to review a C function for memory-safety bugs and explain my reasoning. I'm a security code reviewer. This is a pure code-review question — no 

**moonshotai/kimi-k3 / claude-v0.2.144/run-2**: The user asks me to review a C function for memory-safety bugs. Let me analyze carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > len) 

**moonshotai/kimi-k3 / claude-v0.2.144/run-3**: The user asks me to review a C function for memory-safety bugs. Let me analyze it: ```c static int lookup(int *table, int len, int idx) { if (idx > len) return 

**moonshotai/kimi-k3 / codex-v0.147.0/run-1**: Review the C function. Bugs: off-by-one (idx == len is out of bounds, valid indices 0..len-1), no check for negative idx (idx < 0 leads to out-of-bounds read be

**moonshotai/kimi-k3 / codex-v0.147.0/run-2**: Review: off-by-one — idx > len should be idx >= len. Valid indices 0..len-1. Also negative idx passes the check — if idx is negative, idx > len is false, and ta

**moonshotai/kimi-k3 / codex-v0.147.0/run-3**: Classic off-by-one + negative index issues. idx > len should be idx >= len; negative idx passes check; len could be negative; table could be NULL. Concise revie

**nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-1**: The user is asking me to review a C function for memory-safety bugs. This is a security code review task. Let me analyze the function: ```c static int lookup(in

**nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-2**: The user is asking me to review a C function for memory-safety bugs. This is a straightforward code review task - I don't need to use any of the available agent

**nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-3**: The user is asking me to review a C function for memory-safety bugs. This is a straightforward code review task - I don't need to use any tools for this. Let me

**nvidia/nemotron-3-ultra-550b-a55b:free / codex-v0.147.0/run-1**: The user wants me to review a C function for memory-safety bugs. Let me analyze the function: ```c static int lookup(int *table, int len, int idx) { if (idx > l

**nvidia/nemotron-3-ultra-550b-a55b:free / codex-v0.147.0/run-2**: The user wants me to review a C function for memory-safety bugs. Let me analyze this code carefully. The function is: ```c static int lookup(int *table, int len

**nvidia/nemotron-3-ultra-550b-a55b:free / codex-v0.147.0/run-3**: The user is asking me to review a C function for memory-safety bugs. This is a simple code review task that doesn't require any tools - I can analyze this direc

**openai/gpt-5.6-luna / claude-v0.2.144/run-1**: **Explaining memory safety issues** I think I need to provide a conceptual answer without using tools. I should clarify memory safety regarding conditions where

**openai/gpt-5.6-luna / claude-v0.2.144/run-2**: **Analyzing indexing concepts** I need to develop a conceptual answer without using any tools. I must identify the conditions for index validity, ensuring the i

**openai/gpt-5.6-luna / claude-v0.2.144/run-3**: **Clarifying indexing behavior** I need to explain the reasoning behind indexing considerations without reporting tool specifics. When dealing with `idx`, it’s 

**openai/gpt-5.6-luna / codex-v0.147.0/run-1**: ReasoningThreadItem(content=[], id='rs_0018052b59a0249e016a8cb222d2d887d19d8f224595845bd9', summary=[], type='reasoning')

**openai/gpt-5.6-luna / codex-v0.147.0/run-2**: ReasoningThreadItem(content=[], id='rs_09c1a3d1c71c3a49016a8ccf09365087d1ae462b0bb0c25200', summary=[], type='reasoning')

**openai/gpt-5.6-luna / codex-v0.147.0/run-3**: ReasoningThreadItem(content=[], id='rs_01a86d850017dfa2016a8ccf0eafa487d188a8b87b69c07027', summary=[], type='reasoning')

**openai/gpt-5.6-sol / claude-v0.2.144/run-1**: (none)

**openai/gpt-5.6-sol / claude-v0.2.144/run-2**: **Clarifying index checks** I need to provide a clear answer regarding index validation. First, I should identify off-by-one and negative index errors. A null t

**openai/gpt-5.6-sol / claude-v0.2.144/run-3**: (none)

**openai/gpt-5.6-sol / codex-v0.147.0/run-1**: ReasoningThreadItem(content=[], id='rs_09469fc3a68b8cab016a8cc3a36a4c87d19903383cb8e172d7', summary=[], type='reasoning')

**openai/gpt-5.6-sol / codex-v0.147.0/run-2**: ReasoningThreadItem(content=[], id='rs_00ea991ceea8b5a9016a8ccf2bf1fc87d18e41a148e0843d20', summary=[], type='reasoning')

**openai/gpt-5.6-sol / codex-v0.147.0/run-3**: ReasoningThreadItem(content=[], id='rs_0eaec55e1c83b36b016a8ccf32e67887d1a71350179b0872b9', summary=[], type='reasoning')

**openai/gpt-5.6-terra / claude-v0.2.144/run-1**: (none)

**openai/gpt-5.6-terra / claude-v0.2.144/run-2**: (none)

**openai/gpt-5.6-terra / claude-v0.2.144/run-3**: (none)

**openai/gpt-5.6-terra / codex-v0.147.0/run-1**: (none)

**openai/gpt-5.6-terra / codex-v0.147.0/run-2**: (none)

**openai/gpt-5.6-terra / codex-v0.147.0/run-3**: (none)

**openai/gpt-oss-120b / claude-v0.2.144/run-1**: We need to review function for memory-safety bugs and explain reasoning. The user asks to review function. We should produce explanation. No need to run tools. 

**openai/gpt-oss-120b / claude-v0.2.144/run-2**: We need to review function for memory-safety bugs, explain reasoning. No tools needed. Follow writing style: concise, sentences start with subject doing action.

**openai/gpt-oss-120b / claude-v0.2.144/run-3**: The user wants a review of this C function for memory-safety bugs and explanation. No need for tools. Just answer with analysis. Ensure style guidelines: concis

**openai/gpt-oss-120b / codex-v0.147.0/run-1**: The user asks: "Review this function for memory-safety bugs and explain your reasoning": ```c static int lookup(int *table, int len, int idx) { if (idx > len) r

**openai/gpt-oss-120b / codex-v0.147.0/run-2**: The user asks: "Review this function for memory-safety bugs and explain your reasoning". We have to analyze the static int lookup(int *table, int len, int idx) 

**openai/gpt-oss-120b / codex-v0.147.0/run-3**: The user asks: "Review this function for memory-safety bugs and explain your reasoning: ```c static int lookup(int *table, int len, int idx) { if (idx > len) re

**qwen/qwen3.6-max-preview / claude-v0.2.144/run-1**: The user wants me to review a C function for memory-safety bugs. Let me analyze it carefully.

**qwen/qwen3.6-max-preview / claude-v0.2.144/run-2**: The user is asking me to review a C function for memory-safety bugs. Let me analyze the code carefully.

**qwen/qwen3.6-max-preview / claude-v0.2.144/run-3**: The user wants me to review a C function for memory-safety bugs. Let me analyze the code carefully.

**qwen/qwen3.6-max-preview / codex-v0.147.0/run-1**: The user wants me to review a C function for memory-safety bugs. Let me analyze the code carefully. ```c static int lookup(int *table, int len, int idx) { if (i

**qwen/qwen3.6-max-preview / codex-v0.147.0/run-2**: The user is asking me to review a C function for memory-safety bugs. Let me analyze the code carefully. ```c static int lookup(int *table, int len, int idx) { i

**qwen/qwen3.6-max-preview / codex-v0.147.0/run-3**: The user is asking me to review a C function for memory-safety bugs. This is a read-only code review task, so I don't need to use any tools to read files or exe

**stealth/ox-alpha / claude-v0.2.144/run-1**: Let me analyze this function for memory-safety bugs. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; return table[idx]; } ``` B

**stealth/ox-alpha / claude-v0.2.144/run-2**: Let me look at this function carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; return table[idx]; } ``` The intent: bo

**stealth/ox-alpha / claude-v0.2.144/run-3**: The user asks to review a small C function for memory-safety bugs. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; return table

**stealth/ox-alpha / codex-v0.147.0/run-1**: We need answer only, no tools needed. Need reason memory safety. Function checks idx > len allowing idx==len out of bounds for 0-based array length len. Also ne

**stealth/ox-alpha / codex-v0.147.0/run-2**: (none)

**stealth/ox-alpha / codex-v0.147.0/run-3**: We need answer conceptual. Need maybe mention signed ints, idx negative, off by one > should >=, integer overflow idx+? no arithmetic. table null perhaps len. l

**z-ai/glm-5.2:free / claude-v0.2.144/run-1**: The user wants a review of this C function for memory-safety bugs. Let me analyze it carefully. ```c static int lookup(int *table, int len, int idx) { if (idx >

**z-ai/glm-5.2:free / claude-v0.2.144/run-2**: The user wants a memory-safety review of a C function. Let me reason carefully. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1;

**z-ai/glm-5.2:free / claude-v0.2.144/run-3**: The user wants a memory-safety review of this C function. Let me analyze it. ```c static int lookup(int *table, int len, int idx) { if (idx > len) return -1; re

**z-ai/glm-5.2:free / codex-v0.147.0/run-1**: The bug: `idx > len` should be `idx >= len` or `idx < 0`. Off-by-one allows out-of-bounds read at idx==len, and no negative check.

**z-ai/glm-5.2:free / codex-v0.147.0/run-2**: (none)

**z-ai/glm-5.2:free / codex-v0.147.0/run-3**: (none)

## Wire settings per cell

- **anthropic/claude-fable-5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-fable-5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-fable-5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-fable-5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-fable-5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-fable-5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-fable-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-fable-5 / codex-v0.147.0/run-1**: `{"model": "anthropic/claude-fable-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-fable-5 / codex-v0.147.0/run-2**: `{"model": "anthropic/claude-fable-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-fable-5 / codex-v0.147.0/run-3**: `{"model": "anthropic/claude-fable-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-haiku-4.5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-haiku-4.5", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-haiku-4.5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-haiku-4.5", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **anthropic/claude-haiku-4.5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-haiku-4.5", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-haiku-4.5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-haiku-4.5", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **anthropic/claude-haiku-4.5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-haiku-4.5", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-haiku-4.5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-haiku-4.5", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **anthropic/claude-haiku-4.5 / codex-v0.147.0/run-1**: `{"model": "anthropic/claude-haiku-4.5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-haiku-4.5 / codex-v0.147.0/run-2**: `{"model": "anthropic/claude-haiku-4.5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-haiku-4.5 / codex-v0.147.0/run-3**: `{"model": "anthropic/claude-haiku-4.5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-opus-5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-opus-5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-opus-5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-opus-5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-opus-5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-opus-5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-opus-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-opus-5 / codex-v0.147.0/run-1**: `{"model": "anthropic/claude-opus-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-opus-5 / codex-v0.147.0/run-2**: `{"model": "anthropic/claude-opus-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-opus-5 / codex-v0.147.0/run-3**: `{"model": "anthropic/claude-opus-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-sonnet-5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-sonnet-5 / claude-v0.2.144/run-1**: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-sonnet-5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-sonnet-5 / claude-v0.2.144/run-2**: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-sonnet-5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "disabled"}, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **anthropic/claude-sonnet-5 / claude-v0.2.144/run-3**: `{"model": "anthropic/claude-sonnet-5", "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 24, "system_chars": 373}`
- **anthropic/claude-sonnet-5 / codex-v0.147.0/run-1**: `{"model": "anthropic/claude-sonnet-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-sonnet-5 / codex-v0.147.0/run-2**: `{"model": "anthropic/claude-sonnet-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **anthropic/claude-sonnet-5 / codex-v0.147.0/run-3**: `{"model": "anthropic/claude-sonnet-5", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **deepseek/deepseek-v4-flash / claude-v0.2.144/run-1**: `{"model": "deepseek/deepseek-v4-flash", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **deepseek/deepseek-v4-flash / claude-v0.2.144/run-2**: `{"model": "deepseek/deepseek-v4-flash", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **deepseek/deepseek-v4-flash / claude-v0.2.144/run-2**: `{"model": "deepseek/deepseek-v4-flash", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **deepseek/deepseek-v4-flash / claude-v0.2.144/run-3**: `{"model": "deepseek/deepseek-v4-flash", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **deepseek/deepseek-v4-flash / codex-v0.147.0/run-1**: `{"model": "deepseek/deepseek-v4-flash", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **deepseek/deepseek-v4-flash / codex-v0.147.0/run-2**: `{"model": "deepseek/deepseek-v4-flash", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **deepseek/deepseek-v4-flash / codex-v0.147.0/run-3**: `{"model": "deepseek/deepseek-v4-flash", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **deepseek/deepseek-v4-pro / claude-v0.2.144/run-1**: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **deepseek/deepseek-v4-pro / claude-v0.2.144/run-1**: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **deepseek/deepseek-v4-pro / claude-v0.2.144/run-2**: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **deepseek/deepseek-v4-pro / claude-v0.2.144/run-2**: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **deepseek/deepseek-v4-pro / claude-v0.2.144/run-3**: `{"model": "deepseek/deepseek-v4-pro", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **deepseek/deepseek-v4-pro / codex-v0.147.0/run-1**: `{"model": "deepseek/deepseek-v4-pro", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **deepseek/deepseek-v4-pro / codex-v0.147.0/run-2**: `{"model": "deepseek/deepseek-v4-pro", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **deepseek/deepseek-v4-pro / codex-v0.147.0/run-3**: `{"model": "deepseek/deepseek-v4-pro", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **google/gemini-3.1-pro-preview / claude-v0.2.144/run-1**: `{"model": "google/gemini-3.1-pro-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **google/gemini-3.1-pro-preview / claude-v0.2.144/run-2**: `{"model": "google/gemini-3.1-pro-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **google/gemini-3.1-pro-preview / claude-v0.2.144/run-2**: `{"model": "google/gemini-3.1-pro-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **google/gemini-3.1-pro-preview / claude-v0.2.144/run-3**: `{"model": "google/gemini-3.1-pro-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **google/gemini-3.1-pro-preview / claude-v0.2.144/run-3**: `{"model": "google/gemini-3.1-pro-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **google/gemini-3.1-pro-preview / codex-v0.147.0/run-1**: `{"model": "google/gemini-3.1-pro-preview", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **google/gemini-3.1-pro-preview / codex-v0.147.0/run-2**: `{"model": "google/gemini-3.1-pro-preview", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **google/gemini-3.1-pro-preview / codex-v0.147.0/run-3**: `{"model": "google/gemini-3.1-pro-preview", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **google/gemini-3.7-flash / claude-v0.2.144/run-1**: `{"model": "google/gemini-3.7-flash", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **google/gemini-3.7-flash / claude-v0.2.144/run-1**: `{"model": "google/gemini-3.7-flash", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **google/gemini-3.7-flash / claude-v0.2.144/run-2**: `{"model": "google/gemini-3.7-flash", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **google/gemini-3.7-flash / claude-v0.2.144/run-2**: `{"model": "google/gemini-3.7-flash", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **google/gemini-3.7-flash / claude-v0.2.144/run-3**: `{"model": "google/gemini-3.7-flash", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **google/gemini-3.7-flash / claude-v0.2.144/run-3**: `{"model": "google/gemini-3.7-flash", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **google/gemini-3.7-flash / codex-v0.147.0/run-1**: `{"model": "google/gemini-3.7-flash", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **google/gemini-3.7-flash / codex-v0.147.0/run-2**: `{"model": "google/gemini-3.7-flash", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **google/gemini-3.7-flash / codex-v0.147.0/run-3**: `{"model": "google/gemini-3.7-flash", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **minimax/minimax-m3 / claude-v0.2.144/run-1**: `{"model": "minimax/minimax-m3", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **minimax/minimax-m3 / claude-v0.2.144/run-1**: `{"model": "minimax/minimax-m3", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **minimax/minimax-m3 / claude-v0.2.144/run-2**: `{"model": "minimax/minimax-m3", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **minimax/minimax-m3 / claude-v0.2.144/run-2**: `{"model": "minimax/minimax-m3", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **minimax/minimax-m3 / claude-v0.2.144/run-3**: `{"model": "minimax/minimax-m3", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **minimax/minimax-m3 / claude-v0.2.144/run-3**: `{"model": "minimax/minimax-m3", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **minimax/minimax-m3 / codex-v0.147.0/run-1**: `{"model": "minimax/minimax-m3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **minimax/minimax-m3 / codex-v0.147.0/run-2**: `{"model": "minimax/minimax-m3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **minimax/minimax-m3 / codex-v0.147.0/run-3**: `{"model": "minimax/minimax-m3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **moonshotai/kimi-k3 / claude-v0.2.144/run-1**: `{"model": "moonshotai/kimi-k3", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **moonshotai/kimi-k3 / claude-v0.2.144/run-1**: `{"model": "moonshotai/kimi-k3", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **moonshotai/kimi-k3 / claude-v0.2.144/run-2**: `{"model": "moonshotai/kimi-k3", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **moonshotai/kimi-k3 / claude-v0.2.144/run-2**: `{"model": "moonshotai/kimi-k3", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **moonshotai/kimi-k3 / claude-v0.2.144/run-3**: `{"model": "moonshotai/kimi-k3", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **moonshotai/kimi-k3 / claude-v0.2.144/run-3**: `{"model": "moonshotai/kimi-k3", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **moonshotai/kimi-k3 / codex-v0.147.0/run-1**: `{"model": "moonshotai/kimi-k3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **moonshotai/kimi-k3 / codex-v0.147.0/run-2**: `{"model": "moonshotai/kimi-k3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **moonshotai/kimi-k3 / codex-v0.147.0/run-3**: `{"model": "moonshotai/kimi-k3", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-1**: `{"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-2**: `{"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-3**: `{"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **nvidia/nemotron-3-ultra-550b-a55b:free / claude-v0.2.144/run-3**: `{"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **nvidia/nemotron-3-ultra-550b-a55b:free / codex-v0.147.0/run-1**: `{"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **nvidia/nemotron-3-ultra-550b-a55b:free / codex-v0.147.0/run-3**: `{"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **openai/gpt-5.6-luna / claude-v0.2.144/run-1**: `{"model": "openai/gpt-5.6-luna", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-luna / claude-v0.2.144/run-1**: `{"model": "openai/gpt-5.6-luna", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-luna / claude-v0.2.144/run-2**: `{"model": "openai/gpt-5.6-luna", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-luna / claude-v0.2.144/run-2**: `{"model": "openai/gpt-5.6-luna", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-luna / claude-v0.2.144/run-3**: `{"model": "openai/gpt-5.6-luna", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-luna / claude-v0.2.144/run-3**: `{"model": "openai/gpt-5.6-luna", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-luna / codex-v0.147.0/run-1**: `{"model": "openai/gpt-5.6-luna", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-luna / codex-v0.147.0/run-2**: `{"model": "openai/gpt-5.6-luna", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-luna / codex-v0.147.0/run-3**: `{"model": "openai/gpt-5.6-luna", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-sol / claude-v0.2.144/run-1**: `{"model": "openai/gpt-5.6-sol", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-sol / claude-v0.2.144/run-1**: `{"model": "openai/gpt-5.6-sol", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-sol / claude-v0.2.144/run-2**: `{"model": "openai/gpt-5.6-sol", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-sol / claude-v0.2.144/run-2**: `{"model": "openai/gpt-5.6-sol", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-sol / claude-v0.2.144/run-3**: `{"model": "openai/gpt-5.6-sol", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-sol / claude-v0.2.144/run-3**: `{"model": "openai/gpt-5.6-sol", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-sol / codex-v0.147.0/run-1**: `{"model": "openai/gpt-5.6-sol", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-sol / codex-v0.147.0/run-2**: `{"model": "openai/gpt-5.6-sol", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-sol / codex-v0.147.0/run-3**: `{"model": "openai/gpt-5.6-sol", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-terra / claude-v0.2.144/run-1**: `{"model": "openai/gpt-5.6-terra", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-terra / claude-v0.2.144/run-1**: `{"model": "openai/gpt-5.6-terra", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-terra / claude-v0.2.144/run-2**: `{"model": "openai/gpt-5.6-terra", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-terra / claude-v0.2.144/run-2**: `{"model": "openai/gpt-5.6-terra", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-terra / claude-v0.2.144/run-3**: `{"model": "openai/gpt-5.6-terra", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-5.6-terra / claude-v0.2.144/run-3**: `{"model": "openai/gpt-5.6-terra", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-5.6-terra / codex-v0.147.0/run-1**: `{"model": "openai/gpt-5.6-terra", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-terra / codex-v0.147.0/run-2**: `{"model": "openai/gpt-5.6-terra", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-5.6-terra / codex-v0.147.0/run-3**: `{"model": "openai/gpt-5.6-terra", "reasoning": {"effort": "high", "context": "all_turns"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 0, "system_chars": 2}`
- **openai/gpt-oss-120b / claude-v0.2.144/run-1**: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-oss-120b / claude-v0.2.144/run-2**: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-oss-120b / claude-v0.2.144/run-2**: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-oss-120b / claude-v0.2.144/run-3**: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **openai/gpt-oss-120b / claude-v0.2.144/run-3**: `{"model": "openai/gpt-oss-120b", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **openai/gpt-oss-120b / codex-v0.147.0/run-1**: `{"model": "openai/gpt-oss-120b", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **openai/gpt-oss-120b / codex-v0.147.0/run-2**: `{"model": "openai/gpt-oss-120b", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **openai/gpt-oss-120b / codex-v0.147.0/run-3**: `{"model": "openai/gpt-oss-120b", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **qwen/qwen3.6-max-preview / claude-v0.2.144/run-1**: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **qwen/qwen3.6-max-preview / claude-v0.2.144/run-1**: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **qwen/qwen3.6-max-preview / claude-v0.2.144/run-2**: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **qwen/qwen3.6-max-preview / claude-v0.2.144/run-2**: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **qwen/qwen3.6-max-preview / claude-v0.2.144/run-3**: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **qwen/qwen3.6-max-preview / claude-v0.2.144/run-3**: `{"model": "qwen/qwen3.6-max-preview", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **qwen/qwen3.6-max-preview / codex-v0.147.0/run-1**: `{"model": "qwen/qwen3.6-max-preview", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **qwen/qwen3.6-max-preview / codex-v0.147.0/run-2**: `{"model": "qwen/qwen3.6-max-preview", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **qwen/qwen3.6-max-preview / codex-v0.147.0/run-3**: `{"model": "qwen/qwen3.6-max-preview", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **stealth/ox-alpha / claude-v0.2.144/run-1**: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **stealth/ox-alpha / claude-v0.2.144/run-1**: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **stealth/ox-alpha / claude-v0.2.144/run-2**: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **stealth/ox-alpha / claude-v0.2.144/run-2**: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **stealth/ox-alpha / claude-v0.2.144/run-3**: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **stealth/ox-alpha / claude-v0.2.144/run-3**: `{"model": "stealth/ox-alpha", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **stealth/ox-alpha / codex-v0.147.0/run-1**: `{"model": "stealth/ox-alpha", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **stealth/ox-alpha / codex-v0.147.0/run-3**: `{"model": "stealth/ox-alpha", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`
- **z-ai/glm-5.2:free / claude-v0.2.144/run-1**: `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"], "additionalProperties": false}}}, "stream": true, "tools_count": 0, "system_chars": 3331}`
- **z-ai/glm-5.2:free / claude-v0.2.144/run-1**: `{"model": "z-ai/glm-5.2:free", "max_tokens": 32000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}, "stream": true, "tools_count": 28, "system_chars": 373}`
- **z-ai/glm-5.2:free / codex-v0.147.0/run-1**: `{"model": "z-ai/glm-5.2:free", "reasoning": {"effort": "high", "summary": "auto"}, "stream": true, "parallel_tool_calls": false, "include": ["reasoning.encrypted_content"], "store": false, "tools_count": 9, "system_chars": 21437}`

Full request/response logs live next to each cell as `wire.md`; every request body is fenced JSON and can be replayed with curl against openrouter.ai.
