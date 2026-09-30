# HeadGuard: Selective Head Protection for Low-Bit VLM KV-Cache Quantization

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Nenad Banfic
- 机构：Microsoft
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35800v1) · [PDF](https://arxiv.org/pdf/2609.35800v1)

## TLDR
HeadGuard improves low-bit VLM KV-cache quantization by using offline image- and output-sensitivity scores to keep about 1/8 of physical KV heads’ image keys (and optionally values) in BF16 while the base quantizer handles the rest, substantially recovering accuracy across eight VLMs, three quantizers, and eight benchmarks without replacing the underlying quantizer.

## Abstract
Low-bit key-value (KV) cache quantization saves storage but can sharply degrade vision-language model (VLM) accuracy. We introduce HeadGuard, a composable head-protection method that augments a base KV-cache quantizer with a fixed high-precision mask. Image-sensitivity and output-sensitivity scores select physical KV heads offline, with approximately 1/8 protected in the main experiments; their image keys and optionally values remain in bfloat16 (BF16), while the base quantizes unprotected image entries. Across eight VLMs, three base quantizers, and eight benchmarks (six discriminative and two generative), HeadGuard recovers a substantial fraction of lost accuracy on weaker quantizers, with the strongest gains for Qwen and InternVL. At 2 bits, the six-task discriminative mean over eight models rises from 0.436 to 0.580 on the weakest base; protection can also improve generated answers and caption fidelity to BF16 outputs. Mean accuracy gains persist across all three quantizers with both tested calibration datasets. Keys-only protection retains substantial recovery at lower modeled storage cost. Evaluated through simulated quantization, HeadGuard offers a composable way to improve low-bit VLM accuracy without replacing the underlying quantizer.
