# Median-of-Means as an Extremal Convex Estimator and a Nonconvex Route to the Trimmed Oracle

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Angshul Majumdar
- 机构：IIIT Delhi
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01689v1) · [PDF](https://arxiv.org/pdf/2609.01689v1)

## TLDR
This paper shows that all convex block M-estimators are limited to the median-of-means robustness constant, and introduces a nonconvex block-Lp estimator family whose global minimizers continuously approach the trimmed-block oracle performance as p→0 while maintaining a benign optimization landscape and sub-Gaussian guarantees under heavy-tailed contamination.

## Abstract
We revisit median-of-means estimation from a deterministic optimization viewpoint and develop a family of block-Lp estimators for robust learning with heavy-tailed and adversarially corrupted data. In a block contamination model with at least a fraction 1 minus epsilon of good blocks, we first show that every convex block M-estimator has worst-case robustness constant at least 1 divided by 1 minus 2 epsilon. This matches the classical median-of-means bound and proves that the trimmed-block oracle constant 1 divided by 1 minus epsilon cannot be attained within the convex class. We then introduce a nonconvex block-Lp family for p between 0 and 1 and derive finite-sample deterministic robustness bounds for all global minimizers. As p decreases from 1 toward 0, these bounds continuously approach the trimmed-block oracle constant. For sufficiently small p, the global minimizers coincide with those of the oracle under a mild separation condition. We also show that the block-Lp objectives have a benign landscape, with all local minima remaining close to the truth and no bad basins. Combining these results with block-level concentration yields sub-Gaussian deviation bounds under finite 2 plus delta moments and high-dimensional extensions to robust mean estimation and sparse regression.
