# AttSVD:Prompt-Adaptive Low-Rank KV Cache Compression via Attention-Guided SVD

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Sara Abdali, Jongwoo Ko, Pashmina Cameron
- 机构：Microsoft
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06927v1) · [PDF](https://arxiv.org/pdf/2610.06927v1)

## TLDR
AttSVD is a training-free, prompt-adaptive KV-cache compression method that keeps all tokens but stores them as attention-guided low-rank SVD factors along the feature axis, matching dense-cache performance while using up to 50% of the KV-cache memory.

## Abstract
The key-value (KV) cache of autoregressive transformers grows linearly with context length and dominates memory at long context. Most training-free remedies evict low-importance tokens, an irreversible choice along the sequence axis. We instead keep every token and store it more cheaply along the "feature" axis. We therefore propose AttSVD, a new "interpretable" low-rank compression whose basis is derived from each prompt's own attention geometry: an online, per-prompt truncated SVD that keeps only the directions attention actually reads, cutting persistent per-head KV memory in proportion to the retained rank. We propose two decode-time caching strategies, accumulating and streaming, for short and long generation regimes. Furthermore, we propose two refinements that make compression adaptive. A per-matrix energy rule sizes the logit space and the attention mass independently. An attention-aware basis truncates only in the spaces attention actually reads, preserving both the attention logits and the attention output. The same factors also provide free, per-head interpretability insights into the effective rank and the geometry attention consumes. Across multiple models, on both an agentic benchmark and the full LongBench suite AttSVD stays on par with the dense cache while using up to 50% of the KV-cache memory.
