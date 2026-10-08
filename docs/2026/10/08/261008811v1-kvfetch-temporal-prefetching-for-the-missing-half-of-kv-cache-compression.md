# KVFetch: Temporal Prefetching for the Missing Half of KV Cache Compression

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Linfeng Dong
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08811v1) · [PDF](https://arxiv.org/pdf/2610.08811v1)

## TLDR
KVFetch is a training-free, drop-in framework that adds temporal prefetching to score-based KV cache compression, preventing sequential forgetting by recalling positional successors of evicted tokens to recover verbatim copying without extra attention cost.

## Abstract
As context windows scale to tens or hundreds of thousands of tokens, KV cache compression has become essential for efficient LLM inference. Existing methods fall into three families: score-based eviction, summary compensation, and offload-and-recall. Yet all three decide what to keep or recall by content relevance to the current query. We show this shared design is structurally incomplete. A cache supports two access modes: associative lookup by content and sequential traversal by position; current compressors implement only the first. The gap matters in practice: retrieval-augmented generation, code completion, and structured-data extraction all require the model to reproduce identifiers, field values, or code tokens verbatim from the context. Under compression, content-based eviction retains the head of such a sequence but discards its continuation, causing verbatim copying to break irreversibly midway, a failure we call sequential forgetting. This failure resists better scoring, larger budgets, summary compensation, and dynamic re-scoring; it is the dominant source of remaining quality loss under compression. We propose KVFetch, a training-free, drop-in framework that opens a temporal recall channel for any score-based compressor. It demotes evicted candidates to a quantized cold tier, detects active copying through a monotone read pointer, and prefetches positional successors into fixed-size hot-tier slots without increasing attention cost. On RULER-16K under an iso-budget control, KVFetch recovers verbatim copying from 0.8 to 78.4 and raises the 13-task average by +8.4, with gains concentrating on tasks that require sequential access. On LongBench, where no task requires sequential access, the channel remains dormant and imposes no cost.
