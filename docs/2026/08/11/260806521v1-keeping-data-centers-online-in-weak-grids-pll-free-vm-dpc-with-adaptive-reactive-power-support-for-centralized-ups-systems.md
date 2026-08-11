# Keeping Data Centers Online in Weak Grids: PLL-Free VM-DPC With Adaptive Reactive-Power Support for Centralized UPS Systems

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Jesus D. Vasquez-Plaza, Yonghao Gui, Jin Dong, Jamie Lian, Yilu Liu
- 机构：Oak Ridge National Laboratory, University of Tennessee
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06521v1) · [PDF](https://arxiv.org/pdf/2608.06521v1)

## TLDR
The paper proposes a PLL-free voltage-modulated direct power control (VM-DPC) strategy with adaptive reactive-power support for centralized UPS rectifiers, demonstrating through switching-level and OPAL-RT real-time validation that it restores stable dc-link operation and reliable IT-load power delivery under weak-grid conditions (SCR ≤ 2) where conventional PLL-based PI control becomes unstable.

## Abstract
Data center power systems are increasingly exposed to weak-grid conditions due to the rapid growth of converter-dominated networks and highly dynamic artificial intelligence (AI) workloads. In centralized uninterruptible power supply (UPS) architectures, the front-end rectifier continuously processes the incoming facility power, making its dynamic performance critical for ensuring stable operation and reliable power delivery to information technology (IT) equipment. Under weak-grid conditions, conventional phase-locked loop (PLL)-based proportional-integral (PI) rectifier controllers may exhibit instability due to strong interactions between converter control dynamics and grid impedance. This paper investigates the stability of centralized UPS data center systems operating under weak-grid conditions using a detailed switching-level model developed in MATLAB/Simulink and validated in real time using an OPAL-RT platform. To enhance weak-grid stability and improve converter-grid interaction, a voltage-modulated direct power control (VM-DPC) strategy with adaptive reactive power support is applied to the front-end rectifier. The proposed approach directly regulates active and reactive power without PLL synchronization while dynamically supporting the point of common coupling (PCC) voltage during rapid IT load variations. Results demonstrate that conventional PI-based rectifier control becomes unstable under SCR<=2 conditions, leading to dc-link oscillations and degradation of downstream power delivery. In contrast, the proposed VM-DPC strategy restores stable operation, improves system damping, and maintains reliable power transfer to highly dynamic IT loads under weak-grid operation.
