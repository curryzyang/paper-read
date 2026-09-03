# hLLM: Single Pass Decoding for Generative Reranking

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Emil Laftchiev, Prachi Agrawal, Moe Kayali, Bixing Yan, Qi Xu, Zijie Lei, Chen Qiu, Zhi Hua, Ke Li, Luke Simon
- 机构：Meta Platforms, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01807v1) · [PDF](https://arxiv.org/pdf/2609.01807v1)

## TLDR
hLLM introduces a format-specialized decoding strategy that reads an item–position score matrix from the LLM's prefill hidden states and decodes all ranking ordinals in O(1) forward passes via the Hungarian algorithm, achieving a 64× speedup with ranking quality on par with an autoregressive teacher.

## Abstract
Large language models (LLMs) achieve state-of-the-art generative ranking quality, but the ranking they produce must be decoded, and autoregressive decoding spends one sequential forward pass per emitted token. We observe that the only tokens a ranker must emit are the $N$ ordinal values naming the items in ranked order, and that this narrow, permutation-structured output format admits decoding strategies which are much more efficient than left-to-right generation. We introduce hLLM (Hungarian LLM), a format-specialized decoding strategy that decodes all $N$ ordinals in $O(1)$ forward passes. hLLM reads an $N \times K$ item-position score matrix off the LLM's prefill hidden states with a lightweight self-attention head, then decodes the ordinals as the optimal bipartite assignment of that matrix via the Hungarian algorithm, yielding a valid permutation by construction rather than by repair. Through a systematic study of training signals and backbone adaptation, we show that LoRA-based fine-tuning combined with teacher ranking distillation reaches 28 ms end-to-end inference, a speed-up of $64\times$ while maintaining ranking quality on par with the teacher. We provide a complete ablation decomposing the contributions of architecture, training signal, and backbone adaptation. Our framework connects generative ranking to combinatorial optimization, opening a path toward other $O(1)$-decode mechanisms for real-time ranking.
