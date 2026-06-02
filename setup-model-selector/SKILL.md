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
- `unset ANTHROPIC_AUTH_TOKEN` prevents auth conflicts between sessions

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
  "apiKeyHelper": "bash -c 'source \"$HOME/.claude/secrets.sh\" && case \"$CLAUDE_PROVIDER\" in deepseek) echo -n \"$DEEPSEEK_TOKEN\";; ali-qwen) echo -n \"$ALI_TOKEN\";; zhipu) echo -n \"$ZHIPU_TOKEN\";; *) echo -n \"\";; esac'"
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

## Troubleshooting Reference

| Symptom | Cause | Fix |
|---------|-------|-----|
| `claude` starts without menu | `~/.bashrc` not loaded, or no `.claude/model-selector` | `source ~/.bashrc`; create the file |
| Python `EOFError` | `sys.stdin = open('/dev/tty')` missing or `/dev/tty` unavailable | Add the line; in SSH use `ssh -t` for pty allocation |
| `Auth conflict` warning | Residual `ANTHROPIC_AUTH_TOKEN` from previous session | The `unset` in the function handles this; if persistent, run `unset ANTHROPIC_AUTH_TOKEN` manually |
| API 401/403 | Wrong token for provider | Check `secrets.sh` tokens; verify `CLAUDE_PROVIDER` matches |
| `model-selector invalid` | Malformed JSON | Run `python3 -m json.tool .claude/model-selector` to see the error |

## Security Reminders

Always remind the user:

1. **`~/.claude/secrets.sh`** must have `600` permissions and **never** be committed to git
2. **`.claude/model-selector`** contains no secrets — it **should** be committed to share with the team
3. Custom mode API keys exist only in shell memory and are cleared on exit or next `claude` invocation
4. In multi-user environments, ensure other users cannot read your `secrets.sh`
