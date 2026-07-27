# Self-Poisoning in Adaptive Out-of-Distribution Detection: A Sharp-Threshold Theory and Certified Label-Free Calibration

- 区域：速读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Vishnu Bindu Balachandran
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21673v1) · [PDF](https://arxiv.org/pdf/2607.21673v1)

## TLDR
This paper proves that adaptive out-of-distribution detectors undergo a predictable phase transition to complete self-poisoning when the slope of their admission kernel exceeds one, and introduces a certified admission gate and drift-robust calibration procedure that provably remove this transition and restore label-free false positive rate control, while also establishing a fundamental power ceiling due to the indistinguishability of drift and contamination.

## Abstract
Test-time adaptive out-of-distribution (OOD) detectors update a memory bank from the unlabelled stream. We show this adaptation obeys a provable dynamical law. Modelling bank impurity as a generalized Pólya urn, we prove almost-sure convergence to a mean-field equilibrium whose slope acts as a reproduction number. Below one, impurity stays benign. Above one, the bank is fully poisoned and the detector collapses. The measured admission kernel is affine ($R^2 \ge 0.996$) with slope just below one in every encoder family (a protocol signature), so this detector class is near-critical by design, and across 96 settings the predicted threshold matches the empirical collapse, where ungated dictionaries lose up to $0.163$ AUROC. We then prove that a certified admission gate, reading only a frozen reserve, severs the feedback loop and removes the transition at every contamination rate, even adversarially, while controlling false positives label-free. For the complementary static-calibration failure under drift we give CDC, which restores nominal FPR label-free on all tested drift-affected cells. Finally we prove a two-world impossibility theorem. Drift and contamination are indistinguishable without labels, forcing a closed-form power ceiling our procedure approaches. Together these give a complete possibility/impossibility characterization of label-free adaptive OOD detection.
