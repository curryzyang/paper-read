# Quantize, Qualify, Rerank: A Recipe for Compressing LLMs Without Losing Quality

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Thamme Gowda
- 机构：Microsoft
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18587v1) · [PDF](https://arxiv.org/pdf/2611.18587v1)

## TLDR
The paper presents a metric-qualified compression recipe for Gemma-3-12B translation that removes unused vision/vocabulary components, uses int8/fp8 quantization without resolved quality loss, avoids int4 residual loss and overfitting QLoRA healing, and applies best-of-4 reranking to stay competitive with bf16.

## Abstract
Compressing large language models lowers serving cost, but a single automatic metric may miss quality loss. For the WMT26 Model Compression constrained track, we compress google/gemma-3-12b-it (24.4 GB in bf16) for three translation directions on one H100. Paired bootstrap analysis exposes metric disagreement on 4-bit quantization; guided by WMT24 human meta-evaluation, we use MetricX24-XXL as primary and CometKiwi-XXL as a cross-check. Removing the unused vision stack and non-task vocabulary and using int8 weights or fp8 activations causes no resolved loss, whereas int4 leaves a small residual. QLoRA healing overfits its calibration domain. A Cometoid best-of-4 reranker at $T=0.3$ improves both the 8-bit and 4-bit systems under WMT25 test set. On post-submission WMT26, both remain competitive with bf16 under reference-free metrics; the small difference between the reranked variants is treated as noise.
