# Personalized Federated Hierarchical Gaussian Processes for Privacy-Preserving Modeling of Heterogeneous Distributed Systems

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Xianjian Xie, Hao Yan
- 机构：Arizona State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19337v1) · [PDF](https://arxiv.org/pdf/2609.19337v1)

## TLDR
The paper introduces pFedHGP, a privacy-preserving personalized federated hierarchical Gaussian process that decomposes each client’s latent function into shared global, client-specific structured, and local residual components and uses federated variational inference to model heterogeneous distributed systems with uncertainty-aware predictions.

## Abstract
We present Personalized Federated Hierarchical Gaussian Processes (pFedHGP) for probabilistic regression and classification when data are distributed across heterogeneous clients. Each client's latent function decomposes into (i) a shared global component, (ii) a client-specific deviation that shares the global kernel structure, and (iii) a flexible local residual. Sparse inducing-variable approximations and federated variational inference keep raw data local while the server synchronizes only low-dimensional statistics for the shared component. Full predictive distributions support uncertainty-aware decisions. In application studies, pFedHGP attains perfect fault classification in press tonnage monitoring using 13.77% of labeled cycles and recovers geographic zones in federated air-quality modeling without centralizing station-level time series. An Instantaneous Linear Mixing Model viewpoint links the hierarchy to multi-output Gaussian processes for correlated sensors.
