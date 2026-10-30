# Selective Transfer Learning for Groundwater Level Anomaly Forecasting: Accuracy-Risk Trade-offs

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Yaxuan Wu, Ali Mohammed Mansoor Alsahag, Seyed Sahand Mohammadi Ziabari
- 机构：University of Amsterdam
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37733v1) · [PDF](https://arxiv.org/pdf/2610.37733v1)

## TLDR
This paper evaluates context-aware selective transfer learning for multi-well groundwater anomaly forecasting in the Netherlands, finding that fixed transfer harms a substantial fraction of wells and that CASL modestly improves pooled accuracy and partially rescues many harmed wells, but neither CASL nor global convex blending dominates—revealing an accuracy–risk trade-off rather than uniformly beneficial transfer.

## Abstract
This work studies context-aware selective transfer learning for multi-well groundwater anomaly forecasting in the Netherlands. Source-domain pretraining can raise average accuracy but is not uniformly reliable: it degrades performance on a substantial fraction of heterogeneous wells. Context-Aware Selective Learning (CASL) uses calibration-trained, constrained contextual blending of frozen no-transfer and fixed-transfer parents. Global Convex Blend uses the same parents with one calibration-fitted weight per seed. The corrected task requires nine consecutive observed monthly inputs and an exact three-calendar-month target, without interpolation. Evaluation covers 457 wells and 13,718 test windows under five predefined seeds, with the four-cell maxsim0.60 source pool frozen using Always-TL validation RMSE alone. Fixed transfer harms 18.38-51.86% of wells. CASL has 0.424-1.084% lower RMSE than No TL, partially rescuing 97.53-99.50% and fully rescuing 23.46-43.78% of fixed-harmed wells. Partial rescue can arise structurally from convex blending and does not establish contextual superiority. Global Convex Blend protects more wells in four seeds, while CASL has slightly lower pooled RMSE in four. Neither dominates: the results support an accuracy-risk trade-off on the fixed split, not rolling deployment validity.
