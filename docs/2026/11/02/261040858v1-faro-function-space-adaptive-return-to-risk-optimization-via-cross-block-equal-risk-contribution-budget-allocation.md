# FARO: Function-Space Adaptive Return-to-Risk Optimization via Cross-Block Equal-Risk-Contribution Budget Allocation

- 区域：速读区
- 排名：5
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Xiaojun Wu, Cehao Yang, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40858v1) · [PDF](https://arxiv.org/pdf/2610.40858v1)

## TLDR
FARO is a function-space adaptive optimizer that learns each parameter block’s update geometry from its realized counterfactual return and then reallocates a fixed update budget across blocks using equal-risk-contribution, matching the best hand-designed GPT training recipe and yielding small but robust loss improvements without extra time or memory.

## Abstract
Training a large language model is compute-bound, and current recipes divide the work between optimizers by hand: orthogonalized momentum for attention and MLP matrices, Adam-style updates for the rest. This division rests on human priors about which layer type deserves which geometry, and it fixes a single global update budget that every parameter block shares. We introduce FARO, a function-space adaptive optimizer that makes the partition of parameters into blocks the unit of decision. FARO gives each block a geometry by its realized counterfactual return, then freezes the routes and reallocates the frozen per-block budget by cross-block equal risk contribution (ERC), the risk-parity principle from portfolio theory. On a GPT-style model trained on FineWeb, the framework gives two results. First, its FARO-Adaptive arm reaches 3.2780 nats at the full schedule, matching NorMuonAndAdam (3.2794), the best hand-designed recipe: it recovers the human prior without hand-setting per-layer geometry. Second, FARO-ERC improves on that arm: it lowers the clean-data loss at every one of 6 seeds, by 0.0136 nats on average, a modest but robust gain. Its sign test, paired test, and confidence interval all agree, and it exceeds the measured run-to-run noise at no added time or memory. It works by trimming the riskiest blocks rather than expanding the safest, and it holds up under a corrupted stream, still lowering the mean loss and winning the seed majority. The source code is available at https://github.com/wxj630/FARO.
