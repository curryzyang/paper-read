# Realistic Robustness Evaluation of Tabular Data Driven Models

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Miguel Silva, Eva Maia, João Vitorino, Isabel Praça
- 机构：Polytechnic of Porto
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26818v1) · [PDF](https://arxiv.org/pdf/2611.26818v1)

## TLDR
The paper introduces AURORA, an open-source modular tool that evaluates the robustness of tabular-data ML classification models using multiple adversarial perturbation methods and metrics, with a distance-adjustment mechanism that penalizes unrealistic adversarial samples to ensure more reliable robustness assessment.

## Abstract
The increasing adoption of Machine Learning (ML) models in high-stakes applications has raised critical concerns regarding their robustness against adversarial attacks. While extensive research has focused on adversarial example generation in image and text domains, the study of such examples in tabular data remains comparatively limited, despite its widespread use in real-world systems. This work introduces AURORA, a modular, open-source tool for evaluating the robustness of ML models on tabular data classification. It integrates multiple adversarial perturbation methods and evaluation metrics within a unified framework to systematically assess model behavior under adversarial conditions. Central to AURORA is its evaluation report, which focuses on robustness analysis by quantifying performance degradation, comparing the impact of different perturbation strategies, and identifying model vulnerabilities across features and input regions. The report is complemented by visual artifacts that facilitate the interpretability of robustness patterns. Additionally, AURORA incorporates a distance adjustment mechanism that penalizes implausible adversarial samples based on feature-level constraints, ensuring that the robustness assessment remains grounded in realistic perturbations and is therefore more reliable.
