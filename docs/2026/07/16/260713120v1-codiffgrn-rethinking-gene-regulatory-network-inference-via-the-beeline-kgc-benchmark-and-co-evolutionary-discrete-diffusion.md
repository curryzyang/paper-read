# CoDiffGRN: Rethinking Gene Regulatory Network Inference via the BEELINE-KGC Benchmark and Co-evolutionary Discrete Diffusion

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Jiaze Song, Runhao Zhao, Minghao Xu, Bin Cui, Wentao Zhang
- 机构：National University of Defense Technology, Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13120v1) · [PDF](https://arxiv.org/pdf/2607.13120v1)

## TLDR
CoDiffGRN introduces a co-evolutionary discrete diffusion framework and the BEELINE-KGC benchmark to reformulate gene regulatory network inference as an inductive, ranking-centric graph completion problem, achieving state-of-the-art performance in novel regulatory discovery.

## Abstract
Inferring gene regulatory networks (GRNs) from single-cell transcriptomic data is crucial for biological discovery, yet existing approaches suffer from a fundamental misalignment with real-world needs. Researchers typically seek a small set of high-confidence regulatory interactions for experimental validation, often involving previously unseen genes. However, current benchmarks rely on transductive splits with global classification metrics, while prevailing models struggle to generalize under inductive settings. To bridge this gap, we reformulate GRN inference as an inductive, ranking-centric graph completion problem and introduce \textbf{\benchmark}, a new benchmark that incorporates an inductive gene-holdout split together with knowledge graph completion metrics to better evaluate top-ranked predictions. Building on this, we propose \textbf{\method}, the first co-evolutionary discrete diffusion framework that jointly models biologically coherent discretized gene expression states and regulatory interactions for robust inductive generalization and improved top-ranked regulatory discovery. We further introduce TF-ALL Subgraph Sampling (TASS) for scalable training. Extensive experiments on {\benchmark} show that {\method} establishes new state-of-the-art performance, significantly outperforming existing methods in novel regulatory discovery, and ablation studies further verify the effectiveness of our design.
