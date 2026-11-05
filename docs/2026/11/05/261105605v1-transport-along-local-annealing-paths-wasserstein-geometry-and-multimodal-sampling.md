# Transport along Local Annealing Paths: Wasserstein Geometry and Multimodal Sampling

- 区域：速读区
- 排名：2
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Han Chen, Sifan Liu
- 机构：Duke University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05605v1) · [PDF](https://arxiv.org/pdf/2611.05605v1)

## TLDR
The paper shows that global annealing paths can be inefficient in Wasserstein space due to costly mass transfer between modes, and proposes componentwise annealed transport (CAT), which learns separate transport maps along local componentwise annealing paths from a mode-informed mixture reference—with consistent weight estimation and adaptive schedules—to improve multimodal sampling and transport learning.

## Abstract
Variational approaches to learning transport maps for multimodal sampling can suffer from mode collapse. One way to mitigate this problem is to learn transport along a prescribed path of intermediate distributions defined by geometric annealing. We show that annealing can take a substantial detour in Wasserstein space: when mass moves between modes, the path can be much longer than the distance between its endpoints. We further link path geometry to transport learning, showing that long annealing paths can slow population optimization, while sufficiently regular paths permit rapid convergence. Motivated by these findings, we propose componentwise annealed transport (CAT) to reduce the need for mass transfer between modes. Starting from a mode-informed mixture reference, CAT constructs an exact mixture decomposition of the target and learns separate transport maps along componentwise annealing paths. We estimate the component weights separately and show that these estimates remain consistent even when the learned flows are inexact. We also develop adaptive annealing schedules guided by transport effort. Experiments on multimodal synthetic distributions and Bayesian inference problems demonstrate improvements in transport learning and sampling efficiency.
