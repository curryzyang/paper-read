# How Inner Optimizers Shape Replica Scaling

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Eugene Belilovsky, Stefan Horoi, Edouard Oyallon, Benjamin Thérien
- 机构：CNRS, Université de Montréal, Mila, Concordia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19064v1) · [PDF](https://arxiv.org/pdf/2610.19064v1)

## TLDR
The paper identifies pseudo-gradient covariance and batch-size-dependent noise scaling as key factors in replica scaling for distributed LLM training, and shows that whitening-based inner optimizers substantially improve performance as the number of replicas increases.

## Abstract
Training large language models (LLMs) across geographically distributed and poorly interconnected compute pools or data centers has become a topic of significant interest. This has led to increased study of local optimization methods such as DiLoco for LLMs, especially those that use local (or inner) adaptive or preconditioned optimizers, which are critical for high-performance LLM training. However, a central challenge remains: it is well known that increasing the number of model replicas (replica scaling) while fixing the total training budget leads to monotonically decreasing performance. Existing work has empirically demonstrated that the choice of inner optimizer (Muon v.s. AdamW) can significantly improve this trend, but offers only limited explanation of the performance difference. In this work, we consider a range of inner-optimizers and identify two important factors that impact replica scaling: (1) the covariance structure of the pseudo-gradients and (2) the impact of batch size on the pseudogradient's noise scale. Based on these insights, we theoretically and empirically demonstrate that whitening-based pre-conditioning is a powerful inner-optimizer desideratum. Our empirical evaluation extends the results to reveal that whitening-based inner-optimizers achieve strong replica scaling (for 8-96 replicas), with performance relative to DP improving as parameters and data are scaled.
