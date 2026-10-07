# Learning to Decide, Not to Reason: Parameter-Efficient Decision Operators via Low-Rank Activation Steering

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Ran Li, Lei Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06950v1) · [PDF](https://arxiv.org/pdf/2610.06950v1)

## TLDR
DecisionSteer uses low-rank activation steering to train parameter-efficient System-1 decision operators via behavior cloning, matching or outperforming RL-based skill operators with far fewer parameters while compressing long deliberation into a few tokens without accuracy loss.

## Abstract
Injecting skills into a frozen language model currently costs a million parameters and a reinforcement-learning pipeline. We introduce \method{}, a System-1 decision operator trained by behavior cloning that lowers this cost by roughly two orders of magnitude. The default operator uses 330K parameters to match a 1.33M-parameter operator trained with reinforcement learning, exceeds or achieve comparable performance, while collapsing 3,685-token deliberation into a 6-token decision with no loss in accuracy. A rank-4 variant with 23K parameters, 1/58 of the strongest published skill operator, suffices for SearchQA and near-suffices for LiveMath, where higher rank still helps; the same recipe transfers across five tasks and three backbones, with out-of-distribution gains persisting on LiveMath problems released months after training. The gap to prior work is trainability, and it is set jointly by initialization and architecture: the initialization of prior operators zeroes the gradient of both large factor matrices at the first optimization step, whereas our zero-initialized output projection inside a shared low-rank backbone receives a gradient immediately, which a gradient-flow probe confirms directly. The gain isn't chain-of-thought compression: 23 of 57 LiveMath points beat the base model's best-of-8 sampling, and a logit-lens probe shows the operator amplifies the answer along the model's existing late-layer pathway, not writing it earlier. Gains track the base model's headroom across 13 base--task pairs, and skills compose as approximately linear operators that can be added, interpolated, and hot-swapped at inference time. Code on https://github.com/rlisml/decisionsteer.
