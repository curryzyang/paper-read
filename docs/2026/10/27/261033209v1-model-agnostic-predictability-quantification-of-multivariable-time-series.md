# Model-agnostic predictability quantification of multivariable time series

- 区域：速读区
- 排名：5
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yuxuan Shu, Vasileios Lampos
- 机构：University College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33209v1) · [PDF](https://arxiv.org/pdf/2610.33209v1)

## TLDR
The paper proposes MAPS, a model-agnostic metric that quantifies the intrinsic predictability of multivariable time series forecasting tasks by using covariate information across lookback windows and forecast horizons to assess how consistently similar historical states lead to similar future targets.

## Abstract
Multivariable time series forecasting plays an important role in various domains, where predictions depend on complex interactions among covariates. Forecasting models are commonly evaluated across numerous benchmark datasets. However, forecasting accuracy reflects both model capability and task predictability, making it difficult to characterise the difficulty of a task independently of the model used. Existing predictability measures often fail to capture nonlinear dependencies or are limited to univariate series. In this work, we propose Multivariable Predictability Score (MAPS), a model-agnostic metric for measuring the intrinsic predictability of multivariable time series forecasting tasks. MAPS uses covariate information to assess predictability across different lookback windows and forecasting horizons, and provides a quantitative assessment of the predictive information available for forecasting. We evaluate MAPS across synthetic and real-world forecasting datasets against 6 baseline predictability measures. The former confirms that our method closely aligns with the expected reference predictability (r=0.963). Empirical results further corroborate that MAPS yields more reliable projections in the majority of experimental configurations.
