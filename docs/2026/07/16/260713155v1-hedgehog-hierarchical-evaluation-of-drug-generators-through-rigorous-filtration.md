# HEDGEHOG: Hierarchical Evaluation of Drug Generators Through Rigorous Filtration

- 区域：速读区
- 排名：14
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Daria A. Ryabchenko, Pavel Gurevich, Shamil Kadyrov, Daria Frolova, Kseniia Fedisheva, Sergei A. Nikolenko, Alexander Shapeev, Marina A. Pak
- 机构：Skolkovo Institute of Science and Technology, Ligand Pro
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13155v1) · [PDF](https://arxiv.org/pdf/2607.13155v1)

## TLDR
HEDGEHOG introduces a six-stage filtration benchmark for molecular generators that mimics industrial hit identification, revealing that only 0.65% of generated molecules survive all stages and exposing the gap between standard evaluation metrics and practical medicinal chemistry requirements.

## Abstract
Generative molecular models can support early drug discovery by proposing new candidate compounds de novo. In practice, useful candidates must balance target-relevant activity, synthetic accessibility, physicochemical properties, and other multiparameter design constraints. However, metrics commonly used to evaluate molecular generators only weakly reflect whether the generated compounds are medicinally plausible and suitable for downstream computation. This can produce false positives in model evaluation, incorrect assumptions, and inefficient use of computational resources. We introduce HEDGEHOG, a unified six-stage filtration benchmark that is inspired by industrial hit identification workflows: (i) preprocessing; (ii) physicochemical descriptor screening; (iii) structural alerts and graph-sanity checks; (iv) synthesis feasibility; (v) docking and binding affinity estimation; and (vi) three-dimensional pose and interaction checks. We evaluate 23 molecular generators across three model classes under a standardized protocol. Across 230,000 generated molecules, only 0.65% of initial molecules survive all stages. Our results expose a central limitation of current molecular generators: molecules that appear acceptable under isolated criteria rarely satisfy medicinal chemistry, synthesis, docking, and 3D pose filters simultaneously.
