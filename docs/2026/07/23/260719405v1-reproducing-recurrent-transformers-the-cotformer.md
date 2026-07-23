# Reproducing Recurrent Transformers: The CoTFormer

- 区域：速读区
- 排名：3
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Aras Kavuncu, Bryan Vullo, Alberto Berni
- 机构：University of Southampton
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19405v1) · [PDF](https://arxiv.org/pdf/2607.19405v1)

## TLDR
We reproduce the CoTFormer architecture, confirming its base perplexity and compute efficiency claims while identifying that the adaptive depth module's claimed dynamic routing benefits are not fully reproducible and require further controlled evaluation.

## Abstract
The CoTFormer architecture formalizes Chain-of-Thought as a form of recurrent latent computation, preserving intermediate states as attendable representations to mimic explicit reasoning traces. In this work, we evaluate CoTFormer and its structural variants across perplexity and compute efficiency metrics. Furthermore, we extend evaluation to controlled algorithmic settings to determine whether this recurrent framework improves out-of-distribution generalisation on inductive reasoning tasks.
