# Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Dmitry Osin, Egor Surkov, Petr Mokrov, Igor Udovichenko, Ivan Karpukhin, Evgeny Burnaev, Egor Shvetsov, Alexander Korotin
- 机构：Applied AI Institute, AXXX, ITMO University, Vega Institute Foundation, SB AI Lab
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12586v1) · [PDF](https://arxiv.org/pdf/2610.12586v1)

## TLDR
This paper frames multi-horizon event sequence forecasting as conditional generative modeling, benchmarks prediction accuracy against distributional realism to reveal a fundamental trade-off, and introduces Wasserstein BaryBooster, which aggregates realism-strong diffusion samples into a state-of-the-art predictor to convert realism into accuracy.

## Abstract
Event sequences are chains of random events, each described by heterogeneous (numerical and categorical) features. The problem of event sequence forecasting occurs in finance, healthcare, business process intelligence, and other fields. In this work, we study multi-horizon forecasting of event sequences as a conditional generative modeling problem. We evaluate forecasts not only for prediction accuracy, but also for distributional realism. To this end, we present a benchmark comprising metrics for both quality aspects, strong statistical baselines, recent models adapted from adjacent fields, and curated real-world datasets. Careful evaluation reveals that no method excels at both accuracy and realism, highlighting a fundamental trade-off between the two. Finally, we introduce Wasserstein BaryBooster, an algorithm that aggregates samples from a realism-strong diffusion model into a state-of-the-art predictor, demonstrating that distributional realism can be converted into prediction accuracy. Code is available at https://github.com/xaosina/event-sequence-forecasting.
