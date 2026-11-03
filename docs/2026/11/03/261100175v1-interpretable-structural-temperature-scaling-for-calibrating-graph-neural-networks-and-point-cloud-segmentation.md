# Interpretable structural temperature scaling for calibrating graph neural networks and point-cloud segmentation

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Chenyi Huang
- 机构：University College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00175v1) · [PDF](https://arxiv.org/pdf/2611.00175v1)

## TLDR
The paper proposes Interpretable Structural Temperature Scaling (ISTS), a twelve-parameter, accuracy-preserving linear post-hoc calibrator that sets node-wise temperatures for graph neural networks from eleven human-readable confidence, neighborhood, label-propagation, and distance descriptors, achieving interpretable, faithful calibration that outperforms temperature scaling and eleven baselines on NLL/Brier across multiple graphs and transfers effectively to point-cloud segmentation.

## Abstract
Graph-aware calibrators make graph neural networks (GNNs) more trustworthy by predicting a temperature for each node, usually with auxiliary networks whose decisions are hard to inspect. We propose Interpretable Structural Temperature Scaling (ISTS), a twelve-parameter linear model that sets each node's temperature from named descriptors of its confidence, neighbourhood and closeness to labelled nodes, so every temperature traces back to descriptor contributions. ISTS preserves predictions, and cross-validated regularisation lets the calibration data decide how far the model departs from temperature scaling (TS). Its explanations are faithful at the level of node groups: on test nodes, ISTS softens groups that a global temperature leaves over-confident and sharpens under-confident ones (Spearman correlation 0.67 over 246 groups). On seven graphs with two backbones and eleven baselines, ISTS has the best average rank in negative log-likelihood (NLL) and Brier score and lowers NLL relative to TS by 1.8%, more than twice the gain of an identically fitted entropy-based temperature. It ranked first again on four held-out graphs under a protocol fixed in advance. From about 100 calibration nodes on, ISTS is a cheap and inspectable choice, and on point-cloud segmentation it significantly improves NLL, Brier score and the ranking of points for rejection.
