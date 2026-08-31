# Self-Explainable Multi-Label Graph Neural Network for Correlated Evidence Attribution

- 区域：速读区
- 排名：14
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Yingqi Feng, Yufei Tang, Min Shi, Xingquan Zhu
- 机构：Florida Atlantic University, University of Louisiana at Lafayette
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27574v1) · [PDF](https://arxiv.org/pdf/2608.27574v1)

## TLDR
SEMGNN is an end-to-end self-explainable multi-label graph neural network that jointly learns node classification and sparse, label-conditioned edge explanations by leveraging label-label correlations to faithfully share or separate evidence across different labels.

## Abstract
Multi-label graph learning intends to capture the intrinsic complexity of real-world applications, where one sample is often related to multiple groups or consists of multiple objects. To date, a handful of multi-label graph learning methods exist, but none of them integrate training-time interpretation capability. While post-hoc graph explainers have been developed, they do not explicitly model label-dependent evidence sharing in multi-label graph learners, especially when label pairs are weakly or negatively associated. As a result, post-hoc approaches may miss how evidence should be shared or separated across different labels. This paper advances a new end-to-end self-explainable multi-label graph neural network (SEMGNN), which aims to simultaneously classify multi-labeled nodes and identify edges significantly contributing to each target node w.r.t. predicted labels. Different from post-hoc methods, SEMGNN jointly learns a predictor and a sparse edge-mask explainer within a unified framework and training objective. Label-label correlations are used to improve multi-label node classification and enhance individual label explanations, so that different labels of a node can be supported by distinct yet coherent structural and/or correlated evidence. Experiments and comparisons on synthetic and real-world multi-label networks, in social networking, entertainment, and life sciences, show that SEMGNN achieves competitive or improved predictive performance while providing more faithful and compact label-conditioned explanations.
