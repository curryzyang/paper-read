# MINT: Tensor Decomposition on Stacked Recurrence Matrices for Time Series Data Mining

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Kaamil Kaka, Audrey Der, Evangelos E. Papalexakis, Zachary Zimmerman, Vikram Jayaram
- 机构：University of California, Riverside, Neuralix AI, University of Texas at Dallas
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04157v1) · [PDF](https://arxiv.org/pdf/2608.04157v1)

## TLDR
MINT proposes stacking self-similarity (Mplot/recurrence) matrices of multiple time series into a tensor and applying tensor decomposition to mine interpretable co-clustered cross-series subsequence patterns.

## Abstract
Recurrence plots are a time series data mining primitive applied to a variety of domains (e.g. star light curves, sound waveforms, CCT telemetry). This work proposes tensorized self-similarity matrices as a primitive for univariate time series datasets ($N\times n$) of $N$ time series of length $n$ with a subsequence window of length $m$, and whose tensor-based nature is naturally extensible to multivariate datasets. The proposed method to compute this primitive computes dot plots of size $N \times (n-m+1) \times (n-m+ 1)$ from these datasets, where the subsequent tensor is mined using tensor decomposition methods to mine for co-clustered patterns. We demonstrate our results in mass rapid transit, electricity demand, wind turbine, and car traffic data, finding the MINT pipeline effectively co-clusters cross-sensor patterns in highly regular datasets containing motifs at regular intervals.
