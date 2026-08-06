# A Primal Perspective on Distributionally Robust Optimization: An Investigation on Modeling and Solution Strategies

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yiqi Tian, Bo Zeng
- 机构：University of Pittsburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04123v1) · [PDF](https://arxiv.org/pdf/2608.04123v1)

## TLDR
The paper proposes a primal, distribution-cut-based algorithmic framework (BiCS) for distributionally robust optimization that avoids difficult dual reformulations and efficiently handles standard, almost-sure, chance-constrained, and locally informed DRO variants.

## Abstract
As a popular optimization scheme, distributionally robust optimization (DRO) protects decisions against ambiguity in probability distributions. For (single-stage) DRO, prevailing dual reformulations can become difficult when model or ambiguity-set structures are complex. We study DRO from a primal perspective, working directly with distributions in ambiguity sets on closed, potentially unbounded sample spaces. This perspective leads to an algorithmic framework, referred to as BiCS, that constructs and leverages distribution cuts to achieve strong performance. We show that BiCS is applicable to standard DRO, almost-sure DRO, DRO with various chance constraints, and DRO with ambiguity sets strengthened by local information. Numerical experiments with moment and Wasserstein ambiguity sets show that this framework demonstrates superior performance, including solving cases where the examined compact reformulations are unavailable or computationally difficult. The local-information study also makes changes in worst-case distributions directly visible.
