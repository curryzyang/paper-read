# D-FROST: Decentralized Federated pRompt-tuning via Optimal tranSporT for Non-IID and Imbalanced Data

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Quan Minh Nguyen, Hoang M. Ngo, Trong Nghia Hoang, My T. Thai
- 机构：University of Florida, Washington State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01802v1) · [PDF](https://arxiv.org/pdf/2609.01802v1)

## TLDR
D-FROST proposes a decentralized federated prompt-tuning algorithm that uses optimal transport to align and merge heterogeneous, set-valued prompt sets across clients, with theoretical convergence guarantees and strong empirical results on non-IID and imbalanced data.

## Abstract
Prompt tuning provides a parameter-efficient way to adapt foundation models (FMs) by freezing the pretrained backbone and updating only a small set of learnable prompts. This property makes prompt tuning especially suitable for decentralized federated learning (DFL), where exchanging full-model updates can be prohibitively expensive. However, prompt tuning in DFL introduces new challenges. Prompt sets learned from heterogeneous local data may not be index-wise aligned, making standard decentralized averaging unsuitable. In addition, the algorithm should be theoretically guaranteed to achieve consensus and make progress toward the shared objective. In this work, we provide the first study of prompt tuning in DFL. We formulate decentralized prompt tuning as a Wasserstein-based optimization problem over prompt measures, which captures the set-valued structure of prompts. We then propose D-FROST, an optimal-transport-based (OT-based) decentralized prompt-tuning algorithm that merges neighborhood prompts into compact representative prompt sets through transportation-based matching. We further analyze D-FROST by bounding the Wasserstein consensus error across clients, and establishing convergence of the network-level prompt barycenter to a neighborhood of stationarity. Experiments under heterogeneous client data demonstrate the effectiveness of D-FROST for decentralized prompt tuning.
