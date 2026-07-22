# Cost Accounting for Reactive Computational Graphs: Exhaustive Sweeps, Sequential Mutation, and the Backward-Locality Gap

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Abdallah Khemais
- 机构：University of Sousse
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18323v1) · [PDF](https://arxiv.org/pdf/2607.18323v1)

## TLDR
This paper provides a complete cost accounting for exhaustive sweep, sequential mutation, and batched mutation workloads on reactive computational graphs, deriving exact speedup ratios that depend on the distribution of computational weight across depth, closed-form costs for persistent mutations, and a backward-locality gap that collapses the sweep speedup to 1 under backpropagation.

## Abstract
Exhaustive site-by-site interventions on a neural network's computational graph -- activation-patching sweeps, circuit-discovery searches, systematic ablation studies -- mutate the graph at every candidate site, and their cost is dominated by recomputation after each mutation. On a reactive graph engine whose invalidation provably touches exactly the downstream cone of a mutated node, we give a complete cost accounting for such workloads. First, the aggregate speedup of an exhaustive sweep over independent full recomputations is not a universal constant: if per-layer weight varies regularly with depth at Karamata index q, the ratio converges to (q+2)/(q+1) when weight concentrates near the output and to q+2 near the input, recovering 2 only in the depth-uniform case; a wall-clock corollary predicts a ceiling of about 1.79, below 2, until interpreter overhead is compiled away. Second, we prove the exact cost of a sequence of persistent mutations, never undone between insertions: the interleaved cost exceeds the isolated sum by an exact overcount summed over comparable site pairs, with closed-form extremes over insertion orders, while batched application is order-independent and sub-additive, costing exactly the union of the sites' cones plus the fresh nodes. Third, we prove the exact mirror of forward locality for the backward pass, showing it collapses the aggregate speedup to 1 under backpropagation on architectures without long skip connections. Every identity is validated on NeuroDSL, a reactive graph engine in Julia: measured sweep ratios converge to the predicted limits under four cost profiles; the training-mode ratio collapses to 1 at the predicted rate; and all 18 per-graft sequential costs and the batched total match the closed forms at zero tolerance across three insertion orders.
