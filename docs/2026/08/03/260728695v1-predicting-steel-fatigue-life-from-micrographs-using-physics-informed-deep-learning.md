# Predicting Steel Fatigue Life from Micrographs Using Physics-Informed Deep Learning

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Aryuemaan Kumar Chowdhury
- 机构：Indian Institute of Technology Hyderabad, Oscowl AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28695v1) · [PDF](https://arxiv.org/pdf/2607.28695v1)

## TLDR
TLDR: This paper presents a physics-informed deep learning computer vision framework that predicts the fatigue life of steels directly from optical micrographs by combining a seven-stage preprocessing pipeline, a 28-dimensional physics-based feature extractor, and a CNN with uncertainty quantification, achieving high accuracy on a synthetic benchmark and demonstrating methodological soundness with calibrated predictions.

## Abstract
Here is the plain text version optimized for arXiv's submission form. Custom macros (like \CV and \SI) have been converted to standard text/math so they render correctly on the webpage: Evaluating the fatigue life of structural steels conventionally requires mechanical testing lasting tens to hundreds of hours, making it impractical for rapid quality control. We present CV, a computer vision framework that estimates the fatigue life ($\log N_f$) of lightweight alloy steels directly from optical micrographs without physical testing.The pipeline features a seven-stage OpenCV preprocessing routine to remove artifacts, a 28-dimensional physics-informed feature extractor (quantifying crack morphology, grain structure, porosity, and texture), and a CNN regression model trained with a Gaussian negative log-likelihood (GNLL) loss to jointly predict $\log N_f$ and sample-specific uncertainty $\hatσ$.Evaluating three architectures (SE-CNN, ResNet-50, VGG-16) on a synthetic micrograph benchmark, ResNet-50 achieves $R^2 = 0.93$, RMSE = 0.18 log-cycles, and macro-F1 = 0.91. The GNLL objective reduces Expected Calibration Error by 76% compared to a mean-squared-error baseline (ECE: $0.089 \rightarrow 0.021$). Grad-CAM maps confirm the network attends to metallurgically meaningful microstructural features.Running in under 65 ms per image, the pipeline and synthetic dataset generator are open-sourced. Because validation relies entirely on synthetic micrographs, these results demonstrate methodological soundness under simulated conditions; a domain-transfer study on real field samples is the immediate next step.
