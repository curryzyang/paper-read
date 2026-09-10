# Identifying Habit, Physics, and Nuisance in Robot World Models

- 区域：速读区
- 排名：3
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jinting Hang, Zhenhui Cai
- 机构：Harvest Praxis
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09210v1) · [PDF](https://arxiv.org/pdf/2609.09210v1)

## TLDR
This paper proposes a structural causal model that disentangles operator habit, shared physics, and observation nuisance in robot world models, and shows that freezing the learned physics while adapting only a thin policy/interface improves low-shot transfer and preserves cleaner dynamics across StackCube, DROID, and RH20T.

## Abstract
Teleoperated demonstrations are often multimodal even when the underlying dynamics are nearly deterministic given the executed action. We argue that this multimodality typically mixes three factors--operator habit in action selection, shared physics, and observation nuisance--and that entangled next-observation predictors absorb all three. We formalize the split with a structural causal model a=g(h,z,u), z'=f(z,a), o=r(z,c), and test it with complementary interventions: replacing or shuffling actions at fixed state sharply increases next-state error, whereas appearance and camera changes should not; habit-aware reverse scoring improves ranking of feasible pasts without rewriting the dynamics. The associated adaptation rule is to freeze a shared physics readout and update only a thin interface. On StackCube, DROID, and RH20T this rule improves low-shot transfer relative to training from scratch, retains cleaner dynamics under corrupted adaptation data, and extends from proprioception to pixel observations with multi-view and multi-step checks. We do not equate latent actions with operator habit, and we do not target large-scale video generation benchmarks.
