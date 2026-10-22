# Building a Nested LADDER for LLM Unstructured Post-Training Pruning

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Nicolás Mauricio Cuadrado Ávila, Ivo Gollini Navarrete, Martin Takáč, Samuel Horváth
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28773v1) · [PDF](https://arxiv.org/pdf/2610.28773v1)

## TLDR
LADDER is an incremental layer-wise post-training pruning method that greedily assigns additional sparsity to the layers causing the least end-to-end degradation, producing nested non-uniform masks that are comparable at low sparsity but substantially more robust than uniform and adaptive baselines at high sparsity (70–90%) across OPT, Llama, and Qwen models.

## Abstract
Non-uniform allocation can improve post-training pruning of large language models, yet quality can still degrade sharply at high sparsity. To control degradation as sparsity increases, we introduce LADDER (Layer-Wise Allocation via Damage-Driven Evaluation and Refinement), which allocates sparsity incrementally. At each step, it evaluates pruning an additional fraction of weights from each eligible layer and commits the layer update that causes the least end-to-end degradation per removed parameter. This process produces non-uniform sparsity profiles and exactly nested masks across multiple budgets. We evaluate LADDER on five OPT, Llama, and Qwen models across 10-90% sparsity, using SparseGPT as its candidate-generation backend and comparing against uniform and adaptive allocation baselines. Results reveal a clear operating-regime trade-off: LADDER is comparable or slightly weaker at benign sparsity but becomes substantially more robust from 70% onward. This high-sparsity advantage largely persists after posterior distillation across four of five models and translates into improved retention of aggregate zero-shot accuracy.
