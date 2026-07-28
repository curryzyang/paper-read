# Low-Rank KKT Updates and a Parallel Flipping Mechanism for Model-Based Derivative-Free Optimization

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Donghan Wu, Pengcheng Xie
- 机构：Lawrence Berkeley National Laboratory, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22538v1) · [PDF](https://arxiv.org/pdf/2607.22538v1)

## TLDR
This paper introduces a low-rank updating mechanism for the KKT matrix in least Frobenius norm quadratic models, enabling \(\mathcal{O}(n^2)\) updates and a parallel coordinate-flipping strategy that reduces model maintenance overhead and improves performance on benchmark tests.

## Abstract
Model-based derivative-free optimization relies on quadratic interpolation, but maintaining these models typically requires $\mathcal{O}(m^3)$ linear system solves. We show that for the least Frobenius norm updating model, the associated KKT matrix possesses a fixed inner-product structure. Both single-point replacements and a proposed coordinate-axis flipping operation induce exact Rank-2 perturbations to this matrix. Using this structure, we derive an $\mathcal{O}(n^2)$ update formula for the KKT inverse, eliminating costly refactorizations at each iteration. We integrate the update into a parallel trust-region algorithm where workers independently flip interpolation axes, refresh local models, and synchronize the best configuration. Tests on 530 benchmark problems show the method reduces model-maintenance overhead and achieves higher success rates under tight function-evaluation budgets compared to standard solvers.
