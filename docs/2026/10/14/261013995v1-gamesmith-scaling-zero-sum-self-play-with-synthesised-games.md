# GameSmith: Scaling Zero-Sum Self-Play with Synthesised Games

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Weixian Waylon Li, Jiaxin Zhang, Han Zhou, Chengzu Li, Ke Wang, Fengxiang He, Yiwen Guo
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13995v1) · [PDF](https://arxiv.org/pdf/2610.13995v1)

## TLDR
GameSmith scales zero-sum self-play for LLM reasoning by synthesizing and verifying many game variants and training with the game-agnostic CRAB advantage estimator, raising Qwen3-4B-Base’s 13-benchmark mean pass@1 from 45.5 to 64.9.

## Abstract
Post-training large language models (LLMs) on two-player zero-sum games provides a verifiable reward, and the gains have been shown to transfer to general reasoning. Existing pipelines, however, rely on a handful of hand-written games and on advantage estimators tied to them, so both the supply of games and the advantage estimate on a large corpus limit scaling. We present GameSmith, which scales both. An LLM synthesises games inside templates whose reward, observation, and hidden-information code is fixed. Each game is verified by seed-paired replay and by an independent re-implementation of its specification, then expanded into encoding, rule, and size variants, giving 26 new games in 29 families and 336 verified variants from the three SPIRAL templates. The model is distilled from the self-play of a larger teacher (Qwen3-32B) on these games and then trained by self-play reinforcement learning with CRAB, an advantage estimator that credits each decision against a shrinkage estimate of the expected return of its position and is defined on every variant. On Qwen3-4B-Base, distillation raises the 13-benchmark mean pass@1 from 45.5 to 62.5, above the three SPIRAL games at the same budget, and self-play with CRAB reaches 64.9. The ordering holds across models, and transfer grows with the number of game families.
