# Low-Latency Relay Selection in NR-V2X Vehicular Communications via Graph Isomorphism Networks with Edge Features

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Giambattista Amati, Federica Mangiatordi, Emiliano Pallotti, Simone Angelini, Pierpaolo Salvo, Paola Vocca
- 机构：University of Rome Tor Vergata (UniRoma2), Fondazione Ugo Bordoni (FUB)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14176v1) · [PDF](https://arxiv.org/pdf/2607.14176v1)

## TLDR
This paper introduces an edge-aware Learning-to-Optimise framework using Graph Isomorphism Networks with Edge Features (GINE) to achieve low-latency, near-optimal multi-hop relay selection in NR-V2X vehicular communications, supervised by a MILP oracle and further combined with a hybrid pruning strategy to enable MILP-grade solutions within stringent latency budgets.

## Abstract
Reliable, low-latency uplink connectivity is a key requirement for C-V2X networks in dense urban environments, where fast channel variations and blockages often degrade direct vehicle-to-infrastructure links. Multi-hop relaying can restore coverage, but relay-link activation under radio, capacity, and routing constraints results in an NP-hard optimisation problem, typically solved via Mixed-Integer Linear Programming (MILP), whose runtime scales poorly with graph size. This paper introduces an edge-aware Learning-to-Optimise framework for real-time relay selection. Each V2X snapshot is modelled as a directed graph: node features encode vehicle state and traffic demand, while edge features capture radio-link capacity. An offline MILP oracle generates optimal relay configurations that supervise a Graph Isomorphism Network with Edge Features (GINE), enabling edge-level relay activation through a single forward pass, with tightly bounded inference latency. To bridge learning and exact optimisation, we also propose a hybrid GINE-Pruned MILP (GP-MILP) strategy in which GINE predictions prune the MILP search space. Experiments on a large-scale dataset generated via an OSM-SUMO-GEMV$^2$ pipeline show that GINE closely matches MILP decisions at the link level (accuracy 0.9589), F1-score (0.9544) on validation) and yields consistent end-to-end connectivity gains over a 1-hop MILP baseline (up to 9.2% with four RSUs and 12% with two RSUs). Inference latency remains tightly bounded, with all evaluated instances completing within 5~ms. Moreover, GP-MILP preserves MILP-equivalent solutions (same objective value) while achieving solver runtimes below 30~ms for more than 98%) of the graph instances, making MILP-grade optimisation compatible with stringent NR-V2X latency budgets.


## 精读解读（中文）
### 一、研究动机
在密集城市环境中，C-V2X网络需要可靠低延迟的上行连接，但快速信道变化和阻塞常导致车辆到基础设施的直接链路性能下降。多跳中继可恢复覆盖，然而在无线、容量和路由约束下的中继链路激活问题是一个NP-hard优化问题，传统混合整数线性规划（MILP）求解器运行时间随图规模增长而急剧增加，无法满足实时性要求。

### 二、技术方案（Method）
提出一种边缘感知的学习优化框架。每个V2X快照建模为有向图，节点特征编码车辆状态与流量需求，边特征编码无线链路容量（如基于瞬时SNR的香农容量）。离线MILP oracle生成最优中继配置作为监督信号，训练包含3层消息传递的图同构网络（GINE），该网络通过边特征投影（EdMLP）显式融入无线属性，实现边级中继激活的单一前向传播推理。同时提出混合GP-MILP策略，利用GINE预测剪枝MILP搜索空间以加速精确求解。训练采用类别加权二元交叉熵损失，权重α由训练集正负样本比例设置。

### 三、结果（Result）
GINE在链路级决策上与MILP oracle高度一致，验证集准确率0.9589，F1分数0.9544。相比单跳MILP基线，端到端连接增益可达9.2%（4个RSU场景）和12%（2个RSU场景）。推理延迟严格受限，所有实例在5ms内完成。GP-MILP保持与MILP等价的目标值，且98%以上的图实例求解时间低于30ms，满足NR-V2X严格延迟预算。

### 四、结论（Conclusion）
提出的GINE和GP-MILP方法能在极低延迟下逼近MILP最优中继决策，实现实时多跳中继选择，在保证连接性能的同时将求解延迟降低数个数量级，使精确优化在NR-V2X实时场景中变得可行。

### 五、方法论与关键技术细节
数据集通过OSM-SUMO-GEMV^2管线生成罗马Porta Pia区域1km²密集城市场景，包含449500个图快照，节点特征包含位置、类型和流量需求，边特征为基于香农容量模型的无线链路容量。GINE使用3层消息传递，边特征通过两层MLP（ReLU、Dropout）投影后加入节点更新。损失函数中α = N_neg / N_pos以平衡正负样本。MTZ约束用于消除路由环路。局限性：GINE推断时未显式强制执行流量守恒等全局约束，但经验上表现良好；数据生成依赖离线MILP，大规模场景下标注成本高。
