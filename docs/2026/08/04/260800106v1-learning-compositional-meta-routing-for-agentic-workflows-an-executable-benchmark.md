# Learning Compositional Meta-Routing for Agentic Workflows: An Executable Benchmark

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Natan Vidra, Alina Kapanova, Arun Kanhai, Spurthi Setty
- 机构：Cornell University, CUNY, Stevens Institute of Technology, Anote AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00106v1) · [PDF](https://arxiv.org/pdf/2608.00106v1)

## TLDR
This paper introduces an executable benchmark and a budget-aware meta-router that composes heterogeneous operations from raw task text, achieving 100% success on held-out test tasks at lower cost while revealing lexical generalization as the key limitation on a locked challenge split.

## Abstract
Agentic systems must decide not only what answer to produce, but which reasoning and execution operations should precede it. A controller may answer directly, decompose a request, retrieve evidence, execute code, delegate to a specialist, or verify an intermediate result. Existing routing work largely selects model endpoints, retrieval depth, or tools in isolation. We introduce an executable benchmark and a budget-aware meta-router that composes heterogeneous operations from raw task text. The benchmark contains 216 training, 72 development, 108 held-out test, and 108 locked lexical-shift challenge tasks across data analysis, frozen-corpus research, and document processing. Outcomes are machine checked after operations execute. Independent regularized logistic heads predict operation probabilities from word and character features, are temperature-scaled on development data, and are greedily composed under route-cost and action-count budgets. On the held-out test, the learned policy achieves 100% success versus 93.5% for strong static and fixed workflows, with 43% lower cost than the static policy; a matched learned one-shot router reaches 56.5%. On the untouched challenge split, learned success falls to 75.9% and trails static routing at 93.5%, while remaining 49% cheaper and exceeding one-shot routing by 34.3 points. The gap identifies lexical generalization, rather than route execution, as the principal limitation. These results establish a reproducible testbed and a bounded proof of concept, not evidence of live-LLM performance.
