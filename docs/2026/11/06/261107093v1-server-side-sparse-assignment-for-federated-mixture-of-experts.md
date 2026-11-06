# Server-Side Sparse Assignment for Federated Mixture-of-Experts

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Xue Zheng, Aylin Yener
- 机构：The Ohio State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07093v1) · [PDF](https://arxiv.org/pdf/2611.07093v1)

## TLDR
**TLDR:** The paper proposes \(S^3\)-MoE, a server-side sparse expert assignment framework for federated Mixture-of-Experts that estimates client-specific expert relevance from partial observations and refines assignments via an exploit–explore mechanism, with theoretical recovery guarantees and improved accuracy under strict per-client expert-loading constraints.

## Abstract
Large language models (LLMs) are increasingly recognized for their remarkable capabilities; federated learning (FL) offers a promising framework for collaboratively fine-tuning LLMs on edge devices while achieving data privacy. However, edge devices are inherently heterogeneous: clients may exhibit diverse data distributions and resource constraints, including limited memory and computation budgets. Recent federated Mixture-of-Experts (MoE) approaches address these challenges by using sparse expert activation or partial expert loading. However, existing partial-expert methods rely on heuristic full-pool observations or prioritize system-wide load balance, without guarantees for recovering client-specific relevant experts from partial observations. We propose $S^3$-MoE, a server-side sparse expert assignment framework that estimates client-specific expert relevance from partial observations and refines assignments through an exploit--explore mechanism. We also establish relevance-estimation error and exact Top-$K$ recovery guarantees. Experiments using a CNN-based MoE on CIFAR-100 show that $S^3$-MoE recovers task-dependent client--expert preferences and reduces conflicts caused by correlated expert selection across clients. Compared with Full-20 FedAvg, which gives each client access to all 20 experts for local Top-5 routing, $S^3$-MoE achieves 1.31 percentage points higher mean final accuracy while loading only $5$ experts per client.
