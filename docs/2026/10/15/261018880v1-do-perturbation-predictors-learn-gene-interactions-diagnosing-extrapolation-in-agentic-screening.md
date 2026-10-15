# Do Perturbation Predictors Learn Gene Interactions? Diagnosing Extrapolation in Agentic Screening

- 区域：速读区
- 排名：14
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Ziyuan Gao
- 机构：University of Cambridge
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18880v1) · [PDF](https://arxiv.org/pdf/2610.18880v1)

## TLDR
This paper introduces additive disagreement (AD)—the deviation of a model’s predicted combinatorial perturbation effect from the sum of observed single-gene effects—to show that specialized perturbation predictors often fail to outperform a simple additive baseline on unseen gene combinations and that AD is a more consistent indicator of unreliable interaction extrapolation than standard OOD/uncertainty signals, making it useful for agentic screening.

## Abstract
High-throughput perturbation screens increasingly use machine-learning models to predict the effects of gene combinations that were never measured. A difficult case arises when both genes in a test pair were seen individually during training, but their combination was not. In this setting, standard OOD methods often fail because neither gene appears unfamiliar on its own. We therefore compare each model prediction with a simple additive prediction obtained by summing the two observed single-gene effects. The difference between them, which we call additive disagreement (AD), measures how much extra interaction effect the model introduces for an unseen combination. Across eight prediction methods and three Perturb-seq datasets, specialised neural predictors do not consistently outperform this simple additive baseline. More importantly, predictions with larger deviations from the additive baseline tend to have larger errors. Conventional output-based and embedding-based confidence signals are inconsistent across datasets and models, whereas AD remains informative across all evaluated compositional settings. We further study how this signal can guide decisions in an agentic perturbation-screening workflow. The code is available at https://github.com/zygao930/OOD.
