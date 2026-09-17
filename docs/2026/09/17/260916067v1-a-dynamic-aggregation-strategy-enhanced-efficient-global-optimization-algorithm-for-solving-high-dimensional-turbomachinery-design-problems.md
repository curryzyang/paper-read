# A Dynamic Aggregation Strategy Enhanced Efficient Global Optimization Algorithm for Solving High-Dimensional Turbomachinery Design Problems

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Qineng Wang, Zhendong Guo, Yun Chen, Guangjian Ma, Liming Song, Jun Li
- 机构：AVIC Shenyang Engine Design Institute, Xi'an Jiaotong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16067v1) · [PDF](https://arxiv.org/pdf/2609.16067v1)

## TLDR
The paper proposes DA-EGO, a dynamic aggregation-enhanced efficient global optimization algorithm that decomposes high-dimensional expensive black-box problems into adaptively updated low-dimensional subspaces, demonstrating effectiveness on benchmark functions and turbomachinery aerodynamic design optimizations.

## Abstract
In order to solve the high-dimensional ($d \geq 30$) expensive black-box problems within budget, an efficient global optimization (EGO) algorithm with a dynamic aggregation strategy is proposed, labeled as DA-EGO. Specifically, the DA-EGO decomposes the original high-dimensional design space into a set of low-dimensional subspaces for efficient surrogate-based optimization search, and the optimal solutions of subspaces are combined as an elite point for the global search. Most importantly, the subspaces are not fixed. Instead, the subspace variables are updated in each iteration, according to the variable interaction analyses in the sub- and full-spaces. The perturbation method and the analysis of variance are used to detect variable interactions. To further accelerate the optimization progress, the searching ranges of subspaces are also adaptively adjusted according to the analyses of subspace optimization results of the previous iteration. Tests on 21 benchmark instances, comprising seven functions at 30, 60, and 90 dimensions, show that DA-EGO is effective on separable and partially separable problems under a budget of 1500 function evaluations. Its advantage is case-dependent: on the non-separable shifted Rosenbrock function, GSGA performs better at 60 and 90 dimensions, while the 30-dimensional results are statistically comparable to IKAEA and GSGA. Moreover, the advantage of DA-EGO is also seen in the aerodynamic optimization of a transonic rotor blade with 28 variables as well as the compressor stage optimization with 60 variables. With the above, the effectiveness of the proposed DA-EGO has been well demonstrated.
