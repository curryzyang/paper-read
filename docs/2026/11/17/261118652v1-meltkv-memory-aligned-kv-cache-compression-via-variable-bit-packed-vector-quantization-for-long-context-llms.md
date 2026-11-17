# MeltKV: Memory-Aligned KV Cache Compression via Variable-Bit Packed Vector Quantization for Long-Context LLMs

- 区域：速读区
- 排名：9
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Jiyun Han, Seongjoon Cho, Seungkyu Choi
- 机构：Yonsei University, Kyung Hee University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18652v1) · [PDF](https://arxiv.org/pdf/2611.18652v1)

## TLDR
MeltKV is a memory- and latency-optimized KV-cache vector-quantization framework for long-context LLMs that uses memory-aligned variable-bit index packing and head-wise codebook sharing to achieve sub-4-bit (down to 1-bit) compression with 48.1% lower memory and 52.9% lower latency than state-of-the-art VQ methods at comparable perplexity.

## Abstract
Large Language Models (LLMs) increasingly rely on long contexts, making Key-Value (KV) caches dominate memory usage and inference latency. Existing vector quantization (VQ) methods effectively compress KV caches to sub-4-bit levels but often overlook inefficiencies in memory alignment and decoding speed. This work introduces MeltKV, a memory-latency co-optimized KV cache quantization framework for long-context LLM serving. MeltKV employs a memory-aligned variable-bit index packing scheme that adaptively assigns bit-widths to grouped key channels and compactly stores indices within standard data-types, eliminating redundant bits. Additionally, head-wise codebook sharing reduces the total codebook size while maintaining accuracy. Experiments demonstrate that MeltKV effectively compresses KV representations to sub-4-bit levels down to 1 bit and, at comparable perplexity, achieves 48.1% lower memory usage and 52.9% lower latency than state-of-the-art VQ methods.
