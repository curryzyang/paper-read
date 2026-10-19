# TRACE: Transformer Residual Activation Codebook Encoding for Communication-efficient Distributed Edge Inference

- 区域：速读区
- 排名：8
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Muhammad Azlan Qazi, Alexandros Iosifidis, Qi Zhang
- 机构：Tampere University, Aarhus University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22435v1) · [PDF](https://arxiv.org/pdf/2610.22435v1)

## TLDR
TRACE is a communication-efficient distributed Transformer inference framework that places vector quantization at each layer’s post-attention residual and transmits compact codebook indices so receivers can retrieve precomputed key/value representations via table lookup, enabling communication–computation overlap and adaptive bitrate while reducing communication overhead by up to 22,624×.

## Abstract
Distributed Transformer inference across co-located edge devices is fundamentally communication-bound, as exchanging activations between sequence-parallel partitions dominates inference latency under commodity edge bandwidths. Existing compression schemes reduce this cost but retain a structural bottleneck: the received data must still undergo key/value projection before attention can proceed, serializing computation behind communication. This paper presents Transformer Residual Activation Codebook Encoding (Trace), a framework that addresses these limitations. Trace places a Vector Quantizer (VQ) at the post-attention residual of every Transformer layer and precomputes codebook-indexed key/value representations. During inference, exchanged activations are encoded into compact codebook indices, allowing receivers to directly recover keys and values through table lookup instead of executing the downstream computations required to derive them. By eliminating the received data downstream computation, Trace enables communication--computation overlap and reduces a key latency bottleneck in distributed Transformer inference. A hierarchical clustering further structures the learned codebook into a multi-resolution hierarchy, enabling runtime adaptation of the communication bitrate without retraining. The framework supports two operating variants: one prioritizing accuracy and the other balancing accuracy and efficiency through buffer-compatible quantization. Experiments on ViT-Base (ImageNet-1K and CIFAR-100) and ViViT-B (UCF-101) show that Trace achieves up to 1.89% higher accuracy and up to 1.27x end-to-end inference speedup compared with the state-of-the-art VQ-based distributed inference framework. Compared with uncompressed sequence-parallel inference, Trace reduces communication overhead by up to 22,624x.
