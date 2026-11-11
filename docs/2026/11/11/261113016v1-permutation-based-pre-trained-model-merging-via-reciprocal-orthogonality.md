# Permutation-Based Pre-trained Model Merging via Reciprocal Orthogonality

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Akira Ito, Daiki Chijiwa, Atsutoshi Kumagai
- 机构：NTT Computer and Data Science Laboratories, Tohoku University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13016v1) · [PDF](https://arxiv.org/pdf/2611.13016v1)

## TLDR
The paper proposes a permutation-search method that encourages reciprocal orthogonality to enable linear mode connectivity and parameter-addition model merging at smaller widths, even across different training distributions, yielding predictions that approximate a logit ensemble of the original models.

## Abstract
Ito et al. (2026) showed that sufficiently wide, independently trained neural networks can exhibit linear mode connectivity (LMC) with softmax temperature calibration, even without permutation. LMC means that a low-loss linear path connects the models' parameters. This behavior is explained by layerwise exponentially weighted connectivity (LEWC), whereby each merged layer outputs an exponentially weighted sum of the original models' corresponding representations, yielding ensemble-like predictions. However, prior work observed LEWC with substantial widening, such as 8192 units per hidden layer for MLPs and $16\times$ width for VGG-11, raising the question of whether such widths are necessary. We therefore search for permutations that encourage reciprocal orthogonality (RO), which suppresses interference between each model's weights and the other model's representations. This allows both models' computations to coexist in the merged network, promoting LEWC at smaller widths. We formulate the search as independent layerwise quadratic assignment problems and approximately solve their continuous relaxations using Frank--Wolfe. Experiments show that our method facilitates LMC with less width expansion. It also merges models trained on different data distributions, where weight matching, which maximizes weight similarity through permutations, struggles. The merged predictions approximate those of a logit ensemble of the original models.
