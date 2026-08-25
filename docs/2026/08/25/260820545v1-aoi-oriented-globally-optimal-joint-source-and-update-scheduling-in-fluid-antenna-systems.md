# AoI-Oriented Globally Optimal Joint Source and Update Scheduling in Fluid Antenna Systems

- 区域：速读区
- 排名：2
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Xiaopeng Yuan, Paul Zheng, Anke Schmeink
- 机构：TU Dresden, RWTH Aachen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20545v1) · [PDF](https://arxiv.org/pdf/2608.20545v1)

## TLDR
TLDR: This paper proposes a globally optimal joint source and update scheduling algorithm using fixpoint theory and filtering to minimize the maximum average age of information (AoI) in a fluid-antenna-assisted multi-source status update system.

## Abstract
As a promising technique, fluid antennas enable adaptive radio environment management and interference mitigation through reconfigurable fluid port selections. In this work, to explore the benefits of fluid antennas for data freshness enhancement, we consider a fluid-antenna assisted status update system supported by multiple source nodes monitoring the same environmental status. We assume a subset of the source nodes are activated to report status updates with different periods. Each user is assigned to one source node and equipped with an fluid antenna to adaptively enhance the channel gain to assigned source node while mitigating interference from other activated source nodes. With maximal signal-to-interference-noise ratio (SINR)-based fluid port selection at all users, we formulate an optimization problem to minimize the maximum average age of information (AoI), where source node activation and assignment, i.e., source scheduling, is jointly optimized with the update periods of all activated source nodes. To optimally solve the resulting mixed-integer nonlinear problem, we first consider given source scheduling decision and apply performance achievability analysis. Aided by fixpoint theory, we propose an efficient bisection algorithm for optimal update scheduling. Based on these characterizations, we further propose a filtering algorithm which efficiently eliminates all non-optimal source scheduling decisions. The globally optimal joint solution is then obtained by combining the resulting optimal source scheduling with its corresponding optimal update scheduling. Numerical results validate the optimality of proposed solution and demonstrate the effectiveness of fluid antennas in enhancing data freshness.
