# CoASFL: Coupled Consistency Optimization for Asynchronous Split Federated Learning

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Junhao Cheng, Yunming Liao, Hongli Xu, Yang Xu, Zuan Xie
- 机构：University of Science and Technology of China
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26992v1) · [PDF](https://arxiv.org/pdf/2610.26992v1)

## TLDR
CoASFL is an inconsistency-aware asynchronous split federated learning framework that jointly optimizes activation merging and model aggregation to mitigate horizontal and vertical inconsistencies caused by system and statistical heterogeneity, thereby accelerating training and improving accuracy.

## Abstract
Split Federated Learning (SFL) has emerged as a promising paradigm for training large-scale deep models on resource-constrained edge devices. Although asynchronous SFL alleviates the straggler bottleneck caused by system heterogeneity, it inevitably introduces two coupled dimensions of inconsistency: horizontal inconsistency across clients and vertical inconsistency between clients and the server. These inconsistencies, further exacerbated by statistical heterogeneity, result in biased activation representations, model divergence, and severe client drift. To address these challenges, we propose CoASFL, an inconsistency-aware asynchronous SFL framework that incorporates a dynamic activation merging mechanism and a consistency-aware model aggregation mechanism. Specifically, CoASFL constructs more consistent activation sequences from heterogeneous clients to alleviate horizontal inconsistency, and dynamically adjusts aggregation weights according to client participation frequencies and progress gaps to mitigate vertical inconsistency. By jointly coordinating activation-level and model-level consistency, CoASFL effectively suppresses inconsistency propagation during asynchronous training. Extensive experiments on an 80-device heterogeneous edge testbed demonstrate that CoASFL consistently outperforms state-of-the-art SFL approaches, accelerating training by 1.61$\times$ to 3.74$\times$ and improving final model accuracy by up to 3.26\% under heterogeneous scenarios.
