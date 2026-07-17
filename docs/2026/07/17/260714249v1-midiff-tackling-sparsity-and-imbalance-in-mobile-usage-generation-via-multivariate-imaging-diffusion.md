# MIDiff: Tackling Sparsity and Imbalance in Mobile Usage Generation via Multivariate-Imaging Diffusion

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yilai Liu, Shiyuan Zhang, Hongyang Du
- 机构：The University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14249v1) · [PDF](https://arxiv.org/pdf/2607.14249v1)

## TLDR
MIDiff is a diffusion-based framework that uses Cross-Gramian Angular Sum Field (C-GASF) to transform sparse, heterogeneous mobile usage data into correlation images and employs Triple Attention in a U-Net to effectively generate realistic and diverse traces while overcoming challenges of temporal sparsity, cross-channel heterogeneity, and long-tail usage imbalance.

## Abstract
Mobile usage traces are critical for tasks such as user behavior prediction and app recommendation, yet their use is constrained by privacy restrictions and costly large-scale data collection. Although generative models perform well on general time series, their application to mobile usage data remains challenging because (i) limited user activity causes severe sparsity, (ii) heterogeneous variable types complicate joint modeling, and (iii) functional differences across apps create pronounced usage imbalance. To address these challenges, we propose Multivariate-Imaging Diffusion (MIDiff), a diffusion-based framework operating in an imaging space defined by Cross-Gramian Angular Sum Field (C-GASF). C-GASF transforms sparse multivariate sequences into correlation images, while MIDiff employs Triple Attention in a U-Net to preserve temporal consistency and variable dependencies. Experiments show that MIDiff achieves state-of-the-art performance across fidelity metrics. In particular, it obtains a Discriminative Accuracy (DA) of 0.1526, compared with 0.3476 for the strongest baseline, ZITS-VAE, demonstrating its effectiveness in generating realistic and diverse mobile usage traces. Our code is available at https://github.com/YilaiLiu-HKU/MIDiff.
