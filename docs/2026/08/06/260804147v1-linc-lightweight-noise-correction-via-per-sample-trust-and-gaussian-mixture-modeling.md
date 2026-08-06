# LiNC: Lightweight Noise Correction via Per-Sample Trust and Gaussian Mixture Modeling

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Abhishek Moturu, Babak Taati, Anna Goldenberg
- 机构：The Hospital for Sick Children, T-CAIREM, University of Toronto, Vector Institute, UHN KITE Research Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04147v1) · [PDF](https://arxiv.org/pdf/2608.04147v1)

## TLDR
LiNC introduces a per-sample trainable trust parameter that blends observed labels with model predictions, then uses a 3-component Gaussian Mixture Model to identify and correct noisy labels, achieving consistent accuracy gains on MedMNISTv2 under up to 50% label noise with negligible added overhead.

## Abstract
Label noise is common in medical imaging datasets due to factors such as inter-rater variability, annotation errors, and ambiguous cases. This can severely undermine the reliability and clinical effectiveness of machine learning models trained using those datasets. To address this challenge, we introduce Lightweight Noise Correction (LiNC), which adds a single trainable trust parameter per training sample and learns when to use the observed label and when to defer to the model during a standard training loop. The key idea is to train using a convex combination of the observed label and the model's own predictive distribution, controlled by a per-sample trust parameter. We show that the gradient of this objective drives trust values in opposite directions for clean versus noisy samples in the early training phase, yielding separable trust distributions. We use a 3-component Gaussian Mixture Model over the trust values to separate them into clean, ambiguous, and noisy cases and then execute a short soft-correction phase on the noisy cases and a final hard correction phase. Experiments on ten 2D datasets from MedMNISTv2 under label noise of up to 50% show consistent gains in accuracy and strong mislabel detection. LiNC adds negligible asymptotic overhead: the training-time complexity remains dominated by the base network, with additional memory growing linearly with the size of the training set.
