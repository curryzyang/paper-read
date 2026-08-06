# A Comparative Study of Feature Selection Methods for EHR Diagnosis Codes in Opioid Use Disorder Prediction

- 区域：速读区
- 排名：15
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Zihan Ding, Yinan Liu, Tengfei Ma, Rachel Wong, George Leibowitz, Benjamin Littenberg, Xia Zheng, Richard N. Rosenthal, Fusheng Wang
- 机构：Rutgers University, Stony Brook University, University of Vermont
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04180v1) · [PDF](https://arxiv.org/pdf/2608.04180v1)

## TLDR
A comparative study of five feature-selection methods for EHR diagnosis codes in opioid use disorder prediction finds that NTK-motivated early gradient sensitivity offers the best accuracy–stability balance, while LLM-guided semantic selection adds complementary clinical value despite lower standalone performance.

## Abstract
Feature selection is a critical step in electronic health record (EHR)-based predictive modeling, where input variables are often high-dimensional, sparse, noisy, and redundant. Large feature sets not only increase computational burden and overfitting risk, but also make model interpretation difficult, leading to limited usefulness in clinical settings. In this study, we focus on diagnosis-related features and compare five feature selection paradigms for opioid use disorder (OUD) prediction: recurrence enrichment, NTK-motivated early gradient sensitivity, LightGBM-SHAP, Elastic Net, and large language model (LLM)-guided semantic selection. We use a unified preprocessing and evaluation framework and assess each method by downstream predictive performance, resampling stability, and representation of infrequent diagnosis codes. Our results demonstrate that performance improves with larger feature budgets with diminishing returns beyond a moderate size. NTK sensitivity provides the best overall balance of accuracy and stability, and LLM-guided selection contributes complementary clinically meaningful signals despite lower standalone performance.
