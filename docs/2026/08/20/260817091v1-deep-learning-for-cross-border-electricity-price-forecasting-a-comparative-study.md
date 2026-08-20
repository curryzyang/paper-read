# Deep Learning for Cross-Border Electricity Price Forecasting: A Comparative Study

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Hadeer Elashhab, Sai Srijan Papineni, Marvin Dorn, Veit Hagenmeyer, Benjamin Schäfer
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17091v1) · [PDF](https://arxiv.org/pdf/2608.17091v1)

## TLDR
TLDR: This paper establishes a reproducible framework for cross-border electricity price forecasting by comparing six deep learning models on the Germany-Luxembourg 2024 market under zero-, one-, and few-shot settings, finding that N-HiTS and NBEATSx perform best in limited-data scenarios while transformer models need more tuning.

## Abstract
While publicly available electricity market data presents a valuable resource for forecasting research, the field lacks established benchmark datasets for standardized comparison. As a result, many studies have relied on different datasets and metrics to evaluate methods in isolated settings, making it difficult to assess progress and compare state-of-the-art approaches consistently. In this work, we use public data to evaluate deep learning models for electricity price forecasting (EPF) across multiple market settings. Our goal is to establish a reproducible framework that enables a consistent evaluation of forecasting models. Although deep learning has been explored for day-ahead EPF, many prior studies are limited to single-market settings, narrow feature sets, or fixed training regimes. This work presents a comparative evaluation of six deep learning models--covering state-space, MLP, RNN, and Transformer-based architectures--emphasizing generalization across markets. We simulate low-data target-market conditions using zero-shot, one-shot, and few-shot learning. Our test set focuses on the Germany-Luxembourg (DE-LU) bidding zone in 2024 using a standardized dataset with calendar, historical price, and market-derived features. Our findings suggest that N-HiTS and NBEATSx perform competitively in limited-data scenarios, while transformer-based models can reach comparable accuracy but tend to require more adaptation and tuning. Model performance also benefits from careful feature selection and hyperparameter tuning, and we note that the differences between the strongest models are often small.
