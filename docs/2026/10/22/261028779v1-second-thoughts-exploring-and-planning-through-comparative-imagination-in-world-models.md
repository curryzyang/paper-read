# Second Thoughts: Exploring and Planning through Comparative Imagination in World Models

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Hieu Tran, Hong Yu
- 机构：University of Massachusetts Amherst, University of Massachusetts Lowell
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28779v1) · [PDF](https://arxiv.org/pdf/2610.28779v1)

## TLDR
SDI (Sibling Disagreement in Imagination) uses repeated imagined rollouts of the actor’s own action sequence as a shared reference to scale both exploration and the acceptance of planned actions, enabling world-model agents to selectively plan without extra disagreement ensembles and improving performance across Meta-World, Adroit, and DM-Control.

## Abstract
World models let agents compare imagined outcomes before acting, but an agent must still decide which alternatives to explore and when a proposed plan should replace its learned policy. We introduce SDI (Sibling Disagreement in Imagination), which connects these decisions through a shared actor-based reference. SDI compares action sequences imagined from the same model state, using repeated rollouts of the actor's own sequence to measure variation under fixed behavior. This reference scales both the spread across candidate returns, which provides an exploration signal, and a proposed plan's predicted advantage, which governs action acceptance. The agent executes a planned action when its advantage exceeds the reference variability by a fixed factor; otherwise, it follows the actor. SDI reuses the base agent's world model, actor, and critic without requiring an additional disagreement ensemble. Exploration and planning guide training data collection, while evaluation uses the learned actor alone. Across Meta-World, Adroit, and DM-Control, SDI achieves a higher observed task-average score than every compared baseline in each suite and matches or exceeds the strongest baseline's performance on 15 of 18 tasks. Component ablations and robustness analyses further examine the roles of exploration, planning exposure, and action acceptance. Paired evaluations from identical simulator states show that the gate improves both recovery from actor failures and preservation of successful behavior relative to ungated planning, while substantially reducing return degradation. Together, these results support comparing imagined alternatives against a shared actor reference as a unified approach to exploring and planning with world models.
