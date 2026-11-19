# Optimize the Cob, Then the Kernel: Optimizing Beam Search for Generative Recommendation Inference

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Shing Wai Pun, Kai Wu, Pengfei Xia, Hui Zang, Wei Guo, Yong Liu
- 机构：Huawei Technologies Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23339v1) · [PDF](https://arxiv.org/pdf/2611.23339v1)

## TLDR
By holistically optimizing the beam search inference pipeline with Tree Attention, static KV cache allocation, pre-generated masks, graph compilation, and operator fusion before resorting to custom kernels, the paper achieves up to 25× lower end-to-end latency than vLLM on Ascend NPUs while matching custom-kernel performance, demonstrating that system-level pipeline optimization should precede kernel-level development for generative recommendation.

## Abstract
Generative recommendation (GR) inference differs substantially from conventional LLM serving, featuring long input sequences, wide beam search, and only a few fixed output tokens. Existing LLM serving engines such as vLLM process beams as batched independent sequences, causing redundant KV cache accesses over the shared prompt prefix. Furthermore, vLLM executes each beam search generation step as a separate engine invocation, incurring host-side beam processing overhead between decoding steps and substantial runtime KV block management in PagedAttention. Using Tree Attention, we concatenate beams along the sequence dimension to eliminate redundant KV accesses, and further optimize execution through pre-generated partial-attention masks, static KV cache allocation, loop-unrolled generation dispatch, TorchAir graph compilation, automatic operator fusion, and vocabulary-constrained decoding. Without the use of custom kernels, our approach reduces end-to-end latency by up to 25x over vLLM on Ascend NPUs, and achieves generation latency comparable to a SOTA solution using custom kernels, showing that the generation pipeline should be optimized holistically before resorting to custom kernel development.
