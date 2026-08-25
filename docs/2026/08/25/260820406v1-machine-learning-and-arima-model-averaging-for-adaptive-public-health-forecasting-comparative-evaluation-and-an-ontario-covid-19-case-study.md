# Machine Learning and ARIMA Model Averaging for Adaptive Public Health Forecasting: Comparative Evaluation and an Ontario COVID-19 Case Study

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Yushu Zou, Ye Li, Johra Moosa, Martin Grunnill, Samir N. Patel, Venkata R. Duvvuri
- 机构：University of Toronto, Public Health Ontario, York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20406v1) · [PDF](https://arxiv.org/pdf/2608.20406v1)

## TLDR
This study compares ARIMA, random forest, and XGBoost for adaptive public health forecasting across responsiveness, forecast horizon, and training data depth, and introduces MLAMA, a performance-weighted ensemble that achieves the lowest normalized error and supports condition-specific model selection for operational COVID-19 forecasting.

## Abstract
Public health forecasts must respond to abrupt changes in surveillance data without over-extrapolating noise, reporting artifacts, or temporary trends. We evaluated autoregressive integrated moving average (ARIMA), random forest, and extreme gradient boosting (XGBoost) models using 190 weekly observations of publicly available Ontario COVID-19 case counts from January 2020 to October 2023. Rolling-origin time-series cross-validation preserved temporal order during model tuning and evaluation. Performance was assessed across three operating dimensions: responsiveness following selected turning points, forecast horizons of one to six weeks, and the amount of historical training data. We also developed Machine Learning and ARIMA Model Averaging (MLAMA), a non-negative performance-weighted ensemble with weights that vary by forecast horizon and responsiveness setting. Retrospective comparisons showed that ARIMA adapted rapidly after turning points but its normalized error increased at longer horizons. Random forest and XGBoost were less responsive initially but maintained more stable normalized error over longer horizons. For two-week forecasts at the end of the study period, training on the most recent data outperformed using longer historical periods, particularly for XGBoost. MLAMA achieved the lowest normalized mean absolute percentage error across most forecast horizons and ranked among the best-performing methods across responsiveness settings. These findings support selecting forecasting models according to operating conditions rather than relying on a single universally preferred approach. MLAMA provides a practical framework for combining complementary statistical and machine-learning forecasts. The accompanying Python package is currently maintained in a private repository while software validation and reproducibility testing are completed.
