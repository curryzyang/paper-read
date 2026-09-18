# Fathom: Per-Query Read Depth for Sparse Decoding over Offloaded KV Caches

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Vivek Kalyanarangan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17652v1) · [PDF](https://arxiv.org/pdf/2609.17652v1)

## TLDR
Fathom is a per-query, bit-plane-based key-scanning method for sparse decoding over offloaded KV caches that adaptively reads only the needed bits per key channel, yielding up to 1.67× faster GPU decoding at million-token contexts while maintaining comparable or better accuracy at lower byte traffic.

## Abstract
When agentic sessions run to a million tokens with many sessions resident at once, the KV cache and the index that ranks it live in host memory, and the scan that ranks all n keys for a top-k step becomes the traffic that bounds decoding. We present Fathom, a key scan in which each query decides how many bits of each key channel to read. The 4-bit K cache is stored channel-major as bit planes, so a prefix of t planes is exactly the channel's t-bit quantizer, and the query spends its bit budget by reverse water-filling over the variance-weighted importance of its channels. At one million tokens on Qwen3-8B a decode step is 1.67x faster in GPU time than with the 136-bit scans of Double Sparsity, Loki and SparQ r=32, and in the same GPU time as SparQ's 68-bit read (r=16) Fathom reads 18% fewer bytes with lower attention error on six of seven model and context settings. On RULER-style tasks every per-token scan matches exact top-k decoding, and on real coding-agent sessions Fathom reaches the step agreement of the most accurate 136-bit scan at 92 bits. The store is the 4-bit K copy a quantized serving stack already holds, and the method is not faster when the index is resident in GPU memory.
