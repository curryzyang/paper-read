# The Weighted Connected p-Median Problem

- 区域：速读区
- 排名：5
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Murat Elhüseyni, Burak Kocuk, Miklós Krész
- 机构：University of Szeged, University of Primorska, Yeditepe University, Sabancı University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08844v1) · [PDF](https://arxiv.org/pdf/2607.08844v1)

## TLDR
This paper introduces the weighted connected p-median problem, motivated by sink node selection in distributed sensor networks, and proposes mixed-integer linear programming formulations and a matheuristic to minimize the sum of deployment, access, and connection costs, demonstrating that the matheuristic efficiently yields high-quality solutions for large-scale instances.

## Abstract
The connected p-median problem is defined as a variant of the classical p-median problem when the facility nodes induce a connected subgraph. In this paper, we introduce the weighted version of the above problem when the weight of the facility connection in the objective function is defined by the minimum weight spanning tree of the facility nodes. This approach is motivated by the sink node selection in distributed sensor networks, in which the collected information is shared among the sink nodes through the minimum spanning tree. The weights of the graph determining the network topology of the candidate sink nodes as connection costs are distinguished from the standard access costs of the p-median problem. The fixed deployment costs for the setup of facilities are also considered. The objective is to minimize the overall cost as the sum of deployment cost, access cost and connection cost. We show that the problem is NP-hard and propose three mixed-integer linear programming (MILP) formulations adapted from the traveling salesperson problem literature. Since these formulations are poorly scalable with respect to network size, we develop a four-phase matheuristic method based on linear programming rounding. We conduct an extensive computational study to evaluate the performance of the MILP formulations and 22 variants of the matheuristic under different parameter settings. The results indicate that the MILP models perform effectively on small instances but struggle to solve medium- and large-scale instances within a two-hour time limit. In contrast, several matheuristic variants consistently produce high-quality solutions within minutes. Finally, we analyze the impact of network structure, size, density, and the parameter $p$ on solution quality, providing further insights for network design.
