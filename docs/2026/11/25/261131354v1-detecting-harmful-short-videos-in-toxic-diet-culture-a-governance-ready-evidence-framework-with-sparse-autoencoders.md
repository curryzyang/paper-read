# Detecting Harmful Short Videos in Toxic Diet Culture: A Governance-Ready Evidence Framework with Sparse Autoencoders

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Wenli Zhang, Shuang Geng, Jiaheng Xie, Zhonghan Xiang, Sudha Ram
- 机构：University of Delaware, University of Arizona, Iowa State University, Shenzhen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31354v1) · [PDF](https://arxiv.org/pdf/2611.31354v1)

## TLDR
The paper presents SPACE, a sparse-autoencoder-based framework that detects harmful toxic-diet short videos while generating localized, computationally traceable, policy-grounded, and inspectable evidence for moderation decisions, achieving a harmful-category Macro F1 of 0.8507 on 3,711 TikTok videos and positive stakeholder evaluations.

## Abstract
Algorithmic content moderation is increasingly important for governing short-form video content, yet harmful-content detection research focuses primarily on prediction or limited explanations. This leaves a governance challenge underexplored: producing decision-linked evidence that supports the review and justification of moderation decisions. Using toxic diet culture as an empirical case, we conceptualize governance-ready evidence as computational traceability, evidence localization, policy grounding, and evidence inspectability. We develop the Sparse Autoencoder-based Policy-Aligned Contrastive Evidence (SPACE) framework in a pretrained SAE feature space derived from a large multimodal model. A global relevance gate and decomposable linear evidence head identify decision-linked evidence; segment supervision and within-video ranking localize this evidence; policy alignment maps it to platform guidelines; and Pareto-efficient selection yields a compact, task-specific evidence vocabulary. On 3,711 labeled TikTok videos, SPACE achieves the highest harmful-category Macro F1 among benchmarks across four families, at 0.8507. Its highest-scoring observation overlaps a ground-truth harmful span for 88.0% of harmful test videos, while its evidence representation retrieves the corresponding policy category for 87.0%. Stakeholder evaluations indicate that the SPACE evidence report is perceived as useful for understanding, reviewing, documenting, and responding to moderation decisions. The study contributes computational design science knowledge for embedding governance-ready evidence within predictive content-moderation systems.
