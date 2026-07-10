# Uncertainty-gated selection for block-sparse attention

- 区域：速读区
- 排名：2
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Thomas Rossi
- 机构：Eonpass
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07724v1) · [PDF](https://arxiv.org/pdf/2607.07724v1)

## TLDR
This paper introduces an uncertainty-gated router that improves block-sparse attention by selectively doubling the kept key blocks for queries with uncertain top-k cutoffs, achieving significant recall gains and near-dense accuracy across models while maintaining efficiency.

## Abstract
Block-sparse attention scales long-context language models by replacing the O(N^2) softmax with a per-query top-k selection over key blocks. This cutoff is myopic: when the k-th and (k+1)-th blocks are nearly tied in score, the selector commits without spending extra budget, and a dropped block carrying answer evidence is unrecoverable downstream. We propose a value-of-information router that measures, for each query, how decisively the top-k cut was made, and doubles the kept set for the queries where that gap is smallest; the rule is backbone-agnostic and stacks with existing block-scoring methods such as Quest. On LongBench-v2 medium at n=215 (the entire dataset subset), router-on-Quest reaches paired recall 0.75 vs. top-k 0.47 -- +28 pp over the SSA-style baseline (McNemar p<0.01) -- and lands within 2 pp of dense on RULER NIAH multikey at the same context. The lift reproduces on four models from three architectures (Qwen2.5, Mistral-Nemo, Qwen3.6). At 128K, the router preserves 0.81 and 0.89 of dense accuracy on Qwen2.5-7B-1M and Qwen3.6 (vs. SSA-style top-k at 0.09 on the former) while the fused selection-plus-kernel pipeline runs at 0.62x and 0.80x dense wall time.
