# A Transportable Threshold-Based Framework for Interpretable Classification of Medical Data

- 区域：速读区
- 排名：11
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Antony Garcia, Adrian Noriega, Gabrielle Britton, Xinming Huang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15394v1) · [PDF](https://arxiv.org/pdf/2607.15394v1)

## TLDR
This paper presents a transportable, interpretable classification framework that uses supervised chi-square-guided binarization to apply Bernoulli Naïve Bayes to continuous medical data, achieving high AUC scores while providing transparent, rule-based decision rules and calibrated risk estimates.

## Abstract
Black-box models limit the adoption of artificial intelligence in medicine due to their lack of interpretability and reproducibility. We introduce a statistically grounded framework that provides fully interpretable, rule-based clinical classification using the Bernoulli Naïve Bayes (BNB) model. The method applies supervised $χ^2$-guided statistical binarization to continuous variables, identifying thresholds that maximize association with clinical outcomes within the training data. This transformation allows BNB to operate effectively on continuous medical data without sacrificing its inherent transparency. The approach was evaluated on three benchmark datasets, Pima Indians Diabetes, Wisconsin Breast Cancer, and Heart Failure Prediction, achieving area-under-the-curve (AUC) scores of 0.800 for the Pima analysis, 0.984 for Wisconsin Breast Cancer, and 0.919 for Heart Failure Prediction. In addition to discrimination, probabilistic reliability was assessed using leakage-safe cross-validated calibration analysis including Brier score, calibration intercept/slope, and post-hoc beta calibration, which improved probability calibration across datasets. These results suggest that a statistically interpretable framework can achieve performance comparable to more complex models while providing explicit, clinically meaningful decision rules and calibrated risk estimates. To illustrate this transparency concretely, a complete worked example demonstrates that model inference can be reproduced using only a reference table and basic arithmetic, without access to software or proprietary tools. This work offers a practical approach to supporting trustworthy and generalizable AI in real-world healthcare settings.
