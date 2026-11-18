# When Does Discrete Ricci Curvature Help? An Edge-Level Analysis of Curvature-Enhanced GCNs for PPI Prediction

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Clara Joswig, Elham Gholamzadeh, Ghazal Mostofi, Nico Scherf
- 机构：Max Planck Institute for Human Cognitive and Brain Sciences, ETH Zurich, Center for Scalable Data Analytics and Artificial Intelligence (ScaDS.AI)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21849v1) · [PDF](https://arxiv.org/pdf/2611.21849v1)

## TLDR
Curvature-enhanced GCNs improve aggregate PPI prediction not by mitigating over-squashing at bottlenecks, but by sharpening cluster separation—boosting low-degree/intra-cluster edges while degrading low-curvature inter-cluster edges.

## Abstract
Curvature-enhanced graph convolutional networks (CGCN) incorporate Ollivier-Ricci curvature (ORC), grounded in optimal transport theory, into message passing, motivated by the claim that curvature-weighted edges alleviate "over-squashing" at structural bottlenecks. But does CGCN's improvement actually come from mitigating over-squashing? We investigate this on four real-world protein-protein interaction (PPI) datasets, comparing CGCN against a standard GCN at the level of individual edges rather than aggregate metrics alone. While CGCN improves aggregate AUC, AUPR, and F1 across all four datasets, this gain is concentrated almost entirely on low-degree edges, while performance on low-curvature (bottleneck) edges systematically degrades in three of four datasets, the opposite of what the over-squashing motivation predicts. Examining the learned edge-weight function directly, together with clustering-validity metrics, edge-distance ratios, and a layer-depth ablation across four depths, we find evidence for an alternative account: curvature-weighting sharpens the separation between clusters, which improves intra-cluster predictions at the cost of inter-cluster (bottleneck) ones. We test this account against topologically defined communities rather than the classification labels used elsewhere. Additionally, we offer practical guidance on when to prefer CGCN over standard GCN, depending on whether intra- or inter-cluster predictions matter most.
