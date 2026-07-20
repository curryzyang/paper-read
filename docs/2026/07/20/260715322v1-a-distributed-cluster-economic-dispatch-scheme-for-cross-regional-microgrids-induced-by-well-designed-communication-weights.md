# A Distributed Cluster Economic Dispatch Scheme for Cross-regional Microgrids Induced by Well-designed Communication Weights

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yalin Zhang, Zhongxin Liu, Yulin Chen, Donglian Qi, Zengqiang Chen
- 机构：Nankai University, Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15322v1) · [PDF](https://arxiv.org/pdf/2607.15322v1)

## TLDR
This paper proposes a distributed cluster economic dispatch scheme for cross-regional microgrids that uses eigenvector centrality to design communication weights, enabling marginal cost multi-consensus and satisfying differential power demand ratios among subgrids.

## Abstract
A large-scale microgrid typically consists of several cross-regional subgrids aggregated by a virtual power plant (VPP). However, current consensus based schemes can-not guarantee the feature of differential demand between subgrids. Thus, distributed cluster consensus control induced by communication weights is investigated in this paper to solve the ED problem of a large-scale microgrid, which can achieve the expected cluster via well-designed communication weights. A communication weight matrix design method for a directed and connected graph based on eigenvector centrality is designed, which enables the adjacency matrix of the communication network to have a given leading eigenvector and allows agents in each cluster to have the same eigenvector center value. Based on this, a distributed cluster ED scheme, namely a leader-follower cluster consensus controller, is designed to drive marginal cost (MC) to achieve multiconsensus, thus allocating power among DGs. In addition, the power deficit of each subgrid collected by a VPP can be allocated to utility grids according to predetermined ratios, thus maintaining power supply-demand balance of each subgrid. For this scheme, it should be emphasized that the weighted network used is directed and connected; meanwhile, leader information only can be accessed by a few clusters. Correspondingly, relevant simulations are attached to verify the effectiveness of the designed scheme.


## 精读解读（中文）
### 一、研究动机
当前基于共识的微电网经济调度方案无法保证跨区域子电网之间的差异化需求，尤其是各子电网对不同类型公用事业电网的电价和功率比例需求不同。因此，需要研究一种分布式集群经济调度方案，通过设计通信权重来实现子电网间的差异化调度，满足各子电网的独特需求。

### 二、技术方案（Method）
首先，基于特征向量中心性设计有向连通图的通信权重矩阵，使每个集群内的智能体具有相同的特征向量中心值，从而诱导出预期的集群结构。其次，设计领导者-跟随者集群共识控制器，其中领导者接收虚拟电厂提供的期望电价信息，跟随者与邻居交换边际成本信息，驱动各子电网内所有分布式发电单元的边际成本收敛到该子电网对应的电价凸组合值。同时，构造功率缺额估计方案，通过分布式多共识控制器将子电网的功率缺额按虚拟电厂预设的比例分配给各公用事业电网，维持供需平衡。整个方案采用有向连通加权网络，领导者信息仅由少数集群访问。

### 三、结果（Result）
仿真验证了所提方案的有效性：在包含多个子电网和公用事业电网的大规模微电网系统中，各子电网内分布式发电单元的边际成本实现了多共识，收敛到虚拟电厂设定的不同电价值；功率缺额按预设比例在公用事业电网间精确分配，保证了各子电网的功率供需平衡。与现有共识方案相比，本方案成功实现了子电网间的差异化经济调度。

### 四、结论（Conclusion）
本文针对虚拟电厂聚合的大规模跨区域微电网，提出了一种基于通信权重设计的分布式集群经济调度方案。该方案利用特征向量中心性设计通信权重矩阵，结合领导者-跟随者控制器，有效解决了边际成本多共识和功率缺额按比例分配问题。仿真结果证明了方案的有效性，为含虚拟电厂的跨区域微电网集群经济调度提供了新的解决方案。

### 五、方法论与关键技术细节
关键细节包括：1) 通信网络为有向连通图，通过特征向量中心性设计权重矩阵，使得各集群内智能体具有相同的特征向量中心值，这是实现多共识的基础；2) 控制器采用领导者-跟随者结构，领导者接收虚拟电厂的期望电价信号，仅少数集群需要直接接收；3) 功率缺额估计采用分布式平均一致性算法，分配比例由虚拟电厂根据子电网特性预先设定；4) 方案假设通信拓扑固定且已知，虚拟电厂仅与部分集群通信；5) 局限性在于未考虑通信时延、拓扑切换或节点故障等实际情况，未来可考虑鲁棒性和自适应扩展。
