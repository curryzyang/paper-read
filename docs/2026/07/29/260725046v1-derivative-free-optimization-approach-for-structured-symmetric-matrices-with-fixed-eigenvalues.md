# Derivative-free optimization approach for structured symmetric matrices with fixed eigenvalues

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Carmo P. Brás, Evelin H. M. Krulikovski, Marcos Raydan
- 机构：Federal University of Paraná, NOVA School of Science and Technology (NOVA FCT)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25046v1) · [PDF](https://arxiv.org/pdf/2607.25046v1)

## TLDR
This paper develops a derivative-free optimization model, employing deterministic (GLODS) and heuristic strategies, to solve inverse structured symmetric matrix problems where the eigenvalues are fixed and certain entries are preassigned or must remain nonzero.

## Abstract
A Derivative-Free Optimization (DFO) model is developed and analyzed for solving inverse structured symmetric matrix problems for which the eigenvalues are specified. Some (zero and nonzero) entries are preassigned and cannot be changed, while others should be nonzero but their values are not given. The rest of the entries are completely free. The obtained matrix must meet these criteria and have the specified eigenvalues. This specialized inverse eigenvalue problem is relevant to various applications and is linked to determining the graph, with weights on the undirected edges, of the matrix associated with its sparse pattern. Our novel optimization model requires computing the eigenvalues of a symmetric matrix to evaluate the non-differentiable objective function. We apply deterministic DFO schemes, specifically the global variant GLODS of the well-known family of directional direct search (DDS) methods. We discuss its convergence properties which are based on the fact that the objective function of our model is Lipschitz continuous. Additionally, we explore the potential benefits of using several well-established heuristic strategies to solve the proposed optimization model. We present preliminary numerical results to illustrate and compare the performance of the considered deterministic and heuristic DFO options in various possible scenarios.
