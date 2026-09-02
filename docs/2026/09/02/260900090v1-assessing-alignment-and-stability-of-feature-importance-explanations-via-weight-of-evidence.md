# Assessing Alignment and Stability of Feature Importance Explanations via Weight of Evidence

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Eddie Conti, Claudio Daka, Álvaro Parafita, Antonio L. Alfeo, Axel Brando, Mario G. C. A. Cimino
- 机构：eCampus University, University of Florence, University of Pisa, Barcelona Supercomputing Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00090v1) · [PDF](https://arxiv.org/pdf/2609.00090v1)

## TLDR
This paper introduces a Weight of Evidence-based hypothesis-testing framework to evaluate feature importance methods by quantifying how strongly stochastic attributions support reference hypotheses, enabling principled assessment of alignment, faithfulness, and stability with applications to LIME and SHAP.

## Abstract
Feature importance Methods (FIMs) are widely used in Explainable AI to interpret model predictions, yet attribution scores alone often provide limited insight into the underlying reasoning process. In this work, we introduce a novel perspective by embedding FIMs within a hypothesis-testing framework based on Weight of Evidence (WoE). We quantify how strongly the observed evidence supports any given hypothesis on feature importance. The reference hypothesis can stem from domain knowledge, ground truth, or be derived from the FIM itself. This formulation enables a principled evaluation of FIMs, capturing both their alignment with prior knowledge and their variability. We further provide theoretical results linking WoE to attribution variance. Empirical results shows the applicability and flexibility of our strategy analyzing LIME and SHAP explanations in settings with different reference hypotheses. Overall, our framework offers a complementary tool for assessing FIMs through a contrastive, evidence-based lens.
