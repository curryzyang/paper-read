# Connecting Score Matching, Maximum Likelihood, and Expectation-Maximization in Mixed Linear Regression

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Zhankun Luo, Abolfazl Hashemi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05688v1) · [PDF](https://arxiv.org/pdf/2609.05688v1)

## TLDR
This paper studies parameter recovery in mixed linear regression via variance-preserving diffusion of the response, showing that the denoising score matching objective integrates to maximum likelihood with Gaussian-limit guarantees and decomposes into cross-entropy and Expectation-Maximization gradient structures across diffusion noise levels.

## Abstract
We study variance-preserving diffusion of the response in mixed linear regression (MLR) with unknown mixing weights. Our analysis separates the statistical guarantees of score matching from the loss geometry and optimization signal at a fixed diffusion noise level. The KL divergence links the denoising score matching objective integrated over the diffusion path with the likelihood and a terminal discrepancy. Under mild regularity conditions and terminal schedule, the resulting estimator converges up to the ground truth parameters of MLR, and its scaled error converges to the Gaussian limit of the maximum-likelihood estimator. At a fixed scale of the diffusion noise level, we derive a decomposition linking the score matching loss to cross-entropy and Expectation-Maximization (EM) operators. This decomposition yields an EM-related low-noise gradient expansion with additional correction terms of latent variance. In the high-noise limit, we further characterize gradient descent on this limiting loss under isotropic covariance. Along fixed high signal-to-noise ratio rays, the score matching imbalance gradient and the latent-variance term tend to zero pointwise. Numerical experiments illustrate our theoretical findings and statistical guarantees.
