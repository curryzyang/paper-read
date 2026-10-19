# Generative adversarial networks with Monte Carlo dropout uncertainty quantification for structural health monitoring: Fibre Bragg grating data augmentation comparison in Hawk T1A aircraft

- 区域：速读区
- 排名：9
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Alvaro Peiro, Marios Impraimakis
- 机构：University of Bath
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22436v1) · [PDF](https://arxiv.org/pdf/2610.22436v1)

## TLDR
This paper develops an uncertainty-aware conditional GAN with Monte Carlo dropout for generating and evaluating synthetic fibre Bragg grating and acceleration vibration signals, validated on Hawk T1A aircraft structural health monitoring data to assess whether the augmented signals improve damage classification.

## Abstract
The signal generation capabilities of a novel data augmentation framework are examined in aerospace structures. First, the framework learns class-conditional temporal and spectral characteristics of the measured structural responses. It uses conditional generative adversarial network training and Monte Carlo dropout uncertainty quantification as a Bayesian approximation. This step enables stochastic signal synthesis and uncertainty quantification. Second, the generated responses are rigorously compared against experimental measurements across time, frequency, uncertainty, variability, and feature domains to assess physical realism, statistical consistency, and distributional fidelity. Finally, the synthetic data are evaluated to determine whether they should be incorporated into a supervised damage classification workflow. The framework is validated on the full-scale benchmark dataset from a BAE Systems Hawk T1A aircraft tested at the University of Sheffield's Structural Dynamics Laboratory for Verification and Validation. The test involves acceleration, fibre Bragg grating strain, and nonlinear dynamic response measurements. The results demonstrate that the model accurately captures dominant structural dynamics, it guides on signal use for classification improvement based on uncertainty characteristics, and it provides meaningful uncertainty estimates linked to signal complexity and excitation characteristics. Importantly, the framework offers a realistic generative modelling plan as a robust digital twin component for data-driven structural health monitoring, supporting resilient decision-making for condition assessment in safety-critical aerospace systems.
