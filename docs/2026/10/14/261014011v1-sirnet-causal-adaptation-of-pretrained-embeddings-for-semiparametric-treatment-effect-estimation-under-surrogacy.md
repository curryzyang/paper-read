# SIRNET: Causal Adaptation of Pretrained Embeddings for Semiparametric Treatment-Effect Estimation Under Surrogacy

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Lei Shi, Qiuran Lyu
- 机构：Adobe Research, UC Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14011v1) · [PDF](https://arxiv.org/pdf/2610.14011v1)

## TLDR
SIRNET adapts pretrained embeddings of unstructured post-treatment surrogates through a shared multitask adapter for outcome, propensity, and surrogate-marginalization nuisances, enabling semiparametric efficient treatment-effect estimation from partially observed outcomes.

## Abstract
Modern experiments increasingly produce rich post-treatment objects---such as text, images, and video---that may provide early surrogate signals for outcomes that are delayed, expensive, or observed only for a subset of participants. A pretrained encoder can turn such an object into a strong generic embedding, but the embedding is not trained for the estimation tasks required by a causal estimator and may emphasize information irrelevant to the causal target. We propose SIRNET, a Surrogate-Informed Representation adaptation framework for neural-NETwork-based causal estimation in the presence of unstructured post-treatment surrogates. Starting from pretrained surrogate embeddings, SIRNET learns a shared adapter jointly for outcome prediction, treatment propensity, and arm-specific surrogate marginalization, beyond the generic pretraining objective. The resulting covariate and surrogate representations provide a common interface for these nuisance tasks. The final treatment-effect estimate and confidence interval are obtained from cross-fitted orthogonal scores that attain the semiparametric efficiency bound under the stated nuisance-rate conditions. We also validate SIRNET's performance in synthetic and semisynthetic experiments, as well as the Anti-Amyloid in Asymptomatic Alzheimer's Disease (A4) trial, using frozen pretrained brain-MRI embeddings as surrogates for a long-term outcome.
