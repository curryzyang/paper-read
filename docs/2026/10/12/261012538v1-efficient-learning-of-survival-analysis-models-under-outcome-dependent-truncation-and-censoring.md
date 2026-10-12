# Efficient Learning of Survival Analysis Models Under Outcome-Dependent Truncation and Censoring

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Itai Zilberstein, Ioannis Anagnostides, Arman Kilic, Tuomas Sandholm
- 机构：Optimized Markets, Inc., Medical University of South Carolina, Strategic Machine, Inc., Carnegie Mellon University, Strategy Robot, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12538v1) · [PDF](https://arxiv.org/pdf/2610.12538v1)

## TLDR
This paper proves that Cox survival models under outcome-dependent truncation and right-censoring can be efficiently learned via first-order optimization when the baseline hazard is known—though jointly learning the baseline can create suboptimal local minima—and demonstrates empirically that accounting for truncation reduces bias and yields orders-of-magnitude speedups over EM, extending to neural networks.

## Abstract
Modern machine learning models are typically trained on data assumed to be representative of the predictive tasks the model will face in the future, but practical datasets violate this assumption. We focus on outcome-dependent truncation in which an observation appears in the training data depending on its label. Our work connects two largely distinct literatures: efficient learning under truncation and survival analysis. Existing methods for truncated survival analysis do not characterize the optimization landscape and instead rely on iterative procedures such as expectation maximization. We address this gap and prove that Cox regression can be efficiently learned under truncated and right-censored data using first-order optimization when the baseline hazard is known (despite nonconvexity). In contrast, when the baseline hazard is learned jointly, we construct identifiable and correctly specified models whose negative log-likelihood contains strict suboptimal local minima. On experiments with four survival datasets, we show that accounting for truncation reduces the prediction bias induced by naive Cox regression and extends to neural networks. We also show orders of magnitude speedups compared to standard expectation maximization.
