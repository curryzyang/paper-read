# Behind-the-Meter Photovoltaic Visibility from Net Smart Meters: Deployment Regimes and Operational Insights

- 区域：速读区
- 排名：10
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Jack Zheng, Hao Wang
- 机构：Monash University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12527v1) · [PDF](https://arxiv.org/pdf/2610.12527v1)

## TLDR
This paper shows that for deep-learning-based behind-the-meter PV disaggregation from net smart meters, the deployment regime—especially seen versus unseen households and temporal extrapolation—dominates model choice in determining error, with known-customer accuracy substantially underestimating new-customer errors and limited target-domain fine-tuning reducing cross-region transfer error by 28–36%.

## Abstract
Distribution operators need visibility of behind-the-meter photovoltaic (PV) generation, yet most residential customers are observed only through net smart meters. Deep-learning-based PV disaggregation can restore this visibility, but its operational value depends on whether the model serves known customers, new customers, future periods, or new regions. We quantify this dependence using four deployment regimes that separate household transfer from temporal extrapolation, applied to Ausgrid smart-meter data with cross-dataset adaptation to the Pecan Street data. Using a fixed training protocol, we benchmark representative deep sequence architectures for PV disaggregation under regime-matched evaluation. At a fixed 48-hour context length, daylight mean absolute error (MAE) of the best model rises from 0.104~kW on seen households in the future test period to 0.185~kW on unseen households over the same period, and under a fixed training contract the deployment regime explains far more of the error variation than model choice. Under target-domain normalization, fine-tuning on five target-region households reduces source-model transfer error by 28\%--36\%. Long input windows help known-customer extrapolation, while their new-customer benefits vary by model. These findings suggest regime-matched error budgets, limited target supervision for model adaptation in new regions, and use-case-dependent context selection for energy data analytics.
