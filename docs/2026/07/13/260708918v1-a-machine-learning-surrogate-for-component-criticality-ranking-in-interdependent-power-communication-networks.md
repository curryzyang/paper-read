# A Machine Learning Surrogate for Component Criticality Ranking in Interdependent Power-Communication Networks

- 区域：速读区
- 排名：3
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Sohini Roy, Xheni Hylviu
- 机构：University of Nevada, Las Vegas
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08918v1) · [PDF](https://arxiv.org/pdf/2607.08918v1)

## TLDR
This paper develops a machine-learning surrogate (Gradient Boosting) that predicts cascade severity and ranks component criticality in interdependent power-communication networks, achieving Spearman correlations over 0.85 and demonstrating that inter-layer dependency information is key to its performance.

## Abstract
Cyber-physical power systems are vulnerable to cascading failures caused by tight interdependencies between power and communication infrastructures. Evaluating these failures over large N-k contingency sets with a high-fidelity simulator is computationally prohibitive for resilience planning. Using the previously published Modified Implicative Interdependency Model (MIIM) as the ground-truth cascade simulator, this paper develops a machine-learning surrogate that predicts contingency severity from leakage-free structural features and derives a component-criticality ranking for prioritized hardening analysis. On the IEEE 118-bus system, the Gradient Boosting surrogate achieves Spearman correlations of 0.849 for per-contingency severity prediction and 0.853 for per-component criticality ranking, while remaining stable across three independently sampled datasets. MIIM-derived component criticality itself reproduces only to a Spearman of approximately 0.85 under the present sampling pipeline, and the surrogate operates at this empirical ceiling to within sampling variation. Topological centrality measures on the full interdependent network provide meaningful baselines (Spearman 0.60-0.69), and feature ablation shows that the surrogate's advantage is driven primarily by inter-layer dependency information. These results support a two-stage workflow in which the surrogate rapidly ranks candidate components and MIIM is reserved for selective verification.
