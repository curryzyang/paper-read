# Nearest Graph Laplacians with Prescribed Connected Components: A Convex Framework for Network Reconstruction

- 区域：速读区
- 排名：7
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Udit Raj, Sudeepto Bhattacharya, Prince Kanhya
- 机构：Shiv Nadar Institution of Eminence, Indian Institute of Science Education and Research, Bhopal, Indian Institute of Technology Guwahati
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18128v1) · [PDF](https://arxiv.org/pdf/2608.18128v1)

## TLDR
Given a graph Laplacian, this paper formulates a convex semidefinite optimization framework to find the nearest Laplacian whose graph has exactly a prescribed set of connected components, proving uniqueness and demonstrating minimal-perturbation network reconstruction on synthetic and real social network data.

## Abstract
We study the problem of constructing the nearest graph Laplacian matrix to a given Laplacian while enforcing a prescribed connected-component structure. Let the vertex set be partitioned into nonempty disjoint blocks $C_1,\ldots,C_k$, and let $U=[u_1,\ldots,u_k]$ be the matrix of the corresponding block-indicator vectors. The constraint $MU=0$ ensures that these prescribed indicators lie in the nullspace of the optimized Laplacian $M^\star$, and hence the associated graph has at least $k$ connected components. To guarantee exactly the prescribed components, we impose additional block-connectivity constraints on the principal blocks $M_j=M[C_j,C_j]$. These constraints ensure that each prescribed block induces a connected weighted subgraph. The resulting problem is a convex semidefinite optimization problem with a strictly convex Frobenius-norm objective. We prove existence and uniqueness of the minimizer and show that the optimized Laplacian has exactly the prescribed connected components, with nullspace $\operatorname{span}\{u_1,\ldots,u_k\}$. The framework proposed in this work provides a principled tool for quantifying the minimum structural intervention required to transform a graph-based network into one having a prescribed group-separated structure. Numerical examples, including the Sampson monastery positive-affection network, illustrate the nearest faction-consistent weighted reconstruction and the minimum Laplacian perturbation required to realize the prescribed faction structure.
