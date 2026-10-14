# DoSA: Dots Sparse Attention

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Fanxu Meng, Taosong Fang
- 机构：Xiaohongshu Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13990v1) · [PDF](https://arxiv.org/pdf/2610.13990v1)

## TLDR
DoSA is a lossless sparse-attention method that uses seed-threshold certificates and per-head upper/lower bounds to skip full scoring for tokens provably outside Top-K, preserving exact selection while accelerating the indexer by up to 2.74× and time-to-first-token by up to 1.94×.

## Abstract
Sparse attention visits few keys, yet finding them can still require scoring every key with every indexer head. We introduce DoSA (Dots Sparse Attention), a lossless method for making this computation conditional while preserving exact token selection. Its central observation is that Top-K selection requires sufficient evidence to reject a candidate, not necessarily its full score. A seed set supplies a lower bound on the winning threshold. Nonnegative head projections and joint residual bounds upper-bound positive contributions, while activation-informed aggregation bounds the magnitude subtracted by negative heads. The certificate directs full scoring toward candidates that remain eligible; exact-score filtering further reduces writeback and selection work. We establish the certificate and its exact-selection conditions, and analyze how geometry and selection margins govern its effectiveness. Our GPU implementation accelerates the complete Indexer by up to 2.74 times over SGLang and 1.69 times over LiteTopK across English, Chinese, and code workloads. End-to-end evaluation on GLM-5.2 and DeepSeek-V3.2 achieves up to 1.94 times and 1.50 times time-to-first-token speedups over the two baselines, respectively.
