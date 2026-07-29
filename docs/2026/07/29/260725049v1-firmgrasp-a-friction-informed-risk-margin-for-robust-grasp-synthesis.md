# FIRMGrasp: A Friction-Informed Risk Margin for Robust Grasp Synthesis

- 区域：速读区
- 排名：13
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Clinton Enwerem, John S. Baras, Calin Belta
- 机构：University of Maryland
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25049v1) · [PDF](https://arxiv.org/pdf/2607.25049v1)

## TLDR
FIRMGrasp introduces a family of friction-volatility-aware grasp quality metrics grounded in the Conditional Value-at-Risk (CVaR) risk measure, which guarantees force closure with probability at least β under uncertain friction conditions, generalizing classical deterministic metrics like the Ferrari-Canny epsilon.

## Abstract
Classical grasp quality metrics assume a single deterministic friction coefficient, so they cannot predict whether a grasp retains force closure across the range of friction values the contacting surfaces may exhibit. To predict these failures, we present FIRMGrasp, a family of friction-volatility-aware grasp quality metrics grounded in the Conditional Value-at-Risk (CVaR) risk measure. Unlike standard grasp quality assessors that assume a single friction realization, our metric evaluates the force-closure margin at the CVaR-discounted mean of the adverse friction tail, yielding a risk-adjusted margin $\varepsilon^{(β)}$, the inscribed-ball radius of the risk-adjusted wrench space. We establish its monotonicity in the confidence level $β$, its differentiability in the grasp parameters, and a probabilistic closure certificate that guarantees force closure with probability at least $β$ whenever $\varepsilon^{(β)}$ is positive. Under a calibrated friction distribution, analytic evaluation shows our $\varepsilon^{(β)}$ metric identifies friction-sensitive grasps that the nominal Ferrari-Canny epsilon rates as high-quality, and we compare against the nominal epsilon and recent differentiable baselines. Across 1,599 LEAP Hand and Allegro Hand grasps, 53% of the grasps the nominal Ferrari-Canny margin certifies lose force closure in the adverse friction tail. On the same set, the nominal margin separates realized shake and pick success with probabilities of only 0.53 and 0.67, near chance on shake success, whereas $\varepsilon^{(β)}$ orders the pair correctly with probabilities of 0.63 and 0.78, respectively. In simulated lift trials with gravity enabled at an adverse friction coefficient of 0.2, grasps $\varepsilon^{(β)}$ certifies reach a 70% success rate under lateral pull, against 25% for grasps the nominal margin certifies but $\varepsilon^{(β)}$ rejects.
