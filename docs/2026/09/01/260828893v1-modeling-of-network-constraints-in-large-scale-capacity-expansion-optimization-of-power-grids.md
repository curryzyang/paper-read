# Modeling of Network Constraints in Large-scale Capacity Expansion Optimization of Power Grids

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yu Weng, Lara Booth, Priya L. Donti, Ruaridh Macdonald
- 机构：Massachusetts Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28893v1) · [PDF](https://arxiv.org/pdf/2608.28893v1)

## TLDR
The paper extends the GenX capacity expansion model with fixed-point theorem-based network constraints that embed AC optimal power flow physics at nearly the tractability of simpler transport models, and demonstrates via an ISO New England case study that these constraints capture ACOPF-like impacts on generation investment decisions with modest runtime increases.

## Abstract
Capacity expansion modeling plays a critical role in optimizing the deployment of new generation, storage, and transmission, typically at national and regional levels. To support long-term planning, these models consider a large set of energy technologies and policies, along with decades of weather and demand data. Realistic capacity expansion models thus become high-dimensional optimization problems, with hundreds of millions of variables and constraints, which are challenging to solve. A common strategy to address this complexity is to omit non-linear, non-convex AC optimal power flow (ACOPF) constraints and instead use linearized power balance equations or transport formulations. While these simplifications improve tractability, they limit our understanding of how power flow and the physical properties of power networks impact investment decisions across generation, storage, and transmission infrastructure. This paper addresses this gap by extending the GenX capacity expansion model to incorporate fixed point theorem-based network constraints. These embed ACOPF-based considerations while maintaining the tractability of the planning model, nearly preserving the dimensionality of the transport formulation and incurring only modest runtime increases. This approach is much cheaper than embedding ACOPF directly, making it appropriate for large-scale capacity planning problems. We compare our approach to the original transport-based GenX model as well as a non-linear, non-convex version that incorporates the full ACOPF constraints, for a case study of the ISO New England grid.
