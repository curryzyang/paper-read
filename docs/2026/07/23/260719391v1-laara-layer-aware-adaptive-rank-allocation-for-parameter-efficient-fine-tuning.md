# LAARA: Layer-Aware Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning

- 区域：速读区
- 排名：1
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Ashutosh Tripathi, Surya Deep Singh, Pranab Sahoo, Sriparna Saha
- 机构：Independent Researcher, Indian Institute of Technology, Patna
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19391v1) · [PDF](https://arxiv.org/pdf/2607.19391v1)

## TLDR
LAARA proposes a search-free framework that uses lightweight Fisher estimates to dynamically allocate different adapter ranks per transformer layer, consistently matching or outperforming state-of-the-art parameter-efficient fine-tuning methods while using significantly fewer trainable parameters.

## Abstract
Low-Rank Adaptation is widely used for parameter-efficient fine-tuning, yet existing methods typically assign the same adapter rank to every transformer layer despite their heterogeneous adaptation requirements. In this work, we show theoretically and empirically that uniform rank allocation is fundamentally suboptimal. Motivated by this observation, we propose LAARA (Layer Aware Adaptive Rank Allocation framework), a search-free framework that dynamically allocates ranks using lightweight diagonal Fisher estimates computed during training. LAARA combines projection-wise normalization, logarithmic compression, blended adapter importance estimation, and a vote-to-change dampening mechanism to produce stable and efficient rank adaptation. Experiments on GLUE and MathInstruct benchmark demonstrate that LAARA consistently matches or outperforms popular state of the art approaches such as LoRA, AdaLoRA, DyLoRA, and Bitfit while using significantly fewer trainable parameters. Our results show that Fisher-guided rank allocation provides a principled and effective foundation for adaptive parameter-efficient fine-tuning. The code is publicly available at: https://anonymous.4open.science/r/LAARA-D305/LAARA.py
