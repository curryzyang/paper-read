# RAZeR: Representation Aware Zonotope Reduction

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Vladimir Krsmanovic, Tobias Ladner, Bernd Finkbeiner
- 机构：Technical University of Munich, CISPA Helmholtz Center for Information Security
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17479v1) · [PDF](https://arxiv.org/pdf/2611.17479v1)

## TLDR
RAZeR dynamically selects zonotope reduction methods using a model-predictive-control-inspired heuristic that accounts for future propagation, yielding tighter reachable sets in nonlinear reachability analysis with negligible runtime overhead.

## Abstract
Reachability analysis is a popular technique for verifying the safety of a dynamical system under uncertainty, where the uncertainty is often represented by zonotopes. As the size of the zonotope representation typically grows as the reachability analysis progresses, it must be repeatedly reduced at the cost of additional conservatism. While various methods exist to reduce the size of the representation, combined advantages are not fully leveraged as only a single reduction method is typically used throughout the analysis. In this work, we show how dynamically choosing which method to use can yield significantly tighter results, thereby easing verification. This is realized by introducing a heuristic, derived from model predictive control, that accounts for upcoming propagation of the current zonotope. We argue that order reduction is not merely a post-processing step after propagation but also a pre-processing step that shapes how the zonotope evolves under the system dynamics. We evaluate our approach, RAZeR, on nonlinear benchmarks taken from the ARCH-COMP, where we demonstrate that RAZeR produces tighter zonotopes at a negligible performance overhead.
