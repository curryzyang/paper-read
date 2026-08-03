# Representations from Pretrained Machine-Learning Interatomic Potentials as Coarse Coordinates for Material Generation and Evaluation

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Paul Hagemann, Katharina Ueltzen, Simon Müller, Janine George, Philipp Benner
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28776v1) · [PDF](https://arxiv.org/pdf/2607.28776v1)

## TLDR
The paper proposes the Coarse-Fine Transport Distance (CFTD), a dual-featurizer metric using pretrained MACE interatomic potential features for quality and contrastive GNN features for novelty, to improve evaluation of generative crystal models, and demonstrates that coarse MACE features can also guide material generation.

## Abstract
Generative machine learning is increasingly used for inorganic crystal structure generation. Most models and the corresponding evaluation approaches rely on simple forms of crystal structure representation. In this paper, we showcase the power of atom-averaged features from pretrained Machine-Learning Interatomic Potentials (MLIPs), such as MACE, for such tasks. We first introduce a distance measure that assesses the output of material generative models by capturing both quality and novelty in a single distribution-based evaluation framework. In particular, we introduce the Coarse-Fine Transport Distance (CFTD) using two different featurizers, where the quality component is based on coarse MACE features. We showcase CFTD's versatility in capturing crystal-structure quality while also detecting memorization, and compare it with the recently introduced continuous SUN metrics. We further show that coarse MACE features can be used as guidance for a material generative model.
