# Anti-Patterns — Lessons Learned

Seven concrete failure cases from previous paper-reading runs. Read before starting fact-check.

## 1. Hallucinated arXiv IDs

**What happened**: 37 papers had fabricated arXiv IDs. Plausible-looking IDs like `2605.24220` did not exist.

**Why it happens**: The model knows the arXiv ID format and generates IDs that "look right" but were never assigned.

**Fix**: For every paper, search `"arxiv {ID}"` on the web. Only accept IDs that return a real paper page. If unsure, search by paper title instead.

## 2. Hallucinated GitHub Repos

**What happened**: Multiple code links pointed to repos that didn't exist. The model invents plausible `github.com/org/repo` URLs.

**Fix**: Verify every GitHub link before including it. A 404 = ❌ in the code link column.

## 3. Fabricated Parameters and Scores

**What happened**: Parameter counts, token counts, and benchmark scores were generated from training data priors rather than verified from the actual paper.

**Fix**: Every number must be traceable to an official source (paper PDF, model card, official blog post). When in doubt, leave it blank or mark `Unknown`.

## 4. Time Range Violations

**What happened**: 37 papers were outside the specified time range (2025.01–2026.06). Papers from Dec 2024, July 2026, etc. slipped through.

**Fix**: Check the publication date for every paper. If the date isn't clearly within range, exclude it. "Close" doesn't count — Dec 2024 is NOT in 2025.01–2026.06.

## 5. Wrong Company Attribution

**What happened**: Genie Envisioner was attributed to NVIDIA but actually comes from AGIBOT (智元机器人). The paper mentions NVIDIA hardware but the research is from AGIBOT.

**Fix**: Read the author affiliations on the actual paper, not the acknowledgments section. Hardware sponsors ≠ authors.

## 6. Missed Company Coverage

**What happened**: Only covered companies the user explicitly mentioned. Missed several companies that had published papers in the time range.

**Fix**: After the initial search, run the coverage verification in Phase 6. For each unchecked company, do a targeted search. Better to find nothing than to miss a paper.

## 7. Blind Trust in Parallel Agents

**What happened**: 6 parallel research agents all failed with API 403 errors. The workflow had no fallback and silently produced empty results.

**Fix**: Always verify agent outputs. If agents fail, fall back to manual WebSearch + WebFetch. Never assume agents succeeded just because they didn't error — check the actual content returned.
