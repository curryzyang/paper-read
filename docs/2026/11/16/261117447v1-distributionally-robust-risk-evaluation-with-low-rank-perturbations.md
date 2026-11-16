# Distributionally Robust Risk Evaluation with Low-Rank Perturbations

- 区域：速读区
- 排名：8
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Linglingzhi Zhu, Dongze Wu, Yao Xie
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17447v1) · [PDF](https://arxiv.org/pdf/2611.17447v1)

## TLDR
This paper quantifies the worst-case risk lost by restricting distributionally robust perturbations to shared low-rank row–column subspaces under moment or Wasserstein budgets, characterizes when this restriction is lossless, and develops a curvature-corrected projected gradient ascent with convergence guarantees and computable risk certificates.

## Abstract
We study distributionally robust risk under perturbations restricted to low-rank matrices whose row and column spaces are shared across observations, focusing on how much worst-case risk this restriction sacrifices and how to compute the restricted worst case. Under moment or Wasserstein budgets, we derive quantitative bounds on the gap between the unrestricted and low-rank worst-case risks, characterize when the gap vanishes, and identify the smallest lossless row and column dimensions. To generate worst-case perturbations, we apply projected gradient ascent to a curvature-corrected concave problem and derive computable risk certificates. We establish global sublinear convergence for the corrected objective and linear convergence to a worst-case distribution when the budget constraint is sufficiently active.
