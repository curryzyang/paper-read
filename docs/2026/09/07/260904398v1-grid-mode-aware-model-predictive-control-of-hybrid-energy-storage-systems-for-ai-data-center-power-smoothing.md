# Grid-Mode-Aware Model Predictive Control of Hybrid Energy Storage Systems for AI Data Center Power Smoothing

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Xin Chen
- 机构：Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04398v1) · [PDF](https://arxiv.org/pdf/2609.04398v1)

## TLDR
This paper proposes a grid-mode-aware model predictive control (G-MPC) framework for hybrid battery–supercapacitor storage that smooths AI data center grid-side power by embedding band-pass filter dynamics to explicitly suppress power components near vulnerable grid oscillatory modes while jointly minimizing modal-power violations, degradation, and ramping costs.

## Abstract
To facilitate the grid-friendly integration of highly variable AI data center loads, this paper proposes a grid-mode-aware model predictive control (G-MPC) framework for managing a hybrid energy storage system (HESS) to smooth grid-side power demand. The framework optimally coordinates a battery energy storage system (BESS) and a supercapacitor (SC) by solving a multi-step optimization problem in a receding-horizon manner. In particular, band-pass filter dynamics are directly embedded in the G-MPC formulation to extract and suppress grid-side power components associated with vulnerable grid oscillatory modes, thus mitigating load-induced grid oscillations. The resulting G-MPC optimization jointly minimizes violations of grid-side power-envelope, ramp-rate, and modal-power requirements and the degradation and power-ramping costs of the BESS and SC, while satisfying power limits, state-of-charge limits, and other operational constraints. To enable real-time implementation, a fix-and-re-optimize algorithm is developed to solve each G-MPC problem efficiently while preventing simultaneous charging and discharging. Extensive simulations demonstrate the effectiveness, flexibility, and computational efficiency of the proposed framework. The results also highlight the importance of explicitly suppressing power components associated with vulnerable grid modes, rather than merely reducing overall load variations, to effectively mitigate grid oscillations.
