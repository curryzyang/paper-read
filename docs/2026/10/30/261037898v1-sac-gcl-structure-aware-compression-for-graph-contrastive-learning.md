# SAC-GCL: Structure-Aware Compression for Graph Contrastive Learning

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Muhammad Ifte khairul Islam, Tanvir Hossain, Esra Akbas
- 机构：Georgia State University, Texas A&M University- Texarkana
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37898v1) · [PDF](https://arxiv.org/pdf/2610.37898v1)

## TLDR
SAC-GCL is a graph contrastive learning framework that replaces stochastic augmentation with structure-aware view generation by decomposing graphs into cohesive subgraphs (e.g., k-cores and k-trusses) and compressing them into supernode-based coarsened views, which are hierarchically encoded to learn more robust and discriminative representations for graph classification.

## Abstract
Graph Contrastive Learning (GCL) has achieved remarkable success in self-supervised representation learning by maximizing agreement between augmented views of a graph. Although augmented view generation is the central step in GCL, existing models rely on stochastic augmentation of the input graph, such as edge perturbation and node masking, which lack structural awareness and frequently destroy critical topology or introduce semantically inconsistent views. While recent adaptive methods improve upon random perturbations, they primarily operate on localized node or edge neighborhoods and fail to capture higher-order, macro-level structural organization crucial for graph classification. To address this limitation, we propose Structure-aware Compression for Graph Contrastive Learning (SAC-GCL), a novel framework that employs structural decomposition and graph compression as a principled view generation strategy. Moving beyond random augmentations, SAC-GCL leverages structural decomposition techniques to extract cohesive subgraphs and condense them into supernodes, constructing coarsened graph views that preserve local density and capture higher-level structural patterns while reducing noise and redundancy. We leverage multiple cohesive subgraph models to derive complementary views of the graph, each capturing distinct structural properties. To capture multi-resolution information, a hierarchical view encoder processes these compressed views by initializing super-node features with shared-weight cohesive subgraph embeddings. Our results from extensive experiments on six benchmark datasets demonstrate that structure-aware compression provides a powerful alternative to random perturbations, yielding more robust and discriminative graph representations for graph classification tasks.
