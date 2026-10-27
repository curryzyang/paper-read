# RadonBench: A Benchmark of Classical and Learning-Guided Search Techniques for Problems in Combinatorial Geometry

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Xiaoan Xu, Ethan X. Fang, Jesus A. De Loera, Junwei Lu, Luze Xu
- 机构：Harvard University, University of California, Davis, Duke University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33259v1) · [PDF](https://arxiv.org/pdf/2610.33259v1)

## TLDR
RadonBench provides a reproducible benchmark comparing classical and learning-guided search methods on the open problem of constructing maximum-cardinality Radon-free lattice configurations, finding verified near-miss baselines but no solution reaching the 11-point \(\mathbb{Z}^3\) or 21-point \(\mathbb{Z}^4\) frontiers.

## Abstract
Classical optimization and learning-guided search offer complementary approaches to open problems in discrete mathematics, but their outputs are difficult to compare when search spaces, validity checks, and stopping rules differ. We present \emph{RadonBench}, a benchmark for constructing maximum-cardinality Radon-free lattice configurations: finite subsets of $\mathbb{Z}^d$ admitting no integral Radon partition. It remains open whether Radon-free configurations with $11$ points in $\mathbb{Z}^3$ or $21$ points in $\mathbb{Z}^4$ are possible. If they exist, they would improve the corresponding lower bounds on the integer Radon numbers. We compare exhaustive extension, greedy local search, PatternBoost, AlphaZero, and AlphaEvolve. All outputs use one success predicate: a convex target-sized configuration succeeds exactly when its number of integral Radon points is zero. PatternBoost and AlphaZero construct verified Radon-free configurations of sizes $10$ and $20$, one point short of the respective targets; AlphaZero's best convex target terminals have two integral Radon points in both dimensions. Exhaustive extension over fixed seeds and declared finite search boxes likewise reaches a minimum of two integral Radon points. Greedy local search and AlphaEvolve each produce target-sized near misses with one integral Radon point. No audited run reaches zero. These results establish reproducible near-miss baselines over explicitly scoped search domains.
