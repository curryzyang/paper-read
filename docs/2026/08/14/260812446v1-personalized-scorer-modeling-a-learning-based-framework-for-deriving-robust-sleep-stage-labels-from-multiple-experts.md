# Personalized Scorer Modeling: A Learning-Based Framework for Deriving Robust Sleep Stage Labels from Multiple Experts

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Seyyed Ali Hoseini, Javad Baseri, Hamid Saadatfar, Edris Hoseini Gol, AmirHossein Eshghi
- 机构：University of Birjand
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12446v1) · [PDF](https://arxiv.org/pdf/2608.12446v1)

## TLDR
The paper proposes a learning-based hypnogram framework that models each expert scorer's stage-specific behavior via confusion matrices and aggregates their probabilities to derive more robust sleep stage labels from multi-scored datasets, consistently improving classification performance.

## Abstract
Sleep stage classification is important for the diagnosis and management of sleep disorders, yet most automatic staging studies evaluate models against a single reference hypnogram despite known inter-scorer variability. This study investigates whether multi-scored datasets can be used to construct more reliable reference labels from the collective behavior of multiple experts. We use the publicly available DOD-H and DOD-O datasets. EEG (C3-M2) and chin EMG signals were segmented into 30-s epochs, and 30 features were extracted from each modality, yielding 60 features for EEG+EMG. We propose a learning-based hypnogram (LBH) that models the stage-specific behavior of each scorer using confusion matrices derived from machine-learning models. After column normalization, these matrices estimate the probability of each true sleep stage given each scorer's label; probabilities are aggregated across scorers to assign the final label for each epoch. LBH was evaluated with random forest, support vector machine, and multilayer perceptron classifiers under EEG-only and EEG+EMG settings, and compared with the dataset hypnogram (DH) and best-scorer hypnogram (BSH). LBH consistently improved overall performance. The best results were obtained with random forest and EEG+EMG, reaching 86.07% accuracy, 85.46% precision, and 85.29% F1-score on DOD-H, and 86.04% accuracy, 85.21% precision, and 84.70% F1-score on DOD-O. These findings suggest that personalized scorer modeling can improve reference hypnogram construction without discarding information from individual experts.
