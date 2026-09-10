# Scaling Post-Training Ternarisation to Qwen3-8B Capability Retention, Reproduction, Lossless Packing, and Packed Execution

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Anirudh Malik, M Sparsh Mehra, Poojith Devan
- 机构：OneBit AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09240v1) · [PDF](https://arxiv.org/pdf/2609.09240v1)

## TLDR
This paper scales an existing post-training ternary conversion pipeline from Qwen3-4B to Qwen3-8B, showing improved capability retention at larger scale, lossless lattice-aware packing to 8.24 GiB, and feasible direct packed execution at 15.52 tokens/s, while identifying kernel optimization as the remaining bottleneck.

## Abstract
Ultra-low-bit language models promise reductions in storage and memory traffic, but a nominal "1.58-bit" label does not specify the deployed representation or its execution cost. We study a scale-up of an aggressive post-training conversion pipeline from Qwen3-4B to Qwen3-8B.
  The conversion uses KOTMS rotation, E2M-ATQ adaptive ternarisation, and GPTQ-style error compensation in a weight-only A16 configuration. We do not claim these algorithms as new. Our contribution is the end-to-end scale-up characterisation: an external reproduction gate, matched 4B/8B capability analysis, cross-corpus perplexity, effective-bit accounting, lossless lattice-aware packing, and direct packed execution.
  The 8B model reaches a three-corpus perplexity ratio of 1.361x, with WikiText-2, C4, and PTB ratios of 1.318x, 1.393x, and 1.371x. On eight zero-shot tasks at n = 500, mean accuracy is 64.6% versus 72.4% for FP16, corresponding to 78.5% chance-corrected retention and a 7.8-point absolute cost. The matched 4B run retains 69.6%, yielding an 8.9-point 8B advantage.
  The packed checkpoint is 8.24 GiB and preserves the recorded perplexity to measurement precision. Direct packed execution reaches 15.52 tokens/s in 7.35 GiB, while a preliminary packed GEMV remains slower than FP16 cuBLAS. The result is a validated scale-up baseline: model size improves robustness to aggressive post-training discretisation, actual serialisation is solved for the measured artefact, and direct execution is feasible, while broader seeds, calibration distributions, and kernel optimisation remain open.
