# Dynamic Influence-Weighted Distillation for Single-IMU Activity Recognition

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Bingxuan Xie
- 机构：South China Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24904v1) · [PDF](https://arxiv.org/pdf/2608.24904v1)

## TLDR
TLDR: This paper introduces dynamic influence weighting (DIW), a per-sample adaptive gating of logit and feature distillation losses that allows a single right-arm IMU student to outperform supervised and fixed-weight knowledge distillation by leveraging a four-IMU teacher during training only, achieving substantial macro-F1 gains on the WEAR dataset.

## Abstract
Inertial sensors at multiple body locations can improve activity recognition, but requiring every sensor at inference increases the deployment burden. We study whether four synchronized IMUs available during training can improve a student that uses only the right-arm IMU during fitting and inference. A frozen four-IMU teacher provides logit and feature targets. Fixed-weight knowledge distillation applies each target with the same strength to every fitting sample, although the student may not benefit equally from them. We introduce dynamic influence weighting (DIW), which tests a one-step candidate update on separate fold-internal training participants. DIW then assigns separate sample-wise gates to the logit and feature losses. On WEAR, we evaluate 19 labels and 68,298 complete windows from 22 participants using subject-disjoint five-fold cross-validation. Pooled out-of-fold macro-F1 is 0.561820 for Supervised and 0.571623 for Fixed-weight KD. DIW reaches 0.638451, gains of 7.66 and 6.68 percentage points, respectively. It exceeds Supervised for 18 of 19 labels and 21 of 22 held-out participants. All three routes retain the same 80,915-parameter right-arm student at inference. Under this protocol, DIW converts training-only multi-position information into a stronger single-IMU model without changing deployed sensing or the student forward graph.
