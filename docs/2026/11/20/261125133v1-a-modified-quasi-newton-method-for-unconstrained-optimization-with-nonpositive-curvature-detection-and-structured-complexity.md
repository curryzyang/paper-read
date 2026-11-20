# A Modified Quasi-Newton Method for Unconstrained Optimization with Nonpositive Curvature Detection and Structured Complexity

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Farhad Rahbarnia, Dominique Monnet, Dominique Orban
- 机构：Polytechnique Montréal, Université de Rennes
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25133v1) · [PDF](https://arxiv.org/pdf/2611.25133v1)

## TLDR
The paper presents R2N, a regularized modified quasi-Newton method for large-scale unconstrained smooth optimization that detects and exploits nonpositive curvature, establishes global convergence and structured worst-case complexity, and demonstrates via a modular Julia implementation and CUTEst experiments that its recommended configuration is competitive with trust-region methods.

## Abstract
We consider the convergence, worst-case complexity, and implementation of R2N, a modified quasi-Newton method for large-scale unconstrained smooth optimization. At each iteration, we compute a step that approximately minimizes the sum of a quadratic model of the objective with an adaptive quadratic regularization, and that results in sufficient decrease. The objective is only assumed to be $C^1$, although second derivatives may be used if they are available. The implementation features a broad range of step-computation strategies, from sparse factorization to matrix-free Krylov methods, that satisfy global convergence requirements. When detected, directions of nonpositive curvature are exploited. Our analysis allows unbounded model Hessians, provided they satisfy a mild growth condition. We derive a worst-case evaluation complexity bound that separates the progress made along positive- and nonpositive-curvature directions. By forcing the regularization parameter to vanish near isolated local minimizers, we obtain superlinear local convergence. The implementation specializes naturally to nonlinear least-squares problems. We provide a modular Julia implementation, and use it in a numerical study on the CUTEst test set that assesses the treatment of nonpositive curvature, the subproblem solver, the update of the regularization parameter, and direct versus iterative subproblem solves. An Armijo-Goldstein line search along nonpositive-curvature directions, MINRES-QLP as subproblem solver, and a regularization parameter driven to zero near a solution form our recommended configuration. With exact second derivatives, R2N is competitive with a trust-region method, solving slightly more problems with fewer objective and gradient evaluations. With convex models, the trust-region method performs as well or better.
