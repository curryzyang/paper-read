# CaLA: Causal Latent Adjustment for World Models under Adaptive Policies

- 区域：速读区
- 排名：5
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Robert Ness, Sofiane Ennadir, Oleg Smirnov
- 机构：Microsoft Research, Microsoft Gaming
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31431v1) · [PDF](https://arxiv.org/pdf/2611.31431v1)

## TLDR
The paper introduces Causal Latent Adjustment (CaLA), a DAG-constrained world model that infers a latent player representation from pretreatment history to deconfound adaptive-policy rollouts, yielding more reliable causal difficulty recommendations and substantially lower churn in a controlled Match-3 environment.

## Abstract
World models is answering ``imagine" answers to ``what-if'' questions via imagined rollouts. But rollouts collected by adaptive policies induce treatment-outcome confounding in imagined rollouts. We study this problem in Match-3 difficulty adjustment, where latent player skill influences both assigned difficulty and churn. We build a fully specified Match-3 SCM with sequential mechanics, adaptive assignment, and paired ground-truth interventions, on which unadjusted models fit to the logged trajectories select difficulty settings that raise churn. We then introduce Causal Latent Adjustment (CaLA), a DAG-constrained world model that infers a variational player representation from pretreatment history. Across our evaluations, CaLA provides the most reliable population-level intervention estimates and competitive individualized decisions, although rich handcrafted histories can remain advantageous for individual-level adjustment. We further find that residual correction can degrade causal decision quality despite improving predictive fit, highlighting the need to distinguish predictive accuracy, confounding adjustment and the behavior of downstream causal estimators.
