# Adaptive Depth Aggregation in Graph Transformers for Long-Range Graph Reasoning

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yifeng Lu, Zhen Wang
- 机构：Sun Yat-sen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08500v1) · [PDF](https://arxiv.org/pdf/2611.08500v1)

## TLDR
The paper proposes **AttnRes-GT**, a node-adaptive depth aggregation mechanism using Attention Residuals that lets each node reweight graph-propagation and FFN contributions across layers, improving long-range graph reasoning in Graph Transformers such as GPS and GRIT.

## Abstract
Graph Transformers improve long-range node-to-node communication through global or structure-aware interactions. However, improving cross-node communication does not determine how computations produced at different depths should be combined. Standard residual streams accumulate successive computations with fixed unit coefficients shared across nodes. This fixed aggregation is a residual-interface constraint: once intermediate contributions have been produced, the interface cannot explicitly reweight them by node. We hypothesize that this constraint can create a depth-wise aggregation mismatch when the relative utility of these intermediate contributions varies across nodes and structural contexts. To study this hypothesis, we formalize Graph Transformer residual computation as a causal node-wise history of graph-propagation and feed-forward network (FFN) contributions, making depth aggregation an explicit interface choice. We realize node-adaptive aggregation over this history with Attention Residuals (AttnRes) while preserving the backbone's graph-propagation and auxiliary-state machinery. Block AttnRes reduces the routing cost of long histories relative to Full AttnRes by pooling consecutive contributions. We instantiate the interface in GPS and GRIT and evaluate it on all five ECHO tasks. Both variants achieve lower mean absolute error (MAE) than their independently tuned backbones on every task, and at least one obtains the lowest mean among all compared methods in each task. Routing-only donor-swap interventions support the mismatch hypothesis, while additional ablations examine the key design choices. Together, these results support node-adaptive depth aggregation as a useful complement to cross-node communication in long-range graph reasoning.
