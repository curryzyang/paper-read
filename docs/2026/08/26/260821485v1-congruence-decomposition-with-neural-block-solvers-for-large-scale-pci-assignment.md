# Congruence Decomposition with Neural Block Solvers for Large-Scale PCI Assignment

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yeqing Qiu, Chengpiao Huang, Ye Xue, Akang Wang, Fan Xu, Zhipeng Jiang, Dong Zhang, Ruoyu Sun, Qingjiang Shi, Zhi-Quan Luo
- 机构：Shenzhen Research Institute of Big Data, Tongji University, University of Chinese Academy of Sciences, The Chinese University of Hong Kong, Shenzhen, Sun Yat-sen University, Huawei Technologies, Columbia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21485v1) · [PDF](https://arxiv.org/pdf/2608.21485v1)

## TLDR
The paper proposes a congruence decomposition framework with graph neural network-based block solvers that decouples large-scale 5G Physical Cell Identity (PCI) assignment into Min-\(k\)-Partition subproblems, achieving efficient multi-objective modular interference reduction, collision/confusion elimination, and a 2.04× speedup on real-world networks.

## Abstract
Physical Cell Identity (PCI) assignment is essential for interference management in dense 5G networks. As cellular networks scale, PCI reuse becomes unavoidable, which may cause collisions, confusions, and multiple forms of modular interference. Jointly mitigating these effects gives rise to a large-scale, multi-objective combinatorial optimization problem that is difficult to solve efficiently at practical network scales. In this work, we propose a congruence decomposition framework with neural block solvers for large-scale PCI assignment. The proposed decomposition exploits the arithmetic structure of PCI values to decouple multiple modular interference objectives into a collection of blockwise Min-$k$-Partition subproblems, followed by a graph coloring procedure to resolve PCI conflicts. For the resulting NP-hard Min-$k$-Partition subproblems, we develop neural block solvers by parameterizing their relaxed quadratic formulations with graph neural networks, enabling efficient optimization at large scales. Discrete assignments are recovered through conditional expectation rounding with theoretical guarantees. Experiments on synthetic cellular graphs and real-world 5G networks show that the proposed method consistently outperforms existing modular-interference-aware baselines in modular interference reduction, conflict elimination, and computational efficiency.
