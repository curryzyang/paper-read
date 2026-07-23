# Recovering Clinical Utility Under Differential Privacy: Empirical Validation of Adaptive Federated Aggregation on Heterogeneous Cardiovascular Datasets

- 区域：速读区
- 排名：12
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Rodrigo Tertulino, Laercio Alencar, Ricardo Almeida
- 机构：Federal Institute of Education, Science and Technology of Rio Grande do Norte (IFRN)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19403v1) · [PDF](https://arxiv.org/pdf/2607.19403v1)

## TLDR
This paper validates that the FedCVR framework, using server-side adaptive optimization, recovers clinical utility under differential privacy by outperforming standard federated averaging on real heterogeneous cardiovascular datasets, achieving an F1-score of 79.2% and AUC of 0.96 with a privacy budget of approximately ε=4.2.

## Abstract
Validating federated learning frameworks on real clinical data is an essential step between proof-of-concept demonstrations in controlled synthetic environments and deployment in real multicenter healthcare settings. A prior architectural study by the same authors (Tertulino and Alencar, 2026) demonstrated, on a synthetic six-feature benchmark, that server-side adaptive optimization acts as a temporal denoiser for Differential Privacy noise, answering an open challenge identified in the original pipeline work (Tertulino, 2025). That study used synthetically generated data and explicitly identified real-world validation as a priority future direction. The present work addresses this gap by validating the FedCVR framework on five publicly available real cardiovascular datasets (Framingham, Cleveland, Hungarian, Switzerland, and Long Beach VA), harmonized to the 13-attribute UCI Heart Disease schema and configured as a heterogeneous federated scenario with leave-one-institution-out cross-validation. Results demonstrate that FedCVR preserves its adaptive advantage on real data, achieving an F1-Score of 79.2% and AUC of 0.96 under the operational privacy budget (noise multiplier = 0.8, privacy budget epsilon approximately 4.2), while statistically outperforming standard FedAvg on all evaluated metrics (paired t-tests, all p <= 0.003, significant under the Bonferroni-corrected threshold). The measured privacy cost on real data confirms the graceful degradation pattern observed in the synthetic experiments, providing empirical evidence of the framework's clinical viability in genuine multicenter contexts.
