# SHIFT: Survival Prediction from Incomplete and Heterogeneous Genomic Data

- 区域：速读区
- 排名：14
- 匹配度：1.3/10
- 来源：arxiv
- 作者：Muhammet Sami Yavuz, Ayhan Can Erdur, Sabri Mustafa Kahya, Benedikt Wiestler, Jana Lipkova
- 机构：TUM University Hospital, Munich Center for Machine Learning (MCML), Technical University of Munich (TUM), University of California Irvine
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07725v1) · [PDF](https://arxiv.org/pdf/2607.07725v1)

## TLDR
SHIFT is a missingness-aware transformer-based survival model that uses masked self-attention and variable-rate feature masking to directly predict from incomplete genomic inputs without test-time imputation, achieving strong generalization across heterogeneous cohorts.

## Abstract
Genomic prediction models often fail to transfer across institutions because sequencing panels differ across sites, creating structural feature missingness at deployment. Existing approaches to this challenge typically restrict analysis to genes shared across cohorts, exclude patients with incomplete profiles, or rely on test-time imputation, all of which can reduce robustness and limit the use of multi-center data. We propose Survival prediction Handling Incomplete Features using Transformer (SHIFT), a missingness-aware survival model that directly predicts from incomplete genomic inputs without test-time imputation. SHIFT represents each genomic feature separately and uses masked self-attention, along with a feature-availability mask, so that predictions are based only on observed inputs. Further, we introduce variable-rate feature masking during training to improve robustness to heterogeneous missingness patterns. We evaluate the approach on glioblastoma and lung squamous cell carcinoma with external validation across multiple cohorts, including a challenging setting with severe cross-cohort panel mismatch. Across these settings, SHIFT shows strong generalization and compares favorably with standard survival baselines and imputation-based approaches, while using a single model across differing feature sets. We also find that incorporating patients from incomplete cohorts during development can improve performance on external data, suggesting that partially observed cohorts need not be excluded from model building. These results support missingness-aware modeling as a practical strategy for multi-center survival prediction in precision oncology.
