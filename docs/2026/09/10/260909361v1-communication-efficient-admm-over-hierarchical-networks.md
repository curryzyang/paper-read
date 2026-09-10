# Communication-efficient ADMM over Hierarchical Networks

- 区域：速读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Binh Nguyen, Shuangqing Wei, Truong X. Nghiem
- 机构：Louisiana State University, University of Central Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09361v1) · [PDF](https://arxiv.org/pdf/2609.09361v1)

## TLDR
The paper proposes hADMM, a communication-efficient distributed ADMM algorithm for tree-structured hierarchical optimization that exploits parent-child query-response exchanges to reduce communication costs while guaranteeing asymptotic convergence and, under mild conditions, linear convergence.

## Abstract
This paper develops a novel distributed optimization algorithm based on the Alternating Direction Method of Multipliers (ADMM) to solve hierarchical optimization problems over tree-structured networks, termed hierarchical ADMM (hADMM), with a particular focus on enhancing communication efficiency across the network. By rearranging the augmented Lagrangian to establish a query-response communication mechanism between nodes that explicitly exploits the hierarchical tree structure, the proposed algorithm significantly reduces communication costs compared to existing ADMM-based methods for hierarchical optimization. Furthermore, hADMM guarantees asymptotic convergence under convexity assumptions. We also present a convergence rate analysis based on linear matrix inequalities to characterize the maximum theoretically achievable convergence rates across different network topologies, showing that the proposed hADMM attains linear convergence under mild conditions. Three numerical experiments demonstrate that hADMM is compatible with arbitrary tree network structures and outperforms existing approaches in terms of communication efficiency.
