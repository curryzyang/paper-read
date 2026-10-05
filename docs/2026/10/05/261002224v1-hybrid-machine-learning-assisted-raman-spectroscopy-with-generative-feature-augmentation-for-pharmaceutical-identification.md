# Hybrid Machine Learning-Assisted Raman Spectroscopy with Generative Feature Augmentation for Pharmaceutical Identification

- 区域：速读区
- 排名：12
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Quach Thi Thai Binh, Ton Nu Quynh Trang, Thang B. Phan, Vu Thi Hanh Thu, Nguyen Tuan Hung
- 机构：University of Science, Vietnam National University, Tohoku University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02224v1) · [PDF](https://arxiv.org/pdf/2610.02224v1)

## TLDR
HyMLRaman combines EfficientNet-B3 deep spectral features, classical machine-learning classifiers, and DDPM-based generative feature augmentation to identify six pharmaceutical compounds from Raman spectra, achieving up to 96.31% accuracy for practical Raman-based screening.

## Abstract
Rapid and reliable identification of pharmaceutical residues is important for safeguarding public health, ensuring food safety, and enabling practical Raman-based screening. In this study, we propose HyMLRaman, a hybrid Raman spectroscopy framework that combines deep spectral feature extraction, generative models, and classical machine-learning classifiers to identify six pharmaceutical compounds, including amoxicillin, chloramphenicol, ciprofloxacin, tetracycline, ibuprofen, and paracetamol. Raman spectra are converted into spectral images and encoded with several deep neural-network backbones, among which EfficientNet-B3 yields the most effective representation. The resulting 1536-dimensional embeddings are then used to train downstream classifiers, including SVM, KNN, logistic regression, random forest, XGBoost, and ANN, using stratified 10-fold cross-validation. The hybrid EfficientNet-B3--SVM configuration achieves the strongest baseline performance, reaching 96.31% accuracy and a macro-F1 score of 96.36%, outperforming the standalone CNN baseline. To address limited-data conditions, a generative model, a DDPM-based feature augmentation, is introduced in a PCA-reduced EfficientNet-B3 latent space. The low-data ablation results show that DDPM augmentation provides selective benefits, particularly for KNN with reduced training fractions, and that its effect remains classifier-dependent. Finally, an application-level Raman Pharmaceutical Analyzer demonstrates the feasibility of embedding the trained model into an interactive Raman analysis workflow. These results suggest that HyMLRaman provides a practical and interpretable route for rapid Raman-based pharmaceutical screening.
