# Individual Fairness via Local Predictive Consistency

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Zhouting Zhao, Tin Lok James Ng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33285v1) · [PDF](https://arxiv.org/pdf/2610.33285v1)

## TLDR
The paper proposes local predictive consistency—a node-level relaxation of individual fairness that compares each prediction to a similarity-weighted average of its local neighborhood—yielding an interpretable fairness score and a regularized learning approach with explicit graph construction, applicable to classification, regression, and time-to-event prediction while analyzing fairness–performance trade-offs.

## Abstract
Individual fairness in machine learning requires that similar individuals receive similar predictions. Most existing definitions are pairwise in nature, imposing a Lipschitz constraint that must hold either globally across all pairs of data instances or locally within specified neighborhoods. In practice, however, such pairwise constraints may be overly restrictive and may not directly identify which individuals receive locally inconsistent predictions. We study local predictive consistency as a node-level relaxation of pairwise individual fairness, where each prediction is compared with a similarity-weighted average of predictions in its local neighborhood. This yields an interpretable node-level fairness score and a corresponding regularized learning approach based on local residuals. Since graph-based individual fairness depends critically on the underlying similarity structure, we make the construction of the neighborhood graph explicit and discuss threshold selection through graph-coverage diagnostics. Our approach applies to binary classification, regression, and time-to-event prediction. We further compare this formulation with pairwise constraint-based approaches and analyze the resulting fairness--performance trade-offs.
