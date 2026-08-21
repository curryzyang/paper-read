# TOBYQA: A Trust-Region Method for Derivative-Free Optimization on Time-Varying Functions

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Haoyu Yao, Pengcheng Xie
- 机构：Xi'an Jiaotong University, Lawrence Berkeley National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18124v1) · [PDF](https://arxiv.org/pdf/2608.18124v1)

## TLDR
TOBYQA introduces a drift-compensated, ridge-regularized trust-region DFO framework that jointly models spatial and temporal variations via a unified quadratic interpolation system, improving robustness on time-varying, noisy functions while matching static performance.

## Abstract
Derivative-free optimization (DFO) becomes particularly difficult when function evaluations are affected by temporal drift and observation noise. Conventional trust-region methods generally assume a static landscape, which may lead to stale-data bias and misleading trust-region updates. We propose TOBYQA (Time-augmented Optimization BY Quadratic Approximation), a regularized DFO framework that jointly models spatial geometry and temporal variations within a unified quadratic interpolation system. Specifically, TOBYQA augments the classical KKT interpolation system with a ridge term on the $(1,1)$-block, which accommodates observation noise and ensures well-posedness under a mild full-column-rank condition on the constraint block, thereby relaxing the stringent geometric poisedness requirements of classical methods. To handle non-stationarity, we embed an explicit linear-in-time drift term into the interpolation model, enabling a drift-compensated ratio test that subtracts the estimated temporal component from the observed reduction. Additionally, a diagonal affine-scaling adapts the search geometry to local variation in curvature. Benchmark evaluations on the Moré--Wild 88-function suite across various temporal drifts and dimensions ($n \in \{6,10,20\}$) demonstrate that TOBYQA exhibits enhanced robustness under drift, while maintaining competitive performance in static environments.
