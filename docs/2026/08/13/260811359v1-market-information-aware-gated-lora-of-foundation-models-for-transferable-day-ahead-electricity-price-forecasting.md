# Market-Information-Aware Gated-LoRA of Foundation Models for Transferable Day-Ahead Electricity Price Forecasting

- 区域：速读区
- 排名：8
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Hang Fan, Wei Wei, Shengwei Mei
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11359v1) · [PDF](https://arxiv.org/pdf/2608.11359v1)

## TLDR
This paper proposes a market-information-aware gated-LoRA framework that transfers the Chronos-2 foundation model to day-ahead electricity price forecasting via a multi-source market-information interface and source-domain adaptation, reducing MAE/RMSE by 6.24%/7.99% over zero-shot Chronos-2 under a leave-one-market-out protocol without target-market labels.

## Abstract
Electricity price forecasting is crucial for market participants but remains difficult because prices are volatile, market-specific, and closely tied to anticipated system conditions. Existing supervised methods depend largely on market-specific historical data, limiting their use in newly established or data-scarce markets. This paper proposes a market-information-aware adaptation framework that transfers the Chronos-2 time-series foundation model to day-ahead electricity price forecasting. It first constructs a multi-source market information (MSMI) interface aligning 7-day price context with pre-clearing supply--demand, reserve, maintenance, generator-capacity, and intertie variables, and then trains a source-domain gated low-rank adapter (LoRA), updating about $1\%$ of model parameters without target-market labels. The gate scales the frozen source adapter according to reserve-tightness and operating-state signals. A leave-one-market-out protocol is adopted for evaluating cross-market transferability. Experiments on four Chinese provincial day-ahead spot markets show that the proposed framework reduces the average MAE/RMSE by $6.24\%/7.99\%$ relative to market-information-aware zero-shot Chronos-2 and by $3.05\%/3.52\%$ relative to vanilla Source-LoRA. Experiments show that the gain is not reproduced by a learned global scalar or by random gate initialization, while the additional improvement over Source-LoRA is limited. These results suggest that market-structured inputs and state-dependent gated LoRA can provide a practical transfer path for data-scarce electricity markets.
