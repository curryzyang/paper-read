# Scheduling of Variable-Speed Pumped Storage via Hierarchical Reinforcement Learning

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：SangWoo Park, Kyung-bin Kwon, Dam Kim
- 机构：New Jersey Institute of Technology, Chungnam National University, Pacific Northwest National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28310v1) · [PDF](https://arxiv.org/pdf/2611.28310v1)

## TLDR
This paper proposes a hierarchical reinforcement-learning framework for bidding and dispatching variable-speed pumped storage in two-settlement electricity markets, using feasibility-constrained domain randomization to resolve the day-ahead/real-time circular dependency and action-space modification—rather than reward penalties—to ensure profitable and deliverable commitments.

## Abstract
Variable-speed pumped storage hydropower (VSPSH) plants modulate power continuously in both generation and pumping, a match for the net-load ramps of rising wind and solar. Their flexibility is bounded by hydraulics rather than by a power rating, so the deliverable power range shifts with net head and excludes small outputs entirely. This paper addresses bidding and dispatch for such a plant across a two-settlement market with a hierarchical reinforcement-learning formulation. Its two layers are circularly dependent: a real-time (RT) bid is defined only against a cleared day-ahead (DA) commitment, and the DA reward only against an RT dispatch policy. Our proposed feasibility-constrained domain randomization breaks the cycle by training the RT layer on generated deliverable DA schedules before any bidding policy exists; the DA layer then optimizes against that frozen RT behavior, and the two alternate. Learning a policy at once profitable and deliverable is obstructed by the nonconvex operating region: penalizing infeasibility competes against the revenue the offer earns, discouraging an undeliverable offer without preventing one. We therefore pursue safety through action-space modification rather than through the reward, combining action masking of the bid space, projection of each commitment before settlement, and replacement by a fail-safe controller. Over 48 out-of-sample days it earns $3,313/day more than an equivalent penalty formulation while holding undeliverable commitment at a median of zero, which the penalty formulation does not, and no ablation improves on it without giving up deliverability or the storage target.
