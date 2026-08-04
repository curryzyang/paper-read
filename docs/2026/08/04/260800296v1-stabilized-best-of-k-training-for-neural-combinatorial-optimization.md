# Stabilized Best-of-$K$ Training for Neural Combinatorial Optimization

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Melveena Jolly, Midhun Xavier
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00296v1) · [PDF](https://arxiv.org/pdf/2608.00296v1)

## TLDR
The paper proposes a "Stabilized Best-of-K" variant of Leader Reward that replaces its binary leader/non-leader weighting with a rank-based, budget-indexed signal, and shows in a controlled TSP-100 POMO study that it consistently lowers realized Best-of-8 sampling cost across three training seeds—though the gain is decoder-specific, shrinks with larger K, and comes with no claims of universal superiority.

## Abstract
Leader Reward modifies POMO training to emphasize the best trajectory produced by repeated inference. We test a narrow extension: replace its binary leader/non-leader distinction with a stabilized rank signal indexed by a sampling budget $K$. With the POMO architecture, 3,050-epoch schedule, and TSP-100 test set held fixed, the Leader Reward reimplementation obtains $7.7662$ under 100-start, 8-augmentation greedy decoding, matching the reported $7.766$ at its displayed precision. Under independent sampling, the stabilized $K=8$ recipe lowers realized Best-of-8 cost in all three paired training seeds: $7.7944$ versus $7.8136$. This observation is estimation-only and decoder-specific: three seeds are below the six-seed testing floor, Leader Reward is better at sampled $K=1$, and it remains slightly better under its original augmented-greedy protocol. We make no unbiased-estimator, universal superiority, or state-of-the-art claim.
