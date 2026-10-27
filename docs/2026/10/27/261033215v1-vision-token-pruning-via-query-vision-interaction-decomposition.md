# Vision Token Pruning via Query-Vision Interaction Decomposition

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Harshithanjani Athi, Sravan Kumar Ankireddy, Jianzhong Charlie Zhang, Hyeji Kim
- 机构：The University of Texas at Austin, Samsung Research America
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33215v1) · [PDF](https://arxiv.org/pdf/2610.33215v1)

## TLDR
QViD is a training-free, query-aware visual token pruning method that exploits the low-rank structure of the query–vision interaction matrix—computed from transformer query/key projections and decomposed via SVD—to retain visual tokens most aligned with dominant query-relevant interaction modes, improving VLM efficiency and performance under token budgets.

## Abstract
Large vision-language models (VLMs), which process both visual inputs and text queries, incur high inference costs due to the large number of visual tokens, making visual token pruning a natural approach for improving efficiency. Recent work has leveraged query information to guide token selection, often through heuristics derived from attention patterns or token dynamics. However, these approaches do not explicitly exploit the underlying structure of query-vision interactions. We address this gap by observing that the query-vision interaction matrix, naturally induced by the query and key projections already present in transformer attention, is effectively low-rank, with a small number of dominant latent interaction modes capturing query-relevant semantics. Motivated by this observation, we propose Query-Vision Decomposition (QViD), a novel training-free query-aware visual token pruning method that exploits this structure. Extensive experiments on both image and video understanding benchmarks show that QViD consistently improves performance under matched token budgets, with the largest gains appearing under aggressive compression regimes.
