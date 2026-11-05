# Support Vector Machines Directly Minimise KL Divergence

- 区域：速读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Ivan Silajev
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05557v1) · [PDF](https://arxiv.org/pdf/2611.05557v1)

## TLDR
The paper proves that the dual objectives of support vector classification and regression are exactly constrained KL-divergence minimizations between Gaussian measures, giving SVMs a probabilistic interpretation and unifying kernel machines under an information-theoretic framework.

## Abstract
Support vector machines (SVMs) are fundamentally grounded in geometric margin maximisation and currently lack a mainstream probabilistic interpretation. This keeps them theoretically isolated from probabilistic machine learning models that are naturally comparable and combinable. In this paper, we bridge this gap by proving that the dual objectives of both support vector classification and support vector regression are exact, constrained Kullback-Leibler (KL) divergence minimisation tasks between two Gaussian measures. We further show that this same divergence formulation recovers the exact objective function for kernel ridge regression when domain constraints are removed and $L^2$ regularisation is applied. By demonstrating that SVM duals directly minimise relative entropy, our results provide a unified information-theoretic model for standard kernel machines and lay the foundation for unifying broader kernel-based algorithms under probability theory.
