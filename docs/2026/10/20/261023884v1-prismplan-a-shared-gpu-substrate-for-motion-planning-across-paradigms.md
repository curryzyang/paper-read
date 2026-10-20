# PrismPlan: A Shared GPU Substrate for Motion Planning Across Paradigms

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Hong Wu, ChaoXuan Liu, ShuJie Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23884v1) · [PDF](https://arxiv.org/pdf/2610.23884v1)

## TLDR
PrismPlan introduces a shared GPU substrate for batched collision detection and forward kinematics that lets sampling, search, and optimization planners run on identical device code for fair cross-paradigm comparison, revealing that sampling is most reliable—especially at high DoF—while search offers lower latency on 7-DoF arms and optimization lags when solving from scratch.

## Abstract
GPU acceleration has made motion planning one to two orders of magnitude faster, but it has not made the three paradigms---sampling, search, and optimization---comparable to one another: every GPU-accelerated planner is built around a single paradigm, so comparing across libraries also compares their collision checkers. All three, however, bottleneck on the same GPU primitive: batched collision detection and the batched forward kinematics beneath it. PrismPlan builds that primitive once, as a shared substrate of per-sphere collision--kinematics device code that every planner consumes. Because they all execute the same device code, the backend is held fixed by construction and the paradigms can be compared head-to-head. We run six planners over 1800 MotionBenchMaker problems on three robots (7--14 DoF, one a dual-arm whole-body composite) at an equal 2s budget. On the 7-DoF Panda, sampling (pRRTC) is the most reliable paradigm at 98%, while parallel search (wPA*SE) follows within four points at a 3-4 times$ lower median latency, and the local optimizers trail well behind when made to solve from scratch. On the 14-DoF dual-arm composite, sampling still solves about 90% of feasible problems, while no search or optimization planner clears a third of them. Our open-source code is available at https://github.com/XiaoyubotMotionTeam/PrismPlan.
