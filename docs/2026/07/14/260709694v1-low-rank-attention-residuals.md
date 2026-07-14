# Low-Rank Attention Residuals

- 区域：速读区
- 排名：2
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Jonathan Su
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09694v1) · [PDF](https://arxiv.org/pdf/2607.09694v1)

## TLDR
Low-Rank Attention Residuals (LR-AttnRes) improve large language models by using low-dimensional keys for depthwise routing, decoupling routing from residual content and reducing computational cost.

## Abstract
Attention Residuals replace the fixed residual sum with depthwise attention over previous sub-layer outputs in large language models (LLMs), but use each output as both a full-dimensional key and value. This couples routing with representation and makes depth-routing scores scale with the hidden width $d$. We propose Low-Rank Attention Residuals (LR-AttnRes), which keep full-dimensional residual values while using $r$-dimensional keys, with $r \ll d$, for routing. Projected LR-AttnRes emits learned low-rank keys from existing output projections, decoupling routing from residual content and achieving the best validation loss among the variants tested. Sliced LR-AttnRes uses the last $r$ dimensions of each value as the routing key, removing the auxiliary key-projection path and reducing residual-side FLOPs while still improving performance. Comprehensive sweeps show that depthwise routing can be effective with far fewer dimensions than the model width. We release code and models to facilitate future research.
