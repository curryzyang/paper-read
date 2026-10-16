# Learning Topology-Aware Representations for Mechanics-Relevant TPMS Metamaterials

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Songlin Duan, Shuo Yang, Yujia Zheng, Tobin Filleter
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20684v1) · [PDF](https://arxiv.org/pdf/2610.20684v1)

## TLDR
The paper proposes a topology-aware representation learning framework that integrates persistent homology into a DMAE backbone to encode global structural connectivity in TPMS metamaterials, improving classification and clustering while retaining strong regression performance.

## Abstract
Learning informative representations of mechanical Triply Periodic Minimal Surface (TPMS) metamaterials is important for mechanics analysis and structural design, yet existing methods have rarely explicitly supervised learned representations with information about global structural connectivity that is relevant to mechanical response. We propose a topology-aware representation learning framework that integrates persistent homology into a DMAE backbone to explicitly encode global structural connectivity. A persistence-guided masking strategy prioritizes patches associated with persistent topological features, while an auxiliary persistent-homology decoder encourages the latent representation to retain information about topological feature counts across connected components, tunnels, and voids. We evaluate the learned representations on two complementary TPMS datasets using family classification, mechanical-property classification, unsupervised clustering, and regression. Across the two datasets, our method demonstrates strong performance in both structural family and mechanical-property classification, improving family classification by up to 3.9% while achieving the best linear-probe performance. More notably, unsupervised property-clustering performance improves by up to 26.7% and 51.5% across the two datasets, while strong regression performance is retained with $R^2=0.993$. These results establish persistent topology as an effective inductive bias for representation learning of complex three-dimensional mechanical metamaterials.
