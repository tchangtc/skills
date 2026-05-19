# Skills

Collection of Claude Code custom skills.

## Directory Structure

```
skills/
├── demo-skill/
│   └── hello.md        # Simple greeting demo skill
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
