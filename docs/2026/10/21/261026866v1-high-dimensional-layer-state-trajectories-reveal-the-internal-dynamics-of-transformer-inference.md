# High-dimensional layer-state trajectories reveal the internal dynamics of transformer inference

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Heng Zhao, Yufei Wang, Ruidian Song, Weisheng Chen
- 机构：China Mobile Communications Group Co., Ltd., Sinotrans Logistics Co., Ltd., China Innovation Center of Roche (CICoR), Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26866v1) · [PDF](https://arxiv.org/pdf/2610.26866v1)

## TLDR
Treating ordered layer-state trajectories as the empirical object, the paper shows that transformer inference follows an architecture-compatible, geodesic-biased competitive flow whose layer order is behaviorally consequential and can be selectively steered by local transition actuators and confidence gating without altering non-closure predictions.

## Abstract
Mechanistic studies of large language models localize function in parameters, attention heads or neurons, but those parts do not specify how one inference unfolds. We treat the ordered layer-state trajectory as the empirical process and test whether layer order defines a measurable computation. Across representative Qwen, Llama and Gemma checkpoints, realized order produced paths 1.60--2.24 times as aligned with their endpoint chord as endpoint-preserving shuffles. The order effect transferred to a lexical task, but was stronger in three random initializations of the same Qwen architecture, identifying an architecture-compatible scaffold rather than a training-specific law. Direct hidden states provided stronger mechanism coordinates than vocabulary readbacks, and a task-defined coordinate made candidate competition computable. After additive interventions failed, local transition actuators selectively controlled internal trajectories across checkpoints. A confidence gate then drove 17 of 87 held-out Qwen closure trajectories across the full-vocabulary top-1 candidate boundary while leaving all 203 non-closure top-1 outputs unchanged. Safety-matched action reassignment performed similarly, locating the gain in selective gating and the bounded actuator family rather than fine-grained dose assignment. Layer order exposes an observable, computable and behaviourally consequential process of transformer inference without establishing a complete theory of LLM dynamics or control of answer correctness.
