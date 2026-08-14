# Exploring Oversmoothing with Householder Matrices

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Bhaskar Karol
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12514v1) · [PDF](https://arxiv.org/pdf/2608.12514v1)

## TLDR
HouseGNN replaces standard GCN updates with per-node Householder reflections followed by GroupSort, yielding a piecewise-orthogonal, norm-preserving GNN layer that provably avoids the progressive node-representation collapse responsible for oversmoothing in deep graph networks.

## Abstract
Deep graph neural networks(GNNs) suffer from oversmoothing- a progressive collapse of node representation towards a low information subspace as network depth increases because the normalized graph propagation operator is repeatedly applied directly to the hidden representations. In this work we study Householder Graph Neural Network (HouseGNN). Rather than updating the hidden state like standard GCN, HouseGNN uses the aggregated neighbourhood message solely to estimate a reflection direction; the node embedding is then updated by a Householder reflector followed by GroupSort, yielding a piecewise orthogonal layer that preserves Euclidean norm at every node and at every depth. We prove three core properties: (i) every internal layer preserves the node-wise Euclidean norm; (ii) the Householder reflector is scale scale and sign-invariant in the message; and (iii) pairwise distance between nodes can change through mismatch between node-wise orthogonal operators.
