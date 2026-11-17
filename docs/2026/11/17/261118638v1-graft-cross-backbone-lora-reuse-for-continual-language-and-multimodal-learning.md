# GRAFT: Cross-Backbone LoRA Reuse for Continual Language and Multimodal Learning

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Ha Pham Thien Dinh, Ming Liu, Jiesi Guo, Matteo Vergani, Kewen Liao
- 机构：Deakin University, Australian Catholics University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18638v1) · [PDF](https://arxiv.org/pdf/2611.18638v1)

## TLDR
GRAFT enables cross-backbone LoRA reuse in continual language and multimodal learning by retrieving relevant pretrained adapters and transferring them to a target backbone through a learned linear feature-space bridge, outperforming randomly initialized LoRA adapters on most evaluated tasks.

## Abstract
In continual learning, parameter-efficient fine-tuning enables large language models to acquire new capabilities through lightweight adapters such as LoRA, yet the reuse of pretrained adapters is typically restricted to models sharing the same backbone. This limits the transfer of learned capabilities from language models to multimodal models. We propose GRAFT (Generalist Reuse of Adapters via Feature-space Transfer), a framework for cross-backbone LoRA reuse. GRAFT retrieves the most relevant pretrained LoRA adapter from a modality-aware library and maps it into the target backbone through a learned linear bridge between corresponding source and target feature spaces. We evaluate GRAFT on ten Super-NaturalInstructions text tasks, transferring Qwen2.5 LoRAs to Qwen2.5-VL, and five multimodal tasks, where Qwen2.5-VL LoRAs are directly reused. Compared with randomly initialized LoRA adapters, GRAFT improves performance on most evaluated tasks. These results show that GRAFT provides a simple and effective mechanism for reusing learned capabilities across language and multimodal models in continual learning.
