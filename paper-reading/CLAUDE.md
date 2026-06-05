# Paper Reading Skill — Project Instructions

## 项目说明

这是一个 Claude Code 自定义 Skill，用于系统性搜索、整理、验证和分析 LLM/AI 论文。
当用户输入 `/paper-reading` 时触发交互式搜索流程。

## 目录结构

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 入口 — 交互式配置 + 7 阶段执行流程 |
| `xlsx_writer.py` | 纯标准库 Excel 写入模块（无需 pip） |
| `references/` | 参考资料（栏目规范、公司清单、反模式） |

## /paper-reading Skill 流程

### Step 0: 交互式配置（AskUserQuestion）

通过 2 轮提问确定搜索范围：

**Call 1（范围）**：任务类型 → 时间范围 → 地域范围 → 公司选择
**Call 2（细节）**：研究领域(multiSelect) → 研究者追踪 → 输出格式

展示配置摘要后确认执行。

### 四种执行流程
- **A 全面搜索**: 完整 7 阶段（搜索→整理→验证→Excel→覆盖→分析）
- **B 更新现有库**: 读取现有数据 → 增量搜索 → 合并 → 重新生成
- **C 深度分析**: 针对指定论文生成 ≥10,000 字技术分析报告
- **D 快速查询**: 搜索特定公司/领域，文字摘要输出

### Phase 1–7（详见 SKILL.md）
1. **范围锁定** — 从交互配置派生 config 对象
2. **系统性搜索** — 按 公司×领域 矩阵生成 WebSearch 查询
3. **整理结构** — 15 列 Excel 格式（详见 `references/column-spec.md`）
4. **Fact-Check** — 100% 验证（最关键，详见 `references/anti-patterns.md`）
5. **生成 Excel** — `xlsx_writer.py` 纯标准库
6. **覆盖验证** — 180+ 家机构 + 10 位研究者（详见 `references/company-coverage.md`）
7. **深度分析** — 可选，≥10,000 字/篇

## 关键教训（Anti-patterns）

1. **绝不捏造 arXiv ID** — 曾捏造 37 篇，需三次重建才修复
2. **绝不捏造 GitHub 仓库** — 验证 repo 存在
3. **绝不捏造参数/分数** — 从官方来源引用
4. **严格执行时间范围** — 曾因不严格导致 37 篇超出范围
5. **验证公司归属** — Genie Envisioner 误标 NVIDIA，实为 AGIBOT
6. **主动搜索遗漏** — 不要仅覆盖用户提到的公司
7. **Agent 不可靠** — 并行 Agent 全部因 API 403 失败，用 WebSearch 替代

## 机构覆盖清单（180+ 家）

### 国内 71 家
**头部企业(14)**：字节 阿里 腾讯 百度 华为 智谱 DeepSeek 月之暗面 MiniMax 阶跃星辰 商汤 科大讯飞 快手 美团
**创业/中型(9)**：百川 零一万物 昆仑万维 面壁智能 地平线 小米 智元(AGIBOT) 无问芯穹 生数科技
**互联网/科技(3)**：京东 中国电信AI 联想
**C9高校(9)**：清华 北大 浙大 上交 复旦 南大 中科大 哈工大 西交大
**985强校(12)**：北航 人大 武大 华科 中山 东南 同济 北理 北邮 南开 天大 厦大
**其他重点(7)**：川大 电子科大 华南理工 大连理工 华东师大 北师大 兰大
**新兴研究型(4)**：西湖大学 南科大 上科大 国防科大
**其他特色(3)**：北交 西电 中南
**港校(5)**：港大 港中文 港科大 港理工 港城大
**研究院所(5)**：上海AI实验室 BAAI(智源) 中科院 鹏城实验室 之江实验室

### 国际 110+ 家
**头部企业(12)**：Google Meta OpenAI Anthropic Microsoft NVIDIA Apple Amazon xAI Mistral Cohere IBM
**创业公司(14)**：Databricks TogetherAI HuggingFace StabilityAI Salesforce EleutherAI Nous Reka AI21 AlephAlpha Writer SakanaAI Inflection Adept
**芯片/硬件(4)**：Cerebras SambaNova Groq Graphcore
**美国Top20**：Stanford MIT Berkeley CMU UW Princeton Cornell NYU UT-Austin UIUC Michigan GeorgiaTech Caltech Columbia Harvard UCLA UCSD UPenn Yale Wisconsin
**美国强校(15)**：Brown Duke JHU UMD UMass USC Northwestern Chicago UCI UCD UCSB Purdue PennState OhioState Rice
**美国其他(12)**：StonyBrook Rutgers Minnesota MichiganState Indiana UVA UNC TexasAM ArizonaState Rochester Northeastern Utah
**加拿大(8)**：Toronto Mila UBC Alberta McGill Waterloo SimonFraser Dalhousie
**英国(10)**：Oxford Cambridge UCL Imperial Edinburgh Manchester KCL Bristol Warwick Southampton
**瑞士(2)**：ETH EPFL
**德国(4)**：TUM TU-Berlin MaxPlanck Tübingen
**法国(4)**：ÉcolePoly Sorbonne ParisSaclay INRIA
**其他欧洲(5)**：Amsterdam KULeuven Copenhagen KTH Aalto
**日韩(8)**：Tokyo Kyoto TokyoTech Osaka KAIST SNU POSTECH Yonsei
**东南亚(4)**：NUS NTU SMU Malaya
**中东(4)**：TelAviv Hebrew Technion KAUST
**南亚(4)**：IIT-Delhi IIT-Bombay IIT-Madras IISc
**大洋洲(5)**：Melbourne Sydney ANU UNSW Queensland
**研究机构(5)**：AI2(Allen) LAION TuringInstitute MLCollective VectorInstitute
**垂直行业(7)**：Adobe ToyotaResearch ServiceNow Snowflake Predibase ScaleAI Waymo
