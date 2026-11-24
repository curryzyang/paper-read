# RefineKV: Query-Adaptive KV Cache Compression via Attention-Error Bounds

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Kewei Lian, Jiayi Zhai, Anji Liu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28171v1) · [PDF](https://arxiv.org/pdf/2611.28171v1)

## TLDR
RefineKV is a decoding-time query-adaptive KV cache compression method that uses an attention-output error bound combining cluster importance and distortion to selectively keep compact representatives or expand clusters, retaining near-full-attention quality while achieving up to 7.6× attention speedup and 1.66× faster decoding.

## Abstract
Repeatedly accessing the full key--value (KV) cache is a major bottleneck in long-context language model decoding. We find that small query-specific subsets can accurately approximate full attention, yet their union covers nearly the entire cache, motivating query-adaptive access for the KV cache. A natural approach is to split the KV cache into clusters, using compact representatives for clusters that incur negligible error while expanding the rest to their original KV entries. We derive a selection criterion from an upper bound on attention-output error, which reveals two complementary factors governing the error: importance measures the impact of a cluster, while distortion measures how faithfully the cluster can be represented. Based on this criterion, we propose RefineKV, a decoding-time query-adaptive KV compression method. Experiments on two models and three benchmarks demonstrate that RefineKV retains near-full-attention quality while achieving up to 7.6x speedup in the attention phase and 1.66x faster decoding, establishing a new quality-latency Pareto frontier.
