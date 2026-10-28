# Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Tianqi Chen, Xunchao Li, Linchuan Xie, Guanghua Yu, Jianchen Zhu, Peisong Wang, Jian Cheng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35985v1) · [PDF](https://arxiv.org/pdf/2610.35985v1)

## TLDR
GateRQ uses the retrieval gate to set per-lookup precision for quantized conditional-memory rows—storing 1-bit residual ladders, keeping level 1 for gate computation, and reading deeper levels only for highest-gate lookups—yielding 7.8× GPU table-memory reduction and 11–31% vLLM throughput gains on DeepSeek-V4.1-Flash with only ~1 PopQA point loss at 1.50 bits/lookup and no retraining.

## Abstract
Conditional memory layers, such as DeepSeek's Engram, attach large hashed n-gram tables to a language model, and removing them from DeepSeek-V4.1-Flash costs 36.8 PopQA points. Low-bit quantization loses long-tail facts first, and the standard remedy, giving more bits to frequently accessed rows, backfires: refining lookups by access frequency is worse than refining them at random. We trace this to the gate that scales each retrieved row. A lookup's quantization error is weighted by its gate, which is small for frequent n-grams, large for the rare n-grams of long-tail entities, and computable from a 1-bit code. GateRQ therefore stores each row as a ladder of 1-bit residual codes, keeps level 1 in GPU memory to compute the gate, and reads deeper levels only for the lookups the gate ranks highest. Without retraining, GateRQ cuts GPU table memory by 7.8x on DeepSeek-V4.1-Flash, which raises vLLM throughput by 11%-31% over FP8 tables, while losing about 1 PopQA point at 1.50 bits read per lookup and 0.2 points at 2.10 bits across two models.
