# FALCON-Discover: Discovering Concentrated False-Confidence Regions for Calibration

- 区域：速读区
- 排名：14
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Filippo Cenacchi, Longbing Cao, Runze Yang
- 机构：Macquarie University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18278v1) · [PDF](https://arxiv.org/pdf/2607.18278v1)

## TLDR
FALCON-Discover introduces a post-hoc, model-agnostic framework that identifies compact regions of false-confidence—where models are highly confident yet wrong—by ranking predictions based on discrepancies between confidence, local support, neighborhood agreement, and perturbation stability, and shows across multiple tabular datasets that this discrepancy-based ranking substantially outperforms raw confidence and trust-score baselines in recovering dangerous errors, establishing false-confidence concentration as a family-level discovery problem.

## Abstract
Calibration is usually evaluated in aggregate, but the most dangerous failures are often local: predictions that remain highly confident despite being wrong. We study this failure mode as false-confidence concentration, the extent to which confident errors occupy compact, discoverable regions of prediction space. We introduce FALCON-Discover, a post-hoc, model-agnostic framework that ranks predictions using discrepancy signals from confidence, local support, neighborhood agreement, and perturbation stability. Across seven binary tabular datasets, four seeds, five-fold cross-fitting, and strong learners including XGBoost and CatBoost, we find that false-confidence concentration is recurrent but regime-dependent. At the main confidence threshold, discrepancy-based ranking substantially outperforms the strongest validation-selected calibration or trust-scoring baseline in the strongest regimes, while raw confidence recovers little dangerous-error mass. The best detector varies across datasets: learned discrepancy is strongest when multiple cues must be combined, whereas stability-centered ranking works best when local decisional fragility dominates. These results show that dangerous overconfidence is better treated as a family-level discovery problem than as a single-score calibration problem, and motivate calibration strategies that explicitly target regions where confidence, support, and stability diverge.
