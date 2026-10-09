# Temporal transformer CAN encoder with federated lightweight heads for anomaly detection

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Konstantinos Gyftodimos, Kyriakos Chiotis, Elena Politi, George Dimitrakopoulos, Eirini Liotou
- 机构：ANADELTA P.C., Harokopio University of Athens
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10613v1) · [PDF](https://arxiv.org/pdf/2610.10613v1)

## TLDR
This paper proposes a privacy-preserving in-vehicle CAN anomaly detection framework that combines a lightweight Temporal Transformer encoder for capturing temporal and contextual message patterns with federated lightweight XGBoost heads for collaborative, decentralized classification without sharing raw CAN data.

## Abstract
Modern vehicles rely on large numbers of Electronic Control Units (ECUs) that constantly exchange information over the Controller Area Network (CAN) bus. Due to the rapidity, structure, and repetition of this communication, even slight variations in timing, payload values, or message patterns can point to unusual activity. Whether due to errors, malfunctions, or deliberate interference, these anomalies are frequently subtle and challenging to identify with conventional methods that handle messages separately or rely on manually created rules. Motivated by this gap, we present a privacy-preserving framework for anomaly detection in in-vehicle networks, based on a Temporal Transformer CAN Encoder with Federated Lightweight Heads, to better capture these irregularities. The detection of subtle temporal and contextual anomalies is made possible by a lightweight Transformer encoder that learns how these signals evolve over time, while a federated learning mechanism enables several vehicles or ECUs to work together to improve a shared model without exchanging raw CAN data. This combination of federated learning and temporal sequence modeling provides robust anomaly detection performance while maintaining efficiency and privacy, according to experiments conducted on open-source datasets.


## 精读解读（中文）
### 一、研究动机
现代车辆中大量ECU通过CAN总线高频交换短消息，而CAN缺少内建完整性机制，时序、负载或模式上的细微变化可能对应故障或攻击；现有方法多逐条处理消息或依赖人工规则，忽略时间与上下文，集中式训练还带来隐私和资源受限ECU部署难题。

### 二、技术方案（Method）
框架先将原始CAN日志按标识符和时间戳排序，按ECU计算相邻消息到达时间差，并将8个负载字节与Delta_t组成9维特征，切成T=15的非重叠窗口；随后用轻量Transformer编码器做特征提取，包含线性输入投影、可学习位置编码、2层多头自注意力编码层和自适应均值池化，输出每窗64维嵌入；再以4个XGBoost回归器组成的多输出模型预测窗内正常、DoS、Fuzzy、冒充四类标签的经验比例，损失为平方误差；联邦训练中每个客户端保留本地CAN窗口，用当前全局集成预测并拟合残差，仅上传新梯度提升组件和验证指标，服务器按验证性能选择最佳组件顺序加入全局集成而非平均树权重。

### 三、结果（Result）
集中式全局模型在测试集上准确率0.838、宏F1 0.840、加权F1 0.835，回归MSE 0.021；联邦场景使用两个客户端，每轮平均验证MSE从0.0351降至0.0263再降至0.0244，最终客户端测试准确率分别为0.88和0.89，测试MSE分别为0.1309和0.1316，显示协作学习能提升未见ECU数据的分类泛化但回归误差高于集中式。

### 四、结论（Conclusion）
该工作表明，时序Transformer嵌入加轻量XGBoost头与联邦残差集成可在不交换原始CAN数据的前提下实现较高窗口级异常检测准确率，兼顾隐私、边缘推理效率和协作泛化。未来可引入在线学习以适应动态车辆环境。

### 五、方法论与关键技术细节
关键细节包括数据来自HKSecurity OCSLab公开入侵数据集，联邦实验仅使用CAN_HCRL_OTIDS_UB子集且未参与集中训练；窗口大小T=15，输入维度9，d_model=64，Transformer层数L=2，四分类，非重叠窗口；XGBoost按类别多输出回归，以窗内类别比例为目标和平方误差损失；联邦服务器采用基于验证指标的select-best聚合，因树模型不能权重平均；局限是联邦客户端仅两个、评估为窗口级、集中与联邦MSE差距较大、缺少与多种SOTA的充分对比，且未详述通信成本与在线部署约束。
