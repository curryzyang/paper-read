# Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Weiye Shi, Fanxu Meng, Muhan Zhang
- 机构：Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27269v1) · [PDF](https://arxiv.org/pdf/2607.27269v1)

## TLDR
Converted MHA/GQA-to-MLA models make poor speculative-decoding drafters because low-rank and RoPE approximation errors hurt token acceptance, so this paper proposes a converter-agnostic, training-time functional reconstruction that optimizes converted MLA attention modules to reproduce the original attention blocks' outputs on calibration states, improving draft acceptance across 37 of 64 matched configurations.

## Abstract
Multi-head latent attention (MLA) is increasingly important for long-context LLM inference because compact latent states replace the growing key-value (KV) cache and reduce decoding memory traffic. Yet most capable open checkpoints use multi-head or grouped-query attention (MHA/GQA), so conversion is needed to obtain MLA's cache efficiency without retraining from scratch. Speculative decoding offers complementary acceleration, but its speedup depends on agreement between draft proposals and target verification. We find that direct MHA/GQA-to-MLA conversion can sharply reduce this agreement: low-rank factorization and RoPE handling introduce attention-function errors that may be tolerable for standalone generation but substantially lower draft-token acceptance. We therefore formulate MLA draft construction as functional reconstruction rather than cache compression. Our end-to-end (E2E) method optimizes each converted MLA attention module to reproduce the post-output-projection response of its original MHA/GQA counterpart on calibration hidden states. This converter-agnostic post-conversion procedure preserves the converted cache and inference graph and requires neither verifier logits nor verifier supervision. We evaluate 192 model-converter-backend-method-task configurations spanning four Llama/Qwen draft-target pairs, TransMLA and MHA2MLA, HF and vLLM, and four 200-prompt tasks. With a 0.5-percentage-point reporting tolerance, Functional Reconstruction materially improves acceptance in 37 of 64 matched task cells, leaves 26 practically unchanged, and materially decreases one. Code and evaluation artifacts are available at https://github.com/swyhahaha/FunctionalMLA.
