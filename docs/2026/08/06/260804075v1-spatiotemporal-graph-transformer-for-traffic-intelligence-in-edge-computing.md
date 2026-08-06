# Spatiotemporal Graph Transformer for Traffic Intelligence in Edge Computing

- 区域：精读区
- 排名：1
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Laha Ale, Letian Lin, Na Cao, Zheng Ma, Peng Yu
- 机构：Southwest Jiaotong University, Beijing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04075v1) · [PDF](https://arxiv.org/pdf/2608.04075v1)

## TLDR
The paper proposes a spatiotemporal graph Transformer framework for edge computing traffic forecasting that combines graph neural networks for spatial correlations with Transformer self-attention for long-range temporal dependencies, consistently outperforming recurrent graph-based baselines and enabling more effective proactive resource provisioning.

## Abstract
Accurate traffic forecasting is essential for proactive resource management in edge computing, where service demand evolves dynamically across both space and time. In practical cellular edge systems, traffic exhibits strong spatial correlations among neighboring service regions and long-range temporal dependencies driven by user mobility and application behavior. Existing recurrent forecasting approaches can capture short-term dynamics but often struggle to model long-horizon traffic evolution under non-stationary conditions. To address this challenge, we propose a spatiotemporal graph Transformer framework that jointly models spatial interactions and temporal dependencies for traffic forecasting in edge computing. The framework employs graph neural networks to capture spatial correlations among service regions and leverages Transformer-based self-attention to learn long-range temporal patterns from historical traffic observations. By decoupling spatial representation learning from temporal reasoning, the proposed approach provides an effective mechanism for large-scale spatiotemporal traffic modeling. Extensive experiments on a real-world cellular network dataset demonstrate that the proposed graph Transformer consistently outperforms recurrent graph-based baselines, including GCN-RNN, GCN-LSTM, and GCN-GRU models, across multiple forecasting horizons. The resulting forecasts enable more effective proactive resource provisioning and reduce overload risk compared with reactive management strategies. These results highlight the potential of graph-enhanced attention mechanisms for building intelligent and adaptive edge computing systems.


## 精读解读（中文）
### 一、研究动机
边缘计算中的服务需求在空间和时间上动态变化，现有基于循环网络的流量预测方法虽能捕捉短期动态，但在非平稳条件下难以建模长时间跨度的流量演化，制约了主动资源供给的准确性。为此，需要一种能够同时建模区域间空间相关性与长程时间依赖的流量智能框架。

### 二、技术方案（Method）
提出一种时空图Transformer框架，将空间感知与时间推理解耦。输入为边缘服务区域的历史流量观测序列X(t-L+1:t)和由区域质心经纬度构造的空间图；使用GNN（图卷积网络）按加权邻接矩阵聚合邻近区域流量特征，得到空间表征序列；再将每个区域的时空特征序列输入Transformer编码器，通过缩放点积自注意力建模长程时间依赖；最后通过输出映射层生成多步预测X(t+1:t+H)。训练采用MAE损失，优化所有训练样本、区域和预测时域的平均误差。

### 三、结果（Result）
在真实蜂窝网络数据集上的实验表明，所提GCN-Transformer在多个预测时域上一致优于GCN-RNN、GCN-LSTM和GCN-GRU等循环图基线，尤其在较长预测时域和流量快速变化阶段具有更高的准确性和稳定性；基于预测的主动资源供给相比反应式管理能更有效降低过载风险。

### 四、结论（Conclusion）
通过图神经网络捕获空间相关性并使用Transformer自注意力学习长程时间模式，可以实现大规模时空流量建模，提升边缘计算中多时域流量预测的精度与稳定性，为主动资源供给提供可靠支撑，表明图增强注意力机制在构建智能自适应边缘系统方面具有潜力。

### 五、方法论与关键技术细节
空间图用区域质心经纬度欧氏距离构造全连接加权图，权重为高斯核exp(-d^2/sigma^2)，sigma控制空间衰减率，邻接矩阵进行行归一化；输入可加入小时、星期等上下文特征；Transformer使用缩放点积注意力，解耦空间表示学习与时间推理；损失函数为多时域MAE；实验与GCN-RNN、GCN-LSTM、GCN-GRU在相同设置下比较；资源供给策略g(.)的设计不在本文范围，主要聚焦于预测精度与稳定性。
