# Explaining f-Divergence-Based Regularization via Local Curvature and Sharpness-Aware Minimization

- 区域：速读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Nour Jamoussi, Marios Kountouris
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09367v1) · [PDF](https://arxiv.org/pdf/2609.09367v1)

## TLDR
This paper shows that f-divergence-based regularization and Sharpness-Aware Minimization are locally consistent curvature-sensitive penalties—divergence regularization inducing a Fisher-weighted quadratic form and SAM penalizing the dominant Hessian eigenvalue—and validates this geometric view with α-skew Jensen-Shannon divergence, where maximal curvature penalization at α=1/2 yields flatter minima and the best accuracy/NLL.

## Abstract
Divergence-based regularization and Sharpness-Aware Minimization (SAM) are two prominent approaches for improving generalization in deep learning, both motivated by robustness to perturbations. However, their relationship has remained largely unexplored. Building on classical second-order expansions of $f$-divergences, we show that the two methods are locally consistent under parameter-space perturbations: both induce curvature-sensitive penalties, with divergence regularization yielding a Fisher-weighted quadratic form and SAM penalizing sharpness through the dominant Hessian eigenvalue. For negative log-likelihood objectives with exponential-family output distributions, this correspondence becomes especially transparent, since the Fisher and Gauss-Newton matrices coincide. We further show that the same local geometric perspective extends to input-space perturbations, where divergence-based regularization is defined through transformations of the input. In this setting, the regularizer induces a pullback quadratic form on the input space, providing a more general perturbation framework than standard SAM while preserving the same local sensitivity interpretation. To validate the analysis empirically, we use the asymmetric $α$-skew Jensen-Shannon divergence (JSD) family as a controlled testbed. Its local curvature coefficient scales as $α(1-α)$ and is maximized at the symmetric point $α=\tfrac12$, which recovers the standard JSD. Loss-landscape visualizations in the input-perturbation regime show that stronger induced curvature penalization is associated with flatter local minima. Experiments on four benchmark datasets further demonstrate that both accuracy and negative log-likelihood are consistently best near this regime of maximal curvature penalization.
