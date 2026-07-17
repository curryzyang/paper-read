# Certified Domain Consistency for Multi-Domain Retrieval: Label-Free Per-Domain Contamination Control with Conformal Risk Guarantees

- 区域：速读区
- 排名：9
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Jayakumar Manoharan
- 机构：Electric Power Research Institute (EPRI)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14157v1) · [PDF](https://arxiv.org/pdf/2607.14157v1)

## TLDR
C3R introduces a label-free, drop-in control layer that certifies per-domain contamination budgets in multi-domain retrieval with finite-sample conformal risk guarantees, abstaining rather than silently violating on hard domains and achieving zero violations across thousands of calibrations while retaining more recall than alternative methods.

## Abstract
Retrieval over corpora that mix several domains often returns relevant but wrong-domain evidence that ranking metrics miss and that conformal risk control bounds only marginally, under-covering the worst domains. This work introduces C3R, a drop-in control layer that, from an inferred domain posterior and no query-time label, certifies a per-domain contamination budget where feasible and otherwise abstains rather than silently violating; on the hardest domains it guarantees a reduction, not a tight bound. The core is a two-split scheme built on risk-controlling prediction sets, whose finite-sample transfer bound crosses from the inferred to the true domain with fully estimable slack, supports heterogeneous budgets, and inverts for deployment. Population validity rests on this bound and a controlled simulation; across a thousand resampled calibrations the certificate never violates (a stability result) while marginal control violates the most-contaminated domain in every draw, and soft demotion retains more recall than the strongest calibrated cascade at equal certified contamination. The method replicates across open testbeds including an independent one from public federal regulations, and an LLM-judged downstream probe indicates wrong-authority grounding rises with contamination and falls under control. The layer is frozen-stack and reranker-agnostic.
