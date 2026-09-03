# OutageDiT: A Generative Foundation Model for Power Outage Forecasting and Scenario Simulation

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yunqin Zhu, Feng Qiu, Yao Xie
- 机构：Georgia Institute of Technology, Argonne National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01896v1) · [PDF](https://arxiv.org/pdf/2609.01896v1)

## TLDR
OutageDiT is a generative foundation model that uses a condition encoder and shallow flow decoder to produce realistic seven-day power outage trajectories, improving forecast accuracy, uncertainty quantification, and zero-shot regional transfer.

## Abstract
Power-outage planning requires scenarios before an event occurs. These scenarios must represent uncertainty in magnitude, timing, and duration while preserving temporal dependence. However, severe events are rare, and data from any single region contain few examples of extreme outage and restoration patterns. To address this challenge, we introduce OutageDiT, a foundation model for generating seven-day outage trajectories at quarter-hour resolution, trained on outage and weather records across the United States. Specifically, a condition encoder processes the historical context and known future covariates once per forecast, and a shallow flow decoder reuses the resulting horizon-aligned states to generate complete trajectories. The resulting samples support point forecasting, uncertainty quantification, and conditional event simulation within one deep generative model. Across outage forecasting benchmarks, OutageDiT improves forecast accuracy and scenario quality over strong baselines and supports zero-shot transfer to held-out regions. Together, these results position conditional outage simulation as a bridge from outage forecasting to operational planning under uncertainty.
