# FinVector-Market-4B: A Controlled Study of LoRA Adaptation for Structured Financial Tasks

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Alina Khaybullina
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08882v1) · [PDF](https://arxiv.org/pdf/2610.08882v1)

## TLDR
FinVector-Market-4B demonstrates that rank-16 LoRA adaptation of Qwen3.5-4B on a 22k-example financial corpus yields substantial task-specific gains beyond output-format learning under matched explicit JSON-schema prompting, while remaining bounded by prompt sensitivity and benchmark limitations.

## Abstract
FinVector-Market-4B adapts Qwen/Qwen3.5-4B with rank-16 LoRA on a 22,000-example corpus for structured financial tasks. We evaluate the base and adapted models on the same 600-example benchmark under implicit and explicit JSON-schema contracts. Supplying the schema alone raises base-model JSON validity from 0% to 91.3%. Under matched explicit prompting, the frozen scores improve from 14.7% to 40.0% for FinQA answer exact match, from 48.0% to 82.7% for calculator-expression correctness, from 20.1% to 89.5% for scenario branch-label agreement, and from 52.4% to 87.2% for implication-direction agreement. A post-hoc policy-scoring audit shows that the reported macro-F1 decline reflects a changing label set; using the same three target classes gives 77.4% for the base and 83.1% for the adapter. Filing overlap and calculator-target inconsistencies qualify the benchmark's generalization claims. The results show that compact financial domain adaptation can produce substantial task-specific gains beyond output-format learning under matched prompting, with gains bounded by the evaluated task distribution and prompt contract.
