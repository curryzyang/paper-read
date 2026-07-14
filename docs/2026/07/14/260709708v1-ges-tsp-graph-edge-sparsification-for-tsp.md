# GES-TSP: Graph Edge Sparsification for TSP

- 区域：速读区
- 排名：3
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Tianfeng Chen, Xianyue Li
- 机构：Lanzhou University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09708v1) · [PDF](https://arxiv.org/pdf/2607.09708v1)

## TLDR
GES-TSP proposes a learning-based graph sparsification method that uses GNNs and geometric features to prune up to 99% of edges in Euclidean TSP instances while maintaining solution gaps within 1% of optimal.

## Abstract
Solving large-scale instances of the Traveling Salesman Problem (TSP) exactly is computationally expensive. Researchers often employ graph sparsification methods to improve computational efficiency. Traditional sparsification methods typically rely on fixed heuristics and fail to fully exploit instance-specific structural information. In this paper, we propose Graph Edge Sparsification (GES), a learning-based sparsification approach for Euclidean TSP. By incorporating geometric structural information and combinatorial optimization technology, our proposed method adaptively generates a sparsification graph for different instances, significantly reducing the graph size and accelerating the solving process. Experimental results demonstrate that our sparsification method can prune up to 95% of edges on the MATILDA dataset, while keeping the solution gap within 1% of the optimal value. Moreover, our approach exhibits strong generalization capability on the TSPLIB benchmark.In some large-scale instances, the pruning rate exceeds 99%, while the optimality gap remains below 1%.
