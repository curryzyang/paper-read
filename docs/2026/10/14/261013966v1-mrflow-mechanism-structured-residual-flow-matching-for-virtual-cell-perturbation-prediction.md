# MRFlow: Mechanism-Structured Residual Flow Matching for Virtual Cell Perturbation Prediction

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Haojie Yang, Ran Su
- 机构：Tianjin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13966v1) · [PDF](https://arxiv.org/pdf/2610.13966v1)

## TLDR
MRFlow predicts single-cell perturbation responses as latent distribution transport, using mechanism-structured residual flow matching to move control cell populations toward perturbed populations and achieving top composite performance across gene and drug benchmarks.

## Abstract
Predicting cellular responses to chemical and genetic perturbations is a central test for AI virtual cells, yet many single-cell models reduce each condition to an average expression shift. This target is misaligned with perturbation biology: rare states, resistant subpopulations, and context-dependent effect sizes may coexist under the same intervention. MRFlow treats virtual-cell prediction as conditional transport between empirical single-cell measures. Control and perturbed cells are embedded in a variational latent state space, greedy low-cost supervision is constructed over detached minibatch states, and a conditional flow-matching vector field transports control populations toward perturbed populations. The field decomposes into a mechanism-structured affine dictionary, which recombines shared latent response operators with a low-rank condition-specific correction, and a spectrally controlled residual field for nonlinear cell-level variation. Genetic perturbations are encoded through a regulatory-graph GCN, chemical perturbations through Morgan fingerprints, and both enter the same conditional dynamics interface. Across eight gene and drug perturbation benchmarks, MRFlow attains the highest composite score while preserving competitive raw performance on differential-expression and distributional metrics. The results support latent distribution transport as a principled and empirically effective formulation for perturbation-aware virtual cell modeling.
