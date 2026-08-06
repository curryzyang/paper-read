# LaPrune: Controllable Differentiable Sparsity at Million Scale

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Jakub Antczak, Joanna Wojciechowicz, Łukasz Struski, Jacek Tabor
- 机构：Wrocław University of Science and Technology, Jagiellonian University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04057v1) · [PDF](https://arxiv.org/pdf/2608.04057v1)

## TLDR
LaPrune introduces a mathematically exact-budget differentiable sparsity layer that controls mask hardness via a normalized second-moment constraint while preserving the selected mass, enabling scale-invariant, million-scale top-k selection.

## Abstract
Top-$k$ selection determines which components of a sparse model remain active. Hard selection blocks gradients, while continuous relaxations often couple mask hardness to the selected mass. We introduce LaPrune, a mathematically exact-budget differentiable layer that controls the normalized second moment while preserving the selected mass. A LapSum barrier preserves the selection mass, and a normalized second-moment constraint moves the mask from a dense equal-mass allocation toward hard top-$k$ at each budget. We derive a population prediction of the saturated fraction, a near-binary limiting law, and a tight worst-case guarantee on the near-zero fraction. The normalized hardness parameter is invariant to score scale, while a fixed LapSum temperature is not.
