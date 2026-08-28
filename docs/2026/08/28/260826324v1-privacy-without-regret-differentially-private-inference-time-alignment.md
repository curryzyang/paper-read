# Privacy Without Regret: Differentially Private Inference-Time Alignment

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Ishi Jain, Nandini Bhattad, Sayak Ray Chowdhury
- 机构：Indian Institute of Technology Kanpur
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26324v1) · [PDF](https://arxiv.org/pdf/2608.26324v1)

## TLDR
Adding calibrated noise to reward scores before Best-of-N selection yields differentially private inference-time alignment algorithms (PrivBoN and PrivITP) that simultaneously prevent reward hacking and protect sensitive preference data, matching the information-theoretic regret skyline with zero additional alignment cost.

## Abstract
Best-of-N (BoN) sampling is the simplest and most widely deployed inference-time alignment strategy, but it suffers from two distinct problems: reward hacking, in which the selected response exploits errors in the proxy reward model, and the absence of any privacy protection for the sensitive human preference data used to train that reward model. We show that a single intervention-adding calibrated noise to reward scores before selection-resolves both. Our first result, Private Best-of-N (PrivBoN), establishes that Gumbel noise at an appropriate scale simultaneously provides $ε$-differential privacy and implements KL-regularized alignment. Whenever the privacy budget exceeds a critical threshold $ε^*$, the privacy-mandated noise is the regret-optimal regularization, and privacy imposes zero additional alignment cost-matching the information-theoretic skyline of Huang et al. (2025). Because $ε^*$ depends on an unknown coverage coefficient, we introduce Private Inference-Time Pessimism (PrivITP), which combines $χ^2$-regularized rejection sampling with a two-phase Gaussian mechanism. PrivITP achieves ex-post $(ε,δ)$-DP with a privacy cost independent of the number of responses $n$, cleanly decouples the regularization parameter from the privacy parameter, and attains the skyline up to a noise-inflation term. Experiments across several language models, datasets, and reward models confirm our results: PrivBoN and PrivITP are scaling-monotonic (unlike BoN, which degrades past a critical $n$), and PrivITP matches or outperforms PrivBoN at equivalent privacy levels, with the largest gains in the strong-privacy regime.
