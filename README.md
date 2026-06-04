# Claude Code Multi-Provider Model Selector

**English** | [中文](README.zh-CN.md)

Use Claude Code with DeepSeek, Qwen, GLM, or any Anthropic-compatible API provider — switch models interactively per project, no code changes required.

## What is this?

Claude Code is Anthropic's official AI coding assistant CLI. It natively only supports Anthropic's own API. This project adds a **zero-intrusion** shell function that intercepts the `claude` command and lets you **pick any provider** at startup — no source code modifications, no wrapper scripts, done in three minutes.

```
$ claude
=== Select Model ===
  1) DeepSeek V4
  2) Qwen-3.7-Max
  3) GLM-5.1
  4) custom
Enter number [1-4] (default 1):
```

## What it does

- **Per-project model switching** — each project declares its own model list in `.claude/model-selector`, team members get it automatically via `git clone`
- **Main / subagent model separation** — route the main conversation to a powerful model (e.g. qwen3.7-max) and subagent calls to a cheaper one (e.g. qwen3.6-flash), saving **50-80%** on subagent costs
- **Zero intrusion** — the shell function wraps `command claude`, no modifications to Claude Code itself
- **Custom mode** — enter any model name + base URL + API key on the fly for ad-hoc providers

## Quick start

### 1. Install Claude Code

**Prerequisites:** Node.js ≥ 18 and Python 3.

```bash
# Standard (global network)
npm install -g @anthropic-ai/claude-code

# In China (use npm mirror)
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com

# Verify
claude --version
```

### 2. Get an API key

| Provider | Console | Notes |
|----------|---------|-------|
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | Free credits on signup |
| **Ali-Qwen (DashScope)** | [dashscope.aliyun.com](https://dashscope.aliyun.com) | Pay-as-you-go |
| **Zhipu (GLM)** | [open.bigmodel.cn](https://open.bigmodel.cn) | Free quota on signup |

> Domestic APIs (DeepSeek, DashScope, Zhipu) are **directly reachable from China** — no proxy needed.

### 3. Configure model-selector

Open Claude Code in your project directory and ask:

> "Help me configure model-selector using the setup-model-selector skill"

The skill will:
1. Create `.claude/model-selector` with your model list
2. Write the `claude()` shell function to `~/.zshrc` (macOS) or `~/.bashrc` (Linux)
3. Optionally set up `~/.claude/secrets.sh` for secure token storage
4. Verify everything works

After setup, launching `claude` in any project with a `.claude/model-selector` file will show the model selection menu.

## Platform support

| Platform | Shell | Config file | Status |
|----------|-------|-------------|:--:|
| **macOS** | zsh | `~/.zshrc` | ✅ Full support |
| **Linux** | bash | `~/.bashrc` | ✅ Full support |
| **Windows** | WSL 2 / Git Bash | `~/.bashrc` | ✅ Works via WSL/Git Bash |
| **Windows native** | cmd / PowerShell | — | ❌ Not supported |

> Windows users: install WSL first (`wsl --install`), then follow the Linux instructions. The shell function relies on `/dev/tty`, `command` builtin, and POSIX `export`/`unset` — none of which exist in cmd/PowerShell.

## Network requirements

| Action | Proxy needed? | Notes |
|--------|:--:|-------|
| `npm install` Claude Code | **Maybe** | Use `--registry=https://registry.npmmirror.com` in China |
| `claude` first launch / OAuth | **Maybe** | Anthropic's auth endpoint; set `https_proxy` temporarily if stuck |
| API calls to DeepSeek / Qwen / GLM | **No** | Domestic endpoints, directly reachable from China |
| `git clone` this repo | **Often yes** | Use `https_proxy=http://127.0.0.1:7897` or download ZIP |

## How it works

```
You type: claude
    ↓
Shell function intercepts (claude() in ~/.zshrc)
    ↓
Checks for .claude/model-selector in current project
    ↓
  Found  → Python parses JSON → shows menu → you pick a model → env vars injected
  Absent → all model vars unset → Claude Code uses Anthropic defaults + OAuth
    ↓
command claude launches the real Claude Code binary
```

### Architecture

Three layers:

1. **Environment variable layer** — the `claude()` shell function injects model config into the current shell process before launching Claude Code
2. **Interaction layer** — an embedded Python script (inside the heredoc) handles JSON parsing, menu generation, and user input. UI goes to stderr, data goes to stdout
3. **Authentication layer** — Claude Code's built-in OAuth handles auth by default. Optionally, `apiKeyHelper` in `settings.json` + `~/.claude/secrets.sh` provides per-provider token routing

### Model slot mapping

Claude Code uses 6 model slots. The model-selector maps them to just 2 actual models:

```
"model" (high-capability) → ANTHROPIC_MODEL, ANTHROPIC_DEFAULT_OPUS_MODEL, ANTHROPIC_DEFAULT_SONNET_MODEL
"fast"  (lightweight)     → ANTHROPIC_DEFAULT_HAIKU_MODEL, ANTHROPIC_SMALL_FAST_MODEL, CLAUDE_CODE_SUBAGENT_MODEL
```

This keeps quality high on the main loop while cutting subagent costs.

## Project structure

```
skills/
├── README.md                          ← English (this file)
├── README.zh-CN.md                    ← 中文版
├── setup-model-selector/              ← Core: model-selector setup skill
│   ├── SKILL.md                       ←    Full step-by-step guide (AI-executable)
│   ├── references/
│   │   └── shell-function.md          ←    bash/zsh function templates
│   └── evals/
│       └── evals.json                 ←    51 automated test assertions
├── skill-creator/                     ← Tool: create new skills
└── demo-skill/                        ← Example: a simple hello skill
```

## FAQ

**Q: I switched to a project without model-selector — what happens?**
A: All model env vars are cleared, Claude Code reverts to Anthropic defaults + OAuth. No stale state carries over.

**Q: Is the custom mode API key safe?**
A: It lives only in the current shell process memory. Closing the terminal clears it. The next `claude` invocation also automatically unsets it.

**Q: Can I use this on Windows natively?**
A: No. cmd and PowerShell don't support shell functions. You need WSL (`wsl --install`) or Git Bash.

**Q: Installation fails / network timeout?**
A: Check your npm mirror config. If a proxy (Clash Verge / V2Ray etc.) is running, ensure `https_proxy` is set in your shell.

## License

Copyright 2026 terry

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

See [LICENSE](LICENSE) for the full license text.

## More info

- Full step-by-step setup guide: [setup-model-selector/SKILL.md](setup-model-selector/SKILL.md)
- Shell function implementation details: [references/shell-function.md](setup-model-selector/references/shell-function.md)
