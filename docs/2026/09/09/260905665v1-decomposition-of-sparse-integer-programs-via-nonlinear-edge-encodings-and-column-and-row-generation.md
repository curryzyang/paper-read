# Decomposition of Sparse Integer Programs via Nonlinear Edge Encodings and Column-and-Row Generation

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Gustavo Angulo, Santanu S. Dey
- 机构：Pontificia Universidad Católica de Chile, Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05665v1) · [PDF](https://arxiv.org/pdf/2609.05665v1)

## TLDR
The paper develops an exact, decomposable column-and-row generation framework that closes the Lagrangian duality gap for block-structured sparse integer programs by dynamically separating redundant nonlinear consistency constraints encoded via edge-based nonlinear functions, with theoretical and computational results showing that richer encoding families can exponentially reduce required constraints but may not perform best in practice.

## Abstract
A wide range of sparse integer programs admit a block structure in which subproblems interact through a small set of shared variables. Dualizing the linking equalities yields a decomposable Lagrangian relaxation, but generally introduces a duality gap. Recent work shows that this gap can be closed while preserving decomposability by dualizing exponentially large families of redundant nonlinear consistency constraints on the shared variables. We develop a computational framework for exploiting this idea without explicitly constructing the resulting exponentially large relaxation. Our framework combines nonlinear edge encodings of shared-variable consistency with a column-and-row generation (CRG) algorithm that generates local integer solutions by pricing and encoding constraints by separation. With complete encodings and exact separation, the framework recovers the exact relaxation while retaining independent optimization over the blocks. We introduce several encoding families and establish exponential separations among them: the Generalized family can require exponentially fewer constraints than the Vertex, Monomial, or Reflected families, yet can itself require exponentially many constraints on instances for which a single problem-specific encoding suffices. Computational experiments on decomposed stable-set and dominating-set instances show that CRG substantially outperforms a monolithic formulation across a range of tree topologies and coupling strengths. The results also show that richer encoding families need not perform better computationally, highlighting the choice of encoding as a central issue in effective decomposition.
