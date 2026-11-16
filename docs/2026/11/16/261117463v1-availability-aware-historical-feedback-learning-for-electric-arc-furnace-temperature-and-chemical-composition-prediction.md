# Availability-Aware Historical Feedback Learning for Electric Arc Furnace Temperature and Chemical Composition Prediction

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Ahmed Shoyeb Raihan, Farzana Islam, Ashish Nimbarte, Imtiaz Ahmed
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17463v1) · [PDF](https://arxiv.org/pdf/2611.17463v1)

## TLDR
The paper proposes an availability-aware historical-feedback learning framework that uses only previously released EAF outcome measurements under a measurement-delay rule and shows across twelve tuned regressors that this history-informed representation improves endpoint temperature and chemical composition prediction over temporal-only features.

## Abstract
Electric arc furnace (EAF) steelmaking plays an increasingly important role in recycled and lower-carbon steel production. However, variability in charged materials, energy input, and operating conditions makes accurate prediction of molten steel temperature and final chemical composition challenging. Intermittent or delayed measurements limit the information available for timely prediction. This study develops an availability-aware historical-feedback learning framework for predicting EAF endpoint temperature and the final concentrations of twelve chemical elements. Eight industrial data sources are integrated into three progressively enriched predictor representations comprising 19 static, 39 temporal, and 47 history-informed features. Historical outcomes are incorporated only when eligible under an assumed 60-minute measurement-release delay. Using 19,738 temperature heats and 3,341 chemistry heats, twelve tuned regression algorithms are evaluated through chronological forward validation. The proposed historical-feedback representation reduces root mean squared error (RMSE) in 147 of 156 matched algorithm-target comparisons. For temperature prediction, ExtraTrees achieves an RMSE of 12.290 degrees C, representing a 5.54 percent reduction compared with its temporal-only counterpart. Historical-feature ablation and feedback-delay sensitivity analyses demonstrate the importance of recent outcome information and its availability. In a separate retrospective later-period evaluation, lightweight adaptive residual correction reduces temperature RMSE from 12.502 to 12.275 degrees C without retraining the underlying model. Exploratory deep learning comparisons and target-specific feature-attribution analyses provide additional insights into predictive behavior. The results establish historical outcome availability and sequential feedback as important considerations for EAF endpoint prediction.
