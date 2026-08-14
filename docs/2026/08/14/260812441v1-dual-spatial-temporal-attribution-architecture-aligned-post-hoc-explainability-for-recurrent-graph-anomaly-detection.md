# Dual Spatial-Temporal Attribution: Architecture-Aligned Post-Hoc Explainability for Recurrent Graph Anomaly Detection

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Iyad Assaad Nekka, Hamida Seba, Khaled Walid Hidouci, Karima Amrouche
- 机构：National Higher School of Computer Science (ESI), Université Claude Bernard Lyon 1
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12441v1) · [PDF](https://arxiv.org/pdf/2608.12441v1)

## TLDR
X-AddGraph introduces a strictly post-hoc, architecture-aligned Dual Spatial-Temporal Attribution framework that equips the AddGraph dynamic graph anomaly detector with spatial, short-term, and long-term temporal explanations without altering detection performance (ΔAUC = 0).

## Abstract
Deep learning detectors for anomalies in dynamic graphs have reached strong accuracy, yet they remain opaque: when an edge is flagged, the analyst receives a score but no reason. This opacity is untenable in the cooperative, regulated information systems where such detectors are deployed, where automated decisions must be auditable and trustworthy. We address this gap for AddGraph, the foundational GCN+GRU framework for edge-level anomaly detection in dynamic graphs, which to our knowledge has never been equipped with any form of explainability. We present a strictly post-hoc explainability framework, X-AddGraph, built on a Dual Spatial-Temporal Attribution (DSTA) mechanism whose three components are each aligned with one of AddGraph's architectural modules: a gradient-based relevance attribution over the current adjacency structure (spatial), a direct reading of the contextual attention weights already computed during inference (short-term temporal, at zero additional cost), and a gradient rollback through the recurrent hidden states (long-term temporal). Because the detector is frozen, detection performance is preserved exactly (Delta AUC = 0, verified empirically to ten decimal places). On the UCI Message benchmark, our trained AddGraph baseline reaches an average per-snapshot AUC of 0.8705, exceeding the originally published result; X-AddGraph reproduces every score identically while adding explanations where none existed. Evaluated across four edge populations - confident true positives, low-confidence true positives, false positives, and random samples - the long-term attribution identifies historical snapshots carrying significantly more counterfactual signal than random selection (0.127 vs. 0.074), a capability that no spatially-blind explainer can provide. We release our implementation for full reproducibility.
