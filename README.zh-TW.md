# Claude Code 多供應商模型選擇器

**繁體中文** | [English](README.md) | [简体中文](README.zh-CN.md)

讓 Claude Code 使用 DeepSeek、通義千問、智譜 GLM 或任何相容 Anthropic API 的供應商——無需修改程式碼，專案內互動式切換模型。

## 這是什麼？

Claude Code 是 Anthropic 官方推出的 AI 程式設計助手 CLI。它原生僅支援 Anthropic 自家的 API。本專案透過一個**零侵入**的 Shell 函數技巧，在每次啟動 `claude` 時讓你**自由選擇**想用的模型供應商——無需修改原始碼，無需包裝腳本，三分鐘即可完成。

```
$ claude
=== 選擇模型 ===
  1) DeepSeek V4
  2) Qwen-3.7-Max
  3) GLM-5.1
  4) 自訂
請輸入編號 [1-4]（預設 1）：
```

## 功能特色

- **專案級模型切換**——每個專案在 `.claude/model-selector` 中宣告自己的模型清單，團隊成員 `git clone` 後自動生效
- **主迴圈／子代理分離**——主對話使用高效能模型（如 qwen3.7-max），子代理呼叫使用輕量模型（如 qwen3.6-flash），節省 **50-80%** 子代理成本
- **零侵入**——Shell 函數僅包裝 `command claude`，不對 Claude Code 本身做任何修改
- **自訂模式**——隨時輸入任意模型名稱 + Base URL + API Key 來使用臨時供應商

## 快速開始

### 1. 安裝 Claude Code

**必要條件：** Node.js ≥ 18 與 Python 3。

```bash
# 標準安裝（全球網路）
npm install -g @anthropic-ai/claude-code

# 中國使用者（使用 npm 鏡像）
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com

# 驗證安裝
claude --version
```

### 2. 取得 API Key

| 供應商 | 控制台 | 備註 |
|----------|---------|-------|
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | 註冊即送免費額度 |
| **阿里百煉 (DashScope)** | [dashscope.aliyun.com](https://dashscope.aliyun.com) | 按量付費 |
| **智譜 (GLM)** | [open.bigmodel.cn](https://open.bigmodel.cn) | 註冊即送免費額度 |

> 國內 API（DeepSeek、DashScope、智譜）**從中國可直接存取**——無需代理。

### 3. 設定模型選擇器

在專案目錄中開啟 Claude Code 並告訴它：

> "幫我用 setup-model-selector skill 設定模型選擇器"

Skill 將自動完成：
1. 建立含模型清單的 `.claude/model-selector`
2. 將 `claude()` Shell 函數寫入 `~/.zshrc`（macOS）或 `~/.bashrc`（Linux）
3. （可選）設定 `~/.claude/secrets.sh` 進行安全的 Token 管理
4. 驗證一切正常運作

設定完成後，在任何含有 `.claude/model-selector` 的專案中執行 `claude`，即會顯示模型選擇選單。

## 平台支援

| 平台 | Shell | 設定檔 | 狀態 |
|----------|-------|-------------|:--:|
| **macOS** | zsh | `~/.zshrc` | ✅ 完整支援 |
| **Linux** | bash | `~/.bashrc` | ✅ 完整支援 |
| **Windows** | WSL 2 / Git Bash | `~/.bashrc` | ✅ 透過 WSL/Git Bash 運作 |
| **Windows 原生** | cmd / PowerShell | — | ❌ 不支援 |

> Windows 使用者：請先安裝 WSL（`wsl --install`），再遵循 Linux 指示操作。Shell 函數依賴 `/dev/tty`、`command` 內建指令和 POSIX `export`/`unset`——這些在 cmd/PowerShell 中均不存在。

## 網路需求

| 操作 | 需要代理？ | 備註 |
|--------|:--:|-------|
| `npm install` Claude Code | **可能** | 在中國使用 `--registry=https://registry.npmmirror.com` |
| `claude` 首次啟動 / OAuth | **可能** | Anthropic 的驗證端點；若卡住則臨時設定 `https_proxy` |
| 呼叫 DeepSeek / Qwen / GLM API | **不需** | 國內端點，從中國可直接存取 |
| `git clone` 本倉庫 | **通常需要** | 使用 `https_proxy=http://127.0.0.1:7897` 或下載 ZIP |

## 運作原理

```
你輸入：claude
    ↓
Shell 函數攔截（~/.zshrc 中的 claude()）
    ↓
檢查目前專案中的 .claude/model-selector
    ↓
  找到  → Python 解析 JSON → 顯示選單 → 你選模型 → 注入環境變數
  未找到 → 清除所有模型變數 → Claude Code 使用 Anthropic 預設值 + OAuth
    ↓
command claude 啟動真正的 Claude Code 二進位檔
```

### 架構

三個層次：

1. **環境變數層**——`claude()` Shell 函數在啟動 Claude Code 前將模型設定注入目前 Shell 處理序
2. **互動層**——內嵌的 Python 腳本（位於 heredoc 內部）處理 JSON 解析、選單生成和使用者輸入。UI 輸出至 stderr，資料輸出至 stdout
3. **驗證層**——Claude Code 內建的 OAuth 預設處理驗證。可選地，`settings.json` 中的 `apiKeyHelper` + `~/.claude/secrets.sh` 提供針對各供應商的 Token 路由

### 模型槽位對應

Claude Code 使用 6 個模型槽位。模型選擇器將它們對應至僅 2 個實際模型：

```
"model"（高效能）→ ANTHROPIC_MODEL、ANTHROPIC_DEFAULT_OPUS_MODEL、ANTHROPIC_DEFAULT_SONNET_MODEL
"fast" （輕量級）→ ANTHROPIC_DEFAULT_HAIKU_MODEL、ANTHROPIC_SMALL_FAST_MODEL、CLAUDE_CODE_SUBAGENT_MODEL
```

以此在主迴圈上保持高品質，同時降低子代理成本。

## 專案結構

```
skills/
├── README.md                          ← 英文版
├── README.zh-CN.md                    ← 簡體中文版
├── README.zh-TW.md                    ← 繁體中文版（您正在看的）
├── demo-skill/
│   └── hello.md                       ← 簡單的問候展示 skill
├── paper-reading/
│   ├── SKILL.md                       ← 互動式論文調查工作流程
│   ├── xlsx_writer.py                 ← 純標準庫 Excel 產生器
│   └── references/                    ← 欄位規範、公司清單、反模式
├── setup-model-selector/              ← 核心：模型選擇器設定 skill
│   ├── SKILL.md                       ←    完整逐步指南（AI 可執行）
│   ├── references/
│   │   └── shell-function.md          ←    bash/zsh 函數範本
│   └── evals/
│       └── evals.json                 ←    51 條自動化測試斷言
├── skill-creator/                     ← 工具：建立新的 skill
│   ├── SKILL.md                       ← 可迭代地建立與改善 skill
│   ├── agents/                        ← 子代理定義
│   ├── references/                    ← Skill 撰寫指南
│   └── scripts/                       ← 評估與最佳化腳本
```

## 常見問題

**Q: 我切換到沒有 model-selector 的專案——會發生什麼事？**
A: 所有模型環境變數將被清除，Claude Code 回復至 Anthropic 預設值 + OAuth。不會殘留任何舊狀態。

**Q: 自訂模式的 API Key 安全嗎？**
A: 它僅存在於目前 Shell 處理序的記憶體中。關閉終端機即清除。下一次 `claude` 呼叫也會自動將其取消設定。

**Q: 可以在 Windows 原生環境使用嗎？**
A: 不可以。cmd 和 PowerShell 不支援 Shell 函數。您需要 WSL（`wsl --install`）或 Git Bash。

**Q: 安裝失敗／網路逾時？**
A: 檢查您的 npm 鏡像設定。如果正執行代理（Clash Verge / V2Ray 等），請確保 Shell 中已設定 `https_proxy`。

## Skills

| Skill | 描述 |
|-------|-------------|
| [hello](demo-skill/hello.md) | 向使用者打招呼並顯示系統資訊 |
| [paper-reading](paper-reading/SKILL.md) | 互動式 LLM 論文調查：搜尋、整理為 15 欄 Excel、逐條事實查核、產出深度分析報告 |
| [setup-model-selector](setup-model-selector/SKILL.md) | 設定 Claude Code 多供應商模型選擇器系統（DeepSeek、Qwen、GLM、自訂 API） |
| [skill-creator](skill-creator/SKILL.md) | 建立新 skill、修改與改善既有 skill、執行評估、基準測試效能 |

## 授權

Copyright 2026 terry

根據 Apache License, Version 2.0（「授權條款」）授權；
除非符合授權條款，否則您不得使用本檔案。
您可在以下網址取得授權條款副本：

    http://www.apache.org/licenses/LICENSE-2.0

除非適用法律要求或書面同意，軟體按「現狀」分發，
不提供任何明示或暗示的保證或條件。
有關授權條款下權限和限制的具體語言，請參閱授權條款。

完整授權文字請見 [LICENSE](LICENSE)。

## 更多資訊

- 完整逐步設定指南：[setup-model-selector/SKILL.md](setup-model-selector/SKILL.md)
- Shell 函數實作細節：[references/shell-function.md](setup-model-selector/references/shell-function.md)
