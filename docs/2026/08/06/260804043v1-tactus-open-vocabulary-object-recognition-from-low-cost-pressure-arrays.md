# Tactus: Open-Vocabulary Object Recognition from Low-Cost Pressure Arrays

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Abdul Basit Tonmoy
- 机构：Wabash College, Eximius Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04043v1) · [PDF](https://arxiv.org/pdf/2608.04043v1)

## TLDR
Tactus is an open, open-vocabulary model that matches or exceeds a supervised closed-set CNN on object recognition from low-cost pressure arrays alone, using a small-data recipe of sensor-calibrated normalization, same-sensor masked-autoencoder pretraining, and text-embedding cosine ranking.

## Abstract
Resistive pressure arrays are the cheapest and most widely shipped tactile sensors, yet tactile representation learning has concentrated on optical sensors that image a deforming gel. We present Tactus, an open model that answers text queries from pressure data alone: on the STAG benchmark (27 objects, held-out recordings), it reaches 0.771 +/- 0.062 top-1 over four runs (top-3 0.935), matching, and at best exceeding, the dataset's supervised closed-set CNN at 0.76, with no trained classifier head. The recipe is small-data: 187 training recordings, masked-autoencoder pretraining on 144k unlabeled same-sensor frames, and the sensor's own calibration affine, which recovered more accuracy than every architecture change combined. The released model's errors concentrate in a few contact-ambiguous classes, are uncorrelated with text-target geometry (Spearman rho <= 0.05 over 702 class pairs), and survive paraphrased and even bare-name queries within one point; two diverse frames recover 89% of eight-frame accuracy. Failures are reported with equal precision: cross-sensor pretraining pooling gave no gain, vision co-training degraded touch, and a mis-normalized input pipeline silently discarded 97% of the sensor's dynamic range while producing plausible intermediate results. Weights, code, and the memory layer the model plugs into are released openly.
