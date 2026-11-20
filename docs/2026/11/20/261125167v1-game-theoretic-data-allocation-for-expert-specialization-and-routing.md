# Game-Theoretic Data Allocation for Expert Specialization and Routing

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Mark Lovett, Denis Lim, Soroush Vosoughi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25167v1) · [PDF](https://arxiv.org/pdf/2611.25167v1)

## TLDR
InflEns is a mixture-of-LoRA-experts framework in which expert training allocations and inference routing both arise from the same game-theoretic location game in a fixed prompt-trait space, enabling inspectable, gate-free expert specialization that matches learned gates and allows targeted safety retraining.

## Abstract
Can the allocation used to train experts also predict which expert will perform best on a prompt? Such a connection would make the intended division of labor inspectable before training and allow the allocation itself to guide inference. We introduce InflEns, a mixture of LoRA experts whose training weights and inference routes come from the same location game in a fixed prompt-trait space. Players choose positions to maximize their expected shares of the prompt distribution, without using expert losses. We utilize the game's kernel-general theoretical criterion for when co-located positions become locally unstable to separation. We evaluate InflEns on a corpus assembled from seven safety-related benchmarks, which demonstrates that the highest-share expert has the lowest held-out response negative log-likelihood (NLL) on approximately 90% of prompts across four kernels under a sharpened simplex representation, compared with approximately 15% after permuting allocations across prompts. We demonstrate that the method performs comparably to published learned gates without having to train an explicit gate on the experts. Because the router is fixed, we can trace harmful behavior to a single expert and retrain only that expert, which lowers HarmBench attack success from 0.51 to 0.02 while keeping instruction following. The game also gives us several controls over how the experts specialize, including the kernel choice and its parameters, the trait-space geometry, and the number of experts. Importantly, InflEns is a general framework that can be extended to any encoder and data distribution.
