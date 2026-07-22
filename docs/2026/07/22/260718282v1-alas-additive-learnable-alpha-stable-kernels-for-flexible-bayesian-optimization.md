# ALAS: Additive Learnable Alpha-Stable Kernels for Flexible Bayesian Optimization

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Weibo Huang, Cheng Hua
- 机构：Shanghai Jiao Tong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18282v1) · [PDF](https://arxiv.org/pdf/2607.18282v1)

## TLDR
ALAS introduces a Gaussian process kernel family based on learnable symmetric α-stable spectral components that adapts effective smoothness via the stability parameter α, and a separable variant for high-dimensional robustness, achieving strong empirical performance across diverse Bayesian optimization tasks.

## Abstract
Bayesian Optimization is widely used for expensive black-box optimization, yet its success often depends on choosing a kernel that matches the objective's unknown structure. In this work, we propose ALAS, a flexible Gaussian Process kernel family built from symmetric $α$-stable spectral components. By learning the stability parameter $α$, ALAS adapts its effective smoothness from data, capturing both smooth trends and sharp irregularities. We present two parameterizations: ALAS, a single stationary component with joint spectral modulation, and ALAS-Sep, a separable variant that learns dimension-wise tail behavior to improve robustness on approximately decomposable objectives. Experiments on standard benchmarks and real-world surrogates demonstrate strong and robust performance across diverse settings.
