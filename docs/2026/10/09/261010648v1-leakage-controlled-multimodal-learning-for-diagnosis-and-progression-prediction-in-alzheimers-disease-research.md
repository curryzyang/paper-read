# Leakage-Controlled Multimodal Learning for Diagnosis and Progression Prediction in Alzheimer's Disease Research

- 区域：速读区
- 排名：15
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Akeem Temitope Otapo, Ghazaleh Khodabandelou, Zuheng Ming, Alice Othmani
- 机构：Université Sorbonne Paris Nord (USPN), Université Paris-Est Créteil (UPEC)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10648v1) · [PDF](https://arxiv.org/pdf/2610.10648v1)

## TLDR
TLDR: The paper proposes a leakage-controlled multimodal multitask framework that fuses an adapted SFCN MRI encoder with causal clinical Transformers and task-specific ODE-GRU dynamics to jointly predict Alzheimer’s diagnosis, progression, MMSE, atrophy, and comorbidities from irregular, incomplete longitudinal data, achieving internal diagnosis/progression AUROCs of 0.935/0.884 and external validation AUROCs of 0.767/0.764 while incorporating robust task balancing, comorbidity-aware subgroup auditing, and strict leakage controls.

## Abstract
Alzheimer's disease prediction involves irregular visits, heterogeneous measurements and incomplete modalities. This study presents a multimodal multitask framework combining an adapted SFCN MRI encoder, four causal clinical Transformers, shared fusion and task-specific ODE-GRU dynamics. Fine-tuning and LoRA adapt the final two MRI blocks. Task-DRO balances task losses, while Group-CVaR targets cohort and comorbidity strata. Branch-specific input controls, subject-grouped partitions and empirical causality checks support longitudinal evaluation. Across 2,649 subjects and 17,317 visits from ADNI, OASIS-2 and MIRIAD, internal validation yields diagnosis, stage-1 progression and first-stage-1-visit progression AUROCs of 0.935 +/- 0.002, 0.884 +/- 0.003 and 0.870 +/- 0.005, respectively (mean +/- SD across three seeds). Corresponding hybrid AUROCs are 0.951, 0.909 and 0.896. Next-visit MMSE mean absolute error (MAE) is 1.61 points; worst-stratum diagnosis AUROC is 0.827 +/- 0.008. Sampled ADNI explanations identify task-specific input dependence. OASIS-3 external validation yields network and hybrid diagnosis AUROCs of 0.763 and 0.767, hybrid next-visit progression AUROC of 0.764, diagnosis calibration error decreasing from 0.197 to 0.052, and next-visit MMSE MAE of 0.86. Seed-42 paired ablations of six components yield pooled diagnosis and progression AUROC differences between -0.004 and +0.004; removing clinical encoder inputs lowers diagnosis AUROC by 0.272. The framework integrates longitudinal prediction, missing-modality handling, auxiliary comorbidity modelling and subgroup evaluation within a common pipeline.
