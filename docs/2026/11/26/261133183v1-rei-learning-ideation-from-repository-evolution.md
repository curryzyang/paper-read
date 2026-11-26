# REI: Learning Ideation from Repository Evolution

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Muyu Zou, Xiang Feng, Yufei Xu, Shanshan Ye, Zulong Chen, Lingyu Mu, Jinxin Hu, Jing Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33183v1) · [PDF](https://arxiv.org/pdf/2611.33183v1)

## TLDR
The paper proposes REI, a repository-evolution-driven ideation framework that learns reusable ideation policies from code changes and their subsequent utility signals, and introduces Semantic Prior Optimization and Debiasing (SPOD) to prevent semantic diversity collapse and improve ideation quality, method diversity, cross-task generalization, and long-tail exploration.

## Abstract
As AI systems become increasingly capable of executing and evaluating experiments, ideation is emerging as a bottleneck in automated scientific and engineering iteration. In many real-world domains, useful ideas are sparse and their validation is costly, making direct online exploration inefficient. We observe that repository evolution provides a scalable source of reusable technical experience: code changes record concrete technical hypotheses, while subsequent revisions, adoption, and reuse provide signals about their utility. Based on this observation, we propose REI, a Repository Evolution-driven Ideation framework that learns reusable ideation policies from repository evolution, injecting domain-specific technical experience into model parameters and reducing reliance on costly trial-and-error. We further identify a hidden failure mode in quality-driven ideation optimization: semantic diversity collapse. Although generated ideas can remain lexically diverse, they increasingly concentrate in a small number of dominant method families, limiting cross-task generalization and long-tail exploration. To address this problem, we introduce Semantic Prior Optimization and Debiasing (SPOD), a diversity-preserving alignment mechanism that makes method identity explicit, corrects category-level reward bias, and limits redundant accumulation within the same method family while retaining strong representatives. Experiments on public benchmarks and a real-world industrial setting demonstrate improvements in ideation quality, method diversity, cross-task generalization, and long-tail exploration.
