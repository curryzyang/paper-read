# Matched but Not Better: An Equivalence-Tested Benchmark of Quantum Machine Learning on Six Clinical Datasets and the QML-Health-READY Reporting Framework

- 区域：速读区
- 排名：14
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Mohammed Siraj B, Gousia Habib, Ruban S
- 机构：St Aloysius (Deemed to be University), Bahrain Polytechnic
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05442v1) · [PDF](https://arxiv.org/pdf/2611.05442v1)

## TLDR
In a paired, equivalence-tested benchmark across six clinical datasets, correctly configured quantum classifiers matched but did not outperform tuned classical models—finite-shot estimation was their main practical cost and configuration errors could reverse conclusions—prompting the QML-Health-READY reporting framework for credible QML claims.

## Abstract
Background: Quantum machine learning (QML) is promoted for clinical prediction, but comparisons with classical models are rarely paired or tested for equivalence. Methods: We compared a quantum-kernel support vector machine (QSVM; 4 qubits, tuned bandwidth) and a variational quantum classifier (VQC) with five tuned classical models across six public clinical datasets. All models used identical four-component inputs and 25 cross-validation splits. Paired AUROC differences were assessed using a corrected resampled t-test, Holm-adjusted equivalence tests (margins: +/-0.02 and +/-0.05), and random-effects pooling. Ablation, noise, finite-shot, and implementation-fault analyses were conducted. We propose QML-Health-READY, an eight-domain reporting framework. Results: Neither quantum model significantly outperformed any classical comparator. Pooled across datasets, QSVM differed from the kernel-matched radial basis function (RBF) SVM by -0.006 AUROC (95% CI: -0.017 to +0.004), equivalent to +/-0.02. VQC differed from the best classical model by -0.007 (95% CI: -0.019 to +0.004). QSVM was equivalent to RBF SVM within +/-0.05 in four of six datasets but was significantly worse than the best classical model on NHANES 2017-18 (-0.076). A classically trivial product-state kernel performed as well as the entangling kernel. With depolarizing noise (p = 0.01) and 1,024 shots per kernel entry, QSVM AUROC decreased by 0.054 (95% CI: 0.036 to 0.071). Untuned bandwidth produced near-chance AUROC (0.48-0.59). Conclusions: Correctly configured quantum classifiers approached but did not exceed tuned classical models. Finite-shot estimation, rather than gate noise, was their main practical cost, while configuration errors could reverse conclusions. QML-Health-READY defines reporting requirements for credible claims.
