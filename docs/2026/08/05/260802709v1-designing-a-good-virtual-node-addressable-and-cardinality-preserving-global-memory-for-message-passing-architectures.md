# Designing a Good Virtual Node: Addressable and Cardinality-Preserving Global Memory for Message Passing Architectures

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Félix Marcoccia
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02709v1) · [PDF](https://arxiv.org/pdf/2608.02709v1)

## TLDR
This paper proposes a virtual-node design with addressable, factorized cross-attention slots and an anchoring mechanism that preserves cardinality, overcoming the homogeneous-broadcast bottleneck of standard virtual nodes and achieving 1-WL-level expressivity at O(nMd) cost.

## Abstract
Virtual nodes give message-passing neural networks a simple global communication route, but the standard node--VN--node pipeline compresses the graph into one homogeneous state and broadcasts it identically to every node. Building on the Two-Radius analysis of Mishayev et al., we ask how auxiliary virtual memory can relieve this finite-capacity bottleneck without self-attention. We identify two requirements. First, the global memory should be factorized into independently writable and readable states: this can be achieved using addressable cross-attention slots. Second, addressability alone does not preserve multiplicity, because softmax attention is invariant to uniform replication. Inserting each slot query as a private key/value anchor recovers the discarded normalization mass and yields, on bounded color domains, an injective multiset representation able to implement a 1-WL refinement. Experiments on multiplicity-aware Two-Radius, motif counting, and constrained link-set prediction support this addressable and cardinality-preserving virtual memory at (O(nMd)) arithmetic cost.
