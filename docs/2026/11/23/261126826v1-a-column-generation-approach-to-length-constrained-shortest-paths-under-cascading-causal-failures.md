# A Column-Generation Approach to Length-Constrained Shortest Paths under Cascading Causal Failures

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Nicolò Aicardi, Zuyuan Zhang, Sridhar Radhakrishnan, Kash Barker, Dritan Nace
- 机构：Université de Technologie de Compiègne, University of Oklahoma, Università degli Studi di Genova
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26826v1) · [PDF](https://arxiv.org/pdf/2611.26826v1)

## TLDR
The paper studies the NP-hard problem of selecting the maximum set of cascading causal node failures while preserving a source–terminal path within an α-factor of the original shortest distance, and proposes a MILP formulation, a column-generation algorithm with a three-level pricing cascade, and a greedy heuristic, showing column generation is the most effective for large networks.

## Abstract
In the study of cascading causal node failures, the failure of one set of nodes can trigger the failure of another, possibly non-adjacent, set, and these triggers can propagate in cascades. Given a graph, a set of causal failures, a source-terminal pair, and a constant $α\geq 1$, we study the length-constrained shortest-path problem of finding the maximum subset of causalities whose application preserves a source-terminal path of length at most $α$ times the original distance. We show that the problem is NP-hard, a hardness that reflects the non-local, cascading nature of causal failures. We propose a mixed-integer linear programming formulation with explicit node-integrity variables that decouple the node state from routing, a column-generation algorithm built on a path-based reformulation whose pricing subproblem is solved by a three-level cascade (beam search, label-capped $A^*$, and exact $A^*$ with warm start), and a greedy heuristic as a fast baseline. On the IEEE 300 and Power 5000 benchmarks, all three methods are competitive. In dense synthetic networks of 10,000 to 15,000 nodes, the exact model exhausts its time budget or returns an order of magnitude fewer causalities, whereas column generation remains fast and accurate, emerging as the method of choice for large instances.
