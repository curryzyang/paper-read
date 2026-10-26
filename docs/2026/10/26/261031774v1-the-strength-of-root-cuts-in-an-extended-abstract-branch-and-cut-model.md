# The Strength of Root Cuts in an Extended Abstract Branch-and-Cut Model

- 区域：速读区
- 排名：11
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Boyang Han, Aleksandr M. Kazachkov
- 机构：University of Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31774v1) · [PDF](https://arxiv.org/pdf/2610.31774v1)

## TLDR
Using an extended abstract branch-and-cut model, the paper shows that root-only cutting can be optimal or a reliable—and asymptotically optimal in certain regimes—approximation to minimal-time branch-and-cut trees, while also characterizing settings where internal cuts are necessary.

## Abstract
The branch-and-cut paradigm has led to effective solvers for a wide range of mathematical optimization problems. Despite significant theoretical work on pure branching and pure cutting, less is known about their interaction. We study an extended abstract branch-and-cut model to investigate tradeoffs between branching and cutting, including the time to generate cuts. We prove that, under symmetric branching, some minimal-time tree has all cuts at the root, before the first branching node, and that there is an asymmetric setting where some minimal-time tree has no internal cuts, i.e., cuts both preceded and followed by branching. For other settings, although a root-cut tree may be suboptimal and differ substantially in structure from a minimal-time tree, it nevertheless provides a reliable approximation whose tree time does not deviate arbitrarily from the optimum. For constant cut strength and bounded time functions, we show that the best root-cut tree is asymptotically optimal as the target bound grows. In addition, under a single-cut-per-path restriction, we characterize when some minimal-time tree has an internal cut. Lastly, simulations indicate that the best root-cut tree is much closer to a minimal-time tree than our worst-case approximation guarantee suggests.
