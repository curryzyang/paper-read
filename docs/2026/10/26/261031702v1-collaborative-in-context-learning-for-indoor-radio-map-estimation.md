# Collaborative In-Context Learning for Indoor Radio Map Estimation

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yuanzhe Peng, Jie Xu
- 机构：University of Florida, University of North Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31702v1) · [PDF](https://arxiv.org/pdf/2610.31702v1)

## TLDR
The paper proposes **Poly-Ripple**, a privacy-preserving collaborative in-context learning framework that enables multiple clients to estimate indoor radio maps using large autoregressive vision models with ripple-ordered modeling and importance-aware aggregation—without model updates—and consistently outperforms representative ICL baselines.

## Abstract
Indoor radio map estimation (RME) is essential for wireless applications such as coverage planning, localization, and network deployment. However, most existing methods follow a supervised learning paradigm that requires costly labeled data and task-specific model training. Moreover, indoor environments involve privacy-sensitive information, such as building layouts and structures, that often cannot be centralized. To address these challenges, we make the first attempt to formulate indoor RME as a collaborative in-context learning (ICL) problem. We propose Poly-Ripple, a framework in which multiple clients perform ICL using large autoregressive vision models (LAVMs) without model updates. Each client is prompted by its private demonstrations and predicts the radio map for the same scene query. To capture the causal structure of wireless propagation outward from the transmitter (Tx), we adopt ripple-ordered autoregressive modeling. We further introduce importance-aware aggregation to exploit heterogeneous contextual knowledge distributed across clients under the context length constraint. We provide theoretical analysis and conduct extensive experiments on a public indoor RME benchmark. The experimental results show that Poly-Ripple consistently outperforms representative ICL baselines, while aligning with our theoretical analysis.
