# GreenLeaf Law Embed Tiny: A Compact Embedding Model for Legal Domain Retrieval

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Surya Saka
- 机构：JudicialMind
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24936v1) · [PDF](https://arxiv.org/pdf/2608.24936v1)

## TLDR
GreenLeaf Law Embed Tiny is a compact 0.6B-parameter legal embedding model that uses two-stage training (knowledge distillation plus domain-specific fine-tuning with hard negative mining) on a curated 3.4M-pair corpus to achieve competitive legal retrieval performance (75.11% on MLEB, 64.38% on MTEB(Law)) while supporting efficient quantized deployment.

## Abstract
We present GreenLeaf Law Embed Tiny, a 0.6B parameter embedding model for legal domain retrieval. GreenLeaf-Tiny achieves 75.11% on the Massive Legal Embedding Benchmark (MLEB) and 64.38% on MTEB(Law, v1),demonstrating competitive performance among models under 1B parameters. Our approach combines a two-stage training pipeline that first distills knowledge from a larger teacher model into a compact student architecture, then applies domain-specific fine-tuning with hard negative mining; a carefully curated dataset of 3.4 million query-passage pairs, including 150,000 human-curated samples across diverse legal jurisdictions; and an efficient inference architecture supporting multiple quantization levels (BF16, INT8, binary) enabling deployment in resource-constrained environments. We provide detailed analysis of our training methodology, architectural choices, and comprehensive evaluation across legal retrieval tasks. Our results demonstrate that domain-specific training with high-quality data can improve performance for specialized domain applications
