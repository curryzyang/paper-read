# Product-Aware Deterministic Rounding for Quantized Matrix Multiplication

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Piyush Sao, Narasinga Miniskar, Pedro Valero-Lara, Keita Teranishi, Sudip Seal
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31641v1) · [PDF](https://arxiv.org/pdf/2609.31641v1)

## TLDR
This paper introduces deterministic product-aware rounding for quantized matrix multiplication that coordinates scalar rounding decisions to reduce product error, with polynomial-time guarantees for dynamic activations, an exact bias-dependent analysis for reusable static weights, and empirical improvements over round-to-nearest.

## Abstract
Scalar rounding decisions interact through matrix multiplication. We study deterministic
  product-aware rounding after scales, clipping bounds, and grids are fixed, with each active
  scalar choosing between adjacent levels. For dynamic activation rounding, null-space
  reduction preserves the relaxed product while leaving at most $r$ fractional decisions, where
  $r$ is the rank of the active gap-weighted weight block. Conditional-expectation completion
  gives a deterministic polynomial-time algorithm with squared product error at most $
  \mathrm{OPT}_{\mathrm{dyn}}+rν_{\max}^2/4$, where $\mathrm{OPT}_{\mathrm{dyn}}$ is the best
  admissible error and $ν_{\max}$ is the largest row norm of that block. For reusable static
  weights, the exact expected product-loss metric is the uncentered input second moment with
  fixed output bias; free bias recalibration yields the centered covariance. Exact optimization
  is NP-hard even at rank one. In balanced blocks with $K=1024$ and $r=16$, conditional-
  expectation completion attains a dither-normalized median error of $0.010$, compared with
  $0.899$ for round-to-nearest. Clipping-aware initialization reduces median normalized error
  by a factor of $43.4$ at ten-percent clipping. Held-out Digits experiments show that
  retaining the input mean or correcting the output bias improves median product error over
  round-to-nearest in all four tested bit-width and calibration-size settings.
