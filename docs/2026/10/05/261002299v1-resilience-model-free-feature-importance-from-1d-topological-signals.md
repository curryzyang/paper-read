# $Ψ$-Resilience: Model-Free Feature Importance from 1D Topological Signals

- 区域：速读区
- 排名：8
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Fabian Galis, Darian Onchis, Pedro Real Jurado
- 机构：West University of Timișoara, University of Sevilla
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02299v1) · [PDF](https://arxiv.org/pdf/2610.02299v1)

## TLDR
Ψ-Resilience is a model-free feature-importance method that scores each feature by the 0-dimensional topological persistence of its class-conditional density-disagreement signal, aggregating only robust separation structures that survive up to a user-set scale and enabling auditable, distribution-level feature rankings without relying on a predictive model.

## Abstract
We introduce $Ψ$-Resilience, a model-free feature importance method that derives explanations directly from the data itself via 1D topological signals. Our method constructs a class-disagreement landscape by estimating class-conditional densities and taking their pointwise absolute difference along the feature axis. Then, the 0-dimensional persistence of this 1D signal defines a resilience functional that aggregates only those topological features that survive perturbations up to a robustness scale which is set by the user. This gives us a context-robust importance score that is inherently auditable via the underlying 1D landscapes and their persistence. We evaluate our method on both synthetic and real datasets. On synthetic generators with specified ground-truth importance, $Ψ$-Resilience recovers the ranking of features with high fidelity, achieving Spearman rank correlations up to 0.8 and performing competitively with multiple feature importance methods, including SHAP and mutual information. On real datasets with no known ground truth, our technique agrees with these methods, with correlations up to 0.9. These results show that $Ψ$-Resilience is a stable explanation method that enables rigorous, distribution-level auditing of feature importance without relying on a predictive model.
