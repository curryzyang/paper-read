# Local Reference Geometry Residual Augmentation for Imbalanced Time Series Classification

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Chuanhang Qiu, Yanran Xu, Yue Wang, Anthony Bagnall
- 机构：University of Southampton
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00093v1) · [PDF](https://arxiv.org/pdf/2609.00093v1)

## TLDR
LRG is a lightweight post-hoc feature augmentation method that repairs imbalanced time series classification by adding signed local geometry residuals and LDA-projected summaries to fixed representations, improving minority-class reliability in sparse or rest-dominated feature-space neighborhoods.

## Abstract
Imbalanced time series classification is often addressed by changing the training distribution, objective, logits, or final threshold. These interventions address important biases, yet leave a representation-level question unmeasured: after minority support is reduced, does a learned feature space remain locally reliable around minority regions? We identify a training-local geometry failure: under imbalance, minority cases can lie in sparse, rest-dominated, or mixed feature-space neighborhoods, even when the representation retains useful global class structure. To diagnose and repair this failure, we propose Local Reference Geometry (LRG), a lightweight post-hoc feature augmentation module applied between a fixed feature extractor and the classifier head. Using training features only, LRG measures local exposure and class-mixture risk, then augments each fixed feature with a standardized signed displacement from nearby training geometry and an LDA-projected residual summary. On controlled UCR/Bake Off Redux imbalance benchmarks, paired raw-versus-LRG comparisons show gains for learned, pretrained, and fixed representations, including when LRG is combined with training-level interventions and post-encoder classifier corrections. Ablations show that the gain comes from the signed local residual appended to the original feature, rather than from generic prototype distances, affinity features, scalar statistics, or VLAD-style codes. Further analyses support the proposed local-geometry failure hypothesis: minority neighborhoods become increasingly rest-exposed under imbalance, training-local risk identifies error-prone regions, and LRG gains concentrate in those high-risk regions.
