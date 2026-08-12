# Polyhedral Outer-Approximations for MISOCP: Geometry and Cutting Planes

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Yongzheng Dai
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10055v1) · [PDF](https://arxiv.org/pdf/2608.10055v1)

## TLDR
This paper proposes more efficient polyhedral outer approximations for mixed-integer second-order cone programs by analyzing the diminishing marginal contribution of new supporting cuts, introducing a cut-generation strategy that balances separation depth with angular novelty, and developing a progressive-integrality framework that significantly reduces computational effort.

## Abstract
Mixed-integer second-order cone programs are commonly solved by polyhedral outer approximation (OA), which iteratively strengthens a linear relaxation of the conic feasible region through cutting planes. We study how such approximations can be constructed more efficiently. First, we analyze the marginal contribution of a newly generated cut relative to cuts already present in the relaxation. Using violation- and volume-based measures, we show that this contribution decreases at least as fast as linearly as the new supporting direction approaches an existing one. Motivated by this geometric analysis, we develop a cut-generation strategy that balances separation depth with angular novelty and admits closed-form constructions. Second, we introduce a progressive-integrality OA framework that proceeds from an LP relaxation through partially integral relaxations before reaching the full MILP, thereby using inexpensive early iterations to strengthen the approximation before later mixed-integer solves. Computational experiments on CBLIB instances and large-scale AC unit-commitment models demonstrate complementary benefits from the proposed cut strategy and progressive integrality, substantially reducing the computational effort of outer approximation.
