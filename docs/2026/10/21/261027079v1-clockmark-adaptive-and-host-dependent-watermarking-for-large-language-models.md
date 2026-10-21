# ClockMark: Adaptive and Host-Dependent Watermarking for Large Language Models

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Yupeng Qiu, Han Fang, Ee-Chien Chang
- 机构：National University of Singapore, University of Science and Technology of China
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27079v1) · [PDF](https://arxiv.org/pdf/2610.27079v1)

## TLDR
ClockMark is an adaptive, host-dependent LLM watermarking method that embeds the full payload through stateful countdown sampling guided by the model’s evolving token probabilities, provably preserving the original generation distribution while improving robustness to text editing.

## Abstract
Large language model (LLM) watermarking operates on the next-token distribution that evolves during generation. In streaming generation, each sampled token becomes part of the text and affects subsequent distributions. Embedding therefore proceeds with a changing host, unlike classical watermarking, which adapts embedding to an existing host signal. To accommodate this difference, we formulate a novel embedding framework for LLM watermarking based on two principles. We first argue that embedding should be adaptive, retaining the state of previous sampling decisions to better guide subsequent choices. We further argue that embedding should be host-dependent, using the current LLM distribution to constrain both token selection and state updates. Guided by these principles and the two requirements of distribution preservation and robustness to text editing, we propose ClockMark. It combines adaptive and host-dependent embedding with message spreading, embedding the full payload in each watermarked token. Theoretically, we prove that ClockMark preserves the original LLM sequence distribution, thereby maintaining generation quality. Empirically, extensive experiments against 12 baselines demonstrate improved robustness to text editing, with gains of up to 16.08 percentage points in bit accuracy over the strongest tested baseline.
