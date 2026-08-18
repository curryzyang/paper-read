# Refined outer-approximation algorithms for monotonic optimisation

- 区域：速读区
- 排名：1
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Ahmed Rashwan
- 机构：University of Bath
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13694v1) · [PDF](https://arxiv.org/pdf/2608.13694v1)

## TLDR
The paper introduces refined polyblock outer-approximation algorithms for monotonic optimisation, featuring balanced anchor selection, relaxed termination conditions, vectorised processing, and an efficient tree-based implementation that yield order-of-magnitude speed-ups, packaged as the open-source Python library `polyblocks`.

## Abstract
Monotonic optimisation is a broad class of non-convex problems formulated in terms of monotone functions. Such problems are commonly solved via the polyblock outer-approximation algorithm (POA), a branch-and-bound method that iteratively refines a rectangular outer-approximation of the feasible set. POA scales poorly, however: the number of vertices needed to describe the approximation can grow exponentially, leading to large memory requirements and increasingly expensive subroutines. To address these limitations, we propose three algorithmic improvements: a generalised anchor selection that yields an optimal balanced monotonicity cut, a relaxed optimality condition that guarantees finite termination without continuity assumptions, and a vectorised variant that processes multiple nodes concurrently. We further develop an efficient tree-based implementation, which accelerates POA's core subroutines while storing the outer-approximation compactly. Numerical experiments show that these improvements yield order-of-magnitude speed-ups over standard POA and solve problems on which existing variants fail. Finally, we introduce polyblocks, an open-source Python package implementing the proposed algorithms alongside a framework for developing new POA variants, available at https://github.com/RashwanA/polyblocks.
