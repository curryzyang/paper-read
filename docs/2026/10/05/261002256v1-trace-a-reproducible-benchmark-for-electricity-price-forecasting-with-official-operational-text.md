# TRACE: A Reproducible Benchmark for Electricity Price Forecasting with Official Operational Text

- 区域：速读区
- 排名：13
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Xinyi Yi, Moy Yuan, Ioannis Lestas
- 机构：University of Cambridge
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02256v1) · [PDF](https://arxiv.org/pdf/2610.02256v1)

## TLDR
TRACE is a reproducible benchmark of 7,300 PJM zone–day instances that pairs electricity prices with official operational text reconstructed at the forecast cutoff, showing that such text aligns with price risk—most consistently upper-tail risk—and reduces upper-tail pinball loss by a median 7.4% across time-series foundation models.

## Abstract
Electricity price forecasting (EPF) supports scheduling, bidding, and risk management in electricity markets, yet existing benchmarks focus mainly on numerical inputs, leaving the forecasting value of forecast-time textual context insufficiently evaluated. We introduce TRACE, a reproducible benchmark of 7,300 zone--day instances pairing prices from five zones in a major U.S. market with official operational text available at the forecast cutoff. TRACE reconstructs official operational text at each cutoff, preventing post-cutoff information leakage. We evaluate TRACE for semantic alignment and forecasting value. Semantic assessments align with central movement and both tail risks in ground-truth prices, most consistently for upper-tail price risk. Forecasting value is reflected in a median 7.4\% reduction in upper-tail pinball loss across time-series foundation models. A controlled cross-day text-mismatch ablation reverses the gains, falling below the no-text baseline.
