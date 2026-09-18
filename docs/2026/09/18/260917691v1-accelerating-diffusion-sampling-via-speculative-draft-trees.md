# Accelerating Diffusion Sampling via Speculative Draft Trees

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Marcello Bullo, Yanxiao Liu, Öykü Sıla Güner, Arpan Mukherjee, Deniz Gündüz
- 机构：Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17691v1) · [PDF](https://arxiv.org/pdf/2609.17691v1)

## TLDR
By connecting speculative diffusion sampling to relative entropy coding, this paper proposes speculative draft trees with greedy rejection sampling to replace linear draft chains, improving acceptance rates and accelerating exact diffusion sampling by up to 8.3% over reflection-coupling baselines.

## Abstract
Speculative sampling accelerates diffusion model generation by drafting inexpensive candidate states and correcting them under a coupling that preserves the target distribution exactly, reducing the number of expensive target evaluations. Existing diffusion samplers, notably those based on reflection maximal coupling, are topologically constrained: their lookahead drafts form a chain graph, a single linear sequence, which inherently limits the acceptance rate per target evaluation. We connect speculative sampling in diffusion models to relative entropy coding (REC). This perspective shows the lookahead need not be linear and motivates our central contribution, draft trees, which enrich the candidates considered per round and lower the target function evaluations. We further adopt greedy rejection sampling, an REC algorithm, as the draft-target coupling, improving acceptance while guaranteeing exact target samples. Experiments across diverse target and draft models demonstrate up to 8.3% acceleration over the reflection coupling baseline in practical settings.
