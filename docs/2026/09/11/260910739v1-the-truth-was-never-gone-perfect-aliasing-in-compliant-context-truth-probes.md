# The Truth Was Never Gone: Perfect Aliasing in Compliant-Context Truth Probes

- 区域：速读区
- 排名：11
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Dylan Jayabahu
- 机构：University of Waterloo
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10739v1) · [PDF](https://arxiv.org/pdf/2609.10739v1)

## TLDR
Compliant-context truth probes are perfectly aliased with prescribed-action probes, so their failure on rival contexts does not imply truth is absent—randomized codebooks plus mixed ally/rival fitting can still linearly recover the truthful direction (AUROC ≈ 1.000) even in a reward-trained deceptive policy.

## Abstract
A truth probe fitted where truthful reporting and a task's prescribed action coincide cannot distinguish those targets from its fitting labels alone. We call this failure of semantic identification perfect aliasing. In a controlled binary reporting game, truth and prescribed-action probes fitted on compliant contexts solve the same optimization. On rival contexts their labels are complements, forcing their AUROCs to sum to one; this identity holds across 751 cell-layer pairs to floating-point precision. We separate prescribed output symbols from semantic action using randomized codebooks, then separate truth from prescribed action by fitting on mixed compliant and rival contexts. For a reward-trained Gemma-2-9B policy that answers falsely on all evaluated rival trials, the conventional probe scores $0.006 \pm 0.005$ AUROC across three training seeds, while mixed-fit probes score $1.000$ on the same held-out activations. Mixed fitting uses more training examples and access to labelled rival contexts, so this comparison establishes linear recoverability rather than isolating the benefit of decorrelation. We also show that two compliant-fit probes, both perfect in-distribution, score $0.080$ and $0.986$ on the same rival activations. The findings concern what a probe measures: they do not establish preserved functional belief, causal use of the recovered direction, or a deployable deception detector. Code and aggregate results accompany the paper.
