# 15-Column Specification

Detailed field descriptions with examples for the paper-reading Excel format.

## Column Definitions

### 1. 论文/模型名称
Format: `Model Name`\n`(arXiv: XXXX.XXXXX, Month Year)`\n`Organization`

Example:
```
Seed 2.0
(arXiv: 2601.12345, Jan 2026)
ByteDance
```

### 2. 训练阶段
Training stages used. Common values:
- `CPT` (Continued Pretraining)
- `SFT` (Supervised Fine-Tuning)
- `RLHF` / `DPO` / `PPO`
- `LoRA` / `QLoRA`
- `Pre-training from scratch`

Use `→` to indicate pipeline order: `CPT → SFT → DPO`

### 3. 数据集来源
Where training data came from:
- `开源` (open-source: CommonCrawl, The Pile, etc.)
- `自建` (proprietary/internal)
- `合成` (synthetic/generated)
- `混合` (mixed sources — specify ratio if known)

### 4. 数据集配比
Data mixing ratios between sources. Examples:
- `Web:Code:Math = 60:20:20`
- `Multilingual: 45% English, 30% Chinese, 25% other`
- `Unknown` if not disclosed

### 5. 数据集质量控制
Methods used for data cleaning:
- Deduplication (exact / fuzzy / MinHash)
- Heuristic filtering (length, perplexity, language detection)
- Model-based scoring (classifier, reward model)
- Human review

### 6. 关键超参
Key hyperparameters disclosed:
- Learning rate (peak, schedule)
- Batch size (global, per-device)
- Optimizer (AdamW, Lion, etc.)
- Context length / max sequence length
- Model dimension, layers, heads (if architecture paper)

### 7. 资源/实验时长
Compute resources:
- GPU type and count (e.g., `2048×H100 80GB`)
- Training duration (e.g., `~45 days`)
- Total FLOPs or GPU-hours if disclosed

### 8. 评测方法
Benchmarks and evaluation protocols:
- Standard benchmarks (MMLU, HumanEval, GSM8K, etc.)
- Custom evaluations
- Human evaluation (inter-rater agreement if available)
- Safety/alignment evaluations

### 9. 消融实验
What was ablated and key findings:
- Data size / quality ablations
- Architecture choices
- Training recipe variations
- Scaling law studies

### 10. 泛化能力
Cross-domain or cross-lingual generalization:
- Zero-shot / few-shot transfer results
- Multilingual performance
- Domain adaptation (code, math, medical, legal)

### 11. 数据集/代码是否开源
Status of artifacts:
- `✅ 开源` + links if released
- `⚠️ 部分开源` + what's available
- `❌ 未开源` if not released
- `📅 计划开源` + timeline if announced

### 12. 借鉴点
Actionable takeaways for practitioners:
- Data pipeline techniques worth adopting
- Training tricks (LR schedule, initialization, etc.)
- Architecture decisions with empirical support
- What NOT to do (negative results that are informative)

### 13. 论文链接
Primary paper URL: arXiv abstract page preferred.
Format: `https://arxiv.org/abs/XXXX.XXXXX`
Alternative: blog post, technical report PDF, model card.

### 14. 数据集链接
Dataset URL if publicly available, or `❌`.
- HuggingFace dataset: `https://huggingface.co/datasets/...`
- GitHub: `https://github.com/org/repo`
- Self-hosted: direct download link

### 15. 代码链接
Code repository URL or `❌`.
- GitHub: `https://github.com/org/repo`
- HuggingFace: `https://huggingface.co/org/model`
- Self-hosted: GitLab, BitBucket, etc.

## Paper Data Template

```python
def P(*args):
    """Helper: validates exactly 15 string arguments."""
    assert len(args) == 15, f"Expected 15 args, got {len(args)}"
    return list(args)

P("Model Name\n(arXiv: XXXX.XXXXX, Mon 2025)\nOrganization",
  "CPT → SFT → DPO",
  "开源 (CommonCrawl) + 自建",
  "Web:Code:Math = 70:15:15",
  "MinHash dedup + perplexity filter + model scoring",
  "LR=3e-4, batch=4M tokens, AdamW, ctx=8192",
  "2048×H100, ~60 days",
  "MMLU, HumanEval, GSM8K, MATH, HumanEval+",
  "Data quality: dedup vs no dedup; LR schedule: cosine vs constant",
  "Strong multilingual (45+ languages), zero-shot code generation",
  "✅ 开源 / ❌ 未开源 / ⚠️ 部分开源",
  "MinHash dedup at scale works; synthetic data for code boosts HumanEval 3pt",
  "https://arxiv.org/abs/XXXX.XXXXX",
  "https://huggingface.co/datasets/org/dataset",
  "https://github.com/org/repo")
```
