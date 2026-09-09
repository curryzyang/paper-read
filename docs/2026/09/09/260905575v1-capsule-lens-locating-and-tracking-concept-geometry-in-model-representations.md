# Capsule Lens: Locating and Tracking Concept Geometry in Model Representations

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yiming Tang, Harshvardhan Saini, Samyak Jha, Huaming Chen, Xufeng Duan, Dianbo Liu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05575v1) · [PDF](https://arxiv.org/pdf/2609.05575v1)

## TLDR
Capsule Lens introduces a framework that models each concept's representation region as a simple, interpretable “capsule” geometry, fitted in closed form and validated on held-out samples, enabling localization of concept geometry in static representations and revealing distinct geometric drift patterns across dynamic settings like CLIP pretraining and RL post-training.

## Abstract
Understanding how concepts are encoded in the internal representations of machine learning models is a central problem in mechanistic interpretability, essential both for the science of deep learning and for the trustworthy deployment of increasingly capable models. Existing approaches to interpret model representations mainly map representations onto more interpretable spaces and do not directly characterize how concepts occupy representation space; various hypotheses have been proposed, but often lack of rigorous validation and largely focus on static representations. In this work, we introduce Capsule Lens, a framework that matches the region a concept occupies with a simple, trackable geometric form, a capsule, defined by several interpretable parameters, fitted in closed form to each concept's geometry and validated on held-out samples. We apply Capsule Lens in two major settings: static and dynamic representations. On static representations, we demonstrate how to locate concept geometry across various models, and how the span and norm curves uncover important geometric characteristics. On dynamic representations, we present three case studies tracking representation drifts induced by distinct training settings, CLIP pretraining, RL post-training on visual question answering, and RL post-training on mathematical reasoning. These analyses reveal qualitatively different geometric dynamics, ranging from broad network-wide restructuring in CLIP pretraining to localized and concept-specific changes in RL post-training. Our results include findings aligned with existing literature as well as novel observations. We believe Capsule Lens stands as a promising tool for locating, analyzing, and tracking concept geometry in both static and dynamic representations.
