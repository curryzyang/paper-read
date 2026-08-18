# The Integer Alibi: Localizing Cross-Kernel Divergence in INT8-Quantized LLM Inference

- 区域：速读区
- 排名：15
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Teng-Ruei Chen
- 机构：Krixvon
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13756v1) · [PDF](https://arxiv.org/pdf/2608.13756v1)

## TLDR
Swapping between CUTLASS and Triton INT8 GEMM kernels in vLLM causes bit-level divergence across all tested sequences, but since the INT32 accumulator is exact and order-independent, the divergence is localized to scale application and output rounding—and can be eliminated by using power-of-two scales.

## Abstract
Two GPU kernels implementing the same scaled INT8 GEMM interface are usually treated as interchangeable. We test that assumption: holding the checkpoint, prompts, hardware, inference engine, decoding, and quantization configuration fixed, we swap only the INT8 linear kernel (CUTLASS versus Triton) inside vLLM. At 1.7B each arm reproduces itself bit-for-bit across cold restarts, yet the arms agree on no sequence in any end-to-end comparison we ran (0/8, 0/16, and 0/64). What makes this more than a benchmark discrepancy is an integer alibi: for shared INT8 operands under a verified no-overflow bound, the INT32 dot product is exact and order-independent, so the accumulator cannot be the source of any difference. Feeding both kernels identical operands from every linear layer of Qwen3-1.7B and 8B (196 and 252 layers), we find bit-identical outputs under power-of-two scales, confirming a pinned prediction list 196/196 and 252/252 (pre-registered at 1.7B, pinned but not blind at 8B), and observed differences of at most one bfloat16 spacing under the checkpoints' real scales. This localizes the divergence to scale application and output rounding after the exact accumulator. Applied as a probe checkpoint, the same intervention restores end-to-end bitwise agreement (8/8 and 16/16 sequences). Cross-implementation FP8 GEMM shows a different signature: both the prevalence and the magnitude of differences grow with reduction depth, while the INT8 fraction stays at parts per million and within one spacing over a 64x range of K. Teacher-forced replay ties layers to tokens: flips concentrate at small logit margins, which predict flip risk with ROC-AUC 0.94 on 16,384 positions. We will release the pre-registration, per-layer predictions, manifests with kernel-selection evidence, and a conformance procedure that turns these controls into a concrete check for kernel interchangeability.
