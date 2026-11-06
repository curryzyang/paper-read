# Ramification of Weighted Central Paths and Super-linear Interior-Point Methods for Semi-definite Optimization

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Ali Mohammad-Nezhad, Pouya Sampourmahani, Tamas Terlaky
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07080v1) · [PDF](https://arxiv.org/pdf/2611.07080v1)

## TLDR
The paper proves that a family of weighted AHO central paths in semidefinite optimization becomes analytic at its limit after a common reparametrization, enabling higher-order predictor-corrector interior-point methods with superlinear/Q-order convergence even without strict complementarity.

## Abstract
The local convergence of primal-dual interior-point methods for semi-definite optimization is closely tied to the regularity of the central path at its limiting point. Without strict complementarity, the central path can exhibit fractional power asymptotics and need not be differentiable in the ordinary barrier parameter.
  We show that this obstruction can be removed simultaneously for a family of weighted \AHO~central paths. More precisely, there exists a common ramification exponent $N$ such that all weighted paths in a fixed neighborhood of the identity become analytic at the limiting point after the reparametrization $μ\mapstoμ^N$. Using higher-order derivatives of these reparametrized paths, we construct a feasible $p$th-order predictor-corrector interior-point method.
  Under a uniform predictor regularity condition, and without assuming strict complementarity, we prove that the normalized complementarity gaps converge with $Q$-order at least $(p+1)/ρ$, where $ρ$ is the reparametrization exponent used by the method. We also establish super-linear convergence of the simultaneously vanishing primal-dual blocks, derive an explicit quantitative reduction bound throughout the predictor regularity region, and obtain a doubly logarithmic outer iteration bound once the iterates enter the local super-linear regime. Finally, we illustrate the predicted higher-order behavior on a collection of degenerate and non-degenerate semi-definite optimization problems.
