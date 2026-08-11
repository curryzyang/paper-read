# Wasserstein Mahalanobis Distances for Recovering Latent Geometry

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Chuxiangbo Wang, Shiying Li, Caroline Moosmüller
- 机构：University of Nebraska at Lincoln, University of North Carolina at Chapel Hill
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06560v1) · [PDF](https://arxiv.org/pdf/2608.06560v1)

## TLDR
The paper introduces a Wasserstein Mahalanobis distance that extends covariance-adapted geometry to probability measures via optimal transport displacement fields and tangent-space covariance operators, showing it recovers latent geometric structure by approximating the classical Mahalanobis distance between transformed latent means for Gaussian measures under nonlinear pushforwards.

## Abstract
The Mahalanobis distance is a fundamental covariance-adapted metric for multivariate data and plays a central role in recovering latent geometry from nonlinear observations. We extend this principle from vector-valued data to probability measures by introducing a Wasserstein Mahalanobis distance. Our construction replaces Euclidean displacement vectors with optimal transport displacement fields and local covariance matrices with covariance operators defined on Wasserstein tangent spaces.
  We show that this construction inherits the geometry-recovery property underlying nonlinear independent component analysis. In particular, for Gaussian measures with common covariance transformed by a smooth nonlinear pushforward, the proposed Wasserstein Mahalanobis distance approximates the classical Mahalanobis distance between the transformed latent means. The correspondence is exact for affine transformations and holds up to controlled higher-order error terms for general smooth transformations. These results establish a distribution-valued analog of classical Mahalanobis geometry and provide theoretical support for covariance-adapted learning directly in Wasserstein space. Numerical experiments confirm the theoretical predictions and demonstrate accurate recovery of latent geometric structure.
