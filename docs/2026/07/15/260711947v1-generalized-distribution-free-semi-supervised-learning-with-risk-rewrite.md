# Generalized Distribution-Free Semi-Supervised Learning with Risk Rewrite

- 区域：速读区
- 排名：6
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Yushi Hirose, Hiroo Irobe, Takafumi Kanamori
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11947v1) · [PDF](https://arxiv.org/pdf/2607.11947v1)

## TLDR
This paper proposes a generalized distribution-free semi-supervised learning framework that constructs unbiased risk estimators via linear combinations of component risks, extending PNU learning to multiclass classification and achieving lower variance, with theoretical guarantees and practical methods that match or outperform existing approaches.

## Abstract
Typical semi-supervised learning (SSL) methods rely on distributional assumptions, and their performance degrades when these are violated. While PNU learning, a risk rewriting method, offers a distribution-free alternative, it is restricted to binary classification and its variance optimality remains unclear. In this paper, we propose a generalized framework that constructs unbiased risk estimators using linear combinations of component risks, subsuming PNU learning and extending to multiclass classification. We derive the minimum achievable variance, demonstrating our estimator can attain lower variance than PNU in asymmetric loss scenarios. Furthermore, we establish a generalization bound directly linking this variance reduction to improved learning performance. Based on these theoretical insights, we introduce two practical SSL methods that empirically match or outperform existing approaches on binary and multiclass benchmarks.
