# Counterfactual Marginalisation: Framework for Evaluating Robustness to Nuisance Variables

- 区域：速读区
- 排名：10
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Yasin Ibrahim, Hermione Warr, Robin J. Evans, Konstantinos Kamnitsas
- 机构：University of Oxford
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10778v1) · [PDF](https://arxiv.org/pdf/2609.10778v1)

## TLDR
This paper introduces counterfactual marginalisation, a test-time evaluation framework that intervenes on nuisance variables via a counterfactual image generator and averages predictions to define metrics for robustness, calibration, stability, and worst-case sensitivity of classification models.

## Abstract
Machine learning models can achieve strong test performance while relying on demographic or acquisition-related shortcuts. We propose counterfactual (CF) marginalisation as a test-time evaluation procedure for assessing robustness of classification models to such variables. Given a CF image generator, we intervene on nuisance parent variables such as age or sex, generate CF versions of each test image, and average predictions over a target intervention distribution. This produces intervention-aware predictions that marginalise demographic effects while preserving patient-specific latent information. We use these predictions to define metrics for CF risk, calibration, stability and worst-case sensitivity. We demonstrate this framework's utility for quantitative robustness evaluation.
