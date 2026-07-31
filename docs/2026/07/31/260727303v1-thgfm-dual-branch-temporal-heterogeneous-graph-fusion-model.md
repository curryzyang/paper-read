# THGFM: Dual-Branch Temporal Heterogeneous Graph Fusion Model

- 区域：速读区
- 排名：6
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Yixin Peng, Diego Collarana, Er Jin, Stefan Decker
- 机构：RWTH Aachen University, Fraunhofer FIT
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27303v1) · [PDF](https://arxiv.org/pdf/2607.27303v1)

## TLDR
THGFM is a dual-branch temporal heterogeneous graph transformer that fuses shared-space and relation-type-partitioned attention via type-conditioned non-competitive gated summation and rotary temporal attention, consistently outperforming prior graph transformers on academic benchmarks.

## Abstract
Temporal heterogeneous graphs offer a natural abstraction for dynamic relational systems in which diverse node and relation types co-exist and evolve over time. Learning on such graphs requires jointly modeling cross-type structural heterogeneity and the temporal dynamics of interactions, yet existing methods still struggle to reconcile parameter-efficient cross-type transfer with relation-aware specialization, and typically inject time only as additive features outside the attention kernel. We propose \textbf{THGFM}, a web-scale temporal heterogeneous graph fusion model that addresses both limitations within a unified dual-path architecture. THGFM couples a \textit{Shared-Space Temporal Attention} branch for parameter-efficient cross-type transfer with a \textit{Relational Type-Partitioned Temporal Attention} branch for relation-aware specialization, and integrates them through \textit{Dual-Path Relational--Shared Fusion}, instantiated with \textit{Type-Conditioned Non-Competitive Gated Sum Fusion}: a adaptive mechanism that assigns independent, type-conditioned feature-wise gates to the shared and specialized branches, allowing both to be amplified or suppressed without zero-sum competition. To directly incorporate relative time into the attention score, THGFM further introduces \textit{Rotary Temporal Attention}, which rotates queries and keys by half-phases of relative time before matching. THGFM consistently outperforms baseline graph transformer models on academic graphs benchmarks, delivering a $+3.25\%$ six-task mean gain, with peak relative gains of $+12.37\%$ on OAG-CS PV, $+4.87\%$ on PF-$L_2$, and $+1.18\%$ on PF-$L_1$, and $+4.24\%$, $+3.73\%$, and $+4.61\%$ on OGBN-MAG, HTAG-ArXiv, and HTAG-DBLP, respectively.
