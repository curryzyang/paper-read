# Robustness of LLM-Generated SystemVerilog Assertions to Semantics-Preserving RTL Transformations

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：FNU Aditi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05658v1) · [PDF](https://arxiv.org/pdf/2609.05658v1)

## TLDR
LLM-generated SystemVerilog assertions are not robust to semantics-preserving RTL rewrites such as operand reordering, identifier renaming, or redundant parenthesization, with 9.7%–27.0% of originally correct behaviors becoming incorrect and aggregate accuracy masking substantial instability, showing that point accuracy alone is insufficient for evaluating LLM-based assertion generation.

## Abstract
Large language models (LLMs) are increasingly being explored for automating SystemVerilog Assertion (SVA) generation, yet most evaluations report correctness on a single syntactic representation of an input. Such point accuracy does not reveal whether a model's correct output is stable when the same RTL behavior is written differently. This paper presents a controlled metamorphic evaluation of LLM-based SVA generation under semantics-preserving RTL transformations. Starting from the VERT dataset, we construct a quality-filtered conditional-control pool and a stratified 40-program evaluation set containing 295 assignment behaviors. We evaluate two open code models, Qwen2.5-Coder-7B and DeepSeek-Coder-V2-Lite, with an identical evaluation prompt and greedy decoding. Three transformations are studied: operand reordering, deterministic identifier renaming, and redundant parenthesization. Beyond baseline and transformed accuracy, we measure conditional robustness, invariance failure, and any-flip rate, with 10,000-sample clustered bootstrap intervals at the RTL-program level. Across all six model-transformation conditions, 9.7%-27.0% of behaviors that were correct on the original RTL become incorrect after a semantics-preserving transformation. Aggregate accuracy can therefore hide substantial instability: under identifier renaming, DeepSeek-Coder-V2-Lite improves from 53.9% to 63.7% accuracy while 19.5% of its originally correct behaviors fail. Manual review of 30 sampled correct-to-wrong transitions identifies dropped path predicates, branch-polarity errors, Boolean-structure corruption, and output-contract violations. The results show that point accuracy alone is insufficient for characterizing LLM reliability in assertion generation and motivate robustness-aware evaluation for AI-assisted hardware verification.
