# DePICT: Decision-Preserving Interface for Constrained Downstream Tasks

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Utkarsh Grover, Ravi Ranjan, Agoritsa Polyzou, Wyatt T. Mackey, J. Morris Chang, Leonardo Bobadilla, Xiaomin Lin
- 机构：University of South Florida, DEVCOM Army Research Lab, Florida International University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03945v1) · [PDF](https://arxiv.org/pdf/2610.03945v1)

## TLDR
DePICT builds a decision-preserving interface for constrained downstream tasks by using KKT-based sensitivity ranking to isolate only context directions that actually change the constrained optimum, removing irrelevant inputs and substantially reducing downstream decision regret.

## Abstract
A constrained optimization problem may involve a parameter in its objective and active constraints, yet the final decision may remain insensitive to small changes in that parameter. This raises a fundamental question: which inputs does a decision making system truly depend on? Building on this question, we introduce DePICT, a procedure for constructing decision preserving interfaces by ranking context directions according to the optimizer's solution sensitivity and aggregating them across an operating regime. We study this problem in a high dimensional setting where primitive context parameterizes a constrained task and the downstream agent observes only a selected subset of context directions. For locally regular constrained programs, we derive a Karush Kuhn Tucker (KKT) based characterization of when a context direction is optimizer relevant. Our analysis shows that appearing in the active optimization problem does not necessarily imply that a variable affects the final decision. Some context directions can alter the KKT conditions while leaving the optimal solution unchanged because their effect is absorbed by the dual variables. DePICT is designed to remove exactly these directions. In a controlled diagnosis, it recovers the decision relevant interface exactly and reduces linear predictor regret to 0.009, compared with 0.475 for the strongest competing baseline.
