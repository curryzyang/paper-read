# Format-Aware Fusion for Fast FP4 Pretraining

- 区域：速读区
- 排名：4
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Robert Hu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00053v1) · [PDF](https://arxiv.org/pdf/2610.00053v1)

## TLDR
The paper introduces **format-aware fusion**, co-designing FP4 quantization producers with their scale domains and consumer layouts to accelerate Llama-3 8B pretraining, achieving up to **37.9K tokens/s/GPU** while keeping training loss competitive with bfloat16.

## Abstract
Four-bit floating-point (FP4) Tensor Cores accelerate matrix multiplication, but scale computation, operand packing, layout construction, and saved backward state can erase the gain. We present \emph{format-aware fusion}, which co-designs each quantization producer with its scale domain and consumer layout for native \mxfp{}, global \nvfp{}, and cooperative-thread-array-local \nvfp{}. We evaluate Llama-3-family 8B pretraining through 160 billion tokens using bfloat16 output projections and compiled cross entropy. In matched same-accelerator probes, bfloat16 and Transformer Engine \nvfp{} reach 18.8K and 27.6K tokens/s/GPU, while our fastest custom route reaches 37.9K. \mxfp{} with row-gradient stochastic rounding and fixed-sign 32-value Hadamard weight-gradient preconditioning reaches 37.2K tokens/s/GPU (86.3\% bfloat16 model FLOP utilization) and ends 2.11\% above the raw bfloat16 training-loss endpoint. A Transformer Engine recipe with four final bfloat16 blocks ends 0.87\% above bfloat16 at 27.1K tokens/s/GPU. Downstream rankings differ from training-loss rankings, showing that FP4 outcomes depend jointly on scale contract, operand, and execution path.
