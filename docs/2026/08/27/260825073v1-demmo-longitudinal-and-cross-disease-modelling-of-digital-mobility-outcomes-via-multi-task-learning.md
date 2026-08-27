# DeMMO: Longitudinal and Cross-Disease Modelling of Digital Mobility Outcomes via Multi-Task Learning

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Menghui Zhou, Zhipeng Yuan, Vitaveska Lanfranchi, Po Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.25073v1) · [PDF](https://arxiv.org/pdf/2608.25073v1)

## TLDR
DeMMO is an interpretable multi-task learning framework that jointly models longitudinal digital mobility outcomes across multiple diseases and clinical outcomes via automatic cross-disease relation learning, achieving state-of-the-art prediction performance on the large-scale Mobilise-D dataset.

## Abstract
Digital mobility outcomes (DMOs) derived from wearable sensors characterise mobility in daily life and offer a promising means of monitoring disease progression. Yet most DMO studies examine one disease at one visit; they do not model how multivariate DMO relationships with multiple clinical outcomes evolve jointly across diseases. Technically, existing temporal multi-task frameworks can model progression within an individual disease, but they do not jointly model multiple prediction outcomes across diseases, particularly when disease cohorts do not share participants. To address these gaps, we propose DeMMO, an interpretable framework for longitudinal, multi-disease, and multi-outcome learning. DeMMO represents each disease-outcome objective by a longitudinal DMO coefficient matrix and combines temporal regularisation with stable and visit-specific feature selection. Its central technical contribution is an automatic cross-disease and cross-outcome relation-learning mechanism that learns signed relations directly from these longitudinal mappings, enabling selective information sharing without paired participants. We evaluate DeMMO on the recently released, large-scale, multicentre Mobilise-D dataset, which provides a new opportunity to study 24 harmonised real-world DMOs over five visits across multiple mobility-limiting conditions. Against nine strong linear, longitudinal, and deep-regression baselines, DeMMO achieves the best overall and outcome-specific prediction performance, with significant improvements over the strongest baselines. Stability selection further identifies reliable longitudinal DMO patterns for subsequent clinical validation and disease monitoring. The implementation code and experimental results are available at https://github.com/menghui-zhou/DeMMO.
