# Neyman Orthogonal Activation Steering

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：David Arbour, Erfan Jahanparast, Serina Chang, Avi Feller
- 机构：MIT, Adobe Research, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33217v1) · [PDF](https://arxiv.org/pdf/2610.33217v1)

## TLDR
This paper reframes activation steering as estimating the average gradient of an outcome regression and proposes a Neyman-orthogonal, Stein score–based estimator that combines flexible outcome models with score estimators to achieve double robustness and improve steering performance.

## Abstract
Activation steering is a popular approach for shifting LLM output toward a desired behavior, and increasingly for generating realistic synthetic data. The standard recipe estimates a steering direction by contrasting LLM activations on prompts with and without a target concept, such as truthfulness. In this paper, we separate the estimand (the steering direction these methods target) from the estimator used to recover it, two notions the literature often conflates. We frame nearly all existing methods as plug-in estimators of the average gradient of an outcome regression, with the binary contrastive label fixed as the outcome. Using this framing, we can immediately incorporate flexible modeling approaches and extend existing methods to allow for continuous outcomes such as log-probabilities or oracle ratings. Flexible ML models that fit the outcome well, however, might not estimate the gradient well, which motivates estimators that target the gradient directly. Drawing on the debiased machine learning literature, we develop a complementary estimator built on the Stein score, the Riesz representer of the gradient functional. Combining the two routes gives an orthogonalized estimator with classical double-robustness properties. We illustrate the framework on activation steering applied to a number of benchmark datasets.
