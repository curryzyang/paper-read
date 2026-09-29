# FIDAL: Diversity-Aware Federated Active Learning Under Real-World Distribution Shifts

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：David Dueñas Gaviria, Shadi Albarqouni
- 机构：University of Bonn
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31637v1) · [PDF](https://arxiv.org/pdf/2609.31637v1)

## TLDR
FIDAL is an open-set federated active learning framework that combines calibrated evidential uncertainty, support-set diversity weighting, and adaptive OOD rejection to improve annotation efficiency and balanced accuracy on multi-center medical imaging under real-world distribution shifts.

## Abstract
Federated learning enables collaborative model training across institutions without centralizing data, yet high annotation costs, domain shifts, and class imbalance remain major obstacles, especially when irrelevant out-of-distribution (OOD) samples dilute the labeled data. Existing active learning methods target uncertainty or diversity within in-distribution (ID) data and overlook unknown samples in federated clinical settings. We propose FIDAL, an open-set federated active learning framework that combines calibrated global-local evidential uncertainty, support-set diversity weighting, and adaptive OOD rejection. The rejection gate thresholds a foundation-model Gaussian-coverage signal per client and per round with Otsu's criterion, so that highly informative ID samples are queried while irrelevant outliers are excluded without any hand-tuned threshold. Evaluated on three multi-center medical imaging benchmarks (dermatology, histopathology, and mammography with organically occurring artifacts) in realistic open-set scenarios, FIDAL outperforms detector-based open-set methods by up to about 12 percentage points of balanced accuracy and is the only method on the accuracy-ID purity Pareto front of all three benchmarks. At an equal query budget it spends at least 1.3 times fewer annotations on OOD samples than every accuracy-matched baseline, saving an estimated 7-29 hours of expert reading on the mammography benchmark. By labeling only a fraction of the data pool, it matches or exceeds fully supervised performance across modalities. These results highlight the value of integrating uncertainty, diversity, and OOD rejection in open-set federated active learning for medicine.
