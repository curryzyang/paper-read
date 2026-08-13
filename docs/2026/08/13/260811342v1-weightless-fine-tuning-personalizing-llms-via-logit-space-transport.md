# Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Bohan Zhang, Anqi Ni, Yixin Wang, Paramveer S. Dhillon
- 机构：University of Chicago, University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11342v1) · [PDF](https://arxiv.org/pdf/2608.11342v1)

## TLDR
TLDR: Weightless Fine-Tuning (WFT) is a training-free, decoding-time method that approximates the distributional effect of supervised fine-tuning by transporting supervised residuals across prefixes via a dropout-estimated cross-prefix logit-space operator, achieving competitive personalization performance without updating model weights.

## Abstract
Supervised fine-tuning (SFT) is a standard approach for adapting LLMs to a target distribution, but in settings such as personalization, where each author requires separate weight access, optimization, storage, and retraining, its costs become prohibitive. We propose Weightless Fine-Tuning (WFT), a training-free decoding-time method that approximates the distributional effect of SFT without weight updates. WFT computes supervised residuals on an author's training sequence and transports them to the current prompt through a cross-prefix transport operator estimated from dropout-induced cross-covariance. The operator captures how a perturbation at one context propagates to predictions at another, replacing gradient-based parameter updates with logit-space corrections. On three LaMP personalization benchmarks, WFT achieves the best average performance across datasets, matches or exceeds SFT on individual tasks, and outperforms other lightweight baselines on average. In a budget-controlled comparison, WFT approaches SFT performance using less than 7% of the effective computation. Logit-level analysis shows a cosine similarity of 0.875 between the logit shifts induced by WFT and SFT over 95% of the next-token probability mass, suggesting that WFT captures the distributional effect of supervised adaptation without modifying model weights.
