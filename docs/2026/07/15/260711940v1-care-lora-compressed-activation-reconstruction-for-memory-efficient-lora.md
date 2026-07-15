# CARE-LoRA: Compressed Activation REconstruction for Memory-Efficient LoRA

- 区域：速读区
- 排名：1
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Gengyu Zhang, Haiyin Ran, Zhengbao He, Yuhang Liu, Hanling Tian, Zhehao Huang, Xiaolin Huang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11940v1) · [PDF](https://arxiv.org/pdf/2607.11940v1)

## TLDR
CARE-LoRA reduces the activation memory bottleneck during LoRA fine-tuning by storing compressed activations and a lightweight reconstruction matrix, enabling both low-rank matrices to remain trainable while achieving competitive or superior performance with significantly lower memory usage.

## Abstract
As the scale of large pre-trained models continues to grow, fine-tuning them under limited memory budgets has become increasingly challenging. Low-Rank Adaptation (LoRA), currently one of the most widely adopted parameter-efficient fine-tuning (PEFT) methods, mitigates this challenge by optimizing only low-rank adaptation matrices, thereby greatly reducing the number of trainable parameters. With the parameter overhead substantially reduced, the activations retained for backpropagation have emerged as the primary remaining memory bottleneck during LoRA fine-tuning. To address this, we propose CARE-LoRA, a data-aware Compressed Activation REconstruction framework. By exploiting the inherent projection structure of LoRA, CARE-LoRA replaces the full input activation with the low-rank compressed activation naturally produced by the LoRA branch. It further computes a lightweight reconstruction matrix during the forward pass with negligible additional computation cost, which is used during backpropagation to reconstruct the gradient signal, thereby keeping LoRA matrices fully trainable. Extensive experiments across diverse models and downstream tasks demonstrate that, while substantially reducing the overall memory footprint, CARE-LoRA achieves competitive or even superior performance compared with standard LoRA and representative LoRA variants. Our code is publicly available at https://github.com/fishandyu/CARE-LoRA .
