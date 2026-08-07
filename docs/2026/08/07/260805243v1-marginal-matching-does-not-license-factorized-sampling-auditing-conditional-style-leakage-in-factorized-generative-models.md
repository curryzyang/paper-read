# Marginal Matching Does Not License Factorized Sampling: Auditing Conditional Style Leakage in Factorized Generative Models

- 区域：速读区
- 排名：12
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Duong Bach, Hai Nguyen Hong, Cuong Do
- 机构：VinUniversity
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05243v1) · [PDF](https://arxiv.org/pdf/2608.05243v1)

## TLDR
Matching only the marginal distribution of a style latent to a Gaussian prior does not certify class-invariance, allowing conditional style leakage that fools global MMD yet enables near-perfect label recovery, and eliminating this leakage is necessary but not sufficient for valid factorized sampling.

## Abstract
Factorized generative models commonly regularize a latent style variable z_s by matching its marginal distribution to a fixed Gaussian prior and interpret this as evidence that the style representation is independent of class information. We show that this interpretation is incorrect. Matching only the marginal distribution places no constraint on the class-conditional distributions, allowing the latent style to remain highly predictive of the label despite appearing perfectly Gaussian in aggregate. We derive an exact decomposition showing that this mismatch is one of four conditions required for factorized sampling, and demonstrate that eliminating it is necessary but not sufficient to obtain the intended factorization.
  Empirically, our case-study model and four representative latent baselines achieve near-zero global MMD while still allowing a linear probe to recover class labels with 74%--100% accuracy (10% chance level). Our model reaches 99.15% clustering accuracy, whereas externally evaluated class-conditional generation succeeds only 16% of the time. This leakage remains under six independent perturbations involving model capacity, curriculum, prior geometry, and supervision across two datasets. Four mitigation strategies reduce probe accuracy to 21%--46%, although they leave within-class dependence largely unchanged. A post-hoc conditional prior improves externally evaluated class generation to 0.97 on MNIST without retraining but reaches only 0.41 on CIFAR-10, while an empirical style bank achieves 0.88 on CIFAR-10. These results demonstrate that no divergence computed solely on the marginal distribution of the style latent can certify independence from class labels, and that reporting marginal statistics alone does not verify the property commonly claimed in factorized generative models.
