# QFireNet: A Quantum-Enhanced U-Net for Wildfire Segmentation from Sentinel-2 Imagery

- 区域：速读区
- 排名：10
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Jaiman Munshi, Tanvi Tewary, Sawyer Bloom, Aidan Chu, Chetan Maviti, Kyon Winston-Bey, Harshit Badjatia, Farhan Kittur, Vardhan Madhavarapu, Varun Kota, Joshua Kwon, Nazia Rangwala-Vohra, Franz Klein
- 机构：University of Maryland, College Park
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14160v1) · [PDF](https://arxiv.org/pdf/2607.14160v1)

## TLDR
QFireNet demonstrates that integrating variational quantum circuits into the U-Net bottleneck improves wildfire segmentation from Sentinel-2 imagery compared to classical baselines, and that data mixing mitigates domain shift to further boost performance.

## Abstract
Wildfire detection from satellite imagery is a semantic image segmentation problem that has proven to be difficult due to challenges such as class imbalance, feature complexity, and atmospheric interference. In this paper, we build on the foundational U-Net image segmentation model to develop a quantum-hybrid solution in hopes of more effectively modeling the high-dimensional spectral feature space of the Sen2Fire dataset. We inject a variational quantum circuit in the bottleneck portion of U-Net, specifically the QuFeX and QB-Net ansatzes. We test a classical Feature Pyramid Network (FPN) for further comparative analysis of the model, and we also explore classical improvements to the U-Net model and its training process, including a compression of parameters, alternative loss functions, and uniform mixing of input data. Our primary finding is that under matched conditions, both QB-Net (with an $F_1$ score of 31.18) and QuFeX ($F_1 = 30.79$) outperformed the classical U-Net baseline results ($F_1 = 28.71$). Additionally, the classical FPN achieved a comparable score of 31.13. A crucial finding was that data mixing removed a significant domain shift between the geographically-separated train and test sets, which boosted the classical FPN $F_1$ score to 39.76. We validate the architecture's robustness and generalizability to the wildfire detection problem via cross-dataset transfer on the California Burned Areas (CaBuAr) dataset. Overall, we find that quantum machine learning has potential to provide an advantage in the problem of wildfire image segmentation, and further experiments will continue to validate and expand upon this finding.
