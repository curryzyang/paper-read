# Neutrosophic Ensemble Classification for Uncertainty-Aware Bearing Fault Detection: Evidence from Laboratory and Variable-Speed Industrial Benchmarks

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Maikel Leyva-Vazquez, Dayron Rumbaut Rangel, Lorenzo Cevallos-Torres, Alexis Matheu Perez
- 机构：Universidad Bolivariana del Ecuador, Universidad Bernardo O'Higgins, Universidad de Guayaquil
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06880v1) · [PDF](https://arxiv.org/pdf/2610.06880v1)

## TLDR
The paper proposes a lightweight neutrosophic ensemble decomposition (T-hat, F-hat, entropy, and disagreement) for uncertainty-aware bearing fault detection and shows across corrected CWRU and variable-speed JNU benchmarks that predictive entropy adds useful error signal beyond truth/falsity but that simpler logistic-regression confidence often matches or outperforms the full decomposition, with Jensen-Shannon model fusion and envelope-spectrum fault frequencies offering further promise.

## Abstract
Machine learning classifiers for bearing fault detection produce scalar confidence scores that conflate confident errors with genuinely ambiguous predictions, and the conventional truth/falsity pair (F = 1 - T) is algebraically redundant by construction. We operationalize a refined neutrosophic decomposition of a Random Forest + XGBoost + Logistic Regression ensemble into four indicators -- T-hat (top-class evidence), F-hat (best-competitor evidence), predictive entropy I1-hat, and decision disagreement I2-hat -- evaluated on two bearing benchmarks (CWRU and JNU, 600-1000 rpm) under a leave-one-condition-out protocol. On CWRU, after correcting a file-to-class mapping error, the ensemble reaches 100.00 percent accuracy on three of four held-out loads (92.27 percent on the fourth), leaving too few errors for uncertainty analysis. On JNU, holding out 1000 rpm, accuracy collapses to 40.64 percent, below a majority-class baseline; Logistic Regression (57.91 percent) generalizes far better than the tree ensembles. I1-hat shows a robust association with error beyond T-hat/F-hat, while I2-hat contributes little; standalone Logistic Regression confidence outperforms the full decomposition, a boundary condition we report honestly. Two further results extend this: fusing a time-domain and a frequency-domain model of the same signal and scoring their Jensen-Shannon divergence beats that model own entropy (AURC 0.29 vs. 0.36 on the standard split; 0.54 vs. 0.73 under a harder single-condition reproduction), the only indicator moving correctly under a CWRU-versus-JNU distributional-shift contrast; and, on CWRU alone, literature-verified bearing fault frequencies, correctly demodulated via the envelope spectrum, separate most fault classes almost perfectly (99.57 percent) using three interpretable features. Code, logs, and figures are released for independent verification.
