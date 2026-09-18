# Block Parallelism For Efficient Distributed Long-Context Diffusion Language Model Training

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Tarun Suresh, Pranshu Chaturvedi, Hangoo Kang, Parth Shroff, Ishan S. Khare, Hermann Kumbong, Azalia Mirhoseini
- 机构：Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19242v1) · [PDF](https://arxiv.org/pdf/2609.19242v1)

## TLDR
The paper introduces block parallelism (BP) and context-sharded block parallelism (CSBP) for distributed long-context block diffusion language model training, assigning corrupted-block computation to separate ranks while sharding the shared clean context to keep block-specific K/V and gradients local, yielding up to 1.61× faster full-model training at 512K and 7.59× faster speculative-decoder training at 1M with equal or lower memory.

## Abstract
Block diffusion language models (BDLMs) combine autoregressive dependencies across blocks with parallel denoising within blocks, but long-context training is constrained by distributed attention communication and activation memory. Conventional context parallelism (CP) shards the combined clean-plus-corrupted sequence by position, communicating shared clean K/V together with block-specific corrupted K/V and their gradients. We observe that the BDLM objective separates over target blocks. We introduce block parallelism (BP), a new distributed parallelism dimension that assigns each corrupted-block computation to one rank. To scale BP to long contexts, we introduce context-sharded block parallelism (CSBP), which also shards the shared clean sequence across those ranks. CSBP keeps corrupted K/V and gradients local, avoids replicated clean prefixes, and preserves BDLM training semantics. On 16 H200 GPUs at 256K context, CSBP improves throughput over the best baseline by 1.18-1.45x for supervised fine-tuning and 1.27-1.33x for conversion of autoregressive models to BDLMs, while matching or reducing peak HBM. Full-model speedup reaches 1.61x at 512K. On eight H100 GPUs, CSBP accelerates DFlash2 speculative-decoder training by 2.48x at 512K and 7.59x at 1M. In matched 12-hour DiffusionGemma 26B-A4B SFT runs, CSBP achieves higher pass rates at every trained checkpoint on SWE-bench Verified and Terminal-Bench Lite. Code: https://github.com/ScalingIntelligence/Turbo-dLLM
