# VisHead-Spec: Head-Routed Visual Attention for Multimodal Speculative Decoding

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Xin Guo, Arushi Rai, Xiang Zhou, Qiang Zhang, Siyu Lin, Xiangjun Fan, Lizhu Zhang
- 机构：Meta Recommendation Systems (MRS)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21839v1) · [PDF](https://arxiv.org/pdf/2611.21839v1)

## TLDR
VisHead-Spec improves multimodal speculative decoding under high concurrency by routing visual attention through only a small fixed set of draft-model KV heads using top-layer target image features, thereby cutting image-token compute while preserving acceptance and increasing throughput over DSpark (16.0% vs. 9.5% at batch size 64).

## Abstract
Speculative decoding accelerates vision-language models(VLMs) while preserving the target model's outputs, but its speedup diminishes under high concurrency serving as the system becomes more compute bounded as the batch size increases. This problem is pronounced for multimodal speculative decoding as the long range of the image tokens in the prompt can significantly increase the computational cost during draft token prediction. The block-diffusion drafters (e.g. DFlash, DSpark) can effectively speed up the draft model efficiency by predicting multiple draft tokens in one forward pass, but their speedup for VLMs under high concurrency is still modest (<9%). In order to understand this gap, we examine the information flow between different modalities from target model to draft model and identify the sparsity pattern of visual attention between the target and draft models: only small set of key-value heads in the draft model need direct visual feature attention in the context and only visual features from top level layers in the target model need to be attended in the context. We therefore propose VisHead-Spec, which selects a small, fixed set of key-value (KV) heads to attend to all image features from top level layers in the target model and restricts the remaining heads to text features. On Qwen3-VL-8B and MMSpec, VisHead-Spec-8 lets 8 of the drafter's 40 KV heads read the image while keeping accepted length within 0.3% of the block-diffusion draft model baseline (i.e. DSpark). At batch size 64, its throughput gain over autoregressive decoding increases to 16.0%, compared with 9.5% for DSpark; at batch size 1, its speedup remains comparable to DSpark.
