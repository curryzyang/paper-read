# The Missing "I Don't Know": Why Three Reasoning-Reliability Findings Converge on Calibrated Abstention

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Srijith Ravikumar
- 机构：Amazon.com LLC
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17686v1) · [PDF](https://arxiv.org/pdf/2609.17686v1)

## TLDR
Three seemingly unrelated LLM reliability findings—reasoning RL collapsing tool-reliability, safety-constrained generation causing scale-dependent truncation, and a proof that consistent reasoning without an implicit “I don’t know” function must hallucinate—converge on calibrated abstention as the missing capability, which current leaderboard benchmarks cannot select for because they assign zero reward to declining, so evaluation reform is necessary.

## Abstract
Three recent results describe what look like unrelated LLM reliability problems. Yin et al. (2026) show reasoning RL collapses tool-reliability representations. Suleymanov et al. (2026) show that under safety-constrained generation, large models rewrite flagged spans while small models truncate. Bastounis et al. (2024) prove any consistent-reasoning system without an implicit "I don't know" function must hallucinate infinitely often on broad problem classes. We argue these findings converge on a single intervention: calibrated abstention is what each independently identifies as the missing capability, even though the unavailability they document, a capability gap, a policy gap, and a recursion-theoretic gap, has a different source in each case. Honesty post-training has narrowed the gap in deployed models, but principled closure of the class Bastounis identifies requires a calibrated abstention function whose training signal at the leaderboard level is absent: dominant benchmarks assign zero reward to decline, so the leaderboard gradient that would select for the function does not exist. We propose four changes to evaluation: triple-scoring, abstention-rate reporting, capability-stratified evaluation, and mandatory calibration metrics. Benchmark reform is necessary, not sufficient, for closing the gap the theorem identifies.
