# TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Changjian Zhou, Negin Yousefpour, Jie Qi, Junfeng Fang, Guillermo A. Narsilio, Hans Petter Jostad
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02991v1) · [PDF](https://arxiv.org/pdf/2609.02991v1)

## TLDR
TRACE is a graph-network simulator for granular dynamics that stores inter-particle contact history persistently on edges using attention-based message passing and gated recurrent units—with an edge-identity dictionary to preserve memory across contact rearrangements—and, by physics-structured decoding of contact forces with Coulomb friction, achieves stable long-horizon rollouts, 31–62% lower position error and 58–89% lower final-deposit error than prior learned simulators, while being 8.9–12.2× faster than the material point method on 2D/3D granular column-collapse benchmarks.

## Abstract
Learned graph simulators provide an efficient alternative to high-fidelity solvers for granular dynamics. However, granular motion depends strongly on inter-granular contact history, which is difficult to preserve when particle contacts form, break, and rearrange. Existing simulators mainly store temporal information in node features or node-level memory. Here we introduce TRACE, a graph-network simulator that stores interaction history directly on contact edges. Each edge maintains a persistent memory updated by attention-based message passing and a gated recurrent unit, while an edge-identity dictionary preserves this memory as the contact graph changes. A physics-structured decoder predicts inter-granular normal and tangential contact forces, enforces the Coulomb friction limit, and applies equal-and-opposite internal forces. The model is trained with single-step pretraining followed by autoregressive rollout fine-tuning. We evaluate TRACE on 2D and 3D granular column-collapse benchmarks. In both cases, TRACE produces stable, physically consistent long-horizon rollouts, closely reproducing the final deposit geometry and the kinetic energy released during collapse. Compared with graph network simulator (GNS) and node-memory graph neural simulator (NMGNS), TRACE reduces long-rollout position error by 31-62% and final-deposit error by 58-89% across the two benchmarks, while using fewer parameters and maintaining near-zero particle interpenetration. TRACE also achieves 12.2$\times$ and 8.9$\times$ speedups over the material point method (MPM) reference solver in 2D and 3D, respectively. Our code is available at https://github.com/Data-Driven-Computational-Geotechnics/TRACE.
