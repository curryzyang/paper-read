# From Phase Transition to Systemic Failure: A Decoupled Analytics Framework for GNN Robustness

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Shuai Yan, Dan Peng, Jie Li, Ke Wang
- 机构：Chengdu Jincheng College
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31656v1) · [PDF](https://arxiv.org/pdf/2609.31656v1)

## TLDR
This paper introduces a calibrated synthetic graph-regression framework that decouples label noise from feature distribution shift to show that GNNs remain relatively tolerant to moderate label corruption until a sharp transition near 50% noise, but suffer severe systemic failure under extreme distribution shift, making input-drift monitoring the more critical deployment safeguard.

## Abstract
Data quality is a major bottleneck for the reliable deployment of graph neural networks (GNNs) in real-world graph mining tasks. Among various sources of degradation, label noise and feature distribution shift (hereafter referred to as distribution shift) are two common yet fundamentally different challenges. To study their effects under controlled conditions, this paper constructs a synthetic homophilic graph regression benchmark in which the two factors can be manipulated separately. A total of 41 configurations and 410 runs are conducted to evaluate the behavior of representative GNN models under varying noise and shift conditions. The results show two distinct patterns. First, under additive label corruption, performance remains relatively stable over a broad range of noise settings and begins to deteriorate sharply only after an observed transition region around the 50 percent noise ratio. Second, under extreme feature distribution shift, all tested models suffer substantial degradation, with test MSE increasing by 48 times to 316 times and correlation dropping by 73 percent to 89 percent. These findings suggest that, in the present controlled setting, GNNs are considerably more tolerant to moderate label perturbation than to severe distribution mismatch. The study provides a controlled empirical baseline for understanding how data quality affects GNN-based graph mining systems and offers practical implications for deployment-oriented monitoring and model maintenance.
