# RiskBlend: A Multi-Signal Framework for Test Input Prioritization in Machine Learning Regression Testing

- 区域：速读区
- 排名：13
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Madhusudan Srinivasan, Namith Nishal Raphae
- 机构：East Carolina University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27704v1) · [PDF](https://arxiv.org/pdf/2608.27704v1)

## TLDR
RiskBlend is a classifier-agnostic test input prioritization framework for ML regression testing that fuses four cross-version risk signals (historical failures, prediction shift, decision-boundary shift, and neighborhood change) with validation-learned weighting, consistently outperforming confidence-based baselines in detecting newly introduced misclassifications after model retraining.

## Abstract
When machine learning classifiers are retrained, inputs correctly classified by the previous model version may be misclassified by the updated version, creating regression faults that are costly to detect because verifying predictions against ground truth may require human annotation, expert review, or expensive simulation rather than inexpensive model inference. Test input prioritization addresses this problem by ranking inputs so that a limited verification budget reveals as many regression faults as possible. Existing approaches rely predominantly on single-model confidence scores and do not exploit how predictions, decision boundaries, and local neighborhoods change between model versions. We propose RiskBlend, a classifier-agnostic prioritization framework that combines four complementary risk signals: historical failure patterns, prediction shift, decision-boundary shift, and neighborhood change. These signals are combined using validation-learned APFD-squared weighting. Across four datasets, five classifiers, four regression-update scenarios, and 15 random seeds, totaling 1,200 experimental configurations, RiskBlend achieves the highest average APFD in all 80 dataset-classifier-scenario combinations, with improvements of up to 0.32 APFD over the strongest baseline. Confidence-based methods remain competitive primarily for linear classifiers on sparse categorical features, which we attribute to feature-space geometry. The results show that cross-version behavioral signals provide important complementary information for prioritizing regression faults in machine learning systems.
