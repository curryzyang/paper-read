# Budgeted Proper Loss Design for Uncertain Decision Thresholds

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ankit Sharma
- 机构：International Institute of Information Technology Bangalore
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23247v1) · [PDF](https://arxiv.org/pdf/2611.23247v1)

## TLDR
The paper derives an optimal budgeted proper loss for uncertain decision thresholds by clipping a rescaled upper envelope of the candidate threshold densities at a fixed floor, yielding a sharp worst-case regret multiplier that can be computed by a one-dimensional root search.

## Abstract
A binary probability estimate may be used by several decision makers with different error costs. Proper scoring rules can emphasize selected probability thresholds, but a single average threshold distribution need not give a good worst-case regret guarantee. We study the choice of a proper loss when the threshold distribution belongs to a finite specified family. Among integrable loss weights with a positive pointwise floor and a fixed total mass, we derive the weight that minimizes the sharp, distribution-free multiplier from surrogate regret to threshold-averaged decision regret. The solution clips a rescaled upper envelope of the threshold densities at the prescribed floor; its normalization is found by a one-dimensional root search. We give proofs of sharpness, optimality, and stability under density misspecification, as well as a limitation for atomic threshold laws. An exact histogram implementation and two synthetic experiments across 20 seeds verify the construction. The optimized multiplier improves over uniform and average-density weights, while fitted-model performance does not improve uniformly. The result is a loss-design guarantee under an explicit budget, rather than a general claim of predictive superiority.
