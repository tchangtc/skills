---
name: setup-model-selector
description: Set up the Claude Code multi-provider model-selector system for a project. Use this skill whenever the user wants to configure Claude Code to work with multiple AI model providers (DeepSeek, Qwen, GLM, custom APIs), switch between models interactively, separate main and subagent models for cost optimization, or set up a model-selector configuration file. Also trigger when the user mentions "model-selector", "multi-provider", "switch models", "model menu", or wants to configure Claude Code to use non-Anthropic API providers.
---

# Setup Model-Selector

Guide the user through setting up the Claude Code multi-provider model-selector system. This enables interactive model selection when starting `claude`, with project-level configuration that teams can share via version control.

## Architecture Overview

The system has three layers:

1. **Environment variable layer** — A `claude()` shell function intercepts the `claude` command, reads the project's `.claude/model-selector` JSON, shows an interactive menu, and injects environment variables before launching the real Claude binary.

2. **Interaction layer** — An embedded Python script (inside the shell function) handles JSON parsing, menu generation, and user input. UI goes to stderr (visible to user), data goes to stdout (captured by shell).

3. **Authentication layer** — Claude Code's built-in OAuth handles auth by default. Optionally, `apiKeyHelper` in `settings.json` + `~/.claude/secrets.sh` provides explicit per-provider token management.

## Key Concept: Main/Fast Model Separation

Claude Code uses 6 model slots that should be mapped to just 2 actual models:

```
"model" (high-capability) → ANTHROPIC_MODEL, ANTHROPIC_DEFAULT_OPUS_MODEL, ANTHROPIC_DEFAULT_SONNET_MODEL
"fast"  (lightweight)     → ANTHROPIC_DEFAULT_HAIKU_MODEL, ANTHROPIC_SMALL_FAST_MODEL, CLAUDE_CODE_SUBAGENT_MODEL
```

This keeps the main conversation loop on a powerful model while routing the many subagent/internal calls to a cheaper, faster model — typically saving 50-80% on subagent costs with zero quality loss on the main loop.

## Before You Begin: Prerequisites

Before setting up model-selector, the user needs:

| Prerequisite | Check command | Why needed |
|-------------|---------------|------------|
| **Node.js ≥ 18** | `node --version` | Claude Code runs on Node.js |
| **npm** | `npm --version` | Claude Code is installed via npm |
| **Python 3** | `python3 --version` or `python --version` | model-selector's menu is powered by an embedded Python script |
| **Claude Code CLI** | `claude --version` | The `claude()` shell function wraps the real `claude` binary |
| **Shell profile** | `echo $SHELL` then check `~/.bashrc` or `~/.zshrc` exists | The `claude()` function must live in the shell config file |

If any are missing, guide the user through installation first.

### Claude Code Installation (Step 0)

If Claude Code is not yet installed, here is how to install it:

**Standard installation (global network):**
```bash
npm install -g @anthropic-ai/claude-code
```

**For users in China (use npm mirror):**
```bash
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```

After installation, verify:
```bash
claude --version
```

> **Note:** The `npm install` step may require a network proxy depending on the user's environment.
> If the mirror also fails, suggest setting a proxy temporarily:
> ```bash
> npm config set proxy http://127.0.0.1:7890
> npm install -g @anthropic-ai/claude-code
> npm config delete proxy
> ```
> Once Claude Code is installed, accessing **domestic model APIs (DeepSeek, DashScope, Zhipu) does NOT require a proxy** — they are directly reachable from within China.

## Step-by-Step Setup Process

### Step 1: Detect Shell Environment

Determine the user's shell. On Linux this is almost always bash (`~/.bashrc`). On macOS it's zsh (`~/.zshrc`). Check with:

```bash
echo $SHELL
```

If the user's shell is zsh, use `~/.zshrc` and zsh `read` syntax (`read "var?prompt: "`). If bash, use `~/.bashrc` and bash `read` syntax (`read -p "prompt: " var`).

### Step 2: Gather Provider Configurations

Ask the user which providers they want to configure. For each provider, collect:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Display name shown in the menu (e.g., "qwen-3.7-Max") |
| `provider` | Yes | Provider identifier (e.g., "ali-qwen", "deepseek", "zhipu") |
| `base_url` | Yes | Anthropic-compatible API endpoint URL |
| `model` | Yes | Main model name — maps to OPUS/SONNET/MODEL slots |
| `fast` | No | Fast model name — maps to HAIKU/SMALL_FAST/SUBAGENT slots. If omitted, all slots use `model` |
| `effort` | No | Reasoning intensity: "low", "medium", "high", or "max". If omitted, Claude Code uses its default (usually medium) |

**Common provider presets** (offer these as suggestions):

| Provider | base_url | Example models |
|----------|----------|----------------|
| DeepSeek | `https://api.deepseek.com/anthropic` | deepseek-v4-pro, deepseek-v4-flash |
| Zhipu/GLM | `https://open.bigmodel.cn/api/paas/v4/anthropic` | glm-5.1, glm-4.7-flash |
| Ali-Qwen | `https://dashscope.aliyuncs.com/apps/anthropic` | qwen3.7-max, qwen3.6-flash |
| Custom | User-provided | User-provided |

**How to get API keys** (for users in China — no proxy needed for these sites):

| Provider | Registration / Console | Notes |
|----------|----------------------|-------|
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | Register → API Keys → Create. New users get free credits. |
| **Ali-Qwen (DashScope)** | [dashscope.aliyun.com](https://dashscope.aliyun.com) | Alibaba Cloud account → DashScope console → API Key management. Pay-as-you-go. |
| **Zhipu (GLM)** | [open.bigmodel.cn](https://open.bigmodel.cn) | Register → Developer console → API Keys. New users get free quota. |

Remind the user to copy each API key immediately after creation — they are usually shown only once.

### Step 3: Generate `.claude/model-selector`

Create the project directory `.claude/` if it doesn't exist, then write the JSON file:

```json
[
  {
    "name": "qwen-3.7-Max",
    "provider": "ali-qwen",
    "base_url": "https://dashscope.aliyuncs.com/apps/anthropic",
    "model": "qwen3.7-max",
    "fast": "qwen3.6-flash",
    "effort": "max"
  }
]
```

After writing, validate the JSON:

```bash
python3 -m json.tool .claude/model-selector > /dev/null
```

### Step 4: Write the `claude()` Shell Function

Read the shell function template from `references/shell-function.md`. This file contains the complete, tested `claude()` function for both bash and zsh.

**Important implementation details** (explain these to the user):

- The function uses `command claude "$@"` at the end — `command` bypasses the function itself and calls the real binary from PATH
- Python's `sys.stdin = open('/dev/tty')` is essential because the heredoc consumes stdin; without this, `input()` raises EOFError
- UI output goes to stderr (`file=sys.stderr`), data output goes to stdout — this is because `$()` captures stdout only
- `shlex.quote()` prevents shell injection from model names containing special characters
- `__CUSTOM__` and `__ERROR__` are protocol markers passed via stdout to control bash flow
- `unset ANTHROPIC_AUTH_TOKEN` is placed at the **top** of the function (before the `if` block) — this clears residual tokens from previous sessions while allowing custom mode to set a fresh one. Placing it at the end would clear the token custom mode just set.
- The `else` branch (no model-selector) actively unsets all model-related env vars so Claude Code falls back to its built-in Anthropic API defaults + OAuth
- Custom mode sets `CLAUDE_PROVIDER="custom"` and unsets `CLAUDE_CODE_EFFORT_LEVEL` to prevent stale state leakage
- A `[[ -z "$py" ]]` guard before the heredoc gives a clear error when Python is missing

**Before writing**, check if the user's shell config file already contains a `claude()` function. If it does:
- Show them the existing function
- Ask if they want to replace it
- If yes, replace the old function (match from `claude()` to the closing `}`)

**Writing approach**: Append the function to the shell config file. Add a clear comment block before it:

```bash
# ===== Claude Code model-selector =====
# Auto-generated by setup-model-selector skill
# Detects .claude/model-selector and shows interactive model menu
```

### Step 5: Create `~/.claude/secrets.sh` (Optional)

If the user wants explicit token management (rather than relying on OAuth):

1. Create `~/.claude/secrets.sh` with placeholder tokens for each configured provider:

```bash
# API Keys for Claude Code providers
# Sourced by apiKeyHelper to return the correct key based on CLAUDE_PROVIDER
export DEEPSEEK_TOKEN="<replace-with-your-token>"
export ALI_TOKEN="<replace-with-your-token>"
export ZHIPU_TOKEN="<replace-with-your-token>"
```

2. Set restrictive permissions: `chmod 600 ~/.claude/secrets.sh`
3. Warn the user: **Never commit this file to git. Never share it.**

### Step 6: Configure `apiKeyHelper` (Optional)

Only needed if the user chose explicit token management in Step 5. Add to `~/.claude/settings.json`:

```json
{
  "apiKeyHelper": "bash -c 'source \"$HOME/.claude/secrets.sh\" && case \"${CLAUDE_PROVIDER:-}\" in deepseek) echo -n \"$DEEPSEEK_TOKEN\";; ali-qwen) echo -n \"$ALI_TOKEN\";; zhipu) echo -n \"$ZHIPU_TOKEN\";; *) echo -n \"\";; esac'"
}
```

**Important**: Read the existing `settings.json` first, merge the `apiKeyHelper` field into it, and write back. Never overwrite existing settings.

### Step 7: Configure `.gitignore`

Ensure the project's `.gitignore` allows `model-selector` but blocks secrets:

```gitignore
# Allow model-selector (project config, no secrets)
!.claude/model-selector
```

The `~/.claude/secrets.sh` is user-level (outside the project), so it doesn't need a project `.gitignore` entry. But remind the user never to commit it.

### Step 8: Verify the Setup

Run these verification steps:

1. **JSON validation**: `python3 -m json.tool .claude/model-selector > /dev/null`
2. **Shell function defined**: Tell the user to run `source ~/.bashrc` (or `source ~/.zshrc`), then `type claude` — should show the function definition
3. **Secrets permissions** (if applicable): `ls -l ~/.claude/secrets.sh` — should show `-rw-------`
4. **Settings merge** (if applicable): `python3 -m json.tool ~/.claude/settings.json > /dev/null`

Finally, tell the user to `cd` into the project directory and run `claude` — they should see the model selection menu.

## Platform-Specific Notes

### Linux (bash)

- Config file: `~/.bashrc`
- The `claude()` function uses bash `read -p` syntax
- Python 3 is usually available as `python3`; some minimal distros may need `apt install python3`
- `/dev/tty` is standard on all Linux distributions

### macOS (zsh)

- Config file: `~/.zshrc` (macOS default shell since Catalina)
- The `claude()` function uses zsh `read "var?prompt: "` syntax
- Python 3 is pre-installed or available via Xcode CLI tools (`xcode-select --install`)
- `/dev/tty` works in Terminal.app, iTerm2, and SSH with pseudo-terminal allocation

### Windows

Windows does **not** support the `claude()` shell function directly because:

- Windows shells (cmd.exe / PowerShell) do not support bash/zsh syntax
- `/dev/tty` does not exist on Windows
- The `command` builtin and POSIX `export`/`unset` are bash/zsh-specific

**Recommended approach for Windows users:**

| Option | Setup | Notes |
|--------|-------|-------|
| **WSL 2** (recommended) | Install Ubuntu via `wsl --install`, then follow the Linux (bash) instructions | Full Linux environment, works perfectly |
| **Git Bash** | Install Git for Windows with "Git Bash" component, then follow the Linux (bash) instructions | `/dev/tty` is emulated and usually works |
| **MSYS2 / Cygwin** | Follow Linux (bash) instructions | Heavier setup, but functional |

> Do NOT attempt to use PowerShell or cmd.exe — the shell function is fundamentally incompatible.
> Always guide Windows users to WSL or Git Bash first.

## Network Requirements Summary

| Action | Needs proxy in China? | Notes |
|--------|:--:|-------|
| `npm install -g @anthropic-ai/claude-code` | **Maybe** | Use `--registry=https://registry.npmmirror.com`; if still blocked, set `npm config set proxy` |
| `claude` first launch / OAuth | **Maybe** | Anthropic's auth endpoint may need proxy; if stuck, set `https_proxy` temporarily |
| API calls to DeepSeek / DashScope / Zhipu | **No** | These are all China-hosted or China-accessible endpoints |
| `git clone` from GitHub | **Often yes** | Use `https_proxy=http://127.0.0.1:7897` or configure git proxy |

> ⚠️ The model-selector skill itself does NOT configure any proxy. If the user's environment requires
> a proxy for npm/OAuth/GitHub, they must set it up separately (e.g., `export https_proxy=...` in `~/.zshrc`).

## Troubleshooting Reference

| Symptom | Cause | Fix |
|---------|-------|-----|
| `claude` starts without menu | `~/.bashrc` not loaded, or no `.claude/model-selector` | `source ~/.bashrc`; create the file |
| Python `EOFError` | `sys.stdin = open('/dev/tty')` missing or `/dev/tty` unavailable | Add the line; in SSH use `ssh -t` for pty allocation |
| `Auth conflict` warning | Residual `ANTHROPIC_AUTH_TOKEN` from a previous session (e.g. custom mode) | The `unset` at function entry clears it automatically. If persistent, run `unset ANTHROPIC_AUTH_TOKEN` manually |
| Custom mode API key not working | `unset ANTHROPIC_AUTH_TOKEN` was placed at function end (after custom mode sets it) | Move `unset` to the **top** of the function — clears old tokens, lets custom mode's fresh key survive |
| Wrong provider in project without model-selector | Stale env vars from a previous model-selector session persist | The `else` branch unsets all model vars, forcing Anthropic defaults. Or `cd` to a project with model-selector |
| API 401/403 | Wrong token for provider | Check `secrets.sh` tokens; verify `CLAUDE_PROVIDER` matches |
| `model-selector invalid` | Malformed JSON | Run `python3 -m json.tool .claude/model-selector` to see the error |

## Security Reminders

Always remind the user:

1. **`~/.claude/secrets.sh`** must have `600` permissions and **never** be committed to git
2. **`.claude/model-selector`** contains no secrets — it **should** be committed to share with the team
3. Custom mode API keys exist only in shell memory and are cleared on exit or next `claude` invocation
4. In multi-user environments, ensure other users cannot read your `secrets.sh`
