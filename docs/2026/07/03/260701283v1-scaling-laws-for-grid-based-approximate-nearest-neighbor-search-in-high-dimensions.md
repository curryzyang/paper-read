# Scaling Laws for Grid-Based Approximate Nearest Neighbor Search in High Dimensions

- 区域：精读区
- 排名：5
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Matthew J Liu, Wei Hang Zheng, Vidhan Purohit, Siqi Xie, Chieh-En Li, Jerry Li, Noah Flynn
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.01283v1) · [PDF](https://arxiv.org/pdf/2607.01283v1)

## TLDR
This paper presents the first systematic scaling analysis of grid-based approximate nearest neighbor search, revealing a previously unreported dimensional scaling crossover where multiprobe grids maintain constant scaling efficiency in high dimensions while other methods degrade, offering competitive performance with lower indexing costs.

## Abstract
Grid-based approaches to approximate nearest neighbor (ANN) search have been absent from modern scaling analyses. We present a systematic characterization of a multiprobe grid algorithm with respect to dataset size $N$ and dimensionality $d$. Our experiments reveal a previously unreported $d$-scaling crossover on the GloVe embedding family, in which multiprobe grid search maintains an approximately constant dimensional scaling exponent while other graph-, tree-, and partitioning-based methods exhibit degrading throughput. The advantage comes with near-linear query scaling in $N$, but also with lower indexing cost than competing ANN methods. Our results suggest that grid-based methods such as multiprobe grid may be competitive in rebuild-heavy or high-dimensional settings where indexing cost and dimensional robustness dictate performance. More broadly, recent work has formalized self-attention as an ANN operation. Thus, the $N$- and $d$-scaling properties of ANN algorithms may guide cost analysis of efficient transformer architectures. Code is available at: https://github.com/weiz345/MultiProbeANN.
