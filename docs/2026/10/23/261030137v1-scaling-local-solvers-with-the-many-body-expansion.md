# Scaling Local Solvers with the Many-Body Expansion

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Federico Zahariev, Amr Sabry
- 机构：Ames Laboratory, Indiana University, Iowa State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30137v1) · [PDF](https://arxiv.org/pdf/2610.30137v1)

## TLDR
The paper introduces a Many-Body Expansion framework that scales black-box local solvers for discrete optimization by decomposing problems into fragments, repeatedly improving fragments and targeted unions under a monotone non-worsening rule, and demonstrating better performance than flat solver applications on graph coloring, MAX-CUT, and facility-location benchmarks.

## Abstract
We introduce a Many-Body Expansion framework for scaling black-box solvers for discrete optimization. The method decomposes a large problem into fragments, repeatedly improves each fragment with the rest of the assignment held fixed, and then applies targeted corrections on unions of fragments. The solver itself is unchanged: it only receives a restricted subproblem and returns a candidate assignment. The framework separates decomposition from solver design. Moebius inversion gives an exact fragment expansion of the objective, and for pairwise objectives such as graph coloring, MAX-CUT, and QUBO the expansion closes at second order. The promoted solver is monotone by construction, terminates in finitely many productive sweeps for non-negative integer-valued objectives, and connects to junction-tree dynamic programming when the fragment interaction structure is acyclic and full response functions are propagated. On graph coloring benchmarks, the promoted versions of TabuSearch and simulated annealing (SA) generally outperform flat applications of the same solvers, often finding better solutions in less CPU time, and the gain proves insensitive to the choice of graph partition. A facility-location study delimits the claim: there the partition must respect the objective's interaction locality, and the promoted solver reaches within 0.3-1.4% of GLPK-certified optima at every tested size. The same wrapper interface is used in each solver-swap case, and the facility-location check reuses the same monotone guard with a sign-adjusted interaction diagnostic; the improvements therefore come from the MBE promotion mechanism rather than solver-specific tuning.
