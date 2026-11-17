# Predictive maintenance in manufacturing: The operational value of continual machine learning

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Pascal Janetzky, Michael Klar, Manuel Wenzel, Tobias Schlagenhauf, Stefan Feuerriegel
- 机构：Munich Center for Machine Learning, Bosch Center for Artificial Intelligence, Albstadt-Sigmaringen University, LMU Munich
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18636v1) · [PDF](https://arxiv.org/pdf/2611.18636v1)

## TLDR
Using five years of Bosch maintenance data across 25 product configurations, the paper shows that continual machine learning combined with robust optimization mitigates forgetting in domain-incremental predictive maintenance and reduces cost-related indicators by over 40% versus fine-tuning, domain adaptation, online learning, and configuration-specific baselines.

## Abstract
Predictive maintenance in high-volume manufacturing often faces a domain-incremental learning problem: as new product configurations enter production, prediction models must learn from newly available data while preserving performance on earlier configurations that remain in operation. In this paper, we empirically study the operational value of continual machine learning methods for addressing this challenge in predictive maintenance, using real-world maintenance data from Bosch. The setting at Bosch covers 25 product configurations over five years, which creates a practical challenge for predictive maintenance models, as such models must be updated with data from newly introduced configurations without reducing performance on configurations learned earlier, a phenomenon known as "forgetting". At the same time, retaining all historical sensor data and repeatedly retraining models is often infeasible in high-volume manufacturing since industrial machines generate too large data volumes. To address this challenge, we combine continual machine learning with robust optimization to support predictive maintenance. We then compare continual machine learning with a broad set of baselines, including fine-tuning, domain-adaptation methods, online learning methods, and configuration-specific models. Across experiments, continual machine learning methods achieve stronger predictive performance and lower maintenance costs than the baselines, with a reduction of cost-related indicators of more than 40 % relative to the baselines. Our results demonstrate the operational value of continual machine learning for decision support in maintenance when product portfolios grow over time and historical manufacturing data cannot be fully retained.
