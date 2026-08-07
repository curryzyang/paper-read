# Decoupling Perception from Description: Computation-Grounded Representation Alignment between Multivariate Time Series and Language

- 区域：速读区
- 排名：1
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Xinran Feng, Yi Xie, Chao Zhang, Ruikun Li, Wanyun Ling, Ziyue Li, Chenxi Liu
- 机构：The Hong Kong University of Science and Technology (Guangzhou), Technical University of Munich, Chinese Academy of Sciences, Munich Data Science Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05238v1) · [PDF](https://arxiv.org/pdf/2608.05238v1)

## TLDR
To overcome the self-supervision trap in time-series-language alignment, CGTime decouples perception from description by using deterministic computation to extract ground-truth statistics from real multivariate series and having the LLM only verbalize those precomputed facts, enabling a 4B-parameter model to outperform far larger baselines on multivariate understanding benchmarks.

## Abstract
Training multimodal models to align time series with language runs into a self-supervision trap. The usual recipe asks an LLM to read a series and write a description, so label quality is capped by the perceptual skill the model is supposed to learn. The data can never teach more than the labeler already knows. A second gap makes this worse: most datasets use a single variable, but the patterns that matter (cross-channel correlation, lead-lag structure, co-occurring anomalies) appear only with several variables, right where the labeling LLM's limits are most exposed. These two problems create a trilemma: existing methods are reliable, realistic, or scalable, but none achieves all three. We resolve this by decoupling perception from description. Deterministic code computes a set of statistics from real, open-source multivariate series; the LLM verbalizes those precomputed facts. Perception, which LLMs do poorly, is handled by computation, while the LLM handles expression. This produces CGTime, our 4B-parameter computation-grounded time-series-language model. CGTime outperforms far larger general-purpose models on multivariate understanding tasks: it attains the best multivariate fact score on our held-out benchmark (0.283 vs. 0.173 for GPT-4o-mini and 0.203 for GPT-5.4-nano), a gap that survives Holm-corrected paired significance tests against every baseline. It also states verifiable numerical facts in generated captions more accurately and covers a broader range of statistical properties.
