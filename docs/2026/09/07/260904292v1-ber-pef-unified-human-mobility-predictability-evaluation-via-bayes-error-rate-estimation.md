# BER-PEF: Unified Human Mobility Predictability Evaluation via Bayes Error Rate Estimation

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：En Xu, Jingtao Ding, Zhiwen Yu, Yong Li
- 机构：Northwestern Polytechnical University, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04292v1) · [PDF](https://arxiv.org/pdf/2609.04292v1)

## TLDR
BER-PEF proposes a Bayes-error-rate-based framework with controlled perturbation curves and a shared reference interval to reliably evaluate human mobility predictability estimators across symbolic sequences, numeric trajectories, and contextual representations, without requiring observable ground-truth predictability.

## Abstract
Human mobility predictability concerns the best prediction performance attainable from a given target and input information, but its ground truth is not directly observable on real mobility data. We present BER-PEF, a Bayes-error-rate-based framework that converts BER estimation into mobility predictability estimation and provides a unified protocol for comparing estimators without observable ground truth. The framework maps symbolic sequences, numeric trajectories, contextual features, and learned representations into a common feature--label space, then evaluates estimator outputs along controlled perturbation curves against a shared predictability reference interval by measuring deviations below the interval, above the interval, and across the full interval. Experiments on Foursquare NYC and TKY, GeoLife, and T-Drive show that several BER-based estimators achieve lower reference discrepancy than existing predictability methods on symbolic sequences and numeric trajectories, while their estimates track changes in empirical prediction performance under perturbation. Additional analyses show that contextual inputs and multiple structured representations can be evaluated under the same protocol, and that aggregating evidence across multiple perturbation levels provides a more reliable basis for estimator selection than relying on a single unperturbed observation. BER-PEF therefore offers a unified and verifiable path for evaluating predictability estimators on heterogeneous mobility data when ground-truth predictability is unavailable.


## 精读解读（中文）
### 一、研究动机
人类移动性可预测性关注在给定目标和输入信息下可获得的最佳预测性能，但其真实值在真实移动数据上不可直接观测。现有可预测性估计方法在状态空间、假设和输出约定上差异较大，且大多局限于离散符号序列，难以在异构移动数据（符号序列、连续轨迹、上下文特征、学习表示）上统一比较可靠性。因此需要一个无需可观测真值即可比较可预测性估计器的统一协议，并扩展到多种移动数据形式。

### 二、技术方案（Method）
BER-PEF将可预测性估计转化为贝叶斯错误率（BER）估计问题，通过统一表示层将符号序列、数值轨迹、上下文特征和学习表示映射到共同的特征-标签空间。具体地，构造长度为L的历史窗口h，经适配器（符号查表、数值线性投影、上下文嵌入）生成序列表示，由共享序列编码器（UniMob，GRU骨干）编码，采用均值池化与最后隐藏状态拼接后经线性投影得到样本特征z；标签为下一位置或离散化的下一状态类别。该表示通过下一位置/下一状态监督损失训练。然后使用BER估计器（如最近邻、密度、散度等）在控制扰动下产生下侧和上侧可预测性曲线，并与共享的可预测性参考区间比较，通过归一化的区间下偏差、区间上偏差和全区间偏差评估估计器可靠性。扰动曲线和随机实现用于选择与验证，而非单一静态观测。

### 三、结果（Result）
在Foursquare NYC、Foursquare TKY、GeoLife和T-Drive四个数据集上的实验表明，多个基于BER的估计器在符号序列和数值轨迹上的参考偏差低于现有可预测性方法，其估计值在扰动下能够追踪经验预测性能的变化。此外，上下文输入和多种结构化表示可在同一协议下评估，并且跨多个扰动水平聚合证据比依赖单一未扰动观测更可靠。

### 四、结论（Conclusion）
BER-PEF提供了在真实异构移动数据上无可观测可预测性真值时统一且可验证的可预测性估计器评估路径。它证明了BER估计可作为任务级参考，用于解释不同预测器在不同条件下的表现差异，并支持在统一协议下比较估计器可靠性与表示适用性。

### 五、方法论与关键技术细节
关键细节包括：可预测性定义为给定表示空间中贝叶斯最优错误率的补集；统一表示层是BER-PEF的接口，使得不同输入类型可共用同一BER估计器家族；参考区间由所有估计器在共同扰动水平下的输出确定，评估采用归一化偏差而非静态输出比较；训练使用交叉熵监督学习下一位置分类；UniMob使用GRU作为序列编码器，聚合采用均值池化加最后隐藏状态拼接；现有方法多为仅上侧估计或依赖特定序列形式，BER-PEF通过扰动曲线与多水平聚合提供更可靠的选择依据；局限性可能在于估计结果依赖于历史窗口长度、标签映射和表示学习质量，且对连续轨迹需进行离散化处理。
