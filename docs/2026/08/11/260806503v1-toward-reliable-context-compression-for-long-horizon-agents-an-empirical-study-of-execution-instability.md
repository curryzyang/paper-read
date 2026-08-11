# Toward Reliable Context Compression for Long-Horizon Agents: An Empirical Study of Execution Instability

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Guanghui Min, Liang Wu, Mayank Darbari, Chen Chen, Liangjie Hong
- 机构：University of Virginia, Nokia
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06503v1) · [PDF](https://arxiv.org/pdf/2608.06503v1)

## TLDR
TRACE is a verifier-guided framework that improves reliable context compression for long-horizon agents by evaluating individual compaction events through paired closed-loop continuations, addressing compression-induced execution instability and outperforming existing baselines on AppWorld.

## Abstract
Recurrent context compression controls context growth in long-horizon agents, but its behavioral effects remain poorly understood. In this preliminary empirical study, we show that compression can weaken the influence of recent interactions, increasing blocked actions, repeated exploration, and instability across runs. Motivated by these observations, we introduce TRACE, a verifier-guided framework that evaluates individual compaction events through paired closed-loop continuations from the same environment state and uses summary preferences to optimize a natural-language compression prompt while keeping all models frozen. Initial results on AppWorld show improvements over existing compression baselines in task performance, multi-run reliability, and context--execution efficiency. These findings provide early evidence for boundary-local evaluation as a promising direction for reliable agent context compression.
