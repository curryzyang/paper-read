# SharedSAE: One Feature Dictionary Across Language Models

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Daniil Ognev, Célian Vasson, Lijie Hu, Kentaro Inui, Benjamin Heinzerling
- 机构：MBZUAI, Sorbonne Université, Tohoku University, RIKEN AIP
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04344v1) · [PDF](https://arxiv.org/pdf/2609.04344v1)

## TLDR
SharedSAE learns a single shared sparse feature dictionary across multiple language models by combining per-model encoder-decoder pairs with normalized joint top-k selection and model dropout, preserving reconstruction quality, improving cross-model latent alignment, and enabling frozen-dictionary adaptation of new models.

## Abstract
Sparse autoencoders (SAEs) are widely used to interpret language model activations, but SAE training and latent labelling are typically repeated for every model. Here, we show that a single shared SAE can replace a collection of dedicated per-model SAEs. Our method, SharedSAE, combines a shared dictionary with model-specific encoder-decoder pairs. Unlike the closest prior method, which discards activation magnitudes and requires all models at inference, SharedSAE instead normalizes only selection scores, preserving magnitudes, and uses model dropout for single-model inference. We train SharedSAE on four 1B-scale base language models spanning distinct families and tokenizers. Despite sharing its latents across models, SharedSAE retains 96.6% of dedicated SAEs' mean explained variance; its latent activations exhibit cross-model correlations 1.8 times as high as separate SAEs aligned post-hoc, and its latent descriptions transfer across models. After the dictionary is frozen, new models can be efficiently adapted to it, achieving near-dedicated-SAE reconstruction quality while reusing the shared latent descriptions.
