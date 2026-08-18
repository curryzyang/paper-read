# Graph-MambaNav: Spatial-Temporal Graph Mamba Leveraging Object-Relation Knowledge for Object-Goal Navigation

- 区域：速读区
- 排名：3
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Leyuan Sun, Genxin Chen, Linwei Ye, Yan Zhang, Xi Kan, Yanfei Sun
- 机构：Wuxi University, Wuxi Key Laboratory of Artificial Intelligence and Security, Nanjing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13723v1) · [PDF](https://arxiv.org/pdf/2608.13723v1)

## TLDR
Graph-MambaNav introduces a target-aware spatial-temporal graph encoding framework that uses LLM-derived object-relation knowledge to define node ordering and edge weights in Graph-Mamba, enabling selective Mamba-based scanning to prioritize target-relevant objects and improve object-goal navigation in simulation and real-world deployment.

## Abstract
Object-goal navigation requires an agent to reason over object relationships and prioritize target-relevant objects for efficient decision making in unseen environments. While existing graph-based methods incorporate target-awareness at the feature or attention level, they remain permutation-invariant and lack an explicit mechanism to control information propagation order, limiting their ability to model target-dependent importance and long-range dependencies. In contrast, Graph-Mamba highlights that node prioritization through sequence ordering is critical for effective global reasoning. In this work, we investigate the node prioritization mechanism in Graph-Mamba and study its role in object navigation. We propose Graph-MambaNav, a target-aware spatial-temporal graph encoding framework that introduces a heuristic ordering over objects based on their relevance to the target, allowing more informative objects to be processed later to aggregate richer context. Both node ordering and edge weights are initialized from LLM-derived commonsense object relationships, providing a unified prior for structured reasoning. A spatial module integrates local message passing with global GraphMamba-based selective scanning, while a temporal module applies Mamba-based sequence modeling over object-wise temporal orders, allowing selective aggregation of historical context for long-range temporal reasoning. Experiments on AI2-THOR and RoboTHOR demonstrate improved navigation performance with generalization, and additional real-world robot deployment further validates the effectiveness of our proposed approach.
