# ProToMEx: Rapid, Interpretable Explanations via Structured Representations

- 区域：速读区
- 排名：11
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Athina Georgara, Adarsh Valoor, Sarvapali D. Ramchurn
- 机构：University of Southampton
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04265v1) · [PDF](https://arxiv.org/pdf/2609.04265v1)

## TLDR
ProToMEx introduces a model-agnostic explainability framework that uses Probabilistic Topic Models to learn latent "topics" representing coherent reasons for a classifier's decisions, providing global and local explanations with fidelity comparable to SHAP and LIME while being ~30–40x faster for local explanations.

## Abstract
Existing post-hoc explainers for machine learning classifiers primarily focus on feature attribution, assigning importance scores to individual features. While valuable, this approach struggles to articulate the complex, combinatorial patterns that often drive a model's decision-making process. To overcome this limitation, we introduce ProToMEx, a new paradigm for explainability that leverages Probabilistic Topic Models (PTMs). Our model-agnostic framework learns latent ''topics'' that represent distinct, high-level reasons for a classification, moving beyond simple feature importance to reveal underlying semantic structures. ProToMEx naturally provides both global explanations of a model's overall behaviour and local explanations that can disentangle multiple co-existing reasons for a specific prediction. We demonstrate empirically that ProToMEx not only produces explanations of comparable fidelity to popular methods like SHAP and LIME but also drastically reduces the amortised computational cost of generating local explanations, making it highly suitable for real-time applications. Specifically, we show that ProToMEx is ~30-40x faster than SHAP and LIME over standardised tabular datasets and synthetic datasets.
