# Geometric Coherence via Weighted Matching for 3D Heterogeneous Multi-Agent Reach-Avoid Games

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Prajwal Vijay
- 机构：IIT Madras
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06882v1) · [PDF](https://arxiv.org/pdf/2610.06882v1)

## TLDR
This paper introduces a cardinality-first weighted sequential matching method that uses the Hamilton–Jacobi–Isaacs interception value as a secondary assignment weight to resolve the “Geometric Sprawl” failure of cardinality-only matching in 3D heterogeneous multi-agent reach-avoid games, improving capture counts and interception heights on a deterministic benchmark.

## Abstract
We study assignment quality in 3D heterogeneous multi-agent reach-avoid games and identify a recurring failure mode of cardinality-only matching in geometrically structured scenarios, which we term \emph{Geometric Sprawl}. In these cases, multiple maximum-cardinality assignments are available, but some induce spatially incoherent pairings and inefficient pursuit trajectories. Building on the evasion-space framework of Yan et al.~\cite{yan2022}, we introduce a cardinality-first weighted sequential matching method in which the Hamilton--Jacobi--Isaacs interception value $z_I(s,j)$ is used as a secondary assignment weight. Each sequential stage is solved with a min-cost max-flow backend, while the unweighted baseline uses the same solver with the weight term removed. We evaluate both methods on a deterministic 35-scenario benchmark (7 families & 5 initialization variants) under two regimes: a diagnostic stationary-unmatched setting and a hybrid saddle-point setting with goal-directed unmatched evaders. On this benchmark, the weighted method resolves 13 of 15 geometric stress-test instances that cause repeated timeouts for the unweighted baseline in the diagnostic regime, and under the hybrid regime improves mean captures from $3.20$ to $3.91$ (22\% increase) and mean interception height from $3.87$ to $5.36$ (40\% increase). We also report lower path tortuosity and lower angular-effort proxy values, suggesting smoother pursuit trajectories in this first-order simulation model. We release the simulator and benchmark suite at \href{https://github.com/Prajwal-Vijay/geometric-coherence-weighted-matching}{github.com/Prajwal-Vijay/geometric-coherence-weighted-matching} to support reproducible evaluation of assignment strategies for 3D reach-avoid games.
