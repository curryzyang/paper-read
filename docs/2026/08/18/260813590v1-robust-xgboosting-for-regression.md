# Robust XGBoosting for Regression

- 区域：速读区
- 排名：13
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Iris Aragón Mladosich, Christophe Croux
- 机构：KU Leuven
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13590v1) · [PDF](https://arxiv.org/pdf/2608.13590v1)

## TLDR
The paper proposes robust XGBoost variants for regression, showing that standard XGBoost is sensitive to vertical outliers and leverage points, and finds that the two-step MM-XGBoost loss achieves the best trade-off between robustness and predictive accuracy.

## Abstract
XGBoost is a very popular and powerful method for prediction. It iteratively fits simple decision trees to the residuals of the previous step. An efficient and scalable implementation is available. The standard loss function for XGBoost is the quadratic loss, but a Huber loss can also be used. In this paper, we study the robustness of XGBoost and show that its performance can be affected by vertical outliers and leverage points. To address this, we explore alternative loss functions, based on M-, S-, and τ -estimators from robust regression. Our results indicate that a two-step procedure, referred to as MM-XGBoost, provides the best trade-off between robustness and prediction accuracy.
