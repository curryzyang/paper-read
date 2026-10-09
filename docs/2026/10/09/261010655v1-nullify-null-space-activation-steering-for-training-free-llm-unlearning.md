# Nullify: Null-Space Activation Steering for Training-Free LLM Unlearning

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Wei Zhai, Xiang Liu, Qiang Huang, Rui Qian, Lemao Liu, Ziwei Li, Ziqi Wang, Zhitao Huang, Dejing Dou
- 机构：BEDI Cloud, Tianjin University, King Abdullah University of Science and Technology, Peking University, Zhejiang University, Fudan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10655v1) · [PDF](https://arxiv.org/pdf/2610.10655v1)

## TLDR
Nullify is a training-free LLM unlearning method that uses null-space-constrained activation steering at inference to redirect privacy-related activations away from memorized answers while leaving retained-query activations unaffected, achieving strong forgetting with near-lossless utility and no weight updates.

## Abstract
Large Language Models (LLMs) inevitably internalize substantial amounts of sensitive or private information during pre-training, while LLM unlearning aims to selectively erase specific knowledge to prevent privacy leakage with minimal loss of model utility. However, existing methods struggle to balance forget quality with utility, and typically incur substantial computational costs due to parameter fine-tuning. To address this, we propose Nullify, a training-free, non-destructive activation steering method for LLM unlearning. Nullify employs steering vectors during inference to redirect privacy-related activations away from their memorized answers, while satisfying a null-space constraint that leaves retained-query activations essentially unaffected to maintain utility. Evaluations on TOFU and MUSE show that Nullify matches or surpasses established baselines in forget quality while achieving near-lossless preservation of model utility. By avoiding weight updates entirely, Nullify serves as an efficient, plug-and-play inference-time intervention framework.
