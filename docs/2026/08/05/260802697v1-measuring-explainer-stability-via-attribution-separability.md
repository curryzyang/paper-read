# Measuring Explainer Stability via Attribution Separability

- 区域：速读区
- 排名：12
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Eddie Conti, Álvaro Parafita, Axel Brando
- 机构：Barcelona Supercomputing Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02697v1) · [PDF](https://arxiv.org/pdf/2608.02697v1)

## TLDR
The paper proposes a distribution-based framework that measures the stability of feature attribution rankings by quantifying the separability between importance score distributions, enabling evaluation and comparison of explainers via a new k-stability metric.

## Abstract
Attribution methods (AMs) assign an importance score to each feature and are widely adopted to explain black-box models. However, most methods can produce variable attribution scores due to stochastic components in their definition. In this paper, we propose a distribution-based framework to capture the stability of attribution scores. In particular, our approach allows to understand the degree of separability in the ranked attribution vector and obtain the largest index for which a feature ranking remains reliable. We further extend this framework to compare AMs based on the robustness of their rankings across a dataset. Through experiments, we demonstrate how to apply our method to evaluate explainer stability. Overall, our approach provides a complementary criterion for evaluating the stability of AMs.
