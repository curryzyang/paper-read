# Represent, Then Generate: Multimodal-Conditioned Time-Series Generation under Irregular Missingness

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Haochen Zhang, Jiaheng Guo, Yu-Chao Huang, Nicholas Knoz, Tianlong Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12592v1) · [PDF](https://arxiv.org/pdf/2608.12592v1)

## TLDR
ReCoGen is a two-stage framework that decouples multimodal condition representation from generation—using per-modality masked autoencoders to produce missingness-tolerant tokens and a flow-matching generator to synthesize target signals—and outperforms six existing conditional generators across all sixteen benchmark settings for clinical time-series generation under irregular missingness.

## Abstract
Continuous physiological time series underpin modern clinical monitoring, yet many of the most informative signals are invasive, expensive, or simply unavailable for a given patient. Conditional generation offers a remedy: an absent signal can be synthesized from co-recorded signals and routine clinical variables. Existing generators, however, are built around a single conditioning modality and degrade when forced to handle the heterogeneous, irregularly missing mix of time-variant signals and static covariates seen in practice. We propose ReCoGen (Represent Conditions, then Generate), a two-stage framework that decouples multimodal condition representation from target generation. Stage I trains one masked autoencoder per modality, distilling each time-variant condition into a compact and missingness-tolerant token sequence. Stage II trains a flow-matching generator that fuses these tokens with static conditions to synthesize the target signal. Across three physiological benchmarks, including continuous glucose monitoring on AI-READI and arterial blood pressure generation on MIMIC-III and MIMIC-IV, ReCoGen attains the best downstream utility on all sixteen (dataset, task, metric) settings, surpassing six representative conditional generators; on thirteen of them its utility also reaches or exceeds the utility measured on the real signal, a reference we read as an approximate anchor rather than a ceiling. Ablations trace the gains to the conditioning path: learnable cross-attention over the frozen per-modality encoders, and a dual token-plus-AdaLN route for the static conditions. ReCoGen thus turns routinely collected signals into informative surrogates for invasive or unavailable ones, a step toward less invasive, lower-cost continuous clinical monitoring.
