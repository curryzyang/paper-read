# Multiple Leak Localization in Water Distribution Networks through Graph Neural Networks

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Arvin Ajoodani, Sara Nazif, Pouria Ramazi
- 机构：University of Tehran, University of Calgary
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35972v1) · [PDF](https://arxiv.org/pdf/2610.35972v1)

## TLDR
A graph neural network localizes a variable number of simultaneous leaks in water distribution networks without requiring the leak count in advance or exhaustive leak-combination training, outperforming conventional classifiers on benchmark networks under sparse monitoring.

## Abstract
Leak localization in water distribution networks is challenging when multiple leaks occur simultaneously, particularly under sparse monitoring. Existing data-driven methods often assume a single or predefined number of leaks or require extensive enumeration of leak combinations. This study proposes a graph neural network (GNN) model that localizes a variable number of simultaneous leaks without specifying the leak count in advance or exhaustively generating every possible combination of leak locations for training. The model is evaluated on two benchmark networks of different sizes, the 31-node Hanoi network and the larger 92-node NET3 network, under variable demand, sparse pressure-sensor coverage, variable leak magnitudes, and varying numbers of simultaneous leaks. The GNN outperforms multilayer perceptron, support vector machine, K-nearest neighbors, and random forest classifiers by up to 12% and 20% in accuracy respectively in Hanoi and NET3 networks. Consistent performance across both networks supports the scalability of the proposed approach.


## 精读解读（中文）
### 一、研究动机
水分配网络同时发生多处泄漏时定位困难，稀疏监测下尤其突出；现有数据驱动方法常假设单一或预先给定泄漏数量，或需穷举泄漏位置组合，随候选节点增加计算不可行且泛化受限。论文旨在不预先指定泄漏数、不穷举所有组合的条件下定位可变数量的同时泄漏。

### 二、技术方案（Method）
论文用EPANET生成泄漏场景：随机选择1至N个候选节点同时泄漏、随机时间步，需求乘0.8至1.2随机因子，按Q=CP^0.5的发射器公式为每个泄漏独立赋0<C≤10，并保留总漏量小于同时段基线总流入30%的场景；目标为每个候选节点的二值多标签向量。输入仅取少量压力传感器，先由水头h=p+z和反管长边权构造加权图拉普拉斯，固定传感器水头并最小化连接节点加权差以插值未观测节点水头，再转压力形成全网节点压力特征；随后用GCN做节点级多标签分类，通过多层邻域聚合融合拓扑与水力信息，输出每个节点泄漏概率。GCN以BCE损失和Adam训练，按训练损失10次迭代改进小于1%收敛；数据按80/20划分开发集与测试集，在开发集内用五折交叉验证按平均F1选超参，测试集仅最终评估，并以交叉验证F1学习曲线连续两次数据增量提升小于0.01作为停止生成场景的准则；MLP、SVM、KNN、RF使用相同输入和目标进行对比。

### 三、结果（Result）
在31节点Hanoi网络和92节点NET3网络上，GCN在变化需求、稀疏压力传感器覆盖、变化泄漏强度及不同同时泄漏数下均优于MLP、SVM、KNN和RF，准确率在Hanoi最高提升12%、在NET3最高提升20%。实验使用Hanoi 2000至22000个场景、NET3 4000至44000个场景，并以节点级precision、recall、F1和accuracy评估，两个规模网络表现一致支持方法可扩展性。

### 四、结论（Conclusion）
该研究表明，基于GCN的节点级多标签框架可在不预先指定泄漏数量、不穷举泄漏位置组合的情况下定位可变数量的同时泄漏，并能利用网络拓扑在稀疏传感器条件下重建和传播水力信息。跨两个不同规模基准网络的一致优势说明该思路对更复杂水分配网络具有应用潜力。

### 五、方法论与关键技术细节
关键实现包括：泄漏数从1到全部候选节点随机采样以覆盖多标签配置而非复现真实频率；泄漏仅在随机选定的单个时间步活跃，未研究泄漏持续时间；需求不确定性采用±20%均匀扰动；泄漏强度用发射器系数0<C≤10且指数0.5，阈值按总漏量小于30%基线流入过滤。输入先验是反管长加权图的平滑性，通过拉普拉斯分块求解未观测水头，传感器位置人为选定为4个Hanoi节点和11个NET3节点。训练损失为所有候选节点和场景上的BCE，超参包括GCN层数1至7、每层隐神经元8至256、MLP层数与神经元、KNN的K、SVM的C/核/多项式阶数、RF树数与最大深度。局限包括仅两个基准网络、传感器布设固定、C范围和30%阈值含工程判断、场景随机采样不反映真实泄漏频率、未考虑泄漏时长，且指标为节点级平均。
