# Disentangling 3D Modeling from Spatial Reasoning

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Haoze Sun, Jiequan Cui, Qingshan Xu, Richang Hong
- 机构：HFUT, USTC
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05242v1) · [PDF](https://arxiv.org/pdf/2608.05242v1)

## TLDR
DiSR disentangles 3D perception from spatial reasoning by reconstructing images into structured 3D evidence with expert perception models and fine-tuning an LLM (via LoRA) to reason solely over that evidence, achieving state-of-the-art results on spatial reasoning benchmarks with improved efficiency, interpretability, and modularity.

## Abstract
In this work, we explore an alternative paradigm for spatial reasoning by explicitly disentangling 3D perception from reasoning, rather than jointly acquiring implicit 3D perception and reasoning through large-scale training. Our key observation is that modern perception models excel at estimating continuous 3D geometry, whereas large language models (LLMs) are particularly effective at compositional and symbolic reasoning. Motivated by these complementary strengths, we propose the Disentangled Spatial Reasoner (DiSR), a simple yet effective framework that reconstructs the physical world into structured 3D evidence using off-the-shelf expert perception models and fine-tunes an LLM with LoRA to perform reasoning solely over this explicit geometric evidence. Without large-scale 3D VQA training or complex tool-use policies, DiSR achieves competitive performance on popular spatial reasoning benchmarks. Beyond its strong performance, DiSR offers improved interpretability, modularity, and computational efficiency, demonstrating that explicit separation of perception and reasoning is a scalable and effective alternative paradigm to end-to-end modeling for spatial intelligence.
