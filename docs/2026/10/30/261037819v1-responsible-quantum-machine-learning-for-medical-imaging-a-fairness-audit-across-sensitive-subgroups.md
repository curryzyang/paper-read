# Responsible Quantum Machine Learning for Medical Imaging: A Fairness Audit Across Sensitive Subgroups

- 区域：速读区
- 排名：15
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Giovanni dos Santos Franco, Felipe Mahlow, Ellison Fernando Cardoso, José Adenaldo Santos Bittencourt, Felipe Fanchini
- 机构：University of São Paulo Faculty of Medicine Clinics Hospital, Hospital Israelita Albert Einstein, São Paulo State University (Unesp)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37819v1) · [PDF](https://arxiv.org/pdf/2610.37819v1)

## TLDR
This paper empirically audits subgroup fairness in classical and quantum classifiers for medical imaging (DDI skin lesions by Fitzpatrick skin type and CheXpert chest X-rays by age group), showing that QML can be competitive but is not inherently fair, that smaller subgroup gaps can reflect degraded performance in the best-served group rather than improved care, and that fairness effects are model- and dataset-dependent—so QML requires empirical subgroup-aware auditing, with all quantum models classically simulated and no quantum advantage claimed.

## Abstract
Quantum machine learning (QML) is increasingly explored for medical classification, yet its behaviour under subgroup-aware fairness criteria remains understudied. We present an empirical fairness audit of classical and quantum classifiers for medical imaging, assuming QML is not inherently fair. Two scenarios are evaluated: dermatological lesions on DDI (sensitive attribute: Fitzpatrick skin type) and chest X-rays on CheXpert-derived data (sensitive attribute: age group). Using ResNet-18 embeddings, we train SVM, MLP, QSVM and QCNN under a baseline and three mitigation settings: differentiable Equalized Odds (EO) regularisation, Gradient Reversal Learning (GRL), and both combined. Foundation models (PanDerm, EVA-X) serve as external references. Quantum classifiers may achieve competitive aggregate performance while still exhibiting subgroup disparities. Since a smaller subgroup AUC gap may stem from degrading the best group rather than improving the worst, each mitigation is also tested against a pre-specified non-inferiority margin relative to its baseline. Under this criterion, several configurations with the smallest disparity, notably QCNN with GRL on DDI, are not clinically acceptable due to loss of global discrimination. On DDI, QSVM with GRL+EO performed best and approached PanDerm in the performance/fairness trade-off; on CheXpert, QCNN with GRL achieved the highest aggregate performance but increased disparity, and EVA-X remained stronger. Fairness effects are model- and dataset-dependent, so QML requires empirical subgroup-aware evaluation. All quantum models run in classical simulation; we claim no quantum advantage.
