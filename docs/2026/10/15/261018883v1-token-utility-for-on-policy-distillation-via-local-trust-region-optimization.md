# Token Utility for On-Policy Distillation via Local Trust-Region Optimization

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Narayanan Sadagopan, Yilan Chen, Vijay Lingam
- 机构：UC San Diego, AWS AI Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18883v1) · [PDF](https://arxiv.org/pdf/2610.18883v1)

## TLDR
This paper derives token importance for on-policy distillation from a local KL trust-region optimization, yielding a Fisher-based utility (reverse-KL: student-weighted variance of the student–teacher log-probability ratio; forward-KL: Pearson χ²) that is instantiated as Fisher Utility Weighting and improves mathematical reasoning over uniform OPD.

## Abstract
Token-selection methods for on-policy distillation (OPD) prioritize student-visited positions using diverse signals, including uncertainty, teacher-student disagreement, and mismatch direction. We instead derive token importance from the distillation objective itself: how much can each position's loss decrease under an equal local KL budget on the student's predictive distribution? The answer is the utility $s_t=g_t^\top F_t^\dagger g_t$, where $g_t$ is the logit gradient and $F_t$ is the categorical Fisher matrix. For reverse-KL it equals the student-weighted variance of the student-teacher log-probability ratio, and for forward-KL it equals the Pearson $χ^2$ divergence, so the appropriate utility follows from the choice of objective. On shared training checkpoints, several independently motivated criteria, including student entropy, KL disagreement, and TIP, concentrate their importance on nearly the same positions as the derived utility at a 50\% selection fraction, while diverging at stricter fractions and for direction-specific criteria. We instantiate the utility as Fisher Utility Weighting (FUW), a continuous, mean-normalized token weighting. Across seven mathematical reasoning benchmarks and three Qwen3 student-teacher pairs, FUW improves over matched uniform OPD under both reverse-KL (1.35-4.0 macro points) and forward-KL (1.08-2.71 macro points), and is competitive with existing selective methods using a single closed-form score derived from the training objective.
