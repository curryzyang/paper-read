# EMT Modeling and Coordinated Mode-Transition Ride-Through Control of Modern Data Centers

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Junyuan Zheng, Salish Maharjan, Min Lwin, Soummya Roy, Zhaoyu Wang, Wenlong Shi, Feng Qiu, Rajarshi Roychowdhury
- 机构：INS Engineering, Iowa State University, Argonne National Laboratory, Xcel Energy
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08614v1) · [PDF](https://arxiv.org/pdf/2611.08614v1)

## TLDR
The paper presents a PSCAD/EMTDC electromagnetic-transient model of a modern data center—including UPS/BESS, induction-motor cooling loads, a VFD-driven CRAH, and aggregated server load—with a voltage-based state machine that coordinates UPS mode transitions, CRAH supply path, and ramped post-fault reconnection, and benchmarks its fault/LVRT/HVRT ride-through behavior against PSS/E aggregate models, showing close aggregate agreement while capturing converter and motor-reacceleration transients.

## Abstract
Large data centers are emerging as power-electronic loads whose response to grid voltage disturbances can affect bulk-system stability. This paper presents the composition and control characteristics of a proprietary electromagnetic transient (EMT) model of a modern data center comprising an uninterruptible power supply (UPS) with battery energy storage, induction-motor cooling loads, a computer room air handler (CRAH) driven by a variable-frequency drive (VFD), and an aggregated server load. A voltage-based state machine coordinates three aspects of the facility response: the UPS operating mode (eco, double conversion, or battery), the supply path of the CRAH, and a ramped reconnection of the grid-side UPS converter after the disturbance clears. A 100 MW facility is implemented in PSCAD/EMTDC and benchmarked against the PSSE PERC1 aggregate data center model under a symmetrical three-phase fault and low- and high-voltage ride-through (LVRT/HVRT) events. The two models agree closely in their voltage and active-power trajectories, while the EMT model also resolves the converter and motor-reacceleration transients that the phasor-domain model cannot.
