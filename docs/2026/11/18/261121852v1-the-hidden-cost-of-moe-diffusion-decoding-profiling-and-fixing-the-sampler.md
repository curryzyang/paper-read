# The Hidden Cost of MoE Diffusion Decoding: Profiling and Fixing the Sampler

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Harshit Samrat, Ramakrishna Paramahamsa Kompella
- 机构：Indian Institute of Technology Madras
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21852v1) · [PDF](https://arxiv.org/pdf/2611.21852v1)

## TLDR
After W4A16 quantization, the full-canvas logits/sampling pipeline—not the expert GEMMs—dominates single-user decoding of a 26B diffusion MoE because diffusion decoding processes S× more logits per output token, and the paper removes this cost with lossless/fused sampler optimizations to achieve 2.4–2.7× end-to-end speedup at unchanged accuracy.

## Abstract
Masked diffusion language models (dLLMs) decode by iteratively denoising a full canvas of tokens, so every forward pass runs a per-token sampling and stopping pipeline over the entire canvas-by-vocabulary logits tensor. We profile single-user decoding of a 26B-parameter diffusion Mixture-of-Experts model on a bandwidth-bound edge accelerator (NVIDIA GB10) and report a result that is easy to miss: after weight quantisation, this logits pipeline, not the expert GEMMs, is the single largest consumer of decode time. Unlike autoregressive decoding, where sampling touches one position's logits per committed token, diffusion decoding processes S times as many logit entries per output token, where S is the number of denoising steps. We show this pipeline is largely redundant or fusable and remove it in two lossless tiers: a bit-exact tier whose output is byte-identical to the reference decoder, and an accuracy-parity tier using a fused single-pass entropy kernel and Gumbel-max sampling. Combined with a W4A16 expert kernel, the full stack reaches 2.4-2.7 times end-to-end speedup over bf16 at unchanged benchmark accuracy on GSM8K, HumanEval, and MATH, on a single 273 GB/s device. We confirm the finding on a second, independently built diffusion MoE (LLaDA2.0-mini: pipeline 28.8% of decode, fused W4A16 3.3 times at accuracy parity) and show it disappears on a dense diffusion model (3.6%). The cost is specific to MoE diffusion, where quantisation makes the backbone cheap. Code and quantised weights are released.
