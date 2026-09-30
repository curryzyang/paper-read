# Calibration-First Cross-Cohort Multimodal Temporal Learning for Transferable Asthma-Risk Forecasting

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Taimoor Ahmad
- 机构：Superior University Lahore
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35795v1) · [PDF](https://arxiv.org/pdf/2609.35795v1)

## TLDR
The paper presents CALIBRA, a calibration-first multimodal temporal framework that combines reliability-gated recurrent encoders, cohort-adversarial training, hierarchical probability calibration, and split conformal prediction to forecast short-horizon asthma risk across cohorts with incomplete modalities, demonstrating reproducible controlled-shift performance on a semi-synthetic benchmark without establishing clinical effectiveness.

## Abstract
Asthma deterioration forecasting must remain reli- able when patient populations, sensor ecosystems, and available modalities change across cohorts. Existing models commonly optimize within-cohort discrimination and may produce poorly calibrated probabilities after transfer. We present CALIBRA, a calibration-first multimodal temporal framework for short- horizon risk prediction with incomplete data. Dedicated recurrent encoders process environmental, pulmonary, symptom, medication, wearable, and context streams; a reliability-conditioned gate suppresses stale or absent modalities, while gradient-reversal training discourages avoidable cohort signatures. A shrinkage- based hierarchical logistic layer calibrates probabilities using a patient-disjoint target subset, and split conformal prediction provides abstention-capable prediction sets. To avoid fabricating clinical evidence, we evaluate the complete implementation on a documented three-cohort semi-synthetic benchmark with controlled distribution shift, informative missingness, and sealed target patients. Across five configured seeds, CALIBRA achieved mean target-test AUPRC 0.224 versus 0.240 for the strongest non-ablation comparator, TemporalTransformer; mean AUROC was 0.717, and Brier score was 0.098. Experiments additionally assess complete-modality failures, calibration, conformal coverage, decision curves, subgroup behavior, ablations, runtime, and parameter count. The results verify the method and reproducible pipeline under controlled shift, but do not establish clinical effectiveness. External validation on harmonized real asthma. Overall this artifact provides evidence for carefully governed real-cohort validation.
