# A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering

- 区域：速读区
- 排名：9
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Joshua Wolff Anderson, Yanshan Wang, Shyam Visweswaran
- 机构：University of Pittsburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00298v1) · [PDF](https://arxiv.org/pdf/2611.00298v1)

## TLDR
The paper proposes MICF, a task-agnostic framework that uses mechanistic interpretability and activation-level interventions to reformulate counterfactual fairness constraints directly in transformer activations—without requiring a prior causal model or specific architecture—and demonstrates improved counterfactual fairness on real-world tabular prediction tasks.

## Abstract
Bias in transformer-based models is a growing concern as these architectures become more prevalent in automated decision-making systems, such as prediction models for hiring, lending, and clinical treatment recommendation. Mechanistic interpretability (MI) is a growing body of work that measures meaningful causal effects of activations on model output by identifying human-interpretable features encoded in model activations. When such features correspond to sensitive attributes, they provide a direct way to quantify the bias those attributes introduce and to causally intervene to mitigate it. However, counterfactual fairness (CF) methods have not been systematically adapted to this setting of intervening on interpretable mechanisms in transformers. We propose a framework, Mechanistic Interpretability for Counterfactual Fairness (MICF), that utilizes MI tools to reformulate CF constraints in terms of transformer activations, unifying former approaches into a single pipeline for fairness analysis in transformers. MICF does not require a prior causal model or specific transformer architecture. We evaluate MICF on real-world tabular data and show that CF can be improved across different prediction tasks.
