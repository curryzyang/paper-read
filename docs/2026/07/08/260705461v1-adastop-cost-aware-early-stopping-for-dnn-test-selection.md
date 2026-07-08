# AdaStop: Cost-Aware Early Stopping for DNN Test Selection

- 区域：精读区
- 排名：6
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Bonan Shen, Wei-Jung Huang, Xin Liu, Jiazhou Gao, Tao Ning
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05461v1) · [PDF](https://arxiv.org/pdf/2607.05461v1)

## TLDR
AdaStop is a cost-aware early stopping framework for DNN test selection that stops labeling when the estimated marginal fault discovery rate falls below a cost-benefit threshold, enabling discovery of 65–84% of faults using only 9–31% of the labeling budget.

## Abstract
Existing methods for testing deep neural networks (DNNs) primarily prioritize test inputs likely to reveal model faults under a fixed labeling budget. In practice, choosing that budget is difficult: too little testing misses failures, while too much incurs unnecessary labeling costs. This work studies the stopping problem in DNN testing. We formulate testing as a cost--benefit decision process in which labeling an input incurs cost $c$ and discovering a fault yields value $v$. Based on this formulation, we introduce \textit{AdaStop}, a framework that estimates the marginal fault discovery rate during testing and stops labeling when the estimated rate falls below the threshold $τ= c/v$. Experiments across multiple datasets, architectures, and selection strategies show that $65$--$84\%$ of faults can be discovered using only $9$--$31\%$ of the labeling budget.


## 精读解读（中文）
### 一、研究动机
现有DNN测试方法主要关注在固定标注预算下选择最可能揭示模型错误的输入，但实际中选择预算困难：预算过小会遗漏故障，过大则造成不必要的标注成本。本文针对DNN测试中的停止问题，提出成本感知的早期停止框架AdaStop。

### 二、技术方案（Method）
将测试建模为成本-收益决策过程，标注成本c，故障价值v，最优停止条件为边际故障发现率p(t)低于阈值τ=c/v。AdaStop包含三个模块：1）基于DeepGini的不确定性选择策略，优先选择Gini impurity最高的输入；2）滑动窗口估计器，用最近W个样本的平均值估计当前故障发现率；3）成本感知停止规则，当估计率低于τ且样本数超过最小样本N_min时停止。算法按Gini分数排序迭代：每次选择剩余池中最高分数输入，获取标签记录结果，更新滑动窗口估计，满足条件即终止。

### 三、结果（Result）
在CIFAR-10、SVHN、FashionMNIST三个数据集及ResNet-20、VGG-16、DenseNet-121、ShuffleNetV2四种架构上，AdaStop以9%-31%的标注预算发现65%-84%的故障。以CIFAR-10/ResNet-20为例（τ=0.05），预算使用31%发现84%的故障，效率0.402（全标注0.120），净价值提升18.9%。与固定预算策略相比，AdaStop自动找到预算-召回曲线上的有效操作点。

### 四、结论（Conclusion）
AdaStop提供了一个原则性的、成本感知的停止准则，有效平衡故障发现与标注成本。它基于边际故障发现率递减的实证观察，自动确定停止时机，避免了手动选择预算的困难。实验表明AdaStop在多种配置下都能显著降低标注成本同时保持高召回，且与多种选择策略兼容，具有良好泛化性。

### 五、方法论与关键技术细节
关键点：成本-收益阈值τ=c/v直接由场景决定；滑动窗口大小W（默认20）平衡响应性与噪声，实验表明W在10-50间稳健；最小样本N_min=50确保估计可靠性。先验假设：故障发现率随测试递减，经Mann-Kendall检验验证。与多种停止准则比较（耐心、连续非故障、置信区间），AdaStop在成本和召回间取得最佳平衡。局限：依赖于不确定性排序的递减性质，若排序策略失效则停止点可能不优；窗口和阈值需根据具体场景调整。
