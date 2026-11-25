# Flagging Batch Shift in Flow Cytometry using Jeffreys Divergence between Gaussian Mixtures

- 区域：速读区
- 排名：10
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Jonathan Legrand, Aguirre Mimoun, Audrey Bidet, Pierre-Yves Dumas, Christ{è}le Etchegaray, Baudouin Denis de Senneville
- 机构：CHU Bordeaux, Univ. Bordeaux
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31321v1) · [PDF](https://arxiv.org/pdf/2611.31321v1)

## TLDR
The paper proposes a model-agnostic flow cytometry reliability criterion that represents each patient sample as a Gaussian mixture and flags batch shift via its Monte Carlo-estimated Jeffreys divergence from the training distribution, showing on shifted acute myeloid leukaemia cohorts that rejected samples had a 2.5-fold higher misclassification rate than retained samples.

## Abstract
Machine learning models for clinical flow cytometry are usually evaluated on data drawn from their training distribution. In routine practice, however, acquisition conditions and reagents may change, potentially making predictions unreliable without warning. We propose a model agnostic criterion for prediction reliability based on a notion of distance from the training distribution: each patient sample is represented by a Gaussian mixture model, and its Jeffreys divergence to a reference fitted on the training data is estimated using Monte Carlo integration. We illustrate our approach on real-life shifted cohorts of acute myeloid leukaemia patients, using a classifier trained to predict NPM1 mutation status. First, we show graphically and statistically that pairwise divergences capture acquisition cohort structure. We then calibrate a rejection threshold on a subset of shifted cohort samples and evaluate it on held-out subjects. Across 20 runs, the misclassification rate of rejected samples was 2.5 times larger than for retained samples. These results suggest that input divergence can help identify unreliable predictions, providing a strong candidate component for abstention frameworks, along with quality control measures and classifier confidence.
