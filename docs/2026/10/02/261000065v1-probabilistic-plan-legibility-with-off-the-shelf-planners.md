# Probabilistic Plan Legibility with Off-the-shelf Planners

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Michele Persiani, Thomas Hellström
- 机构：Umeå University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00065v1) · [PDF](https://arxiv.org/pdf/2610.00065v1)

## TLDR
The paper proposes a probabilistic method for legible planning in arbitrary PDDL domains using off-the-shelf planners and second-order theory of mind to model the observer’s perspective, showing that legibility generally trades off with plan efficiency and requires a balancing regularization factor.

## Abstract
Legible planning is the creation of plans that best disambiguate their goals from a set of other candidates from an observer's perspective. In this paper we propose a method for legible planning for arbitrary PDDL domains, by extending previous research on legibility to classical planning without requiring to construct ad-hoc planners. We also discuss how the observer perspective may be estimated through a second order theory of mind that connects the planner's and the observer's task spaces. Our solution can for example be deployed in human-robot teaming scenarios, where an autonomous robot in a team can implicitly communicate its goal by producing legible plans. We present benchmark results on several PDDL planning domains. Our results generally show that plan legibility is a trade-off with plan efficiency, however, not all planning domains allows to increase legibility in the same way and a regularizing factor to balance legibility and efficiency was proved necessary.
