# GHC:Expanding Residual Interfaces in Hyper-Connections

- 区域：速读区
- 排名：3
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Tianyu Li, Hongtao Zhang, Dongchen Han, Jingshu Liu, Bojun Wang, Chen Jiang, Yulong Huang, Wei Chen, Tianyu He, Xiangyu Zhang, Gao Huang
- 机构：StepFun, University of Chinese Academy of Sciences, Tsinghua University, The Hong Kong University of Science and Technology (Guangzhou)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31350v1) · [PDF](https://arxiv.org/pdf/2611.31350v1)

## TLDR
GHC expands residual branch read/write interfaces by partitioning each branch into parallel groups with distinct stream mixtures and learned per-stream output aggregation, consistently improving training efficiency by 35% over Pre-Norm and 10% over IHC while unlocking gains from wider residual states.

## Abstract
Hyper-Connections expand residual capacity across parallel streams, yet restrict every branch to narrow read and write interfaces: each branch still reads a single stream mixture and writes scaled copies of one output vector to all streams. To lift this bottleneck, we propose Grouped Hyper-Connections (GHC). By partitioning each branch into parallel groups along attention heads or FFN channels, GHC supplies each group with a distinct stream mixture and aggregates their separate outputs into each stream with learned weights. Extensive experiments across dense and Mixture-of-Experts (MoE) models show that GHC consistently improves upon Identity Hyper-Connections (IHC) with negligible parameter and memory-access overhead, increasing training efficiency by 35% over Pre-Norm and 10% over IHC. Moreover, expanding residual interfaces overcomes the diminishing returns of adding streams, allowing wider residual states to yield further gains.
