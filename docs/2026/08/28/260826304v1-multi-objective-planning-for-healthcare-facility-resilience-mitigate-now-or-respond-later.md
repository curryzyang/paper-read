# Multi-Objective Planning for Healthcare Facility Resilience: Mitigate Now or Respond Later?

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Gizem Toplu-Tutay, John J. Hasenbein, Matt Kammer-Kerwick, Erhan Kutanoglu
- 机构：The University of Texas at Austin
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26304v1) · [PDF](https://arxiv.org/pdf/2608.26304v1)

## TLDR
This paper develops a bi-objective two-stage stochastic optimization model for healthcare facility flood resilience, jointly optimizing permanent hardening and scenario-dependent patient evacuations to trade off expected economic losses against socially vulnerability-weighted service disruption impacts, and demonstrates with exact and Lagrangian decomposition methods on Texas hospitals and nursing homes.

## Abstract
Flooding can damage healthcare facilities, interrupt local care capacity, and trigger costly patient evacuations. Addressing these risks requires long-term resilience investments under uncertainty. We develop a bi-objective two-stage stochastic optimization model that jointly determines permanent facility hardening and scenario-dependent evacuation decisions. The first objective minimizes expected evacuation, physical damage, and business-interruption costs. The second minimizes a service-disruption impact index that combines the duration and scale of service loss with a place-based social-vulnerability weight. We develop an exact Benders decomposition and a scalable Lagrangian-dual method with tailored primal recovery, embedding both within an adaptive procedure for constructing informative Pareto frontiers. A case study of 3,752 hospitals and nursing homes in Texas evaluates the framework under climate-informed tropical-cyclone flood scenarios. The results show that minimizing economic losses alone can systematically allocate less protection to facilities located in socially vulnerable areas, while moderate movement along the Pareto frontier can substantially reduce disruption impacts at limited additional expected cost. The exact decomposition solves all tested instances, including larger stress tests for which the extensive formulation becomes memory-limited, while the Lagrangian method provides substantially faster high-quality solutions.
