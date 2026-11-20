# A Model of Diverse Sampling from Language Models

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Manuel Prada-Corral, Yahya Emara, Timothy J. O'Donnell, Ryan Cotterell, Tim Vieira
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25003v1) · [PDF](https://arxiv.org/pdf/2611.25003v1)

## TLDR
The paper proposes PoolDPP, a tractable finite-pool importance-weighted K-DPP sampler (with a greedy MAP variant) for diverse language-model generation that provably approaches the target K-DPP as pool size grows and improves quality–diversity and precision–recall trade-offs on open-ended generation, text-to-SQL, and mathematical reasoning.

## Abstract
Language models often produce high-quality individual samples but poor sets, with repeated samples clustering around the same semantic modes. We formalize diverse generation as sampling a size-$K$ subset of complete strings from a determinantal point process (DPP), where the likelihood encodes item quality, and the embedding geometry encodes repulsion between similar outputs. Exact inference over all strings is intractable, so we propose PoolDPP: draw a finite candidate pool from a tractable proposal, importance-weight the candidates toward the target quality, and run a $K$-DPP sampler on the induced pool kernel; a greedy MAP variant provides deterministic selection. We prove a finite-sample bound with an explicit constant: the KL divergence between the sampler's output and the target $K$-DPP decays as O(1/N) in the pool size. Empirically, PoolDPP extends the quality--diversity frontier on open-ended generation and the precision--recall frontier on ambiguous text-to-SQL (Ambrosia), and on mathematical reasoning (GSM8K), it raises diversity at about the same pass@$K$.
