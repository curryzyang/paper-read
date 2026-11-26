# Quantum Machine Learning for Signature Forgery Detection

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Nabila, Md Farhan Shahriyar, Nowshin Tabassum Puspa
- 机构：Southern University Bangladesh, Hajee Mohammad Danesh Science and Technology University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33163v1) · [PDF](https://arxiv.org/pdf/2611.33163v1)

## TLDR
This paper proposes a hybrid quantum-classical pipeline for offline signature forgery detection that combines a frozen EfficientNetB0 feature extractor, quantum-compatible PCA, and nearest-neighbor/quantum-kernel classifiers, achieving 92.62% accuracy on a held-out fold and 91.26% mean accuracy in stratified five-fold cross-validation.

## Abstract
Offline handwritten signatures remain a primary behavioural biometric in legal and financial documents. Detecting skilled forgeries from a static raster image is hard because pen pressure, timing and stroke order are missing. This work studies a family of quantum machine learning pipelines for offline signature forgery detection on a public Kaggle corpus of images split into two classes. We pair a ZZ feature map quantum kernel with three classical learners: K-Nearest Neighbours, Support Vector Machine and Random Forest. We then propose a deeper hybrid that uses EfficientNetB0 as a frozen feature extractor, reduces the resulting 1280 dimensional representation to a qubit register sized subspace through a quantum compatible principal component projection and decides class membership with a nearest neighbour rule. On a single held out test fold the proposed hybrid reaches 92.62 percent accuracy. On stratified five fold cross validation the same pipeline yields a mean accuracy of 91.26 percent with a standard deviation of 1.13 percent. The pipeline keeps a quantum embedding step that is portable to NISQ hardware. We report a controlled ablation across six quantum variants, confusion matrices, a t SNE projection and per class precision, recall and F1 score.
