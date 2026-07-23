# Decodable but Not Detectable: A Leakage Fingerprint for Near-OOD Benchmarks

- 区域：速读区
- 排名：15
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Vishnu Bindu Balachandran
- 机构：Independent AI Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19393v1) · [PDF](https://arxiv.org/pdf/2607.19393v1)

## TLDR
A paper identifies a benchmark leak in near-OOD detection where a trained class is mislabeled as OOD, proposes a "decodable but not detectable" leakage fingerprint (high supervised decodability paired with collapsed unsupervised detection) to diagnose it, and demonstrates that under corrected protocols, perturbation-based OOD signals remain decodable by supervised methods but undetectable by unsupervised ones.

## Abstract
While auditing a perturbation-based OOD detector on a document benchmark, we recorded an AUROC of 0.326 -- well below the 0.5 chance level. The cause is a benchmark leak: the designated "OOD" class is one the model was trained on, so its examples sit inside the in-distribution fit set and the detector is penalized for correctly ranking them as familiar. Deleting the class and retraining 35 models across two domains raises the score to 0.911. We distill the contamination into a leak fingerprint -- near-perfect supervised decodability (AUROC approximately 1) coupled with unsupervised detection collapsed below 0.65 -- and validate it on a controlled battery of 52 settings (20 leaked, 32 clean) across ResNet-50 and ViT-B/16 on CIFAR-10/100, achieving sensitivity 18/20 and specificity 31/32 in embedding space; the matched fit-set-exclusion controls are perfect at 20/20. An in-the-wild audit of 24 standard near/far OOD benchmark pairs fires on exactly one (the intrinsically hard CIFAR-100 vs CIFAR-10 pair) and on no far-OOD pair, confirming specificity and that standard cross-dataset construction is clean. Under the corrected protocol, perturbation signals are decodable but not detectable: a supervised reader recovers the OOD signal (AUROC 0.87-1.00) while no unsupervised detector does, and the perturbation method does not improve on plain Mahalanobis distance. We provide a theoretical account of why and, for transparency, retract an earlier circular correlation. The contributions are a corrected protocol and a validated leak diagnostic, not a new OOD method.
