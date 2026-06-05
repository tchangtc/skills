# Claude Code 国内大模型配置指南

**简体中文** | [English](README.md) | [繁體中文](README.zh-TW.md)

让 Claude Code 用上 DeepSeek、通义千问、智谱 GLM 等国内大模型——无需修改代码，项目内交互式切换模型供应商。

## 这是什么？

Claude Code 是 Anthropic 官方推出的 AI 编程助手命令行工具。它原生只支持 Anthropic 自己的 API。本项目通过一个**零侵入**的 Shell 函数技巧，让你在每次启动 `claude` 时**一键选择**用哪家大模型——不需要修改 Claude Code 源码，国内模型 API 直连无需代理，三分钟搞定。

```
$ claude
=== 选择模型 ===
  1) DeepSeek V4
  2) Qwen-3.7-Max
  3) GLM-5.1
  4) 自定义
请输入编号 [1-4]（默认 1）：
```

## 能做什么

- **项目级模型切换**——每个项目在 `.claude/model-selector` 中声明自己的模型列表，`git clone` 后团队成员开箱即用
- **主循环 / 子代理分离**——主对话用强力模型（如 qwen3.7-max），子代理调用用轻量模型（如 qwen3.6-flash），**省 50-80%** 子代理费用
- **零侵入**——Shell 函数仅包装 `command claude`，不对 Claude Code 本身做任何修改
- **自定义模式**——随时输入任意模型名称 + Base URL + API Key 来使用临时供应商

## 三步上手

### 第一步：安装 Claude Code

**前提**：需要 Node.js ≥ 18 和 Python 3。

```bash
# 检查 Node.js
node --version   # 需要 ≥ 18

# 检查 Python
python3 --version

# 安装 Claude Code（国内用户用镜像）
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com

# 验证安装
claude --version
```

> 如果 npm 镜像也超时，设置代理：`npm config set proxy http://127.0.0.1:7890`，装完再 `npm config delete proxy`。

### 第二步：获取 API Key（三选一即可）

| 厂商 | 模型示例 | 注册地址 | 费用 |
|------|---------|---------|------|
| **DeepSeek** | deepseek-v4-pro | [platform.deepseek.com](https://platform.deepseek.com) | 注册送额度 |
| **阿里百炼** | qwen3.7-max | [dashscope.aliyun.com](https://dashscope.aliyun.com) | 按量付费 |
| **智谱** | glm-5.1 | [open.bigmodel.cn](https://open.bigmodel.cn) | 注册送额度 |

以上三个网站国内**直连不需要代理**。拿到 Key 后保存好——通常只显示一次。

### 第三步：配置模型选择器

在项目目录下执行 `claude`，如果还没有配置文件，直接告诉 Claude Code：

> "帮我用 setup-model-selector skill 配置国内大模型"

它会引导你完成：
1. 创建 `.claude/model-selector`（存模型列表）
2. 往 `~/.zshrc`（Mac）或 `~/.bashrc`（Linux）写入 `claude()` 函数
3. （可选）配置 `~/.claude/secrets.sh` 安全存储 API Key
4. 验证一切正常

配置完成后，在任意有 `.claude/model-selector` 的项目目录下启动 `claude`，就会弹出模型选择菜单。

## 系统兼容性

| 系统 | Shell | 配置文件 | 状态 |
|------|------|------|:--:|
| **macOS** | zsh | `~/.zshrc` | ✅ 完整支持 |
| **Linux** | bash | `~/.bashrc` | ✅ 完整支持 |
| **Windows** | WSL 2 / Git Bash | `~/.bashrc` | ✅ 通过 WSL/Git Bash 运行 |
| **Windows 原生** | cmd / PowerShell | — | ❌ 不支持 |

> Windows 用户：请先安装 WSL（`wsl --install`），再按 Linux 指引操作。Shell 函数依赖 `/dev/tty`、`command` 内建和 POSIX `export`/`unset`——这些在 cmd/PowerShell 中均不存在。

## 网络要求一览

| 操作 | 需要代理？ | 备注 |
|------|:--:|------|
| `npm install` 装 Claude Code | 可能需要 | 国内用 `--registry=https://registry.npmmirror.com` |
| `claude` 首次 OAuth 认证 | 可能需要 | 临时设 `https_proxy` |
| 调用 DeepSeek / Qwen / GLM API | **不需要** | 国内直连 |
| `git clone` 本项目 | 可能需要 | 用 `https_proxy=http://127.0.0.1:7897` 或直接下载 ZIP |

## 原理简述

```
你输入 claude
    ↓
Shell 函数拦截（~/.bashrc 里的 claude()）
    ↓
检测项目里有没有 .claude/model-selector
    ↓
  有 → Python 解析 JSON → 弹出菜单 → 你选模型 → 注入环境变量
  没有 → 清除模型变量 → Claude Code 走 Anthropic 默认 + OAuth
    ↓
command claude 启动真正的 Claude Code
```

### 架构

三个层次：

1. **环境变量层**——`claude()` Shell 函数在启动 Claude Code 前将模型配置注入当前 Shell 进程
2. **交互层**——内嵌的 Python 脚本（位于 heredoc 内部）处理 JSON 解析、菜单生成和用户输入。UI 输出至 stderr，数据输出至 stdout
3. **认证层**——Claude Code 内置的 OAuth 默认处理认证。可选地，`settings.json` 中的 `apiKeyHelper` + `~/.claude/secrets.sh` 提供针对各供应商的 Token 路由

### 模型槽位映射

Claude Code 使用 6 个模型槽位。模型选择器将它们映射至仅 2 个实际模型：

```
"model"（高性能）→ ANTHROPIC_MODEL、ANTHROPIC_DEFAULT_OPUS_MODEL、ANTHROPIC_DEFAULT_SONNET_MODEL
"fast" （轻量级）→ ANTHROPIC_DEFAULT_HAIKU_MODEL、ANTHROPIC_SMALL_FAST_MODEL、CLAUDE_CODE_SUBAGENT_MODEL
```

以此在主循环上保持高质量，同时降低子代理成本。

## 项目结构

```
skills/
├── README.md                          ← 英文版
├── README.zh-CN.md                    ← 简体中文版（你正在看的）
├── README.zh-TW.md                    ← 繁體中文版
├── demo-skill/
│   └── hello.md                       ← 简单的问候展示 skill
├── paper-reading/
│   ├── SKILL.md                       ← 交互式论文调研工作流程
│   ├── xlsx_writer.py                 ← 纯标准库 Excel 生成器
│   └── references/                    ← 栏目规范、公司清单、反模式
├── setup-model-selector/              ← 核心：模型选择器配置 skill
│   ├── SKILL.md                       ←    完整操作手册（AI 自动执行）
│   ├── references/
│   │   └── shell-function.md          ←    bash/zsh 函数模板
│   └── evals/
│       └── evals.json                 ←    51 条自动化测试用例
├── skill-creator/                     ← 工具：创建新的 skill
│   ├── SKILL.md                       ← 可迭代地创建和改善 skill
│   ├── agents/                        ← 子代理定义
│   ├── references/                    ← Skill 编写指南
│   └── scripts/                       ← 评估与优化脚本
```

## 常见问题

**Q: 切换到没有 model-selector 的项目——会怎样？**
A: 所有模型环境变量将被清除，Claude Code 恢复至 Anthropic 默认 + OAuth。不会残留任何旧状态。

**Q: 自定义模式输入的 API Key 安全吗？**
A: Key 只存在当前终端进程内存里，关掉终端就没了。下次启动 `claude` 也会自动清除。

**Q: Windows 原生能用吗？**
A: 不能。cmd 和 PowerShell 不支持 Shell 函数。必须先装 WSL（`wsl --install`）或 Git Bash。

**Q: 安装失败 / 网络超时怎么办？**
A: 检查 npm 镜像设置，确认代理（Clash Verge / V2Ray 等）在运行且 `https_proxy` 已设置。

## Skills

| Skill | 描述 |
|-------|-------------|
| [hello](demo-skill/hello.md) | 向用户打招呼并显示系统信息 |
| [paper-reading](paper-reading/SKILL.md) | 交互式 LLM 论文调研：搜索、整理为 15 列 Excel、逐条事实核查、产出深度分析报告 |
| [setup-model-selector](setup-model-selector/SKILL.md) | 配置 Claude Code 多供应商模型选择器系统（DeepSeek、Qwen、GLM、自定义 API） |
| [skill-creator](skill-creator/SKILL.md) | 创建新 skill、修改和改善已有 skill、执行评估、基准测试性能 |

## 许可证

Copyright 2026 terry

本项目基于 Apache License, Version 2.0（"许可证"）授权；
除非符合许可证，否则您不得使用本文件。
您可在以下网址获取许可证副本：

    http://www.apache.org/licenses/LICENSE-2.0

除非适用法律要求或书面同意，软件按"原样"分发，
不提供任何明示或暗示的保证或条件。
有关许可证下权限和限制的特定语言，请参阅许可证。

完整许可证文本见 [LICENSE](LICENSE)。

## 更多信息

- 完整的 Step-by-Step 配置流程：[setup-model-selector/SKILL.md](setup-model-selector/SKILL.md)
- Shell 函数实现细节：[references/shell-function.md](setup-model-selector/references/shell-function.md)
