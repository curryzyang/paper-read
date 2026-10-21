# EGiME: Entropy-Guided Model Evaluation in Few-Shot Learning

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Dequan Jin, Tao Li, Lifeng Xing, Shihui Ying, Hui Zhao
- 机构：Shanghai University, Guangxi University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27029v1) · [PDF](https://arxiv.org/pdf/2610.27029v1)

## TLDR
EGiME is a classifier-free, semi-supervised few-shot model-selection criterion that scores pre-trained feature spaces by K-means clustering all labeled and unlabeled samples and fusing inter-cluster separability and intra-cluster compactness entropy terms, yielding stable rankings highly correlated with full-pool accuracy under scarce labels.

## Abstract
The feature-extraction quality of pre-trained models sets the ceiling of downstream transfer learning, yet few-shot model selection remains difficult: supervised evaluation on scarce labels is unstable and yields fluctuating rankings. We propose Entropy-Guided Model Evaluation (EGiME), a semi-supervised criterion that assesses a candidate model from the clustering structure of its feature space without any classifier training. EGiME performs $K$-means clustering over all labeled and unlabeled samples, then combines two entropy terms: an inter-cluster entropy measuring global separability, and an intra-cluster entropy measuring the compactness of labeled anchors, fused through an inverse-frequency weight that emphasizes small clusters. On five few-shot benchmarks and nine pre-trained models, EGiME achieves a correlation score of 0.966 with the full-pool ground-truth accuracy obtained by averaging the accuracies of K-means, KNN, and SVM. At labeling ratios of 4\%--20\%, it produces markedly more stable model rankings than cross-validated supervised baselines, establishing it as a practical alternative to conventional supervised evaluation for pre-trained model selection under data scarcity.
