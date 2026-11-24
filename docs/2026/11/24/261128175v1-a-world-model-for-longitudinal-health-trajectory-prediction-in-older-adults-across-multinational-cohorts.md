# A world model for longitudinal health-trajectory prediction in older adults across multinational cohorts

- 区域：速读区
- 排名：12
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Jingyi Wu, Chenghua Guo, Qianlin Zuo, Pengfei Li, Luxia Zhang
- 机构：Peking University, Peking University First Hospital
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28175v1) · [PDF](https://arxiv.org/pdf/2611.28175v1)

## TLDR
This study introduces a Joint-Embedding Predictive Architecture–based health world model trained on the US HRS and externally validated in ELSA and CHARLS that represents evolving health states in older adults, predicts multi-horizon mortality and ADL/IADL worsening, and simulates action-conditioned counterfactual health trajectories.

## Abstract
Aging is characterized by continuously evolving health states, yet most existing prediction models focus on static health risk at isolated time points rather than explicitly modelling how health trajectories unfold over time. We developed a health world model based on the Joint-Embedding Predictive Architecture to represent evolving health states and simulate future trajectories under specified actions. The model combines a state encoder, an action- and context-conditioned predictor, a stop-gradient target encoder, and clinical outcome heads. We trained the model on the US Health and Retirement Study (HRS) and evaluated it without refitting in the English Longitudinal Study of Ageing (ELSA) and the China Health and Retirement Longitudinal Study (CHARLS). Open-loop evaluation assessed discrimination and calibration for mortality and worsening of activities of daily living (ADL) and instrumental activities of daily living (IADL). In the held-out HRS test set, the areas under the receiver operating characteristic curve (AUROCs) for mortality, ADL worsening, and IADL worsening were 0.89, 0.93, and 0.93 at the first horizon and 0.84, 0.84, and 0.85 at the fifth horizon, respectively. Predicted risks stratified subsequent outcomes across horizons. Across the evaluated horizons, mortality AUROC ranged from 0.867 to 0.881 in ELSA and from 0.796 to 0.801 in CHARLS. Simulated trajectories preserved the expected risk ordering across predefined action regimes. In counterfactual simulations, changes in lifestyle actions shifted predicted risks in directions consistent with observed associations. The model provides a framework for longitudinal risk prediction and action-conditioned simulation in older adults.
