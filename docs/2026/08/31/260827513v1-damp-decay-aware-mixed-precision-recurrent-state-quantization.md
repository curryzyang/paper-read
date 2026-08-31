# DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization

- 区域：速读区
- 排名：6
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Tao Zhang, Jianchao Tan, Pingwei Sun, Yanqi Yu, Zixu Jiang, Yuchen Xie, Xunliang Cai, Ziqian Zeng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27513v1) · [PDF](https://arxiv.org/pdf/2608.27513v1)

## TLDR
DAMP introduces a post-training mixed-precision quantization method for recurrent states in Gated DeltaNet and Kimi Delta Attention language models that identifies high-risk channels via quantization-error energy and decay-based persistence, storing them at higher precision while keeping the rest in INT8 to preserve FP32-level accuracy at 9.9 bits per value while cutting recurrent-state storage by 69.1%, accelerating updates by up to 2.01x, and reducing full-model TPOT by up to 10.9%.

## Abstract
Softmax attention stores key and value vectors for every preceding token, causing inference memory to grow with sequence length. Recent language models incorporating Gated DeltaNet (GDN) or Kimi Delta Attention (KDA) reduce this cost by replacing the KV cache in most layers with fixed-size recurrent states. However, these recurrent states are commonly stored in FP32 and consume substantial GPU memory; their updates are memory-bandwidth bound and contribute significantly to decoding latency. To our knowledge, we are the first to study post-training quantization of recurrent states in GDN and KDA based language models. We find that uniform quantization provides a poor accuracy--storage trade-off: INT8 and FP8 already degrade accuracy on complex reasoning tasks, while INT4 and NVFP4 reduce it to near zero. We further find that most quantization-error energy is concentrated in a small subset of channels and that the relative decay strength of state channels remains stable across prompts and tasks. Motivated by these findings, DAMP uses both quantization-error energy and decay-based persistence to identify high-risk channels during offline calibration. It stores these channels at higher precision and the remainder in INT8. We evaluate DAMP on Qwen3.6-35B and Kimi-Linear-48B across six benchmarks covering mathematical reasoning, general reasoning, and code generation. At 9.9 bits per state value, DAMP maintains average accuracy close to the FP32 baseline. DAMP reduces recurrent-state storage by 69.1%, accelerates the recurrent-state update kernel by up to 2.01x, and lowers full-model TPOT by up to 10.9%.
