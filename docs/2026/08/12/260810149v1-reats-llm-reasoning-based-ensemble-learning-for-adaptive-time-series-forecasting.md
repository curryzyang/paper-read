# REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Xu Zhang, Chang Xu, Hui Sun, Nan Ma, Zijian Zhang, Peng Wang, Wei Wang, Li Zhao
- 机构：Fudan University, Microsoft Research, Nankai University, Jilin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10149v1) · [PDF](https://arxiv.org/pdf/2608.10149v1)

## TLDR
REATS leverages LLM chain-of-thought reasoning to act as an interpretable ensemble router that produces sample-adaptive weights for time series forecasting, using hybrid textual-numerical inputs, diverse weight supervision, and a two-stage SFT + GRPO fine-tuning framework with a reciprocal reward mapping to outperform competitive ensemble baselines and generalize to unseen models.

## Abstract
Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rely on fixed rules or black-box models based solely on numerical inputs, failing to leverage LLM reasoning for interpretable weighting decisions. We propose REATS, which leverages LLM reasoning capabilities as an intelligent ensemble router that jointly processes textual temporal pattern descriptions and numerical features to produce interpretable, sample-adaptive ensemble weights through chain-of-thought reasoning. To enable effective LLM-based ensembling, we study its key design choices and propose: (i) a structured input pipeline that transforms raw time series into hybrid textual--numerical representations with fixed token cost, enabling rule-based chain-of-thought construction without API dependency, augmented with retrieved similar-sample priors; (ii) a diverse multi-row weight supervision scheme coupled with a token-efficient percentage-table format that reduces numerical complexity and mitigates LLM hallucinations; and (iii) a two-stage fine-tuning framework combining SFT with GRPO, where a reciprocal reward mapping transforms the continuous unbounded MSE gap into bounded signals with amplified near-oracle sensitivity, addressing the uniform sensitivity and outlier-dominated advantage compression inherent in naive reward designs for regression-based GRPO. Experiments on eight benchmarks demonstrate that REATS outperforms competitive ensemble baselines while providing natural language explanations and demonstrating strong transfer learning and out-of-domain generalization to unseen candidate models.
