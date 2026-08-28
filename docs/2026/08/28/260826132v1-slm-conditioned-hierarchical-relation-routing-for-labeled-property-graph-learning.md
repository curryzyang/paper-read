# SLM-Conditioned Hierarchical Relation Routing for Labeled Property Graph Learning

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Michal Podstawski
- 机构：NASK National Research Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26132v1) · [PDF](https://arxiv.org/pdf/2608.26132v1)

## TLDR
The paper introduces SLM-Conditioned Hierarchical Relation Routing, an architecture that uses a small language model to generate target-conditioned queries for hierarchically selecting graph messages within and across relationship types, producing bounded residual updates that refine a topology-GNN anchor for property-rich labeled graph learning.

## Abstract
Labeled property graphs combine relational structure with heterogeneous textual and categorical properties attached to both nodes and relationships. Conventional graph neural networks typically represent these properties as static feature vectors, limiting their ability to determine which semantic evidence should influence message propagation for a particular prediction target. We propose SLM-Conditioned Hierarchical Relation Routing, an architecture that integrates a small language model directly into graph message selection. A topology GNN provides a stable structural representation and prediction anchor. For each target node, incident messages combine the neighbor's structural state, node-property encoding, relationship-property encoding, and relationship type. A parameter-efficient SLM processes structured graph soft tokens and produces a target-conditioned routing query. This query first selects relevant messages within each relationship type and subsequently routes information across relation-level summaries. The resulting representation provides a bounded residual update to the topology anchor, preserving structural evidence while allowing contextual semantic information to modify the prediction. The architecture supports interpretable analysis at both the neighbor and relationship-type levels and provides a general mechanism for integrating language-derived semantics into property-rich graph learning.
