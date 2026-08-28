# Subgraph Filtering for Fair Graph Neural Networks

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Haohui Lu, jiyuan Tian, Fangyu Zhou, Shahadat Uddin
- 机构：The University of Sydney, Charles Darwin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26437v1) · [PDF](https://arxiv.org/pdf/2608.26437v1)

## TLDR
SF-GNN is a lightweight, architecture-agnostic framework that mitigates structural bias in graph neural networks by identifying and stochastically filtering bias-prone edges during message passing, achieving improved fairness with competitive predictive performance.

## Abstract
Graph neural networks (GNNs) can exhibit unfair behavior even when sensitive attributes are excluded from node features, because graph topology and message passing propagate group-correlated signals under sensitive homophily. Existing fairness-aware GNN methods mainly constrain representations or prediction distributions at a global level, without explicitly controlling the local structural pathways through which biased information propagates during aggregation. We propose Subgraph Filtering for Fair Graph Neural Networks (SF-GNN), a lightweight and architecture-agnostic framework that mitigates structural bias at its source. SF-GNN identifies bias-prone edges by combining sensitive homophily with structural propagation amplifiers, including hub participation and triadic closure. It then incorporates stochastic edge filtering into each message-passing step to selectively downweight or remove these edges while preserving the remaining graph structure. Training further incorporates a statistical-parity regularizer with a warm-up schedule to stabilize optimization. Experiments on five benchmark datasets show that SF-GNN achieves consistent fairness improvements while maintaining competitive predictive performance, leading to a better fairness--accuracy trade-off than recent fairness-aware GNN baselines.
