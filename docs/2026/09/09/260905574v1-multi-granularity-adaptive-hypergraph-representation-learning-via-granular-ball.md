# Multi-granularity Adaptive Hypergraph Representation Learning via Granular-ball

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Sen Zhao, Yifan Guan, Jinyuan Ni, Gaojie Xu, Zhang Xu, Xiaoyu Lian, Yi Liu, Yi Wang, Wei Wang
- 机构：Chongqing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05574v1) · [PDF](https://arxiv.org/pdf/2609.05574v1)

## TLDR
MGHRL proposes an adaptive granular-ball-based multi-granularity hypergraph representation learning framework that generates hyperedges via coarse-to-fine splitting and integrates cross-granularity features with a hierarchical reversible multi-column network, significantly outperforming baselines on benchmark datasets.

## Abstract
Hypergraph representation learning aims to capture high-order information in graphs by constructing hyperedges that simultaneously connect multiple nodes. These hyperedges adapt to the graph's topological features, facilitating the extraction of high-order relationships at multiple granularities. Most prior work relies on predefined definitions to generate hyperedges, overlooking the diversity in graph topological structures and the multi-granularity characteristics of hyperedges. As a result, this limits their ability to effectively and adaptively discover high-order relationships and efficiently process complex structural information. To address this limitation, we propose a novel framework called \underline{M}ulti-\underline{G}ranularity \underline{H}ypergraph \underline{R}epresentation \underline{L}earning (MGHRL). MGHRL introduces an Adaptive Granular Hypergraph Generation strategy, which generates hyperedges at multiple levels of granularity through the adaptive splitting of granular-ball, effectively capturing high-order relationships based on the graph's topological structure. Additionally, we propose a Multi-Granularity Hypergraph Network with multiple sub-networks, capturing features from hyperedges at different granularities and integrating them via hierarchical reversible connections. Experimental results show that MGHRL significantly outperforms baseline models on benchmark datasets.
