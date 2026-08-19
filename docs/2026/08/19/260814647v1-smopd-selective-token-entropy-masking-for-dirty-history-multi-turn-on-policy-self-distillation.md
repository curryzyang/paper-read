# SMOPD: Selective Token-Entropy Masking for Dirty-History Multi-Turn On-Policy Self-Distillation

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Chenyang Jiang, Changhan Huang
- 机构：South China Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14647v1) · [PDF](https://arxiv.org/pdf/2608.14647v1)

## TLDR
SMOPD proposes a loss-only stabilization method that masks the lowest-entropy (overconfident) tokens from the middle-turn generalized Jensen–Shannon distillation loss in dirty-history multi-turn on-policy self-distillation, consistently improving multi-turn accuracy by 1.0–2.5 percentage points across Qwen3 1.7B–8B models while adding no parameters or inference overhead, and showing that token-level entropy uncertainty is a more reliable stabilization signal than scalar final-answer correctness.

## Abstract
Dirty-history rollouts make multi-turn on-policy self-distillation (OPSD) brittle: once a student emits an erroneous intermediate reply, later turns are conditioned on that reply, and uniform distillation can spend loss on tokens that carry little corrective signal. We introduce SMOPD (Selective Masking for On-Policy Distillation), a loss-only stabilization method for multi-turn OPSD. For each generated middle-turn reply, SMOPD ranks token positions by student entropy and removes the lowest-entropy 20% from the clipped generalized Jensen-Shannon distillation loss; final-answer and FULL-preservation losses are unchanged. This design targets token-level uncertainty rather than coarse trajectory outcomes, adds no parameters, and has zero inference-time overhead. We compare SMOPD with a correctness-scaling variant that multiplies a common detached reliability proxy using final-answer correctness. On LiC with Qwen3 models, SMOPD improves SHARDED-view accuracy by 1.0-2.5 percentage points in single-seed 1.7B, 4B, and 8B comparisons, and a small 4B multi-seed check shows a +1.7pp mean SHARDED gain over baseline (two-tailed p = 0.022). Adding the outcome scalar is harmful without masking at 1.7B (-4.0pp) and remains scale-dependent when combined with masking (+1.3pp at 4B, neutral at 1.7B, and -0.5pp at 8B). These archived aggregate results suggest that token-level uncertainty is a more reliable stabilization signal than scalar final-answer correctness in this evaluated dirty-history OPSD setting, while leaving causal mechanism tests and broader benchmark validation to future work.
