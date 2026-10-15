# Tracing Morphology, Semantics, and Divergence in Language Acquisition

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Forough Shirin Abkenar, Haoshuo Fu, Liang Feng, Ning Yan, Masood S. Mortazavi
- 机构：Futurewei Technologies
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19041v1) · [PDF](https://arxiv.org/pdf/2610.19041v1)

## TLDR
This paper traces intermediate checkpoints of open-source LLMs to show that morphological competence emerges before semantic embeddings stabilize, and that while larger training datasets improve divergence recognition, pretraining co-occurrence and inference repetition impair divergence recognition and associative link generation.

## Abstract
Understanding the dynamics of language acquisition in Large Language Models (LLMs) is crucial for uncovering how statistical representations evolve into structured linguistic capabilities. However, most existing studies focus primarily on fully trained models, leaving the developmental trajectory across intermediate training stages largely underexplored. In this work, we leverage intermediate checkpoints from open-source models (e.g., Pythia and OLMo) under teacher-forcing evaluation to systematically investigate language acquisition across training steps and model scales. We focus on four core characteristics: morphological structure acquisition, embedding drift, repetition dominance, and co-occurrence effects. Our findings reveal that models acquire morphological structures well before semantic embeddings stabilize. Furthermore, we show that training dataset size has a positive impact on divergence recognition, while co-occurrence during pre-training and repetition during inference have a negative impact on divergence recognition and associative link generation.
