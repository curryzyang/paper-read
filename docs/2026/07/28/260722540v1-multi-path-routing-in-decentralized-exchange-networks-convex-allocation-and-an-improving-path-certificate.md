# Multi-Path Routing in Decentralized Exchange Networks: Convex Allocation and an Improving-Path Certificate

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Ilia Zhavoronkov
- 机构：Planet 9 Group Corporation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22540v1) · [PDF](https://arxiv.org/pdf/2607.22540v1)

## TLDR
This paper presents a graph-theoretic and convex optimization framework for multi-path routing in decentralized exchange networks, introducing an improving-path certificate that verifies solution quality via a single shortest-path query, and empirically demonstrates competitive performance against production DEX aggregators on Ethereum mainnet.

## Abstract
We present a graph-theoretic and convex optimization framework for multi-path routing in decentralized exchange networks, together with its implementation and empirical evaluation on Ethereum mainnet. The framework models the market as a directed token multigraph whose arcs carry AMM exchange functions. Routing is decomposed into two implemented layers: candidate path generation via gas-aware marginal k-shortest-path enumeration, where edge scores embed expected execution cost directly into graph traversal with an explicit pool-simple constraint tracked during path construction, and continuous flow allocation over the selected candidates solved as a concave maximization over a simplex with a per-pool price-impact cap. Under standard concavity and monotonicity assumptions, the KKT conditions imply marginal-output equalization across active paths. The central technical contribution is an improving-path certificate: after solving the allocation on k=20 candidate paths, the KKT multiplier is used as a threshold to determine via a single shortest-path query whether any omitted pool-simple path could improve the current solution; in our implementation the certificate confirms sufficiency in the majority of epochs. Execution is protected by an on-chain slippage tolerance enforced at the smart-contract level. We evaluate the implemented engine against four production DEX aggregators on repeated WETH-USDT quote observations across six trade sizes on Ethereum mainnet: median shortfall is below 5 bps across all sizes and top-3 quote rank exceeds 57% of epochs.
