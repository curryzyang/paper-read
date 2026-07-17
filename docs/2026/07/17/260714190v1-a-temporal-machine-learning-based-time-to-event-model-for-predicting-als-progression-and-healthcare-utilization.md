# A Temporal Machine Learning-Based Time-to-Event Model for Predicting ALS Progression and Healthcare Utilization

- 区域：速读区
- 排名：13
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Zongliang Yue, Qi Li, Terry Heiman-Patterson, Frank Bearoff, Zhaohui Qin, Huanmei Wu
- 机构：Auburn University, Fisk University, Emory University, Temple University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14190v1) · [PDF](https://arxiv.org/pdf/2607.14190v1)

## TLDR
This paper introduces a digital-twin-inspired temporal machine learning time-to-event model that integrates longitudinal ALSFRS-R trajectories with survival analysis to predict individualized functional decline and healthcare utilization, specifically wheelchair-free survival, in ALS patients.

## Abstract
Amyotrophic lateral sclerosis (ALS) is a progressive and heterogeneous neurodegenerative disease in which predicting clinically meaningful milestones, such as assistive device use, remains challenging. We developed a time-to-event, digital-twin-inspired framework that integrates longitudinal ALS Functional Rating Scale-Revised (ALSFRS-R) trajectories with survival modeling to support individualized prediction of functional decline and assistive device utilization. We constructed a harmonized longitudinal dataset by integrating diagnosis records, ALSFRS-R assessments, activities of daily living, and demographic information, followed by preprocessing to ensure data quality, temporal alignment, and cohort consistency. Correlation-based clustering identified coherent functional domains spanning bulbar, upper limb, axial, lower limb, and respiratory systems. Generalized additive mixed models characterized nonlinear, domain-specific functional decline across all domains. In addition, a temporal machine learning model was developed to predict longitudinal functional decline and capture stage-dependent disease progression. Cox proportional hazards modeling further identified lower limb function, particularly walking and stair climbing, as the strongest predictors of earlier wheelchair access. Building on these results, we implemented a digital twin-inspired temporal machine learning-based time-to-event (TTE) model that generates individualized survival curves and dynamically predicts wheelchair-free survival. This framework provides a scalable, interpretable, and clinically actionable approach for linking ALS progression with personalized decision support, with applications in proactive care planning, clinical trial stratification, and precision medicine.
