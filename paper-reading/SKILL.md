---
name: paper-reading
description: >
  Systematic paper-reading workflow: search latest LLM papers (2025-2026),
  organize by company, generate structured Excel with 15 columns,
  fact-check with 100% verification, and produce deep analysis reports.
---

# Paper Reading Skill

Systematically search, organize, fact-check, and analyze LLM/AI papers.
Interactive: user defines scope before execution begins.

## When to Use

- User types `/paper-reading`
- User asks to "survey recent papers", "track latest models", "调研论文"
- User wants a structured Excel with papers organized by company/category
- User requests deep analysis of specific papers (≥10K chars/paper)

---

## STEP 0: Interactive Configuration (REQUIRED)

When invoked, **always** ask the user to configure the search scope BEFORE any work.
Use two `AskUserQuestion` calls (max 4 questions per call).

### Call 1 — Scope (4 questions)

```
AskUserQuestion(questions=[
  {
    header: "任务类型",
    question: "你想做什么？",
    options: [
      { label: "全面搜索",   description: "从零开始搜索+整理+验证+生成Excel（完整7阶段）" },
      { label: "更新现有库", description: "基于已有Excel搜索新增/遗漏论文并合并" },
      { label: "深度分析",   description: "对指定论文生成≥10,000字技术分析报告" },
      { label: "快速查询",   description: "搜索特定公司/领域的最新论文，文字输出" }
    ],
    multiSelect: false
  },
  {
    header: "时间范围",
    question: "搜索哪个时间段的论文？（严格执行）",
    options: [
      { label: "最近6个月",        description: "当前日期往前推6个月" },
      { label: "最近1年",          description: "当前日期往前推12个月" },
      { label: "2025.01–2026.06",  description: "覆盖完整LLM爆发期" }
    ],
    multiSelect: false
  },
  {
    header: "地域范围",
    question: "覆盖哪些地区的公司？",
    options: [
      { label: "全部（国内+国外）", description: "180+家（71国内+110+国际）全覆盖" },
      { label: "仅国内",           description: "71家国内公司/大学/研究院" },
      { label: "仅国外",           description: "110+家国际公司/大学/研究机构" }
    ],
    multiSelect: false
  },
  {
    header: "公司选择",
    question: "覆盖哪些公司？（可在Other输入自定义）",
    options: [
      { label: "全部公司",  description: "地域范围内所有公司" },
      { label: "头部公司",  description: "国内10家(阿里/DeepSeek/字节/智谱/月暗面/商汤/百度/腾讯/华为/阶跃)+国外10家(OpenAI/Google/Meta/Anthropic/MS/NVIDIA/Mistral/xAI/Apple/Amazon)" },
      { label: "基座模型",  description: "仅发布过基座模型的公司" }
    ],
    multiSelect: false
  }
])
```

### Call 2 — Details (3 questions)

```
AskUserQuestion(questions=[
  {
    header: "研究领域",
    question: "关注哪些领域？（可多选，Other可输入：架构创新/多模态/代码数学/安全对齐）",
    options: [
      { label: "全部领域",     description: "基座+后训练+数据+架构+Agent+多模态" },
      { label: "核心LLM",     description: "基座模型技术报告 + RLHF/DPO/GRPO后训练" },
      { label: "Agent+推理",  description: "Agent架构、GRPO、RLVR、工具调用" },
      { label: "数据工程",     description: "数据策展、合成数据、质量控制" }
    ],
    multiSelect: true
  },
  {
    header: "研究者",
    question: "是否追踪特定研究者？（Other可补充人名）",
    options: [
      { label: "不需要",     description: "仅按公司搜索" },
      { label: "默认研究者", description: "何恺明(MIT) + 李飞飞(Stanford) + Stanford CRFM" },
      { label: "默认+自定义", description: "默认3位 + Other补充" }
    ],
    multiSelect: false
  },
  {
    header: "输出格式",
    question: "需要什么输出？",
    options: [
      { label: "仅Excel",         description: "15列结构化表格，按公司组织" },
      { label: "Excel+深度分析",  description: "Excel + 每篇≥10,000字分析报告" },
      { label: "Excel+趋势总结",  description: "Excel + 2,000字趋势洞察Markdown" },
      { label: "仅深度分析",      description: "指定论文的分析报告（不生成Excel）" }
    ],
    multiSelect: false
  }
])
```

### Configuration Summary

After both calls, display summary and confirm:

```
📋 搜索配置
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
任务:   {task_type}
时间:   {time_range}
地域:   {geographic}
公司:   {companies}
领域:   {domains}
研究者: {researchers}
输出:   {output_format}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```
AskUserQuestion(questions=[{
  header: "确认",
  question: "以上配置是否正确？",
  options: [
    { label: "确认，开始执行" },
    { label: "修改配置" }
  ],
  multiSelect: false
}])
```

If "修改配置", restart from Call 1.

---

## Execution Flows

Based on Q1 (任务类型):

| Flow | Phases | Output |
|------|--------|--------|
| **A. 全面搜索** | 1→2→3→4→5→6→7 | Excel (+ analysis if selected) |
| **B. 更新现有库** | Read existing → 2(gaps) → 4 → 5 → 6 | Updated Excel |
| **C. 深度分析** | Ask which papers → 7 | Markdown report |
| **D. 快速查询** | 2(targeted) | Text summary |

---

## Phase 1: Scope Lock

Derive configuration from interactive answers:

```python
config = {
    "time_range": ("2025.01", "2026.06"),
    "geographic": "all",
    "companies": ["OpenAI", "Google", ...],
    "domains": ["foundation", "post_training", "agent", ...],
    "researchers": ["何恺明", "李飞飞"],
    "output": "excel",
}
```

**STRICT**: Every paper must satisfy `date in time_range` AND `company in companies`.

---

## Phase 2: Systematic Search

Build queries dynamically from `config.companies × config.domains`.

### Search Matrix

| Domain | Query Template |
|--------|---------------|
| Foundation | `"{Company} technical report arxiv {year}"` |
| Post-Training | `"{Company} RLHF DPO alignment {year} arxiv"` |
| Data | `"data curation LLM pretraining {year} arxiv"` |
| Architecture | `"{Company} MoE Mamba architecture {year} arxiv"` |
| Agent/RL | `"{Company} LLM agent reinforcement learning {year}"` |
| Multimodal | `"{Company} vision language multimodal {year} arxiv"` |
| Code/Math | `"{Company} code generation math reasoning {year}"` |
| Safety | `"{Company} safety alignment red team {year}"` |

### Rules

1. **No parallel agents** — use direct `WebSearch` + `WebFetch` (agents fail with API 403, anti-pattern #7)
2. **≥2 queries per company** to maximize coverage
3. **Record immediately**: title, company, date, arXiv ID, source
4. **Proactive gap search**: 3-4 cross-company topic searches after per-company searches

---

## Phase 3: Organize — 15-Column Format

Every paper fills ALL 15 columns. See `references/column-spec.md` for field details.

| # | Column | Key Question |
|---|--------|-------------|
| 1 | 论文/模型名称 | Name + arXiv ID + date + org |
| 2 | 训练阶段 | CPT / SFT / RL / LoRA? |
| 3 | 数据集来源 | Open-source / proprietary / synthetic? |
| 4 | 数据集配比 | Mixing ratios? |
| 5 | 数据集质量控制 | Dedup / filtering / scoring? |
| 6 | 关键超参 | LR, batch size, context length? |
| 7 | 资源/实验时长 | GPU count, training time? |
| 8 | 评测方法 | Benchmarks? |
| 9 | 消融实验 | What was ablated? |
| 10 | 泛化能力 | Cross-domain / cross-lingual? |
| 11 | 数据集/代码是否开源 | Yes/No + links |
| 12 | 借鉴点 | Key takeaways |
| 13 | 论文链接 | arXiv / blog URL |
| 14 | 数据集链接 | Dataset URL or ❌ |
| 15 | 代码链接 | GitHub URL or ❌ |

**Order**: 🌍 International → 🇨🇳 Domestic → 🤖 Other → 👨‍🔬 Researchers → 📊 Independent

**Missing info**: Use `未披露` for unknown facts, `❌` for missing links. **NEVER** fabricate numbers.

---

## Phase 4: Fact-Check (CRITICAL — 100% pass)

For EVERY paper, verify:

```
□ arXiv ID matches paper title?
□ Parameter count from official source?
□ Token count from official source?
□ Benchmark scores from official source?
□ Date within time range?
□ Company attribution correct (author affiliations, not acknowledgments)?
□ All links reachable?
```

### Verification Protocol

```
WebSearch("arxiv {ID}")                    → confirm title matches
WebSearch("github.com/{org}/{repo}")       → confirm repo exists
WebSearch("{paper title} authors")         → confirm affiliation
```

### Golden Rules (see `references/anti-patterns.md`)

| # | Rule | Example Failure |
|---|------|----------------|
| 1 | ❌ NEVER fabricate arXiv IDs | 37 papers had fake IDs |
| 2 | ❌ NEVER fabricate GitHub repos | Plausible URLs that 404 |
| 3 | ❌ NEVER fabricate numbers | Parameter counts from priors |
| 4 | ✅ ALWAYS enforce time range | Dec 2024 ≠ 2025.01 |
| 5 | ✅ ALWAYS verify attribution | Genie Envisioner → AGIBOT, not NVIDIA |
| 6 | ✅ ALWAYS check coverage gaps | Run Phase 6 |
| 7 | ✅ ALWAYS fallback from agents | Direct WebSearch if agents fail |

---

## Phase 5: Generate Excel

```python
from xlsx_writer import generate_xlsx

HEADERS = [
    "论文/模型名称", "训练阶段\n(CPT/SPT/LoRA)",
    "数据集来源", "数据集配比", "数据集质量控制方法",
    "关键超参", "资源/实验时长", "评测方法",
    "消融实验", "泛化能力", "数据集/代码是否开源",
    "借鉴点", "论文链接", "数据集链接", "代码链接"
]

generate_xlsx("output.xlsx", HEADERS, papers,
              sheet_name="LLM Papers {time_range}",
              col_widths=[28, 18, 22, 22, 22, 20, 18, 22, 22, 20, 18, 28, 35, 35, 35])
```

**Naming**: `llm_papers_{start}_{end}.xlsx` (full) / `_updated.xlsx` (incremental)

**Reproducibility**: Also generate `generate_excel_by_company.py` — standalone script with hardcoded data.

---

## Phase 6: Coverage Verification

```python
for company in config.companies:
    found = any(company.lower() in str(row).lower() for row in papers)
    if not found:
        # Search one more time, then document reason
```

**Report format**:
```
📊 覆盖报告
✅ OpenAI: 2篇    ⚠️ Apple: 1篇(论文有限)    ❌ Tesla: 无LLM基座论文
总计: N篇, M/K家公司覆盖
```

---

## Phase 7: Deep Analysis (when selected)

Per-paper report (≥10,000 Chinese characters):

```
# {Paper Title} 深度分析
## 1. 基本信息        — 标题、作者、arXiv ID、日期、链接
## 2. 背景与动机      — 为什么重要？解决什么问题？
## 3. 技术细节        — 架构、数据管线、训练配方
## 4. 数据工程        — 来源、规模、质量控制、配比
## 5. 评测结果        — Benchmark得分表格、竞品对比
## 6. 消融实验        — 每个消融的结论和insight
## 7. 创新与局限      — 核心贡献 + 诚实评估
## 8. 开源与可复现性  — 开放了什么？复现难度？
## 9. 影响与后续      — 引用数、衍生工作、行业启示
```

After all papers: **Cross-Paper Comparison** chapter (training pipelines, data strategies, trends).

---

## Key Project Files

| File | Role |
|------|------|
| `SKILL.md` | This file — skill instructions |
| `xlsx_writer.py` | Pure-stdlib Excel generator |
| `CLAUDE.md` | Project-level instructions for this directory |

## Reference Files

| File | Purpose |
|------|---------|
| `references/column-spec.md` | 15-column field descriptions with examples |
| `references/company-coverage.md` | 180+ institution checklist + domain tags + researchers |
| `references/anti-patterns.md` | 7 concrete failure cases from previous runs |

---

## Anti-Pattern Quick Reference

Before any phase, re-read `references/anti-patterns.md`:

| # | Anti-Pattern | Prevention |
|---|-------------|------------|
| 1 | Fabricated arXiv IDs | WebSearch `"arxiv {ID}"` for every paper |
| 2 | Fabricated GitHub repos | Verify repo exists before linking |
| 3 | Fabricated parameters/scores | Only use numbers from official sources |
| 4 | Time range violations | Check date for every paper |
| 5 | Wrong company attribution | Check author affiliations |
| 6 | Missed company coverage | Run Phase 6 coverage check |
| 7 | Blind trust in agents | No parallel agents — use direct WebSearch |
