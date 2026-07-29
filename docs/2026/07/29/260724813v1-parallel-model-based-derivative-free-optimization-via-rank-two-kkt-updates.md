# Parallel Model-Based Derivative-Free Optimization via Rank-Two KKT Updates

- 区域：速读区
- 排名：3
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Donghan Wu, Pengcheng Xie
- 机构：University of California, Berkeley, Lawrence Berkeley National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24813v1) · [PDF](https://arxiv.org/pdf/2607.24813v1)

## TLDR
This paper presents a parallel derivative-free optimization method that reduces the computational cost of updating quadratic interpolation models from \(\mathcal{O}(m^3)\) to \(\mathcal{O}(n^2)\) by exploiting rank-two KKT perturbations through coordinate reflections, while preserving interpolation set poisedness and ensuring first-order global convergence.

## Abstract
Derivative-free optimization (DFO) addresses unconstrained problems $\min_{\x\in\RR^n} f(\x)$ where $f$ is accessed only through a zeroth-order oracle. Model-based trust-region methods construct underdetermined quadratic interpolation models from $\mathcal{O}(n)$ points and solve a KKT system to determine model parameters, costing $\mathcal{O}(m^3)$ operations and limiting parallel scalability. It is shown that the KKT matrix for the minimum Frobenius norm updating model depends entirely on inner products of shifted coordinates. Reflecting the interpolation set across a single coordinate axis preserves these inner products and changes only one row and column of the KKT matrix, inducing a rank-at-most-two perturbation whose inverse update via the Sherman-Morrison-Woodbury formula costs $\mathcal{O}(n^2)$ when $m=\mathcal{O}(n)$. The reflection is an isometry in centered Euclidean trust regions and preserves the poisedness constant of the interpolation set; together with standard fully linear model-management assumptions this supports first-order global convergence. The mechanism is embedded in a master-worker parallel algorithm with a Truncated Conjugate Gradient subproblem solver. Numerical results on 530 benchmark problems compare performance against an established DFO solver.
