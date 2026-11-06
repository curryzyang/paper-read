# Scalable Bayesian Gaussian Process Classification for Cancer Histopathology: Calibrated Uncertainty Under Distribution Shift

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yunru Zheng, Wun Ting Chan, Sampras Dsouza, Zhenyu Hong
- 机构：New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07127v1) · [PDF](https://arxiv.org/pdf/2611.07127v1)

## TLDR
The paper proposes a scalable Bayesian Gaussian process classifier for cancer histopathology that combines accelerated RPCholesky low-rank factorization, HMC posterior sampling, and pivots-as-inducing-points on frozen Phikon embeddings to deliver better-calibrated and more accurate predictions under hospital-level distribution shift, reducing calibration error and false negatives relative to SVGP and neural baselines.

## Abstract
Reliable uncertainty quantification is essential for clinical deployment of cancer diagnosis models, yet neural networks and variational Gaussian process methods can produce overconfident predictions, particularly under the distribution shifts that arise when models trained at one hospital are applied at another. We present a scalable Bayesian Gaussian Process Classification (GPC) framework that operates on frozen pathology foundation model embeddings (Phikon) and combines accelerated Randomly Pivoted Cholesky (RPCholesky) for low-rank kernel factorization, Hamiltonian Monte Carlo (HMC) with non-centered parameterization for posterior sampling, and a pivots-as-inducing-points scheme for prediction. This makes HMC posterior sampling in the low-rank latent representation tractable at N approximately 300,000 training points, enabling HC-based low-rank GPC on substantially larger datasets than prior MCMC-based demonstrations. We evaluate on two histopathology benchmarks for breast cancer metastasis detection: PCam and CAMELYON17-WILDS, where the latter tests calibration under hospital-level distribution shift. Compared to stochastic variational GP and neural network baselines, our method improves calibration and predictive performance - reducing expected calibration error by up to 88% and false negative rate by up to 90% - with the largest gains appearing under distribution shift, suggesting that HMC-based posterior sampling provides more trustworthy uncertainty estimates for cross-site pathology classification.
