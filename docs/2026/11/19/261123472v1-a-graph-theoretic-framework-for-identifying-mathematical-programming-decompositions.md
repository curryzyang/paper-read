# A Graph-Theoretic Framework for Identifying Mathematical Programming Decompositions

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Nicholas N. Kalamaris, Christos T. Maravelias
- 机构：Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23472v1) · [PDF](https://arxiv.org/pdf/2611.23472v1)

## TLDR
The paper proposes a graph-theoretic framework that represents a mathematical program as a bipartite variable–constraint graph, applies projections and coarsening, and uses integer programming to identify complicating variables and/or constraints, enabling systematic discovery and comparison of variable, constraint, and cross decompositions.

## Abstract
We develop a framework for identifying combinations of complicating variables and/or constraints that can be used to formulate mathematical programming decompositions. A mathematical program is represented by a graph which accounts for the structural and functional relationship between variables and constraints. Graph projections are used to focus on variable- or constraint-based decompositions. A series of coarsening operations is used to generate a reduced graph based on the original or projected graph. On the reduced graph, we use integer programming to identify different combinations of complicating variables and/or constraints. Specifically, variables and constraints are identified as complicating based on their structural role and/or their functionality (contribution to nonlinearity) in the mathematical program. The framework allows us to assess the viability of different decomposition types (variable, constraint, cross) and identify multiple potential decomposition formulations of the same type (e.g. different combinations of complicating variables for Benders decomposition). The systematic nature of our framework facilitates broader studies into the efficacy of different decompositions across a range of problems including energy markets, process design, and machine learning.
