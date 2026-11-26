# Sparse Adaptation for In-Context Learning on Data Streams

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：João Neves, Afonso Lourenço, Lizy K. John, Eric P. Xing, João Gama
- 机构：The University of Texas at Austin, University of Porto, Carnegie Mellon University, Polytechnic of Porto
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33325v1) · [PDF](https://arxiv.org/pdf/2611.33325v1)

## TLDR
SAIL is a sparse-adaptation framework for tabular foundation models on evolving data streams that reuses the KV cache and only rebuilds a class-balanced, micro-cluster-based in-context support set when structural or predictive-performance drift signals indicate the current context is inadequate, reducing redundancy and computation while preserving recent structural information.

## Abstract
The Internet of Things (IoT) generates massive data streams, making edge computing essential for low-latency applications and 5G networks. Tabular foundation models (TFMs) enable adaptation through in-context examples rather than parameter updates, but evolving streams challenge context relevance and computational efficiency. This work introduces SAIL, a framework for sparse adaptation of TFMs that reuses the model's key--value cache between adaptation events. SAIL reconstructs its support set only when drifts in stream structure indicate potential context inadequacy, while the structural representation itself is updated by changes in predictive performance. SAIL combines prequential error monitoring with online, class-specific micro-clustering to detect changes in cluster mass, class separability, and feature-space coverage. Upon adaptation, a context budget is allocated proportionally to class mass, and the most recently updated micro-clusters provide representative observations for refitting. This limits context redundancy and computational cost while preserving recent structural information.
