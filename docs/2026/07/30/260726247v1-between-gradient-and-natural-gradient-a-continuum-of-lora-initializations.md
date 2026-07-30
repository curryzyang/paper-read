# Between Gradient and Natural Gradient: A Continuum of LoRA Initializations

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Dianze Liu, Farshid Ghezelbash
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26247v1) · [PDF](https://arxiv.org/pdf/2607.26247v1)

## TLDR
This paper introduces Unified LoRA (ULoRA), a two-parameter family of gradient-based LoRA initializations that unifies existing methods and shows that the optimal level of curvature preconditioning is task-dependent, often lying strictly between previously published endpoints.

## Abstract
Low-rank adaptation (LoRA) fine-tunes large pretrained models at a fraction of the cost of full fine-tuning, but its performance depends strongly on how the adapters are initialized. Recent schemes initialize the adapters from the downstream loss gradient: some project the raw gradient onto its top directions, while others first whiten it with an estimate of the loss curvature. We show that these seemingly distinct methods are points on a single continuum: a two-parameter family of preconditioned gradient initializations, which we call Unified LoRA (ULoRA), governed by a spectral whitening exponent and an Adam-like diagonal exponent. Sweeping this family under a full learning-rate search, we find that no single fixed preconditioning strength dominates: the best operating point is task-dependent and frequently lies strictly inside the family, away from the published endpoints. Treated as an upper bound of this family, a tuned ULoRA configuration matches or exceeds full fine-tuning on all five GLUE tasks with RoBERTa-base and is competitive with the strongest baselines on GSM8K with LLaMA-2-7B. Our deployable, search-free variant, ULoRA-Auto, selects per-layer exponents from measured spectral statistics, approaches this upper bound at no additional search cost, and ranks at or near the top among deployable LoRA methods. Our results show that a principled design space for LoRA initialization and curvature preconditioning should be treated as a tunable dimension rather than a fixed design decision.
