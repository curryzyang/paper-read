# MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Minsang Kim, Seungjun Baek
- 机构：SK Telecom, Korea University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30206v1) · [PDF](https://arxiv.org/pdf/2610.30206v1)

## TLDR
MoEZip is a routing-aware KV cache compression method for sparse MoE LLMs that combines attention weights with a Fisher-information-based routing-fragility score to preserve expert selection during cache eviction, achieving large performance gains under aggressive compression such as 10% KV retention.

## Abstract
Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token. However, in long-context inference, memory remains a major bottleneck because the KV cache grows linearly with sequence length. Existing KV cache compression methods reduce this cost for dense transformers, but overlook a problem specific to MoE: KV eviction can change which experts are selected during answer generation, degrading the generation quality. We propose MoEZip, a routing-aware KV cache compression for sparse MoE language models. To estimate the sensitivity of expert routing to perturbation, we propose a novel metric based on the Fisher information matrix of routing distributions. MoEZip combines this metric with attention weights for routing-aware scoring of contexts. Finally, we compose a complementary scoring system that combines eviction methods for dense and sparse-MoE architectures. Experiments show that MoEZip achieves robust performance under aggressive cache compression on various benchmarks. At a KV retention ratio of 10\%, MoEZip improves over the SoTA baseline by +24 and +20 points on average on LongBench and RULER, corresponding to 2.3$\times$ and 4.9$\times$ higher scores, respectively.
