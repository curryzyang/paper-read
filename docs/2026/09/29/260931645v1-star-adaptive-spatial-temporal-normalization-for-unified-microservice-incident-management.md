# STAR: Adaptive Spatial-Temporal Normalization for Unified Microservice Incident Management

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Xinhua Miao, Linyu Zhu, Bowei Yang, Zhengong Cai
- 机构：Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31645v1) · [PDF](https://arxiv.org/pdf/2609.31645v1)

## TLDR
STAR is a self-supervised spatial-temporal representation learning framework that uses temporal and spatial adaptive normalization to handle non-stationary dynamics and heterogeneous service dependency graphs, enabling unified anomaly detection, failure triage, and root cause localization in microservice systems with state-of-the-art performance.

## Abstract
Automated incident management in large-scale microservice systems relies on learning robust representations from multimodal observability data, including metrics, logs, and traces. Although recent self-supervised frameworks enable unified modeling for anomaly detection (AD), failure triage (FT), and root cause localization (RCL), they often struggle with non-stationary temporal dynamics and heterogeneous service dependency structures. In this paper, we propose STAR, a Spatial-Temporal Adaptive Representation learning framework that explicitly addresses these challenges through adaptive normalizations. STAR introduces two tightly coupled mechanisms: Temporal Adaptive Normalization (TAN), which dynamically normalizes multivariate time series using multi-scale temporal context, and Spatial Adaptive Normalization (SAN), which performs structure-aware normalization over service dependency graphs. Unlike prior methods that treat normalization as static or task-agnostic, STAR formulates it as a learnable, context-conditioned transformation aligned with the intrinsic properties of microservice systems. The resulting adaptive representations are integrated into a unified self-supervised framework, enabling end-to-end unsupervised support for AD, FT, and RCL tasks. Extensive experiments on two real-world microservice benchmarks demonstrate that STAR consistently outperforms all state-of-the-art baselines, yielding significant and stable improvements across all three tasks. Our results highlight adaptive normalization as a principled and effective mechanism for robust multimodal representation learning in complex software systems.
