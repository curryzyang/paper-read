# NeoTriFuse: Reliability-Aware Multimodal Fusion under Missingness Heterogeneity for Neonatal Mortality Risk Prediction

- 区域：速读区
- 排名：15
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Jiyuan Tian, Qincheng Shen, Ye Lin, Yu Gao, Haohui Lu
- 机构：The University of Sydney, Charles Darwin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26436v1) · [PDF](https://arxiv.org/pdf/2608.26436v1)

## TLDR
NeoTriFuse is a reliability-aware multimodal fusion framework that treats missingness as an explicit signal to dynamically modulate static, temporal, and summary modality contributions, achieving competitive neonatal mortality risk prediction (F1 0.6736, AUROC 0.9454) under heterogeneous data completeness.

## Abstract
Neonatal mortality risk prediction from bedside monitoring data remains challenging due to extreme class imbalance, heterogeneous clinical risk factors, multi-scale temporal dynamics, and substantial missingness. We propose NeoTriFuse, a reliability-aware multimodal fusion framework for missingness-heterogeneous neonatal monitoring data. Unlike conventional multimodal approaches that treat missingness primarily as a preprocessing issue, NeoTriFuse models missingness as an explicit reliability signal that dynamically modulates modality contributions during fusion. The framework integrates static perinatal variables, local-global temporal encoders, and patient-level statistical summaries through reliability-guided gating mechanisms, while jointly optimizing mortality prediction and an auxiliary length-of-stay objective. NeoTriFuse achieves competitive performance, with an F1 score of 0.6736 +/- 0.0216 and an AUROC of 0.9454 +/- 0.0056. Ablation studies indicate that the local-global temporal architecture and patient-level summary branch contribute most substantially to predictive performance, while reliability-aware gating provides additional improvements on threshold-dependent metrics under heterogeneous observation completeness. Sensitivity analyses further suggest stable performance across nearby hyperparameter settings. Overall, the findings support reliability-aware multimodal fusion as a practical approach for neonatal mortality prediction under realistic clinical missingness conditions.
