# Learning Across Heterogeneous Feature Spaces with Group Robustness

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Xenia Konti, Arjun Tschand, Chuan Hong, Nicoleta J. Economou-Zavlanos, Michael M. Zavlanos
- 机构：Duke University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10153v1) · [PDF](https://arxiv.org/pdf/2611.10153v1)

## TLDR
The paper proposes a group-robust learning framework for heterogeneous feature spaces that uses group-specific encoders mapped to a shared Gaussian-anchored latent space and optimizes worst-group excess loss, outperforming state-of-the-art methods on medical datasets.

## Abstract
In clinical applications, patients undergo different combinations of tests, and machine learning models must therefore ensure accurate predictions across heterogeneous feature spaces. Current approaches upweight the patients with the highest loss, without accounting for the limited predictive information in their features preventing their loss from going any lower. Moreover, when patients' feature spaces are fully disjoint, current methods reduce to training independent models, preventing knowledge transfer across them. We propose a framework for group robust learning across heterogeneous feature spaces, where groups are patients sharing a feature space. Since a high loss may simply reflect uninformative features, we instead optimize for worst-group excess loss, the gap between a group's loss and an estimate of its achievable optimum. To allow collaboration between groups, we use group-specific encoders mapping into a shared latent space in which learnable Gaussian anchors cluster patients by outcome. On tabular and imaging medical datasets, including fully disjoint feature settings, our framework outperforms state-of-the-art methods when groups differ in their optimal losses or cannot train a good model on their own, reducing worst-group loss by up to 79% and excess loss by up to 95% with up to 18$\times$ fewer parameters.
