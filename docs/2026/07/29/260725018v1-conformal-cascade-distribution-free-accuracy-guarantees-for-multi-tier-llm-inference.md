# Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yifan Dou, Shikan Fang, Shibo Li
- 机构：Florida State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25018v1) · [PDF](https://arxiv.org/pdf/2607.25018v1)

## TLDR
Conformal Cascade replaces confidence-threshold deferral in LLM cascades with a conformal prediction set size rule, providing distribution-free, finite-sample accuracy guarantees and enabling explicit cost–accuracy trade-offs without model training or logprob access.

## Abstract
Large language model (LLM) cascades reduce inference cost by routing easy queries to a small model and deferring hard queries to a larger one. Production cascades govern this deferral through a confidence threshold, but LLM confidence scores are miscalibrated, the threshold must be tuned per model pair and per domain, and no setting yields a formal bound on cascade accuracy. We introduce \textbf{Conformal Cascade} (CC), a multi-tier inference framework that uses conformal prediction set size as the deferral rule: accept when the calibrated set collapses to a single answer, defer otherwise. The procedure delivers a distribution-free, finite-sample accuracy guarantee. By a per-tier union bound, the prediction set at the accepting tier covers the correct answer with probability at least $1 - Kα$ for any user-specified $α$; under a selection-preservation condition (consistent with, but not strictly implied by, our marginal coverage results), the bound tightens to $1 - α$. We further characterise expected cascade cost as an explicit function of $α$ and the calibration-set acceptance rate. Across 18 multiple-choice benchmarks spanning science, medicine, commonsense, and standardized exams, evaluated on two-tier cascades drawn from four open-weight model families, CC strictly improves over the strongest calibration-tuned heuristic cascade on the majority of family--benchmark pairs, with the largest gains on reasoning-heavy benchmarks where majority vote is unreliable; on easier benchmarks the cascade commits the vast majority of queries to the small model at no accuracy cost. Extension to open-ended generation requires an answer-clustering step that we leave for future work. The method requires no model training and only black-box API access.
