# Judging

Judge: see per-cell judge.json (`judge_model`). Bug columns locate each planted finding: in the thinking, the output, both, or missed.

| model | harness | off-by-one | negative index | hypotheses | self-corr | thinking/output | register | false claims | verdict |
|---|---|---|---|---|---|---|---|---|---|
| `anthropic-claude-fable-5` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 1 | [judge](anthropic-claude-fable-5/claude-v0.2.144/run-1/judge.md) |
| `anthropic-claude-fable-5` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 5 | 0 | draft | narrated | 0 | [judge](anthropic-claude-fable-5/claude-v0.2.144/run-2/judge.md) |
| `anthropic-claude-fable-5` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](anthropic-claude-fable-5/claude-v0.2.144/run-3/judge.md) |
| `anthropic-claude-fable-5` | codex-v0.147.0/run-1 | output only | output only | 0 | 0 | none | narrated | 0 | [judge](anthropic-claude-fable-5/codex-v0.147.0/run-1/judge.md) |
| `anthropic-claude-fable-5` | codex-v0.147.0/run-2 | output only | output only | 0 | 0 | none | narrated | 0 | [judge](anthropic-claude-fable-5/codex-v0.147.0/run-2/judge.md) |
| `anthropic-claude-fable-5` | codex-v0.147.0/run-3 | output only | output only | 0 | 0 | deliberation | narrated | 0 | [judge](anthropic-claude-fable-5/codex-v0.147.0/run-3/judge.md) |
| `anthropic-claude-haiku-4.5` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 1 | [judge](anthropic-claude-haiku-4.5/claude-v0.2.144/run-1/judge.md) |
| `anthropic-claude-haiku-4.5` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 6 | 0 | draft | narrated | 1 | [judge](anthropic-claude-haiku-4.5/claude-v0.2.144/run-2/judge.md) |
| `anthropic-claude-haiku-4.5` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 1 | [judge](anthropic-claude-haiku-4.5/claude-v0.2.144/run-3/judge.md) |
| `anthropic-claude-haiku-4.5` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](anthropic-claude-haiku-4.5/codex-v0.147.0/run-1/judge.md) |
| `anthropic-claude-haiku-4.5` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 1 | [judge](anthropic-claude-haiku-4.5/codex-v0.147.0/run-2/judge.md) |
| `anthropic-claude-haiku-4.5` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 3 | 1 | draft | narrated | 0 | [judge](anthropic-claude-haiku-4.5/codex-v0.147.0/run-3/judge.md) |
| `anthropic-claude-opus-5` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](anthropic-claude-opus-5/claude-v0.2.144/run-1/judge.md) |
| `anthropic-claude-opus-5` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](anthropic-claude-opus-5/claude-v0.2.144/run-2/judge.md) |
| `anthropic-claude-opus-5` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 2 | [judge](anthropic-claude-opus-5/claude-v0.2.144/run-3/judge.md) |
| `anthropic-claude-opus-5` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](anthropic-claude-opus-5/codex-v0.147.0/run-1/judge.md) |
| `anthropic-claude-opus-5` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 9 | 0 | draft | narrated | 2 | [judge](anthropic-claude-opus-5/codex-v0.147.0/run-2/judge.md) |
| `anthropic-claude-opus-5` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 7 | 0 | draft | narrated | 2 | [judge](anthropic-claude-opus-5/codex-v0.147.0/run-3/judge.md) |
| `anthropic-claude-sonnet-5` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](anthropic-claude-sonnet-5/claude-v0.2.144/run-1/judge.md) |
| `anthropic-claude-sonnet-5` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](anthropic-claude-sonnet-5/claude-v0.2.144/run-2/judge.md) |
| `anthropic-claude-sonnet-5` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](anthropic-claude-sonnet-5/claude-v0.2.144/run-3/judge.md) |
| `anthropic-claude-sonnet-5` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 0 | [judge](anthropic-claude-sonnet-5/codex-v0.147.0/run-1/judge.md) |
| `anthropic-claude-sonnet-5` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](anthropic-claude-sonnet-5/codex-v0.147.0/run-2/judge.md) |
| `anthropic-claude-sonnet-5` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](anthropic-claude-sonnet-5/codex-v0.147.0/run-3/judge.md) |
| `deepseek-deepseek-v4-flash` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 5 | 2 | deliberation | narrated | 1 | [judge](deepseek-deepseek-v4-flash/claude-v0.2.144/run-1/judge.md) |
| `deepseek-deepseek-v4-flash` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 4 | 2 | deliberation | narrated | 1 | [judge](deepseek-deepseek-v4-flash/claude-v0.2.144/run-2/judge.md) |
| `deepseek-deepseek-v4-flash` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](deepseek-deepseek-v4-flash/claude-v0.2.144/run-3/judge.md) |
| `deepseek-deepseek-v4-flash` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](deepseek-deepseek-v4-flash/codex-v0.147.0/run-1/judge.md) |
| `deepseek-deepseek-v4-flash` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 6 | 2 | draft | narrated | 0 | [judge](deepseek-deepseek-v4-flash/codex-v0.147.0/run-2/judge.md) |
| `deepseek-deepseek-v4-flash` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 5 | 0 | deliberation | narrated | 1 | [judge](deepseek-deepseek-v4-flash/codex-v0.147.0/run-3/judge.md) |
| `deepseek-deepseek-v4-pro` | claude-v0.2.144/run-1 | output only | output only | 0 | 0 | deliberation | narrated | 0 | [judge](deepseek-deepseek-v4-pro/claude-v0.2.144/run-1/judge.md) |
| `deepseek-deepseek-v4-pro` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 3 | 1 | draft | narrated | 0 | [judge](deepseek-deepseek-v4-pro/claude-v0.2.144/run-2/judge.md) |
| `deepseek-deepseek-v4-pro` | claude-v0.2.144/run-3 | output only | output only | 0 | 0 | deliberation | narrated | 0 | [judge](deepseek-deepseek-v4-pro/claude-v0.2.144/run-3/judge.md) |
| `deepseek-deepseek-v4-pro` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](deepseek-deepseek-v4-pro/codex-v0.147.0/run-1/judge.md) |
| `deepseek-deepseek-v4-pro` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](deepseek-deepseek-v4-pro/codex-v0.147.0/run-2/judge.md) |
| `deepseek-deepseek-v4-pro` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](deepseek-deepseek-v4-pro/codex-v0.147.0/run-3/judge.md) |
| `google-gemini-3.1-pro-preview` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](google-gemini-3.1-pro-preview/claude-v0.2.144/run-1/judge.md) |
| `google-gemini-3.1-pro-preview` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](google-gemini-3.1-pro-preview/claude-v0.2.144/run-2/judge.md) |
| `google-gemini-3.1-pro-preview` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](google-gemini-3.1-pro-preview/claude-v0.2.144/run-3/judge.md) |
| `google-gemini-3.1-pro-preview` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 0 | [judge](google-gemini-3.1-pro-preview/codex-v0.147.0/run-1/judge.md) |
| `google-gemini-3.1-pro-preview` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 3 | 0 | draft | mixed | 0 | [judge](google-gemini-3.1-pro-preview/codex-v0.147.0/run-2/judge.md) |
| `google-gemini-3.1-pro-preview` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](google-gemini-3.1-pro-preview/codex-v0.147.0/run-3/judge.md) |
| `google-gemini-3.7-flash` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 7 | 0 | deliberation | narrated | 0 | [judge](google-gemini-3.7-flash/claude-v0.2.144/run-1/judge.md) |
| `google-gemini-3.7-flash` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 0 | [judge](google-gemini-3.7-flash/claude-v0.2.144/run-2/judge.md) |
| `google-gemini-3.7-flash` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 5 | 0 | draft | narrated | 0 | [judge](google-gemini-3.7-flash/claude-v0.2.144/run-3/judge.md) |
| `google-gemini-3.7-flash` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 0 | [judge](google-gemini-3.7-flash/codex-v0.147.0/run-1/judge.md) |
| `google-gemini-3.7-flash` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 7 | 0 | draft | narrated | 0 | [judge](google-gemini-3.7-flash/codex-v0.147.0/run-2/judge.md) |
| `google-gemini-3.7-flash` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 5 | 0 | draft | narrated | 0 | [judge](google-gemini-3.7-flash/codex-v0.147.0/run-3/judge.md) |
| `minimax-minimax-m3` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 9 | 2 | deliberation | mixed (fragments) | 0 | [judge](minimax-minimax-m3/claude-v0.2.144/run-1/judge.md) |
| `minimax-minimax-m3` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 5 | 0 | draft | narrated | 2 | [judge](minimax-minimax-m3/claude-v0.2.144/run-2/judge.md) |
| `minimax-minimax-m3` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 5 | 1 | draft | narrated | 0 | [judge](minimax-minimax-m3/claude-v0.2.144/run-3/judge.md) |
| `minimax-minimax-m3` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 5 | 0 | draft | narrated | 0 | [judge](minimax-minimax-m3/codex-v0.147.0/run-1/judge.md) |
| `minimax-minimax-m3` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 6 | 1 | draft | narrated | 2 | [judge](minimax-minimax-m3/codex-v0.147.0/run-2/judge.md) |
| `minimax-minimax-m3` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 6 | 2 | deliberation | narrated | 1 | [judge](minimax-minimax-m3/codex-v0.147.0/run-3/judge.md) |
| `moonshotai-kimi-k3` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 13 | 2 | draft | narrated | 4 | [judge](moonshotai-kimi-k3/claude-v0.2.144/run-1/judge.md) |
| `moonshotai-kimi-k3` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 10 | 4 | deliberation | narrated | 0 | [judge](moonshotai-kimi-k3/claude-v0.2.144/run-2/judge.md) |
| `moonshotai-kimi-k3` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 6 | 0 | deliberation | narrated | 2 | [judge](moonshotai-kimi-k3/claude-v0.2.144/run-3/judge.md) |
| `moonshotai-kimi-k3` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 7 | 0 | deliberation | telegraphic (fragments) | 1 | [judge](moonshotai-kimi-k3/codex-v0.147.0/run-1/judge.md) |
| `moonshotai-kimi-k3` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 4 | 0 | draft | mixed | 0 | [judge](moonshotai-kimi-k3/codex-v0.147.0/run-2/judge.md) |
| `moonshotai-kimi-k3` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 4 | 0 | summary | telegraphic (fragments) | 1 | [judge](moonshotai-kimi-k3/codex-v0.147.0/run-3/judge.md) |
| `nvidia-nemotron-3-ultra-550b-a55b-free` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](nvidia-nemotron-3-ultra-550b-a55b-free/claude-v0.2.144/run-1/judge.md) |
| `nvidia-nemotron-3-ultra-550b-a55b-free` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 1 | [judge](nvidia-nemotron-3-ultra-550b-a55b-free/claude-v0.2.144/run-2/judge.md) |
| `nvidia-nemotron-3-ultra-550b-a55b-free` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](nvidia-nemotron-3-ultra-550b-a55b-free/claude-v0.2.144/run-3/judge.md) |
| `nvidia-nemotron-3-ultra-550b-a55b-free` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 1 | [judge](nvidia-nemotron-3-ultra-550b-a55b-free/codex-v0.147.0/run-1/judge.md) |
| `nvidia-nemotron-3-ultra-550b-a55b-free` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](nvidia-nemotron-3-ultra-550b-a55b-free/codex-v0.147.0/run-2/judge.md) |
| `nvidia-nemotron-3-ultra-550b-a55b-free` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 2 | 0 | draft | narrated | 0 | [judge](nvidia-nemotron-3-ultra-550b-a55b-free/codex-v0.147.0/run-3/judge.md) |
| `openai-gpt-5.6-luna` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 0 | [judge](openai-gpt-5.6-luna/claude-v0.2.144/run-1/judge.md) |
| `openai-gpt-5.6-luna` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 9 | 0 | draft | narrated | 0 | [judge](openai-gpt-5.6-luna/claude-v0.2.144/run-2/judge.md) |
| `openai-gpt-5.6-luna` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 0 | [judge](openai-gpt-5.6-luna/claude-v0.2.144/run-3/judge.md) |
| `openai-gpt-5.6-luna` | codex-v0.147.0/run-1 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-luna/codex-v0.147.0/run-1/judge.md) |
| `openai-gpt-5.6-luna` | codex-v0.147.0/run-2 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-luna/codex-v0.147.0/run-2/judge.md) |
| `openai-gpt-5.6-luna` | codex-v0.147.0/run-3 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-luna/codex-v0.147.0/run-3/judge.md) |
| `openai-gpt-5.6-sol` | claude-v0.2.144/run-1 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-sol/claude-v0.2.144/run-1/judge.md) |
| `openai-gpt-5.6-sol` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](openai-gpt-5.6-sol/claude-v0.2.144/run-2/judge.md) |
| `openai-gpt-5.6-sol` | claude-v0.2.144/run-3 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-sol/claude-v0.2.144/run-3/judge.md) |
| `openai-gpt-5.6-sol` | codex-v0.147.0/run-1 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-sol/codex-v0.147.0/run-1/judge.md) |
| `openai-gpt-5.6-sol` | codex-v0.147.0/run-2 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-sol/codex-v0.147.0/run-2/judge.md) |
| `openai-gpt-5.6-sol` | codex-v0.147.0/run-3 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-sol/codex-v0.147.0/run-3/judge.md) |
| `openai-gpt-5.6-terra` | claude-v0.2.144/run-1 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-terra/claude-v0.2.144/run-1/judge.md) |
| `openai-gpt-5.6-terra` | claude-v0.2.144/run-2 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-terra/claude-v0.2.144/run-2/judge.md) |
| `openai-gpt-5.6-terra` | claude-v0.2.144/run-3 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-terra/claude-v0.2.144/run-3/judge.md) |
| `openai-gpt-5.6-terra` | codex-v0.147.0/run-1 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-terra/codex-v0.147.0/run-1/judge.md) |
| `openai-gpt-5.6-terra` | codex-v0.147.0/run-2 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-terra/codex-v0.147.0/run-2/judge.md) |
| `openai-gpt-5.6-terra` | codex-v0.147.0/run-3 | output only | output only | 0 | 0 | none | none | 0 | [judge](openai-gpt-5.6-terra/codex-v0.147.0/run-3/judge.md) |
| `openai-gpt-oss-120b` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 4 | 0 | draft | mixed | 0 | [judge](openai-gpt-oss-120b/claude-v0.2.144/run-1/judge.md) |
| `openai-gpt-oss-120b` | claude-v0.2.144/run-2 | output only | output only | 0 | 0 | deliberation | narrated | 0 | [judge](openai-gpt-oss-120b/claude-v0.2.144/run-2/judge.md) |
| `openai-gpt-oss-120b` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 6 | 0 | draft | mixed | 1 | [judge](openai-gpt-oss-120b/claude-v0.2.144/run-3/judge.md) |
| `openai-gpt-oss-120b` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 5 | 0 | deliberation | narrated | 0 | [judge](openai-gpt-oss-120b/codex-v0.147.0/run-1/judge.md) |
| `openai-gpt-oss-120b` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 5 | 0 | deliberation | narrated | 0 | [judge](openai-gpt-oss-120b/codex-v0.147.0/run-2/judge.md) |
| `openai-gpt-oss-120b` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 7 | 2 | deliberation | narrated | 0 | [judge](openai-gpt-oss-120b/codex-v0.147.0/run-3/judge.md) |
| `qwen-qwen3.6-max-preview` | claude-v0.2.144/run-1 | output only | output only | 0 | 0 | deliberation | narrated | 0 | [judge](qwen-qwen3.6-max-preview/claude-v0.2.144/run-1/judge.md) |
| `qwen-qwen3.6-max-preview` | claude-v0.2.144/run-2 | output only | output only | 0 | 0 | deliberation | narrated | 1 | [judge](qwen-qwen3.6-max-preview/claude-v0.2.144/run-2/judge.md) |
| `qwen-qwen3.6-max-preview` | claude-v0.2.144/run-3 | output only | output only | 0 | 0 | deliberation | narrated | 0 | [judge](qwen-qwen3.6-max-preview/claude-v0.2.144/run-3/judge.md) |
| `qwen-qwen3.6-max-preview` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 5 | 0 | draft | narrated | 0 | [judge](qwen-qwen3.6-max-preview/codex-v0.147.0/run-1/judge.md) |
| `qwen-qwen3.6-max-preview` | codex-v0.147.0/run-2 | thinking+output | thinking+output | 4 | 0 | draft | narrated | 1 | [judge](qwen-qwen3.6-max-preview/codex-v0.147.0/run-2/judge.md) |
| `qwen-qwen3.6-max-preview` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 4 | 0 | deliberation | narrated | 0 | [judge](qwen-qwen3.6-max-preview/codex-v0.147.0/run-3/judge.md) |
| `stealth-ox-alpha` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 7 | 3 | deliberation | narrated | 0 | [judge](stealth-ox-alpha/claude-v0.2.144/run-1/judge.md) |
| `stealth-ox-alpha` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 8 | 3 | draft | narrated | 2 | [judge](stealth-ox-alpha/claude-v0.2.144/run-2/judge.md) |
| `stealth-ox-alpha` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 6 | 0 | draft | narrated | 1 | [judge](stealth-ox-alpha/claude-v0.2.144/run-3/judge.md) |
| `stealth-ox-alpha` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 7 | 2 | draft | telegraphic (fragments) | 0 | [judge](stealth-ox-alpha/codex-v0.147.0/run-1/judge.md) |
| `stealth-ox-alpha` | codex-v0.147.0/run-3 | thinking+output | thinking+output | 6 | 1 | deliberation | telegraphic (fragments) | 0 | [judge](stealth-ox-alpha/codex-v0.147.0/run-3/judge.md) |
| `z-ai-glm-5.2-free` | claude-v0.2.144/run-1 | thinking+output | thinking+output | 3 | 0 | draft | narrated | 0 | [judge](z-ai-glm-5.2-free/claude-v0.2.144/run-1/judge.md) |
| `z-ai-glm-5.2-free` | claude-v0.2.144/run-2 | thinking+output | thinking+output | 4 | 0 | deliberation | narrated | 2 | [judge](z-ai-glm-5.2-free/claude-v0.2.144/run-2/judge.md) |
| `z-ai-glm-5.2-free` | claude-v0.2.144/run-3 | thinking+output | thinking+output | 4 | 2 | draft | narrated | 0 | [judge](z-ai-glm-5.2-free/claude-v0.2.144/run-3/judge.md) |
| `z-ai-glm-5.2-free` | codex-v0.147.0/run-1 | thinking+output | thinking+output | 2 | 0 | summary | telegraphic | 0 | [judge](z-ai-glm-5.2-free/codex-v0.147.0/run-1/judge.md) |
