# ADIndex: Layer-Adaptive Sparse Attention Indexing via Group-Level Distillation

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Jin-Fei Qi, Yiduo Li, Jiang-Xin Shi, Kan Liu, Tao Lan, Hanlin Tang, Yu-Feng Li
- 机构：Nanjing University, Alibaba Group
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.12956v1) · [PDF](https://arxiv.org/pdf/2611.12956v1)

## TLDR
ADIndex is a layer-adaptive, distillation-driven sparse-attention indexing method that uses calibrated per-layer query groups and shared token banks with lightweight distilled group indexers to reduce repeated full-prefix scans, preserving near-lossless long-context performance while achieving up to 6.22× prefill and 3.40× decoding kernel speedups and 1.54× end-to-end serving speedup.

## Abstract
DeepSeek Sparse Attention (DSA) reduces the computational cost of attention through token-level selection. However, its indexer still scores the entire causal prefix for each query, making indexing a dominant source of latency in long-context inference. Notably, the indexer alone can account for more than 50% of total prefill GPU time at long context lengths. To address this bottleneck, we propose ADIndex, an Adaptive and Distillation-driven Indexing method for token-level sparse attention. ADIndex integrates three key components: (i) a layer-wise calibration strategy that adaptively accommodates cross-query retrieval overlap, motivated by our observation of pronounced inter-layer heterogeneity; (ii) a group-level distillation scheme that leverages this heterogeneity to efficiently train adaptive layer-wise group indexers, capturing salient retrieval signals from individual queries; and (iii) a low-latency inference strategy that reduces repeated full-prefix scans through token bank sharing within query groups while retaining query-specific refinement. Experiments on DeepSeek-V3.2 and GLM-5.1 demonstrate that ADIndex preserves near-lossless task performance on LongBench, LongBench v2, and RULER while delivering substantial efficiency gains over standard DSA, including prefill and decoding kernel speedups of up to 6.22x and 3.40x, respectively, at a context length of 256K across the layer-wise reuse configurations, as well as an end-to-end serving speedup of 1.54x at a context length of 128K.
