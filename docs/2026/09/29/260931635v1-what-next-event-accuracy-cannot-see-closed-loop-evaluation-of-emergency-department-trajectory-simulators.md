# What Next-Event Accuracy Cannot See: Closed-Loop Evaluation of Emergency Department Trajectory Simulators

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Zhen Xuen Brandon Low
- 机构：Monash University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31635v1) · [PDF](https://arxiv.org/pdf/2609.31635v1)

## TLDR
The paper introduces EDSim-Bench, a closed-loop evaluation of emergency department trajectory simulators on MIMIC-IV-ED and MC-MED, showing that near-identical next-event accuracy hides large rollout failures and that all-position supervision improves stability but does not fully resolve them, motivating simulator evaluation beyond next-event metrics.

## Abstract
Clinical trajectory models are usually evaluated by next-event accuracy on observed histories. Simulation is different: models must condition on their own generated events, allowing errors to compound. Although this problem is well known in sequence modelling, it has not been systematically quantified for clinical trajectory simulators. We developed EDSim-Bench to evaluate this failure mode using 425,028 MIMIC-IV-ED stays, with external replication on MC-MED, and release the evaluation protocol and scoring code. Starting from held-out visit prefixes, models generate the remainder of each visit and are evaluated on termination, event composition, timing, conditional fidelity, and occupancy forecasting, with a train-only order-3 n-gram as a reference baseline. Despite next-event accuracies within 0.001, three neural architectures behaved very differently under rollout. Across seeds, one Transformer recipe ranged from 0.43 to 0.96 in termination score and from 4.2- to 137-fold the divergence of the n-gram; no prefix-trained neural model approached the n-gram on termination or event composition. Inference-time interventions improved termination but did not jointly recover composition and timing. Supervising every eligible sequence position rather than only the final prefix position was associated with one to two orders of magnitude lower divergence across Transformer, GRU, and LSTM models, with the pattern persisting under model scaling, temporal shift, and external-site evaluation. Nevertheless, even the best model generated visits approximately half as long as observed, and model rankings reversed on occupancy forecasting, a downstream quantity relevant to bed management. These results show that next-event accuracy is insufficient to evaluate clinical trajectory simulators and motivate closed-loop evaluation across seeds, rollout criteria, and downstream tasks.
