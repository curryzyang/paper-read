# Evaluating Time Series Foundation Models for Electricity Price Forecasting: Contamination Risk, Distributional Shifts, and Covariate Dependence

- 区域：精读区
- 排名：6
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Zhenghua Pan, Ahmed Aziz Ezzat
- 机构：Rutgers, The State University of New Jersey, USA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02623v1) · [PDF](https://arxiv.org/pdf/2607.02623v1)

## TLDR
This paper benchmarks time series foundation models for electricity price forecasting, finding that while they are competitive and benefit from covariate support, they often do not outperform domain-specific methods, yet simple ensembles of both capture complementary information and achieve the best overall performance.

## Abstract
Time series foundation models (TSFMs) have shown strong zero-shot forecasting performance, but their generalization in covariate-driven, non-stationary settings is underexplored. Electricity price forecasting (EPF) presents a challenging testbed due to complex temporal dependencies, distributional shifts, and strong reliance on structural and contextual information. We propose a two-dataset-benchmarking framework for EPF to mitigate contamination risk and enable fair evaluation of TSFMs. We examine key aspects of EPF including point and probabilistic forecasting performance, tail behavior, price spikes, and comparisons against domain-specific methods. We find that TSFMs are highly competitive and often outperform general-purpose baselines. Yet, their performance depends critically on covariate support, and they do not consistently surpass domain-specific methods tailored to EPF. Interestingly, simple ensembles of TSFMs and domain-specific methods appear to have significant potential, suggesting that the two approaches capture complementary predictive information.
