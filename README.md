# Skills

Collection of Claude Code custom skills.

## Directory Structure

```
skills/
├── demo-skill/
│   └── hello.md        # Simple greeting demo skill
├── setup-model-selector/
│   ├── SKILL.md         # Multi-provider model-selector setup guide
│   ├── references/
│   │   └── shell-function.md  # bash/zsh shell function templates
│   └── evals/
│       └── evals.json   # Test cases and assertions
└── README.md
```

## Skill Format

Each skill is a markdown file with YAML frontmatter:

```markdown
---
name: skill-name
description: What this skill does
version: 1.0.0
---

Instructions for the AI to follow...
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [hello](demo-skill/hello.md) | Greets the user and displays system information |
| [setup-model-selector](setup-model-selector/SKILL.md) | Set up Claude Code multi-provider model-selector system (DeepSeek, Qwen, GLM, custom APIs) |
