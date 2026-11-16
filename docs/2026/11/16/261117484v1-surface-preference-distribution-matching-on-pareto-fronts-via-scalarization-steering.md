# SURFACE: Preference Distribution Matching on Pareto Fronts via Scalarization Steering

- 区域：速读区
- 排名：3
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Liuyuan Jiang, Prasanna Sattigeri, Lisha Chen
- 机构：University of Rochester, IBM Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17484v1) · [PDF](https://arxiv.org/pdf/2611.17484v1)

## TLDR
SURFACE adaptively steers scalarization weights using estimated weight-to-Pareto-front geometry to match a desired preference distribution, achieving provable convergence and improved balance and coverage in finite Pareto approximations.

## Abstract
Constructing a finite Pareto representation requires allocating a limited number of solutions across the Pareto front (PF). A desired preference distribution specifies this allocation by assigning more solutions to some PF regions and fewer to others. Scalarization generates Pareto solutions by varying objective weights and solving single-objective problems. However, a distribution of scalarization weights generally does not translate into the same distribution of Pareto solutions along the PF, because the weight-to-solution map is nonlinear and unknown in advance.To account for this distortion, we introduce SURFACE (Scalarization Updates for Redistributing Finite Approximations with Chart Estimation}), which adaptively updates scalarization weights to match a desired PF distribution. SURFACE estimates how each region of the weight grid corresponds to an area of the PF from the current scalarized solutions, then redistributes the weights accordingly. The method supports parallel, warm-started, inexact optimization with standard single-objective solvers. Theoretically, we establish that, under the stated regularity conditions, SURFACE achieves linear convergence of the preference distribution mismatch to a finite-resolution error floor of $\mathcal{O}(N^{-2/(M-1)})$, where $N$ is the number of adaptive weights and $M$ is the number of objectives. Empirically, experiments across multiple benchmarks demonstrate improved target-mass balance and PF coverage compared with established baselines.
