# D-SLR: The Disjoint Row-Sparse plus Low-Rank Decomposition

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Vincent Szolnoky
- 机构：Chalmers University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10636v1) · [PDF](https://arxiv.org/pdf/2610.10636v1)

## TLDR
D-SLR introduces a closed-form disjoint row-sparse plus low-rank matrix decomposition that acts as a drop-in for truncated SVD, matching or improving reconstruction at equal parameter cost while avoiding tuning and providing an a posteriori optimality certificate.

## Abstract
Compressing a matrix for reconstruction still defaults to the truncated SVD, approximating the data with a single low-rank structure. It is common to reduce the residual further by adding an overlapping row-sparse component, but methods that solve this joint problem often require iterative solvers and tuning of regularization parameters. We propose the Disjoint Row-Sparse plus Low-Rank (D-SLR) decomposition, a closed-form drop-in for the truncated SVD that improves or exactly matches it. D-SLR restricts rows to either being stored verbatim or approximated by the low-rank fit, never both. Under squared error this restriction costs nothing: the joint optimum is attainable disjointly with fewer parameters at every non-trivial rank and stored row count (shape). With zero stored rows D-SLR reduces to the truncated SVD, so it never does worse at equal cost. The algorithm scores the entire error-versus-parameters tradeoff, and the solution is chosen afterwards by a supplied error target or parameter count, or by a selection rule. The grid and solution together cost three SVDs, with no tuning or regularization. We derive an assumption-free, a-posteriori lower bound on the error at every shape, giving each solution a computable certificate on the potential gain of any other choice of rank and stored rows. Experiments on synthetic and real data (LLM embedding tables, network traffic, hyperspectral images) confirm the gains and quantify the certificate.
