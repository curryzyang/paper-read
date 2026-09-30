# The Decision Value of Perception Compute

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Hoang Pham Cong, Ho Viet Duc Luong
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35910v1) · [PDF](https://arxiv.org/pdf/2609.35910v1)

## TLDR
This paper defines the decision value of perception compute and introduces DEEP, a budget-constrained decision-oracle benchmark showing that better perception often fails to improve—and can even harm—downstream decisions, so adaptive perception should be allocated by decision-level value rather than perception-level gain alone.

## Abstract
Adaptive perception spends extra computation on inputs where perception is expected to improve. When perception feeds a downstream decision system, a better perception output need not produce a better decision. We define the decision value of perception compute as the change in downstream loss from escalating an input from a cheap to an expensive perception mode. Because this value can be negative, the allocation of perception compute should be judged against a budget-constrained decision oracle, with uniform full-fidelity inference as a baseline rather than an upper bound. We introduce DEEP (Decision Evaluation for Escalated Perception), a benchmark that scores pre-escalation allocators against this oracle under selection, latency and energy budgets, charging each allocator for its own computation. With deployed monocular geometry on KITTI and nuScenes, we find that 34--54% of the escalations that change downstream loss make it worse; harmful escalations also occur for the published PDM-Closed planner, evaluated open-loop on nuPlan with real detector outcomes. On nuScenes, perception-level gain frequently disagrees in sign with decision value. This mismatch has practical consequences: choosing among fixed deployable signals by missed-object perception gain rather than by decision value reduces realized test decision gain by 7.4% of the all-cheap loss on average. Learned allocators recover part of the oracle's value by finding beneficial escalations but select nearly as much harm as random, and once their own computation is charged at a 20% latency budget, only the lightweight routers, at about 3.5\% of a full detector pass, still beat random.
