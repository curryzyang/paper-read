# The Failures of Marginal Influence-Based Attribution Methods for Global Time Series Explanations

- 区域：速读区
- 排名：4
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Amadeo Tunyi
- 机构：XITASO GmbH
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16236v1) · [PDF](https://arxiv.org/pdf/2607.16236v1)

## TLDR
This paper proves that marginal influence-based attribution methods for time series explanations conflate direct and mediated temporal dependencies under autocorrelation, and introduces the concept of DAG-faithfulness to demonstrate that standard methods like SHAP and their time-series-aware extensions fail to recover the model's learned conditional independence structure.

## Abstract
Explainability methods for time series models predominantly produce flat attribution scores: they quantify the direct influence of a feature at a timestamp by a scalar. We prove that the dominant failure mode of such methods is not the scalar format itself but a fundamental computational mismatch: existing methods compute scores via marginal conditioning or off-manifold gradients, both of which conflate direct temporal dependencies with mediated ones under autocorrelation. We also define DAG-faithfulness: an explanation is DAG-faithful if the temporal dependency graph it encodes is Markov-equivalent to the temporal directed acyclic graph (DAG) implicitly learned by the model. Particularly, we observe that standard attribution methods, specifically SHAP, are not DAG-faithful in general, and that recent time-series-aware extensions inherit the same computational limitation.
