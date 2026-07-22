# Beyond Single-Dimensional Compression: The Compound Sparsity Frontier of Large Language Models

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Chao Han, Haozhe Hu, Xiaoyu Shen
- 机构：Eastern Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18280v1) · [PDF](https://arxiv.org/pdf/2607.18280v1)

## TLDR
This paper introduces a compound sparsity framework that combines static parameter pruning with dynamic token skipping, demonstrating that distributing compression across both dimensions delays performance degradation and achieves better trade-offs than single-mechanism compression.

## Abstract
Large language models (LLMs) are often compressed through static parameter pruning or dynamic token-level computation, yet aggressive sparsification can trigger rapid performance degradation beyond an essential sparsity boundary. This work asks \emph{whether combining these two mechanisms can delay such degradation by distributing the compression burden}. We study a minimalist compound sparsity framework that first applies low-rank approximation and channel pruning to obtain a statically compressed backbone, and then introduces lightweight routers for per-token dynamic layer skipping. This design enables independent control of parameter sparsity and token-level computation sparsity. Experiments across language understanding and modeling benchmarks show that compound sparsity consistently outperforms single-mechanism compression under the same total sparsity, delaying the decay point on understanding tasks and preserving stronger modeling performance. Further analysis reveals cross-dimensional interference between parameter pruning and token skipping, and shows that near-balanced allocation is most effective under a fixed sparsity budget. These results demonstrate that compound compression provides a practical way to improve LLM compression, while revealing a broader cross-dimensional sparsity boundary that ultimately limits further compression. Code will be available at https://github.com/EIT-NLP/LLM-Pruning.
