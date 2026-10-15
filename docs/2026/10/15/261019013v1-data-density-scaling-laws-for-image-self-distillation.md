# Data Density Scaling Laws for Image Self-Distillation

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Alvard Barseghyan, Ani Vanyan, Hakob Tamazyan, Hrant Khachatrian
- 机构：YerevaNN, Yerevan State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19013v1) · [PDF](https://arxiv.org/pdf/2610.19013v1)

## TLDR
This paper shows that in image self-distillation, repeated training on smaller random subsets can outperform training on larger unique datasets, and proposes a modified Chinchilla-style scaling law that explicitly accounts for both unique sample count and repetition density to better capture data-compute trade-offs.

## Abstract
Current scaling law formulations suggest that increasing the number of unique samples in a dataset improves model performance, while repeated exposure to the same samples provides diminishing value. In this work, we examine this assumption for image self-distillation models. Through systematic experiments across diverse datasets, namely Maxar, SATLAS, Waymo, nuPlan, Ego4D, ImageNet, and YFCC15M, we demonstrate that the effects of sample repetition on downstream performance are non-trivial and dataset-dependent. We identify settings where repeatedly training on a smaller random subset can outperform training on a larger set of unique samples. This finding highlights a limitation of existing scaling laws. To address this gap, we propose a modified version of a Chinchilla-style scaling law that explicitly accounts for two factors: the number of unique samples and repetition per sample. This formulation provides a framework for understanding data-compute trade-offs and improves prediction in some regimes where repetition plays a central role, although its benefits are not consistent across datasets. Finally, we examine how subset selection and augmentation affect downstream performance.
