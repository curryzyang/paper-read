# Fast and Memory-Light Evaluation of Density-Based Clusterings with the DISCO Index in R

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Amin Entezari
- 机构：Università di Milano-Bicocca
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25114v1) · [PDF](https://arxiv.org/pdf/2611.25114v1)

## TLDR
The discoCVI R package’s version 0.2.0 computes the DISCO density-based clustering validity index exactly from the single-linkage merge tree of the mutual-reachability MST, achieving linear memory use and large speed and memory improvements over previous R and Python implementations while correctly handling noise labels.

## Abstract
DISCO is a recent internal cluster validity index for density-based clustering that, unlike earlier indices, also evaluates the quality of noise labels. The discoCVI package makes DISCO available in R. This article describes the design of the package and a typical workflow, in which DISCO is used to compare clusterings and to choose the parameters of HDBSCAN without ground truth, followed by the implementation introduced in version 0.2.0. DISCO is defined through density-connectivity distances between all pairs of points, so direct implementations store several n-by-n matrices. We show that every quantity DISCO needs can be read off the single-linkage merge tree of the mutual-reachability minimum spanning tree, so that the index can be computed exactly with memory that grows linearly with the number of points, while the running time remains quadratic as in the original definition. The implementation is tested against the previous version, agrees with the original Python implementation to within $3 \times 10^{-13}$, and corrects the score of singleton clusters to match the published definition. In benchmarks, discoCVI is 23 to 138 times faster than its previous version for 500 to 4,000 points and 3 to 9 times faster than the Python reference for 500 to 8,000 points, using a fraction of the memory of both, and it scores 100,000 points in about 50 seconds with less than 200 MB of memory.
