# Eliminating Propagation Delay: Attention-Based Spatial-Temporal Fusion Graph Convolution Network for Traffic Flow Prediction

- 区域：精读区
- 排名：1
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Jinpeng Chen, Ziyu Yu, Tao Wang, Jun Ma, Hongbo Gao, Senzhang Wang, Zufeng Zhang, Kaimin Wei
- 机构：Jinan University, Central South University, University of Science and Technology of China, Beijing University of Posts and Telecommunications, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24885v1) · [PDF](https://arxiv.org/pdf/2607.24885v1)

## TLDR
The paper proposes an Attention-Based Spatial-Temporal Fusion Graph Convolution Network (A-STFGCN) that eliminates propagation delay errors and efficiently captures both long-term and short-term temporal features for accurate traffic flow prediction.

## Abstract
Predicting traffic flow is crucial to optimizing transportation systems and improving urban mobility. Many graph convolution-based models have been proposed to extract spatial-temporal features and predict traffic flow. However, most focus on spatial-temporal and semantic correlation in topological relationships. There are two primary problems to address. Firstly, the convolutional structure in the model focuses on utilizing static spatial dependencies and spatial-temporal relationships in topological structures, while neglecting the different information propagation delays between adjacent nodes in the convolution. Secondly, these methods often stack a large number of complex structures, resulting in a substantial increase in computational time during the model training phase, thereby disregarding the model's requirements for timeliness. In this paper, we propose a novel network called the Attention-Based Spatial-Temporal Fusion Graph Convolution Network (A-STFGCN). We design a spatial-temporal fusion block to extract the spatial-temporal feature correlations with propagation delay errors removed and to capture both long-term and short-term temporal characteristics of the data within a multi-head self-attention mechanism based on a mask matrix. Extensive experiments on five real-world datasets demonstrate that our method achieves the best overall performance while having good computation and data utilization efficiency compared with the eight baseline methods.


## 精读解读（中文）
### 一、研究动机
现有图卷积交通流预测模型主要利用拓扑结构中的静态空间依赖和时空关系，忽略了相邻节点间不同的信息传播延迟，同时堆叠大量复杂结构导致训练阶段计算时间显著增加，无法满足模型对时效性的要求。

### 二、技术方案（Method）
提出一种基于注意力的时空融合图卷积网络（A-STFGCN）。首先通过谱聚类构建宏观图，结合传输块将宏观区域特征传递到节点分支；然后设计时空融合块（STF-Block），利用基于动态时间规整（DTW）的掩码矩阵构造延迟时间图，并通过多头自注意力机制同时捕获短期和长期时间特征；最后使用空间-时间融合图卷积（GSTF-GCN）消除传播延迟误差，同步提取时空相关性。输入为历史N个传感器节点的T1步交通观测，输出预测未来T2步流量。

### 三、结果（Result）
在五个真实交通数据集上的实验表明，A-STFGCN在预测精度上全面优于DCRNN、STGCN、Graph WaveNet、STSGCN、PDFormer等八种基线方法，同时保持较好的计算效率和数据利用效率，取得最优综合性能。

### 四、结论（Conclusion）
A-STFGCN有效解决了图卷积模型中传播延迟被忽略以及计算开销大的问题，通过延迟感知的时空融合图和多头自注意力机制实现了准确且高效的交通流预测。

### 五、方法论与关键技术细节
关键细节包括：1）利用DTW算法估计节点间信息传播延迟步数，构建延迟时间图；2）多头自注意力模块使用基于DTW相似性的掩码矩阵，关注具有特定时间偏移的时间步；3）通过谱聚类构建宏观图以降低大规模网络的计算复杂度；4）损失函数采用MSE；5）在五个真实交通数据集（含PEMS系列）上验证，与八种基线对比；6）模型在保持高精度的同时具有较好的计算效率和数据利用效率。
