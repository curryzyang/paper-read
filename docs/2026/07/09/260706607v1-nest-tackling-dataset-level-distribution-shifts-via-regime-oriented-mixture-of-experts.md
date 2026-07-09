# NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts

- 区域：精读区
- 排名：1
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Lanhao Li, Bingshu Xie, Lijun Sun, Xin Xue, Haoyi Zhou, Jianxin Li
- 机构：Beihang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06607v1) · [PDF](https://arxiv.org/pdf/2607.06607v1)

## TLDR
NEST proposes a two-phase mixture-of-experts framework that identifies distinct operational regimes via moment-entropy clustering and uses regime-oriented routing to dynamically recompose specialized experts for accurate long-term time series forecasting under dataset-level distribution shifts.

## Abstract
Accurate long-term forecasting in complex systems is frequently compromised by dataset-level distribution shifts, where diverse underlying behavioral modes and evolving system states drive the dynamic multivariate time-series. While existing methods predominantly focus on local temporal shifts, they fail to explicitly model the global structural challenge where datasets are composites of distinct operational regimes. In this paper, we propose NEST, a specialized framework designed to model and recompose these evolving structures through a two-phase dense MoE architecture. NEST first facilitates structural specialization by partitioning the dataset into distinct operational regimes through unsupervised clustering in a principled moment-entropy space. We introduce a regime-oriented router mechanism that generates initial expert weights based on temporal content, subsequently refined through geometric modulation to regime centroids. Crucially, rather than acting as monolithic predictors, individual experts function as specialized kernels that capture regime-specific dynamics by evolving unique variate-attention patterns. Extensive evaluations on diverse benchmarks, including heterogeneous network traffic and physical phenomena, demonstrate that NEST consistently achieves state-of-the-art performance. Our code and datasets are available at https://github.com/Aaralshin/NEST


## 精读解读（中文）
### 一、研究动机
现有方法主要关注局部时间偏移，未能显式处理数据集级别的分布偏移，其中复杂系统的时间序列由不同运行状态组成，导致长期预测性能下降。

### 二、技术方案（Method）
提出NEST两阶段稠密混合专家框架。第一阶段：通过无监督聚类在矩-熵空间（均值、方差、SVD熵）对数据切片（长度L+H）进行分区，识别不同运行状态，并训练对应状态专家（变体注意力模块）捕获状态特定变量依赖；同时训练共享专家保留全局知识。第二阶段：冻结专家池，训练面向状态的router，先基于输入时间内容通过Transformer编码器和线性头生成初始权重，再通过输入到状态质心的欧式距离计算几何调制因子（逆二次函数加软化因子α）调整权重，最终与共享专家权重（Sigmoid生成）组合得到预测。

### 三、结果（Result）
在异构网络流量和物理现象（如电离层总电子含量）等基准上，NEST一致取得最先进性能；注意力多态性和权重置换分析验证了其变量依赖重组能力。

### 四、结论（Conclusion）
NEST通过显式建模和重组运行状态的结构性变化，有效解决数据集级分布偏移，在长期预测中实现SOTA性能。

### 五、方法论与关键技术细节
数据切片跨越历史窗口和预测窗口（L+H）用于状态发现，推理时仅用历史窗口L避免数据泄漏；使用MSE损失训练；超参数包括状态数M和软化因子α；复杂度来自两阶段训练和无监督聚类；局限性是矩-熵特征对状态可分性的依赖，以及假设历史窗口统计量足以代表未来状态。
