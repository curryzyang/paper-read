# Is 4 Bits Enough for EEG Sleep Staging? A Subject-Level Benchmark of MXFP4, NVFP4 and FP8

- 区域：速读区
- 排名：4
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Emese Batizi, Hossein Valavi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31436v1) · [PDF](https://arxiv.org/pdf/2611.31436v1)

## TLDR
This subject-level benchmark shows that pure 4-bit post-training quantization can degrade EEG sleep-staging accuracy, but MXFP4/NVFP4 with FP8 first and last layers (especially NVFP4) stays within ~0.5 percentage points of FP32 without retraining or QAT.

## Abstract
Staging sleep on a wearable device keeps the raw electroencephalogram (EEG) private and saves the energy needed to transmit it. It also requires small, energy-efficient neural networks. We benchmark 13 post-training quantization (PTQ) configurations, from FP16 to the block-scaled 4-bit formats MXFP4 and NVFP4, for five-stage sleep staging from single-channel Fpz-Cz EEG. We use Sleep-EDF-78 (78 subjects), subject-wise cross-validation, three training seeds, value-exact emulation, and per-subject paired statistics. All 8- and 16-bit formats stay within 0.45 percentage points (pp) of FP32 Macro-F1. With 4-bit weights and activations, an epoch-wise CNN loses 1.98 to 3.04 pp, and a temporal-context network loses at most 1.19 pp. A same-encoder ablation shows that temporal context explains little of this gap. At equal block size, NVFP4 outperforms MXFP4. The first layer, which quantizes the raw EEG, is the most sensitive layer in both networks. Keeping the first and last layers in FP8 brings both tested 4-bit formats within 0.48 pp of FP32. This recipe adds at most 2.1% weight storage, needs no retraining, and is equivalent to quantization-aware training (QAT) within an exploratory 1-pp margin. The 4-bit losses fall on the same subjects across architectures (Spearman correlation coefficient = 0.69 to 0.79), and they reduce N3 recall the most. On the nested Sleep-EDF-20 subset, NVFP4 with FP8 first and last layers again stays within 0.25 pp of FP32. Under MXFP4, however, the ranking of the architectures reverses, and FP8 first and last layers do not fully recover two of the three tested models. In our emulation, NVFP4 with FP8 first and last layers thus loses little accuracy without QAT in both cohorts.
