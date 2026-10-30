# Depth through Recurrence: Towards Ultra-Efficient On-Device ASR

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Chen Feng, Tianyi Xu, Ramchalam Kinattinkara Ramakrishnan, Yicheng Lin, Shaojie Zhuo, Zhaocong Yuan, Chenzheng Su, Xiaopeng Zhang
- 机构：McGill University, Qualcomm AI Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37833v1) · [PDF](https://arxiv.org/pdf/2610.37833v1)

## TLDR
The paper proposes a block-recurrent ASR architecture that replaces parameterized depth with a few CKA-guided weight-shared recurrent blocks and knowledge distillation, retaining ~97.4% of large-model accuracy with an order of magnitude fewer parameters and enabling ultra-efficient, personalized on-device speech recognition.

## Abstract
Modern automatic speech recognition (ASR) systems have achieved remarkable accuracy by scaling model depth and capacity, but at the cost of increased memory, energy, and computational demands. On edge devices where ASR is often most needed, such as watches and glasses, deploying such large models is infeasible due to extremely constrained resources. This raises a fundamental question: can we achieve high representational power in deep ASR models without scaling up parameterization? In this work, we revisit the role of depth and identify layer wise representational dynamics, in which most layers learn functionally similar transformations. Motivated by this insight, we propose a block-recurrent ASR architecture that replaces parameterized depth with a small set of recurrent blocks, each consisting of weight-shared layers, thereby preserving effective depth while drastically reducing model size. Through representation-guided grouping and knowledge distillation, block-recurrent models retain the accuracy of large reference models while using an order of magnitude fewer parameters. Across Open ASR Leaderboard benchmarks, a model with only two shared blocks recovers 97.4% of the accuracy of large models on average. The compact backbone further enables efficient on-device personalization through lightweight MoE-LoRA adaptation, allowing user-specific models to match or surpass the accuracy of general-purpose ASR systems with significantly lower inference cost. By reusing weights across recurrent steps, the proposed architecture reduces memory-access overhead and inference energy consumption. Together, these results show that high quality ASR can be achieved without large parameterization, and that structured recurrence provides a principled path towards ultra-compressed, energy-efficient, and personalized speech recognition on the edge.
