# Hybrid Ensemble Learning for EEG-Based Epileptic Seizure Forecasting

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Mason Dana, Khandaker Mamun Ahmed
- 机构：Dakota State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35876v1) · [PDF](https://arxiv.org/pdf/2609.35876v1)

## TLDR
This paper presents a calibrated hybrid ensemble that stacks five deep learning and three classical machine learning models via logistic regression for patient-independent EEG-based epileptic seizure forecasting, achieving 74.2% seizure-level sensitivity at 1.24 false alarms per hour with an average 16.9-minute warning time on CHB-MIT under strict leave-one-patient-out evaluation.

## Abstract
Epileptic seizure forecasting aims to provide actionable warnings before seizure onset, yet patient-independent generalization and false-alarm control remain major challenges. We propose a calibrated hybrid ensemble for EEG-based seizure forecasting that combines five deep learning models and three classical machine learning models through a logistic regression stacking meta-learner. The proposed pipeline integrates signal preprocessing, handcrafted feature extraction, class-imbalance handling, probability calibration, and clinically motivated post-processing. We evaluate the framework on CHB-MIT using strict Leave-One-Patient-Out (LOPO) cross-validation, with threshold and post-processing parameters selected only on held-out meta data. On the filtered cohort, excluding patients with anomalous preictal rates below 1\% or above 15\%, the model achieves 74.2\% seizure-level sensitivity at 1.24 false alarms per hour, with an average warning time of 16.9 minutes. A test-tuned oracle constrained to the target false-alarm budget achieves 60.9\% sensitivity at 0.951 false alarms per hour, highlighting the importance of reporting sensitivity together with realized false-alarm rates. Our code is available at: https://github.com/DanaMason/IEEE-CARS-Hybrid-Ensemble-Learning-for-EEG-Based-Epileptic-Seizure-Forecasting
