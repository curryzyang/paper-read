# Generative Query Suggestion via Intent Coverage and Query-Level Credit Assignment

- 区域：速读区
- 排名：15
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Xinpeng Liu, Lu Ma, Jiayi Qiao, Mengyu Zhou, Linglong Li, Xiaofeng Bian, Haonan Chen, Xiaoxi Jiang, Guanjun Jiang
- 机构：Peking University, Alibaba, Pengcheng National Laboratory, National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19209v1) · [PDF](https://arxiv.org/pdf/2609.19209v1)

## TLDR
The paper proposes an Intent-Driven Query Suggestion Framework that combines intent-aware diversity modeling with query-level credit assignment to jointly optimize individual query quality and slate-level intent coverage, improving click-through rate, query quality, and intent coverage in offline and online evaluations.

## Abstract
Generative query suggestion aims to enhance user engagement by anticipating user intents and recommending relevant follow-up queries. A central challenge is to generate slates whose individual queries are useful while the slate covers distinct intents. We propose an Intent-Driven Query Suggestion Framework with dual-stage optimization. First, intent-aware diversity modeling constructs intent-aligned supervised fine-tuning (SFT) data and uses an Intent-Aware Diversity Reward to optimize intent coverage. Second, query-level credit assignment routes individual quality signals to the corresponding query tokens while sharing a slate-level diversity signal across the slate. Experiments on a large-scale production dataset, including online A/B testing and offline evaluation, show improvements in click-through rate, query quality, and intent coverage.
