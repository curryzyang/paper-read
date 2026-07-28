# Randomized Constructive Heuristics for the VRPTW: A Focus on Regret-k

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Florian Rascoussier, Romain Billot, Lina Fahed, Christine Solnon
- 机构：IMT Atlantique, INSA Lyon
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22581v1) · [PDF](https://arxiv.org/pdf/2607.22581v1)

## TLDR
This paper introduces a novel randomization of the Regret-k heuristic for the VRPTW by separating customer selection and insertion decisions, and evaluates it within multi-start, local search, and ACO frameworks on standard benchmarks to explore the trade-off between solution quality and computational cost.

## Abstract
The Vehicle Routing Problem with Time Windows (VRPTW) requires a fleet of capacitated vehicles to serve customers within strict time windows while minimizing total travel time. Constructive heuristics are fundamental for generating solutions and commonly serve as starting points for metaheuristics such as Iterated Local Search (ILS), Genetic Algorithms, and Ant Colony Optimization (ACO). This work studies three classical constructive heuristics - Nearest Neighbor, Best Insertion, and Regret-k - within a randomized, multi-start framework, a setting that remains largely under-explored despite their well-established deterministic use. We address how to effectively randomize these heuristics and, in particular, propose a novel randomization of Regret-k by separating the ''who'' (which customer to insert next) and ''where'' (insertion position) decisions, applying a probabilistic selection proportional to the regret value to preserve the heuristic's foresight while injecting the diversity needed for a multi-start approach. We further study the impact of combining these greedy randomized constructions with Local Search and ACO. Experiments follow the DIMACS 2021 conventions (integer, truncated Euclidean distances) on the Solomon and Gehring \& Homberger benchmarks (100--1000 customers), comparing against the Best-Known Solutions and the state-of-the-art Hybrid Genetic Search solver, with all critical components implemented in modern C++ and bound to Python via pybind11. To the best of our knowledge, the randomization of Regret-k has never been examined; our analysis highlights the trade-off between solution quality and computational cost, providing a preliminary step toward hybrid methods (ACO, ILS, Branch-and-Price) for the Time-Dependent VRPTW within the MAMUT project.
