# Sensitivity Analysis of GRU, LSTM and Transformer Encoder in Classification of Automated Driving Systems

- 区域：精读区
- 排名：4
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Bidhya Shrestha, Christos Papadopoulos
- 机构：University of Memphis
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28665v1) · [PDF](https://arxiv.org/pdf/2607.28665v1)

## TLDR
GRU, LSTM, and Transformer encoder models accurately classify automated driving systems from vehicle telematics (macro F1 ~0.90–0.93), but a proposed robustness benchmark reveals that temporal jitter is the dominant failure mode, collapsing macro-F1 to 0.44–0.50 across all models.

## Abstract
Automated driving systems (ADSs) are becoming ubiquitous. Future Software Defined Vehicles (SDVs) may be able to run multiple ADSs, both native and aftermarket such as Comma.ai's Openpilot. Monitoring systems to independently verify which automated driving system is active are important for safety monitoring, regulatory compliance, insurance assessment, and anomaly detection. In this paper, we first evaluate the effectiveness of three sequence-based classification models: Gated Recurrent Units (GRU), Long Short-Term Memory (LSTM) networks, and a Transformer encoder model for identifying Level 2 automated driving systems using vehicle telematics data alone: Comma Openpilot, Tesla Autopilot, and Cadillac Super Cruise, along with manual driving. All three models achieve strong clean-data performance with macro F1-scores of 0.92 (GRU), 0.90 (LSTM), and 0.93 (Transformer encoder model) when trained on clean data; threat-matched training yields 0.904-0.916 macro F1 with only a modest clean-data penalty. Second, we introduce a modular robustness evaluation framework that simulates realistic telematics degradation through five corruption families at five severity levels (L1-L5). Continuous channels are perturbed using additive white Gaussian noise with cumulative drift, correlated cross-channel noise, and temporal jitter. Binary event signals are subjected to burst loss, delayed transitions, spurious toggles and cross-feature inconsistencies inspired by communication errors. Robustness is measured using macro-F1, which gives equal weight to each class and is suitable for imbalanced multiclass evaluation. Our evaluation reveals a sharp failure-mode split: event-level corruptions reduce macro-F1 only slightly (greater than equal to 0.87 at L5), while temporal jitter collapses macro-F1 to 0.44-0.50 across GRU, LSTM, and Transformer encoder model.


## 精读解读（中文）
### 一、研究动机
自动驾驶系统（ADS）日益普及，软件定义汽车可能同时运行多种原生或后装ADS，而依靠系统自报状态并不可靠，存在误报、故障或被恶意篡改的风险。需要通过车辆遥测数据独立验证当前激活的驾驶系统，以支持安全监控、合规审查、保险评估和异常检测。

### 二、技术方案（Method）
使用车辆遥测数据进行四分类（Comma Openpilot、Manual Driving、Tesla Autopilot、Cadillac Super Cruise），输入为11维特征（6个连续通道：vEgo, aEgo, gas, yawRate, steeringAngleDeg, steeringRateDeg；5个二进制事件通道：standstill, brakeLightsDEPRECATED, leftBlinker, rightBlinker, brakePressed），时间窗口T=32。评估三种序列模型：6层堆叠GRU（隐藏单元64）、6层堆叠LSTM（隐藏单元64）、Transformer编码器（输入投影256维、可学习位置编码、6个编码器块、8个注意力头），最后用最后一个时间步表示接线性分类器。训练使用Adam优化器、batch size 256、学习率0.0001、最多100轮、早停patience=7、基于类别比例的交叉熵损失。鲁棒性评估框架包含五种噪声族（随机漂移、时间抖动、相关通道扰动、事件通道突发/切换/毛刺、跨特征不一致），各5个严重级别L1-L5，并使用威胁匹配训练（每个batch以0.85概率施加一种L1-L3的噪声）进行增强。

### 三、结果（Result）
干净数据下三个模型均表现良好：GRU macro-F1=0.92，LSTM=0.90，Transformer编码器=0.93；威胁匹配训练后macro-F1为0.904-0.916，干净数据惩罚较小。鲁棒性测试显示事件级扰动影响较小（L5下macro-F1仍≥0.87），但时间抖动严重破坏性能，GRU从L1的0.497降至L5的0.437，LSTM从0.502降至0.431，Transformer也降至约0.44-0.50。随机漂移下Transformer略优（L5=0.820），相关扰动下各模型下降幅度有限。

### 四、结论（Conclusion）
三种序列模型都能有效基于遥测数据识别L2级自动驾驶系统，Transformer编码器在干净数据上略优且对连续信号退化更鲁棒；但所有模型对时间抖动高度敏感，这是当前序列模型用于ADS识别的关键局限性。事件级二进制扰动相对容易处理，而时间对齐误差是实际部署中需要优先解决的脆弱点。

### 五、方法论与关键技术细节
数据集来自Comma、Cadillac和Tesla数据集，共超过340万条标记样本，按70/15/15分层划分。超参数未广泛调优，选择序列长度32和学习率0.0001基于验证集。鲁棒性度量使用macro-F1以平衡类别不平衡。时间抖动通过前后平移连续通道模拟ECU时钟偏移或总线调度延迟，是最大失效模式。威胁匹配训练采用eval-matched增强，但仅使用L1-L3严重级别训练，测试覆盖L1-L5。局限性包括：未进行大规模超参数搜索，模型可能非全局最优；Manual类召回率较低（0.76-0.80），表明人类驾驶与自动驾驶行为存在重叠。
