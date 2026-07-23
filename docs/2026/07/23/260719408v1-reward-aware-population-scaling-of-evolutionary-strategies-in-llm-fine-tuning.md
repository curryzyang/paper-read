# Reward-Aware Population Scaling of Evolutionary Strategies in LLM Fine-Tuning

- 区域：速读区
- 排名：6
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Sung Cho, Gyubin Han
- 机构：University of Pennsylvania
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19408v1) · [PDF](https://arxiv.org/pdf/2607.19408v1)

## TLDR
The paper shows that the conflicting population-size requirements in evolutionary-strategy fine-tuning of LLMs—small for cross-entropy reward but large for binary reward—stem from reward granularity and z-score advantage normalization rather than an intrinsic population limit, with the failure of small populations being an implementation artifact that can be resolved by disabling normalization.

## Abstract
Using Evolutionary Strategies (ES) for fine-tuning large language models is attractive because it is memory-efficient, parallel, and compatible with black-box or discrete rewards. Yet its population-size conclusions conflict sharply: fine-tuning with cross-entropy (CE) reward succeeds with $N=1$, while binary-reward training often needs $N \approx 30$. We show this gap is largely about reward design and normalization, not population size. In the capable-model regime we study, z-score advantage normalization can cause $N=2$ to fail. Disabling normalization lets binary-reward ES with $N=2$ improve on GSM8K and TREC across capable models spanning 0.5B-7B, where the normalized variant collapses or degrades. This small-$N$ risk is set by reward granularity: binary accuracy reward induces a zero-advantage probability $q$ that depends in closed form on base accuracy, batch size, and intra-pair correctness correlation; a zero-training probe on Qwen2.5-Instruct/GSM8K matches the formula with mean absolute error 0.020 across 12 configurations and finds the availability threshold $N_{\mathrm{avail}}$ to be small in this capable-model regime. The implication is not that $N=2$ is universally sufficient, but that small-population failure in capable-model binary ES can be an implementation artifact rather than an intrinsic population limit.
