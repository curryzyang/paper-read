# Optimized Instance Alteration for Explaining and Assessing Robustness of Classifiers

- 区域：速读区
- 排名：10
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Evgenii Kuriabov, David Miller, Jia Li
- 机构：The Pennsylvania State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06637v1) · [PDF](https://arxiv.org/pdf/2607.06637v1)

## TLDR
The paper proposes a unified optimization framework with an explainability-aware \(L_0\) penalty and a Tolerance Region Confusion Matrix to generate interpretable counterfactual explanations and assess classifier robustness under structured perturbations.

## Abstract
In this work, we propose a unified approach for diagnosing misclassification and assessing the robustness of black-box classifiers. Central to our method is an optimization framework that modifies an instance so that the classifier predicts a specified target label, while ensuring that the modification remains easily explainable. The objective function contains two components: an explainability-aware $L_0$ (XA-$L_0$) penalty that promotes sparse and interpretable modifications, and a classifier loss objective that steers the perturbed instance toward the desired output. This integrated optimization formulation is used both to identify the underlying causes of misclassification and to evaluate robustness by determining how an instance can change within a tolerance region before being reassigned to another class. To quantify robustness, we introduce the Tolerance Region Confusion Matrix (TOR-Confusion Matrix), which measures a classifier's susceptibility by modeling the class-to-class transition probabilities induced by tolerance-bounded perturbations. We validate the proposed method on both image and tabular datasets, demonstrating its ability to jointly deliver interpretability and robustness assessment.
