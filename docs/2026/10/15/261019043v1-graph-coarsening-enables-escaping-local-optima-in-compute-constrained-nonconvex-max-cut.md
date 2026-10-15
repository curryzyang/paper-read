# Graph Coarsening Enables Escaping Local Optima in Compute-Constrained Nonconvex MAX-CUT

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：M. Harper Langston, Pierre-David Letourneau, Dalton Jones, Harris Teague, Peter Scott, Mingu Lee, Richard Lethin, Chris Lott, Roland Memisevic, Fatih Porikli
- 机构：Qualcomm AI Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19043v1) · [PDF](https://arxiv.org/pdf/2610.19043v1)

## TLDR
Combining a structure-aware spectral graph-coarsening warm start (CMG) with a moment-based nonconvex continuous relaxation (PPR) escapes local optima and improves compute-constrained MAX-CUT, achieving near-optimal and scalable results on structured sparse graphs.

## Abstract
Because its binary optimization landscape contains exponentially many local optima, MAX-CUT is highly sensitive to initialization. We study Particle Polynomial Relaxation (PPR), a moment-based nonconvex continuous reformulation possessing an advantageous optimization landscape. We warm-start PPR with Combinatorial Multigrid (CMG), a spectral graph-coarsening method that produces structure-aware initial solutions in near-linear time without training data. On \texttt{t2g20} ($n=400$), benchmark instance with known exact optimum, the combined CMG+PPR pipeline reaches $97.5\%$ of optimum on average and $98.4\%$ on the best run. An extended variant with discrete local-search refinement reaches the published optimum on all sixty Biq Mac instances evaluated by a recent neural branch-and-bound method. Using a sparse CSR representation, the same approach scales to G-set instances with up to $20{,}000$ vertices reducing memory requirements by up to $3333\times$ while maintaining a consistent improvement over the CMG warm start. Gains are largest on sparse weighted graphs; on dense graphs we complement the pipeline with spectral sparsification.
