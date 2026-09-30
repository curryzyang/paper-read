# CADENCE: A Confidence-Adaptive Dual-Expert Network for Fast and Accurate Time Series Classification

- 区域：速读区
- 排名：1
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Onisa Mpaunda
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35929v1) · [PDF](https://arxiv.org/pdf/2609.35929v1)

## TLDR
CADENCE is a CPU-native confidence-adaptive dual-expert time series classifier that routes between a convolutional linear expert and a distributional interval expert, achieving near state-of-the-art UCR accuracy (0.8864, comparable to HIVE-COTE 2.0) while running in about 17.53 seconds per dataset.

## Abstract
Time series classification (TSC) exhibits a sharp trade-off between accuracy and computational scalability. Meta-ensembles like HIVE-COTE 2.0 reach state-of-the-art accuracy but require extensive compute, whereas ultra-fast random convolutional transforms (e.g., MiniRocket, Hydra) run in seconds but struggle with phase-independent distributions, signal kinematics, and decision tree fragmentation on large class counts.
  In this work, we present CADENCE (Confidence-Adaptive Dual-Expert Network for time series Classification Excellence), a unified, CPU-native dual-expert architecture. CADENCE decouples representation learning into two specialized pathways: (i) a Convolutional Linear Expert pairing 10,000 deterministic dilated features with closed-form L2-regularized Woodbury ridge classification, and (ii) a Distributional Interval Expert pairing competing dilated kernels (Hydra) with dyadic Cornish-Fisher moment approximations across signal kinematics and FFT spectral bands, fitted with an ExtraTrees ensemble. An internal validation meta-router with rare-class preservation dynamically selects between pure expert routing and confidence-weighted soft blending, followed by a full refit on 100% of training data.
  Evaluated across all 109 equal-length UCR Archive datasets over 30 resamples (3,270 total runs), CADENCE achieves a grand mean accuracy of 0.8864. This ranks #2 across the archive, surpassed only by HIVE-COTE 2.0 (0.8895, p_Holm = 0.295, no statistically significant difference), while outperforming Hydra+MultiRocket (0.8818), MultiRocket (0.8797), and HIVE-COTE 1.0 (0.8786, p_Holm = 0.048). CADENCE closes the gap to HIVE-COTE 2.0 to 0.31 percentage points while taking an average of only 17.53 seconds per dataset on a dual-core CPU. Source code and evaluation scripts: https://github.com/onisa-jr/CADENCE.git
