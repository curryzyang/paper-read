# Constraint-Aware Discrete Black-Box Optimization Using Tensor Decomposition

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Keisuke Onoue, Ryosuke Kojima
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09370v1) · [PDF](https://arxiv.org/pdf/2609.09370v1)

## TLDR
This paper proposes a constraint-aware tensor-decomposition surrogate model for discrete black-box optimization that integrates feasibility constraints via a differentiable T-norm penalty to improve sample efficiency by steering search away from infeasible regions.

## Abstract
Discrete black-box optimization is often addressed using approaches such as Sequential Model-Based Optimization (SMBO), which aims to improve sample efficiency by fitting surrogate models that approximate a costly objective function over a discrete search space. In many real-world problems, the set of feasible inputs is often given by logical constraints known in advance. However, existing surrogate modeling techniques generally fail to capture the symbolic rules governing feasibility in discrete input spaces. In this paper, we propose a surrogate modeling approach based on tensor decomposition that captures the structure of discrete search spaces while directly integrating feasibility information. To implement this approach, we formulate surrogate model training as a constrained polynomial optimization problem and solve a relaxed formulation using a differentiable penalty term derived from T-norms. Our experiments on both synthetic and real-world benchmarks, including a pressure vessel design task, demonstrate that the proposed method improves sample efficiency by effectively guiding the search away from infeasible regions.


## 精读解读（中文）
### 一、研究动机
离散黑箱优化常用SMBO并通过代理模型提升样本效率，但现实问题中可行输入往往由预先已知的逻辑约束决定。现有代理建模技术通常难以在离散输入空间中捕获支配可行性的符号规则，导致搜索容易浪费在不可行区域。

### 二、技术方案（Method）
本文提出一种基于张量分解的代理建模方法：将离散搜索空间表示为张量，用低秩张量分解学习目标函数在离散组合上的结构；同时把预先给定的逻辑可行性约束编码为多项式/符号约束，与代理训练共同构成约束多项式优化问题，并用由T-norms导出的可微惩罚项进行松弛求解，从而可用梯度方法优化分解因子；在SMBO循环中，用该代理预测目标并评估可行性，采集函数在惩罚后选择候选点，查询昂贵黑箱目标并更新数据。

### 三、结果（Result）
在合成基准和真实基准（包括压力容器设计任务）上，所提方法相比现有代理/SMBO方法提升了样本效率，并能有效引导搜索远离不可行区域。

### 四、结论（Conclusion）
将张量分解代理与逻辑可行性约束直接结合，可为带约束离散黑箱优化提供一种可微、可扩展的建模范式，使有限评估预算更聚焦于可行且高价值的区域。

### 五、方法论与关键技术细节
关键点包括：输入为离散变量组合与已知逻辑约束，先验/结构假设为目标在张量分解下具有低秩性；训练损失由目标拟合误差与T-norm可行性惩罚组成，需调节张量秩、惩罚权重、采集策略和初始设计；实现上需将约束写成可微多项式形式并做松弛；局限可能在高维离散空间、复杂逻辑约束、张量秩选择及惩罚权重敏感性，真实任务含压力容器设计验证了实用性。
