# A Sparsity Analysis of Traffic Forecasting Architectures: How Much Missing Data is Too Much?

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Mohamed Hamad, Bilal Mutahir, Mohamed Mabrok, Nizar Zorba, Hamid Saeedi, Halim Yanikomeroglu
- 机构：University of Doha for Science and Technology, Qatar University, Carleton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26847v1) · [PDF](https://arxiv.org/pdf/2611.26847v1)

## TLDR
This paper benchmarks GNN, Transformer, and state-space traffic forecasting models under increasing inference-time sensor sparsity and finds a trade-off in which higher full-data accuracy often comes with sharper degradation, implying that model selection should prioritize robustness to expected sensor reliability rather than peak accuracy alone.

## Abstract
Traffic forecasting models are typically evaluated under ideal conditions with complete data. This evaluation does not reflect the frequent sensor failures and communication outages common in real-world deployments. This paper presents a comprehensive analysis of multivariate traffic prediction models to evaluate their performance under varying levels of sensor data loss during inference. We benchmark several architectural paradigms, including graph neural networks, attention-based Transformers, and selective state-space models, across sparsity levels ranging from zero to complete sensor loss, using two widely used multi-channel traffic benchmarks. To ensure consistent comparison across traffic variables, we use normalized metrics and define a usability threshold to identify when predictions become unreliable. Our results show a clear trade-off between baseline accuracy and robustness: models with the highest accuracy under full-data conditions often degrade most sharply as data becomes sparse, while less accurate models maintain more stable performance. These findings show that model selection should be based on the expected reliability of the sensor network rather than peak accuracy alone. This work provides a practical framework for assessing traffic forecasting models and highlights the importance of robustness in real-world applications.


## 精读解读（中文）
### 一、研究动机
真实部署中的交通传感器网络常因故障、通信中断或维护而出现数据缺失，但现有交通预测模型多在全数据理想条件下评测，无法反映推理阶段传感器失效时的可靠性。论文旨在系统评估多变量交通预测模型在不同传感器缺失程度下的性能退化，回答“缺失多少数据会导致预测不可用”，并强调模型选择不能只看全数据峰值精度。

### 二、技术方案（Method）
研究在PEMS04和PEMS08两个多通道交通基准上评测GNN、注意力Transformer和选择性状态空间模型（Mamba类）等架构。输入为5分钟分辨率、历史与预测窗口均为12步的多变量张量，包含流量、速度和占有率三个目标通道；推理时按稀疏度ρ随机屏蔽k=round(ρN)个传感器，仅对三个交通目标通道做零值填充，填充值在z-score标准化空间取−μc/σc，辅助协变量保持不变，且不重新训练模型。每个稀疏度用固定种子43、44、45生成三个独立掩码，同一掩码贯穿全部时间步和测试集；用z-score空间的分通道vMAE/vRMSE及通道平均指标评估，并做12个预测步的逐horizon分析和相对基线的退化分析，再依据应用误差阈值定义可用性崩溃点。

### 三、结果（Result）
结果显示存在明显的精度—鲁棒性权衡：全数据条件下精度最高的模型在传感器变稀疏时往往退化最剧烈，而基线精度较低的模型性能更稳定。跨GNN、Transformer和状态空间模型的对比表明，模型排名会随稀疏度变化，仅凭全数据vMAE/vRMSE无法判断部署可靠性；归一化指标和可用性阈值能够识别预测何时超过应用可接受误差并变得不可用。

### 四、结论（Conclusion）
论文提出了一套可复现的推理阶段稀疏性基准框架，用于比较多变量交通预测模型在传感器缺失下的鲁棒性。结论是模型选择应结合预期传感器网络可靠性、应用误差阈值和稀疏条件下的退化曲线，而不能只追求全数据峰值精度；该工作为实际部署中的鲁棒性评估提供了操作化依据。

### 五、方法论与关键技术细节
关键实现包括：使用PEMS04/PEMS08三通道数据，t_in=t_out=12、5分钟粒度；掩码只作用于流量、速度、占有率三个目标通道，按训练集均值方差做z-score并采用归一化零填充；推理阶段不重训，每个稀疏度固定三个随机掩码以隔离掩码波动；评估排除易在近零真值处失真的百分比误差，采用vMAE/vRMSE、通道平均、逐预测步和相对基线退化，并以NCHRP指南选定的10%误差阈值定义崩溃点。局限性是主要采用均匀随机掩码和零填充，未覆盖空间/时间相关故障、恒定值或异常高值等故障模式，且未系统比较前向填充或均值填充等替代处理。
