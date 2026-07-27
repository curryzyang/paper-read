# Ordered Action Tokens for Visuomotor Policy Learning

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Chaoqi Liu, Yue Zhao, Haonan Chen, Xiaoshen Han, Jiawei Gao, Ehsan Adeli, Yilun Du
- 机构：Harvard University, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21670v1) · [PDF](https://arxiv.org/pdf/2607.21670v1)

## TLDR
Ordered Action Tokenization (OAT) is a learned action tokenizer that satisfies three key desiderata—high compression, total decodability, and an ordered token space—by discretizing action chunks into compact, prefix-decodable token sequences that enable efficient and flexible visuomotor policy learning across diverse tasks and backbones.

## Abstract
Action tokenization maps continuous robot action chunks to discrete tokens and has become an important interface for modern visuomotor policies. Existing approaches either rely on analytical discretization methods that produce prohibitively long token sequences or learned latent tokenizers that lack structure, limiting their compatibility with downstream policies. In this work, we identify three desiderata for action tokenization - high compression, total decodability, and an ordered token space - and introduce Ordered Action Tokenization (OAT), a learned action tokenizer that satisfies all three. OAT discretizes action chunks into an ordered sequence of tokens using a transformer with registers, finite scalar quantization, and ordering-inducing training mechanisms. By training each token prefix to decode into a valid action chunk, OAT places coarse control information in early tokens and uses later tokens to refine residual detail, yielding an anytime tradeoff between inference cost and action fidelity. We validate OAT in two prevailing uses of action tokens: autoregressive policies that generate tokens for control, and token co-training policies that use token losses to shape the vision-language model context consumed by a flow-based action expert. Across three policy backbones and more than 60 tasks spanning five simulation benchmarks and real-world settings, OAT consistently delivers strong policy performance while offering significantly greater flexibility at inference time.
