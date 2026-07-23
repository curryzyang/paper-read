# STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification

- 区域：速读区
- 排名：14
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Haoran Guo, Yutong Lu, Li Zhang
- 机构：University College London, University of Oxford
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19385v1) · [PDF](https://arxiv.org/pdf/2607.19385v1)

## TLDR
STN-TGAT proposes a novel framework combining a temporal Transformer with a graph attention network, an NMI-based prior, and learnable soft-threshold sparsification to improve Top-K portfolio construction by adaptively modeling dynamic stock relationships and aligning training with practical ranking objectives.

## Abstract
This paper tackles the problem of stock ranking and portfolio construction under realistic investment settings by jointly modeling temporal dynamics and cross-sectional dependencies. We propose the Soft-Threshold NMI-prior Transformer Graph Attention Network (STN-TGAT), which integrates a temporal Transformer with a Graph Attention Network to capture long-horizon sequential patterns and dynamic inter-stock relationships. An NMI-based prior graph combined with a soft-threshold sparsification mechanism enhances structural robustness by mitigating noisy correlations while preserving informative connections. The portfolio formation process incorporates practical considerations, including Top-5 selection within the Top-50 $S\&P$ 500 constituents, explicit weight allocation, and transaction cost adjustment, thereby aligning the evaluation with real-world trading conditions. Empirical results on real-world data demonstrate that STN-TGAT consistently outperforms benchmark models from predictive accuracy and investment profitability measured by portfolio returns. These findings suggest that combining decision-aligned training with adaptive relational modeling provides a coherent and practically effective framework for data-driven portfolio construction.
