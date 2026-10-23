# When Reconstruction Is Not Enough: Doubly Robust Counterfactual and Interventional Mediation Analysis with Learned Multimodal Representations

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Cong Cao
- 机构：Yale University, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30220v1) · [PDF](https://arxiv.org/pdf/2610.30220v1)

## TLDR
The paper shows that reconstruction-trained multimodal representations can fail to preserve the information needed for causal identification—especially for interventional mediation—inducing first-order bias that doubly robust estimation and cross-fitting cannot remove, and proposes a workflow with diagnostics to detect representation insufficiency and avoid misleading causal conclusions.

## Abstract
Learned representations of high-dimensional multimodal health records are increasingly used to adjust for confounding, yet they are usually trained to reconstruct the data rather than preserve the information that causal identification requires. We study counterfactual outcomes under alternative treatments, including phenotype-specific effects and patient-level counterfactual risk profiles of the kind digital twins provide, and interventional direct and indirect effects under exposure-induced intermediate confounding. We give conditions under which a representation preserves identification and show that interventional mediation is more demanding than counterfactual comparison. We prove that no covariate-only training objective, whether reconstruction, contrastive, or physics-informed, can certify that a representation is sufficient, and that, in a linear structural model, a representation can lose arbitrarily little reconstruction accuracy yet induce arbitrarily large bias. We decompose the error of cross-fitted doubly robust estimators into a first-order representation bias, which neither double robustness nor cross-fitting removes, and a second-order remainder of nuisance-estimation errors, so coverage worsens as the sample size grows when the representation is insufficient. We propose a workflow combining modality-specific variational autoencoders trained outside the estimation sample, cross-fitted doubly robust estimators, locked phenotypes, select-then-confirm pathway analysis, portable representations, and diagnostics for representation insufficiency, exposure leakage, and sensitivity. In simulations, discarding a rare, moderately strong confounder gave indirect-effect intervals with 2% coverage at n = 3,000; reconstruction loss missed the problem, and a simple predictive diagnostic flagged it in every replicate.
