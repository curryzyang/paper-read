# NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts

- 区域：精读区
- 排名：1
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Lanhao Li, Bingshu Xie, Lijun Sun, Xin Xue, Haoyi Zhou, Jianxin Li
- 机构：Beihang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06607v1) · [PDF](https://arxiv.org/pdf/2607.06607v1)

## TLDR
NEST proposes a two-phase regime-oriented mixture-of-experts framework that tackles dataset-level distribution shifts by first partitioning data into distinct operational regimes via unsupervised clustering in moment-entropy space and then dynamically recomposing specialized experts to capture regime-specific dynamics, achieving state-of-the-art forecasting performance.

## Abstract
Accurate long-term forecasting in complex systems is frequently compromised by dataset-level distribution shifts, where diverse underlying behavioral modes and evolving system states drive the dynamic multivariate time-series. While existing methods predominantly focus on local temporal shifts, they fail to explicitly model the global structural challenge where datasets are composites of distinct operational regimes. In this paper, we propose NEST, a specialized framework designed to model and recompose these evolving structures through a two-phase dense MoE architecture. NEST first facilitates structural specialization by partitioning the dataset into distinct operational regimes through unsupervised clustering in a principled moment-entropy space. We introduce a regime-oriented router mechanism that generates initial expert weights based on temporal content, subsequently refined through geometric modulation to regime centroids. Crucially, rather than acting as monolithic predictors, individual experts function as specialized kernels that capture regime-specific dynamics by evolving unique variate-attention patterns. Extensive evaluations on diverse benchmarks, including heterogeneous network traffic and physical phenomena, demonstrate that NEST consistently achieves state-of-the-art performance. Our code and datasets are available at https://github.com/Aaralshin/NEST


## 精读解读（中文）
### 一、研究动机
现有方法主要关注局部时间偏移，忽略了数据集级别的全局结构挑战——数据集由不同操作模式组成，单一模型被迫学习平均表示，无法准确捕捉各模式动态。NEST旨在通过显式建模和重组这些演化结构来解决这一问题。

### 二、技术方案（Method）
NEST采用两阶段密集MoE架构。第一阶段：通过无监督聚类在矩-熵空间（均值、方差、SVDEn）将数据集划分为不同操作模式，训练多个专用专家（变体注意力模块）和共享专家；第二阶段：路由器先基于输入时序内容通过Transformer编码器生成初始权重，再通过几何调制（计算输入到模式中心的欧氏距离，用反二次函数和软化因子α调整）细化权重，最后加权融合专家输出，训练采用MSE损失。

### 三、结果（Result）
在异质网络流量和物理现象等多个基准上，NEST一致达到最先进性能，其注意力多态性和权重置换分析验证了其在变量依赖结构重组中的独特能力。

### 四、结论（Conclusion）
NEST通过解耦演化动力学为专用核，有效捕捉驱动数据集分布偏移的操作模式间的结构转换；其无监督发现模块和模式导向路由器实现了精确的专家编排，在长期预测中显著优于现有方法。

### 五、方法论与关键技术细节
关键点：使用矩-熵空间（均值、方差、SVDEn）作为聚类特征，数据切片长度为L+H但推理时仅用L计算特征并假设统计一致性；路由器使用反二次函数和软化因子α∈(0,1]实现几何调制；两阶段训练中阶段1训练专家、阶段2冻结专家训练路由器；损失函数为MSE；超参包括模式数M和α；复杂度依赖于专家数量；局限性包括聚类质量影响性能及假设窗口内统计一致可能不适用于快速变化模式。
