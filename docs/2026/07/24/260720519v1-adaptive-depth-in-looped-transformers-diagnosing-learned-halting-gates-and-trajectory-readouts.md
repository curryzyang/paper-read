# Adaptive Depth in Looped Transformers: Diagnosing Learned Halting Gates and Trajectory Readouts

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Andrei Cristian Popescu, Haitz Sáez de Ocáriz Borde, Pietro Liò
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20519v1) · [PDF](https://arxiv.org/pdf/2607.20519v1)

## TLDR
This paper reveals that adaptive depth in looped Transformers is primarily a joint problem of trajectory formation and exit readout, not just gate learning, by showing that fixed-prior depth supervision and simple post-hoc confidence readouts often outperform jointly trained halting gates.

## Abstract
Looped Transformers increase test-time computation by repeatedly applying a shared recurrent block. Learned halting objectives in looped Transformers typically use a single exit distribution both as the inference-time stopping rule and as the training-time weighting of per-depth losses. This entangles exit selection with trajectory formation: the gate not only chooses which recurrent state to use, but also determines how strongly each intermediate state is supervised. Consequently, poor adaptive-compute performance can arise from the readout, the induced trajectory, or their interaction. We study adaptive depth in looped Transformers through this trajectory--readout lens, across controlled synthetic tasks (modular arithmetic and binary parity) and large-scale Ouro-1.4B and 2.6B checkpoints. We find that fixed-prior depth supervision, which shapes the trajectory without an input-dependent halting policy, produces difficulty-aware trajectories whose intermediate states expose useful stopping signals, and that simple post-hoc confidence readouts often match or outperform learned linear and MLP gates. Fitting gates on frozen trajectories localizes the failure: it appears to stem mainly from the trajectory induced by joint gate training rather than from limited gate expressivity. The same pattern is present in Ouro evaluations, where pretrained ponder gates are competitive but not uniformly Pareto-optimal, and measured latency confirms that the resulting reductions in average exit depth translate into practical inference-time savings. Our systematic diagnostic evaluation reframes adaptive depth in looped Transformers as a joint problem of trajectory formation and exit readout, rather than gate learning alone, highlighting a distinction that prior learned-halting work has often left implicit.
