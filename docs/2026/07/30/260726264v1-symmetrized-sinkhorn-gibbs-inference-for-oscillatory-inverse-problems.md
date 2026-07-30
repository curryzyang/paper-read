# Symmetrized Sinkhorn-Gibbs Inference for Oscillatory Inverse Problems

- 区域：速读区
- 排名：5
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Gabriel Huerta, Mohammad Motamed
- 机构：University of New Mexico, Sandia National Laboratories
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26264v1) · [PDF](https://arxiv.org/pdf/2607.26264v1)

## TLDR
The paper introduces a symmetrized Sinkhorn-Gibbs inference framework that combines normalization of signed oscillatory signals with a symmetrized Sinkhorn loss to improve posterior inference and robustness in oscillatory inverse problems by reducing nonconvexity and cycle-skipping effects.

## Abstract
Oscillatory inverse problems often exhibit highly nonconvex discrepancy landscapes due to signal misalignment and cycle-skipping phenomena, posing significant challenges for uncertainty quantification. While Gibbs posteriors provide a flexible framework for incorporating problem-specific discrepancy measures, their performance depends strongly on the empirical risk landscape induced by the chosen discrepancy measure. Optimal transport accounts for the spatial and temporal structure of the underlying feature domain when comparing oscillatory signals. However, the direct application of classical optimal transport is precluded because observed and predicted signals are typically signed and therefore do not satisfy the positivity requirements of classical transport formulations. We introduce a symmetrized Sinkhorn-Gibbs inference framework for oscillatory inverse problems. The proposed approach combines a normalization procedure for signed signals with a symmetrized Sinkhorn loss that exploits complementary transport information from the normalized signals and their normalized negations. The resulting loss is incorporated into the Gibbs posterior framework, yielding a Gibbs inference methodology tailored to oscillatory data. We establish smoothness properties of the proposed loss, prove well-definedness of the resulting Gibbs posterior, derive robustness guarantees, and develop an adaptive sampling strategy for posterior computation. Numerical experiments demonstrate less oscillatory empirical risk landscapes with fewer spurious local minima, more accurate posterior inference, greater robustness to observational noise, and improved population-level recovery than Gibbs posteriors based on Euclidean and trace-wise Wasserstein losses.
