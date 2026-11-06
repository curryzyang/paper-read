# LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Teresa Delgado, Hugo Hazard, Martin Benfeghoul, Jun Wang, Zafeirios Fountas
- 机构：University College London, Huawei
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07025v1) · [PDF](https://arxiv.org/pdf/2611.07025v1)

## TLDR
LowRAM is a composable test-time KV-cache compression method that uses cross-layer low-rank key compression and amortizes values by learning a per-head key-to-value predictor with sparse residuals for poorly reconstructed tokens, enabling near-lossless 4× compression, up to 5× higher decode throughput, and up to 26.9× compression when combined with quantization and eviction.

## Abstract
Autoregressive decoding relies on the KV cache, whose memory footprint grows linearly with context length and caps batch size and throughput. Existing post-training methods exploit redundancy across tokens, layers, and feature dimensions, or lower numerical precision. We identify a complementary axis: within each attention head, values are largely predictable from their corresponding keys. We exploit this with value cache amortisation, which fits a lightweight per-head predictor at test time and stores residuals only for the tokens it reconstructs worst, giving $4\times$ near-lossless value compression. The predictor can be initialised by meta-learning for substantially reduced prefill overhead, or fitted from scratch in settings that allow a one-off cost, such as multi-query inference. We pair value amortisation with cross-layer low-rank key compression to produce LowRAM, an asymmetric compression pipeline that stays close to lossless across three model families. By reconstructing only a selected subset of KV pairs at each decoding step, LowRAM can keep decoding overhead minimal and achieve up to $5\times$ higher peak decode throughput at $4\times$ compression. LowRAM further composes with quantisation and eviction, reaching $26.9\times$ compression at $94.5\%$ of baseline performance on long contexts. These results show that treating keys and values as structurally distinct enables efficient, aggressive, and composable KV cache compression.
