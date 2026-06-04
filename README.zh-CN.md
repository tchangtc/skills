# Claude Code 国内大模型配置指南

**中文** | [English](README.md)

从零开始，让 Claude Code 用上 DeepSeek、通义千问、智谱 GLM 等国内大模型。

## 这是什么？

Claude Code 是 Anthropic 官方推出的 AI 编程助手命令行工具。它原生只支持 Anthropic 自己的 API，但国内用户因网络问题很难直接访问。

这个项目通过一个**零侵入**的 Shell 函数技巧，让你在每次启动 `claude` 时**一键选择**用哪家大模型——不需要修改 Claude Code 源码，国内模型 API 直连无需代理，三分钟搞定。

```
$ claude
=== 选择模型 ===
  1) DeepSeek V4
  2) Qwen-3.7-Max
  3) GLM-5.1
  4) 自定义
请输入编号 [1-4] (默认 1):
```

## 能做什么

- 在 **同一个项目** 里随时切换不同的大模型
- 主循环用强力模型（如 qwen3.7-max），子代理用轻量模型（如 qwen3.6-flash），**省 50-80% 费用**
- 配置文件跟着项目走，`git clone` 后队友开箱即用
- 国内模型 API **直连不需要代理**

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

| 厂商 | 模型 | 注册地址 | 费用 |
|------|------|---------|------|
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
3. 配置 `~/.claude/secrets.sh` 安全存储 API Key（可选）
4. 验证一切正常

配置完成后，在任意有 `.claude/model-selector` 的项目目录下启动 `claude`，就会弹出模型选择菜单。

## 系统兼容性

| 系统 | 方式 | 说明 |
|------|------|------|
| **macOS** | zsh + `~/.zshrc` | 原生支持，完美工作 |
| **Linux** | bash + `~/.bashrc` | 原生支持，完美工作 |
| **Windows** | WSL 2 或 Git Bash | 不支持 cmd/PowerShell，必须先装 WSL：`wsl --install` |

## 网络要求一览

| 操作 | 需要代理？ | 备注 |
|------|:--:|------|
| `npm install` 装 Claude Code | 可能需要 | 用 `--registry=https://registry.npmmirror.com` |
| `claude` 首次 OAuth 认证 | 可能需要 | 临时设 `https_proxy` |
| 调用 DeepSeek / Qwen / GLM API | **不需要** | 国内直连 |
| `git clone` 本项目 | 可能需要 | 或直接下载 ZIP |

## 项目结构

```
skills/
├── README.md                          ← 英文版
├── README.zh-CN.md                    ← 中文版（你正在看的）
├── setup-model-selector/              ← 核心：模型选择器配置
│   ├── SKILL.md                       ←    完整操作手册（AI 自动执行）
│   ├── references/
│   │   └── shell-function.md          ←    bash/zsh 函数模板
│   └── evals/
│       └── evals.json                 ←    51 条自动化测试用例
├── skill-creator/                     ← 工具：用来创建新 skill
└── demo-skill/                        ← 示例：一个简单的 hello skill
```

## 原理简述

```
你输入 claude
    ↓
Shell 函数拦截（~/.zshrc 里的 claude()）
    ↓
检测项目里有没有 .claude/model-selector
    ↓
  有 → Python 解析 JSON → 弹出菜单 → 你选模型 → 注入环境变量
  没有 → 清除变量 → Claude Code 走官方默认（Anthropic API）
    ↓
command claude 启动真正的 Claude Code
```

## 常见问题

**Q: 切换项目后模型变了？**
A: 环境变量跟随当前终端。如果你在项目 A 选了 Qwen，切到项目 B（没有 model-selector），变量会被清除，走回 Anthropic 默认。

**Q: 自定义模式输入的 API Key 安全吗？**
A: Key 只存在当前终端进程内存里，关掉终端就没了。下次启动 `claude` 也会自动清除。

**Q: Windows 能直接用吗？**
A: 不能。cmd 和 PowerShell 不支持 Shell 函数。必须先装 WSL（`wsl --install`）或 Git Bash。

**Q: 安装报错 / 网络超时怎么办？**
A: 检查 npm 镜像设置，确认代理（Clash Verge / V2Ray 等）在运行且 `https_proxy` 已设置。

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
