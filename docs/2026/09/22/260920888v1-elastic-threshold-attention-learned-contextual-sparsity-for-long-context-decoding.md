# Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding

- 区域：速读区
- 排名：11
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Themistoklis Haris, Henry Li, Maryam Karimzadehgan
- 机构：Boston University, Google
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20888v1) · [PDF](https://arxiv.org/pdf/2609.20888v1)

## TLDR
Elastic Threshold Attention (ETA) is an end-to-end trainable sparse attention method that learns query-dependent dynamic thresholds and multiplicatively suppresses sub-threshold logits rather than deleting them, enabling long-context decoding with dense-model quality and up to 2.5× faster wall-clock decoding via a block-sparse Triton kernel.

## Abstract
Massive KV caches can cause severe memory-bandwidth bottlenecks during long-context decoding. Sparse attention methods mitigate this via selective loading, but that comes at a cost: rigid heuristics drop necessary context, leading to quality degradation. We introduce \textbf{Elastic Threshold Attention (ETA)}, an end-to-end trainable architecture that achieves hardware-accelerated decoding speed without sacrificing dense model quality. ETA predicts dynamic, contextual thresholds directly from query representations, allowing the model to allocate dense-like context to difficult retrieval or reasoning steps while pruning routine tokens. To learn this policy from scratch without representation collapse, ETA \emph{multiplicatively suppresses} sub-threshold logits toward zero during training rather than deleting them. Training against this smooth uniform attention floor provides a distributed probability reservoir that \textbf{causes localized attention sinks on initial tokens to disappear}. It also enables the model to hard-prune uninformative KV blocks at inference time and absorb incidental tokens co-admitted by coarse GPU block selection. As a result, a 1.45B pretrained ETA model rivals dense attention across language modeling, commonsense reasoning, and long-context needle retrieval at $\approx 85\%$ training sparsity and $\approx 38\%$ active decode density. At inference time, we implement a custom decode kernel in Triton that screens KV blocks in $O(1)$ time using cached geometric-probabilistic bounds, delivering up to $2.5\times$ wall-clock decode speedups over FlashAttention-2 on sequences up to 512K tokens. Finally, we introduce an offline calibration algorithm for domain-specific deployments that freezes per-head constant thresholds to eliminate predictor overhead, cutting attention compute by an additional $27\%$.
