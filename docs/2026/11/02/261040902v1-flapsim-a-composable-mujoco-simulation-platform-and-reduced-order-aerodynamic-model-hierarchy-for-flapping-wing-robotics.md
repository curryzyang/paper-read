# FlapSim: A Composable MuJoCo Simulation Platform and Reduced-Order Aerodynamic Model Hierarchy for Flapping-Wing Robotics

- 区域：速读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Mingshan He
- 机构：Institute of Science Tokyo
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40902v1) · [PDF](https://arxiv.org/pdf/2610.40902v1)

## TLDR
FlapSim is a modular open-source MuJoCo platform for flapping-wing robotics whose composable reduced-order aerodynamic hierarchy achieves about 0.966 mean wrench fidelity at roughly 68× speedup over a 50 μs blade-element reference by combining multirate timing, 3D inflow/gust coupling, analytical geometry scaling, and phase-locked stroke harmonics, which are especially important during frequency transitions.

## Abstract
Flapping-wing simulation must reconcile high-frequency wingbeat aerodynamics with the slower dynamics relevant to flight control and reinforcement learning. We present FlapSim, a modular open-source MuJoCo simulation platform that combines robot descriptions, wing geometry, and composable aerodynamic models in a deterministic simulation pipeline. Across $48$ held-out scenarios spanning frequency, gimbal, wind, frequency-step, gust, and cross-robot flat-plate regimes, we compare five reduced-order configurations operating at $1\,\text{ms}$ with a $50\,μ\text{s}$ quasi-steady blade-element reference. The built-in hover cycle-averaged baseline achieves a $67.51\times$ CPU speedup but only $0.6593$ mean wrench fidelity. Combining multirate $21$-substep clock synchronization, three-dimensional linear/quadratic inflow and gust coupling, analytical blade-element geometry scaling, and phase-locked $1f\text{--}6f$ harmonics raises mean fidelity to $0.9646$ at a $65.19\times$ speedup in a five-block model. A streamlined four-block model without explicit step-transient lag states achieves $0.9662$ fidelity at a $67.98\times$ speedup. Controlled ablations show that stroke harmonics are particularly important during frequency transitions, improving held-out frequency-step fidelity by $+0.3176$. Transfer-function analysis explains this effect: fixed-window cycle averaging retains harmonic contributions when the wingbeat frequency changes, so within-cycle reconstruction also improves the filtered wrench. Once phase alignment and harmonic synthesis are included, explicit transient lag states provide no additional benefit in this benchmark. These results characterize the accuracy--computation tradeoff of the aerodynamic hierarchy and identify timing, inflow, geometry, and harmonic representation as central considerations for reduced-order flapping-wing simulation.
