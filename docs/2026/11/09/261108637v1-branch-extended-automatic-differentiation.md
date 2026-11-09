# Branch-Extended Automatic Differentiation

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jan Hückelheim, Jeffrey Larson, Matt Menickelly
- 机构：Argonne National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08637v1) · [PDF](https://arxiv.org/pdf/2611.08637v1)

## TLDR
BEAD is a JAX-based Python package that automates branch-extended automatic differentiation by identifying inactive branches of piecewise-differentiable functions within tolerance and computing their extended gradients, enabling more robust nonsmooth optimization without manual derivative code.

## Abstract
We present branch-extended automatic differentiation (BEAD), a software package that provides information about inactive branches of piecewise-differentiable functions, intended for use in nonsmooth optimization algorithms. BEAD is implemented in Python, building on the popular JAX framework. For supported nonsmooth operations such as abs and max, BEAD identifies alternative branches within tolerance from the given input, and computes gradients of the resulting branches extended to the given input. Such information has been previously used for robust optimization methods, but has required error-prone and tedious manual differentiation, unlike BEAD, which is fully automated for functions written in NumPy-like JAX code. Our experiments show that our approach is as accurate as manually written derivative code, and offers more flexibility in modifying the function and choosing between branch-discovery rules. While we were originally motivated by the manifold sampling algorithm for nonsmooth composite objectives, we also integrate BEAD branch-extension gradients into a nonsmooth BFGS-SQP solver. On two small nonsmooth test problems, the resulting path-aware search resolves failures or substantially reduces the number of evaluations required by the BFGS-SQP solver.
