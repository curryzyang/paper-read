# Uncertainty calibration in Bayesian M/EEG source imaging

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Ismail Huseynov, Mohammad Orabe, Srikantan Nagarajan, Stefan Haufe
- 机构：Charité-Universitätsmedizin Berlin, Physikalisch-Technische Bundesanstalt Braunschweig und Berlin, Technische Universität Berlin, University of California San Francisco
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.06979v1) · [PDF](https://arxiv.org/pdf/2611.06979v1)

## TLDR
This paper presents a simulation-based framework for evaluating and recalibrating uncertainty in Bayesian M/EEG source imaging, showing that SBL with S-FLEX provides better localization, tighter posterior uncertainty, and closer-to-nominal coverage than BMN with sLORETA, while post-hoc isotonic recalibration further improves credible-region calibration.

## Abstract
M/EEG source imaging requires accurate localization and reliable uncertainty estimates, yet posterior credible regions are rarely assessed for empirical calibration. We present a simulation-based framework for uncertainty quantification and calibration of empirical Bayesian inverse methods with closed-form conditional Gaussian posterior summaries. We compare Bayesian minimum norm (BMN) with sLORETA depth weighting and sparse Bayesian learning (SBL) with sparse basis field expansions (S-FLEX). S-FLEX allows retained coefficients to contribute nonzero marginal posterior variance at locations where voxel-wise SBL yields degenerate variances. For BMN, we derive joint source- and noise-variance updates through evidence maximization. We test whether adaptive noise learning yields near-calibrated uncertainties. Both methods retain residual miscalibration, motivating post-hoc isotonic recalibration of credible-region levels using empirical coverage. Simulations assess fixed- and free-orientation models across signal-to-noise ratios (SNR), source sparsity levels, and subject-specific head models, using oracle, baseline-estimated, and adaptively learned noise. Before recalibration, SBL+S-FLEX yields lower Wasserstein localization error, smaller posterior uncertainty, and coverage closer to nominal credibility than BMN+sLORETA. Isotonic recalibration improves both methods, with larger gains for conservative BMN+sLORETA posteriors; transfer across mismatched SNR, sparsity, and head models remains condition dependent. Noise specifications yield broadly consistent reconstruction and uncertainty trends within each estimator. In real auditory MEG data, SBL+S-FLEX provides more focal localization and tighter uncertainties than BMN+sLORETA, suggesting greater statistical power for identifying bilateral auditory sources.
