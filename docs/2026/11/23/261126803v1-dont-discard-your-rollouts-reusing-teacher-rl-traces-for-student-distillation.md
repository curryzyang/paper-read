# Don't Discard Your Rollouts: Reusing Teacher RL Traces for Student Distillation

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Vashisth Tiwari, Emma Strubell, J. Zico Kolter
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26803v1) · [PDF](https://arxiv.org/pdf/2611.26803v1)

## TLDR
The paper shows that teacher RL rollouts can be effectively reused for student distillation by selecting data with GRPO metadata—using easy all-correct prompts for an SFT warm start, then mixed-success prompts for DPO ordered by difficulty, and choosing completions via cached teacher log-likelihoods—matching canonical distillation without extra generation cost.

## Abstract
RL post-training methods such as PPO and GRPO are computationally expensive, with substantial resources devoted to sampling rollouts, which contain multiple completions per prompt along with their respective rewards. Canonical distillation, however, discards these traces and uses more compute to regenerate data from the final teacher. We ask if and how we can reuse the saved teacher RL rollouts to distil student models. Reusing rollouts is non-trivial: naive SFT on the rollouts underperforms canonical distillation, and naive DPO, while performant, is unstable, collapsing on weaker students. We show that treating rollout reuse as a data selection problem using metadata already recorded during GRPO substantially reduces this gap. We use prompt pass rates to order the data, using the easiest prompts for an SFT warm start prior to using mixed-success prompts for DPO. For each prompt, we use saved teacher log-likelihoods as a proxy for selecting student-compatible completions. Across mathematical reasoning and Python coding tasks, with students from multiple model families, our two-stage recipe achieves comparable average performance to canonical distillation, while incurring no additional inference cost for dataset construction.
