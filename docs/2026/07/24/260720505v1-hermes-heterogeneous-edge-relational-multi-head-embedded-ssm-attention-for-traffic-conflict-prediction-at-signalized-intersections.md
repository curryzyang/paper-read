# HERMES: Heterogeneous Edge-Relational Multi-Head Embedded SSM Attention for Traffic Conflict Prediction at Signalized Intersections

- 区域：精读区
- 排名：6
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Md Monzurul Islam, Subasish Das
- 机构：Texas State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20505v1) · [PDF](https://arxiv.org/pdf/2607.20505v1)

## TLDR
HERMES proposes a heterogeneous edge-relational graph neural network with SSM-informed multi-head attention that models diverse road-user interactions as temporal scene graphs, achieving state-of-the-art traffic conflict prediction and cross-site transferability at signalized intersections.

## Abstract
Surrogate safety measures (SSMs) enable proactive traffic safety assessment, but many existing methods evaluate pairwise interactions independently or flatten multi-agent scenes into fixed feature vectors, limiting their ability to represent heterogeneous interaction structure and evolving scene-level risk. This study formulates traffic conflict assessment as temporal heterogeneous scene-graph classification and proposes HERMES, a heterogeneous edge-relational graph neural network with SSM-informed multi-head attention. Vehicles and pedestrians are represented as heterogeneous nodes, while vehicle-vehicle, vehicle-pedestrian, and pedestrian-pedestrian interactions are encoded as relation-specific edges with continuous kinematic and surrogate-safety descriptors. Relation-specific attention, dynamic node-edge updates, safety-aware graph pooling, and temporal sequence learning are jointly used to estimate scene-level conflict probability. HERMES was evaluated using 109,028 trajectory-derived sequences from a signalized urban intersection and tested on an independently collected comparable intersection dataset. Enhanced HERMES achieved an AUC-ROC of 0.9898 +/- 0.0013, an AUC-PR of 0.9412 +/- 0.0067, and an F1 score of 0.8449 +/- 0.0103. At a 5% false-alarm rate, it detected 95.7% of conflict sequences, outperforming the strongest Transformer baseline and XGBoost. In zero-shot external evaluation, HERMES achieved an AUC-ROC of 0.9752 and an AUC-PR of 0.7829. Joint source-target training further improved target-site performance with limited target-site data. These findings show that preserving heterogeneous interaction topology, safety-informed edge semantics, and short-term temporal evolution improves scene-level conflict classification and supports transferable roadside safety monitoring at signalized intersections.


## 精读解读（中文）
### 一、研究动机
现有基于替代安全措施（SSM）的交通冲突评估方法多独立评估成对交互或将多智能体场景压平为固定特征向量，无法表征异构交互结构和演变的场景级风险。本研究将交通冲突评估建模为时序异质场景图分类，以保留交互拓扑和短期时序演化。

### 二、技术方案（Method）
输入为信号化交叉口视频提取的109,028条轨迹序列，经预处理生成节点级运动变量和交互级SSM描述符。将车辆和行人表示为异质节点，车辆-车辆、车辆-行人、行人-行人交互编码为关系特定边，包含连续运动学（距离、相对速度）和代理安全指标（TTC、PET、DRAC）。关键模块包括：SSM嵌入的多头关系注意力动态调节交互重要性；动态节点-边更新实现消息传递中交互状态双向精炼；安全感知图池化聚合场景级特征；时序序列编码（如LSTM/GRU）建模短期演化。训练采用交叉熵损失，通过多类基线对比及零样本跨站点评估验证可迁移性。

### 三、结果（Result）
增强HERMES在独立测试集上AUC-ROC达0.9898±0.0013，AUC-PR为0.9412±0.0067，F1分数0.8449±0.0103。在5%假警率下检测出95.7%冲突序列，远超最强Transformer基线（81.0%）和XGBoost（61.5%）。零样本外部评估AUC-ROC为0.9752，AUC-PR为0.7829；联合源-目标训练仅用20%目标域数据即达最优低假警灵敏度0.9869±0.0057。

### 四、结论（Conclusion）
保留异构交互拓扑、安全信息边语义和短期时序演化显著提升了场景级冲突分类性能，并支持跨相似信号化交叉口的可迁移性，为低假警率的路边安全监控提供了有效框架。

### 五、方法论与关键技术细节
数据：城市信号化交叉口109,028条轨迹序列，独立类似交叉口用于零样本评估。先验：SSM描述符嵌入边特征指导注意力，实现安全感知消息传递。损失：未明确说明但适用交叉熵。超参：多种子分析（±标准差）评估稳健性。复杂度/约束：图构建和消息传递依赖轨迹质量，感知误差（抖动、遮挡）可能影响SSM估计。局限性：未显式处理空间城市拓扑和信号相位信息，轨迹自动提取误差仍需进一步控制。
