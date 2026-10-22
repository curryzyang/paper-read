# Scalable Stress-Constrained Topology Optimization: A Super-resolution and Simultaneous Approach Based on Machine Learning

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Xiangyu Sun, Shirin Hosseinmardi, Ramin Bostanabad
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28703v1) · [PDF](https://arxiv.org/pdf/2610.28703v1)

## TLDR
The paper proposes a simultaneous neural topology optimization (SNTO) framework that jointly trains custom neural networks for state, adjoint, and design variables using continuous adjoint analysis and automatic differentiation, with hardware-aware multi-GPU partitioning and slicing to enable scalable, super-resolution stress-constrained designs at millions of degrees of freedom.

## Abstract
Large-scale topology optimization (TO) remains computationally demanding, especially for stress-constrained problems. To address this challenge, we propose the simultaneous neural topology optimization (SNTO) framework where we represent state, adjoint, and design variables with custom neural networks (NNs) whose parameters are jointly optimized within a single optimization loop that leverages continuous adjoint analysis and automatic differentiation. This optimization minimizes a multi-component loss function that combines the design objective, an aggregation of the local stress constraints, and the potential energy functionals. Our NNs have a unique architecture that accelerates convergence while enabling the networks to capture sharp gradients and boundaries which are critical to stress-constrained TO. To achieve scalability to millions of degrees of freedom (DoF), we develop a hardware-aware training scheme in which the design domain is partitioned into subdomains that are distributed across multiple GPUs. To control peak GPU memory usage, we further slice each subdomain into smaller regions whose loss gradients are evaluated sequentially and accumulated to update the NN parameters. Unlike domain decomposition approaches, our partitioning naturally ensures field continuity across the subdomains and does not require the introduction of additional terms into the loss function. For validation, we first evaluate the proposed framework on various 2D stress-constrained benchmarks and compare our results to a conventional finite element-based approach, showing that SNTO produces super-resolution designs with sharper boundaries, smaller gray areas, and lower volume fractions. We then consider large-scale 3D problems with up to eight million collocation points and distribute the training over up to eight GPUs.


## 精读解读（中文）
### 一、研究动机
大规模应力约束拓扑优化因局部应力约束数量随离散分辨率增长、传统嵌套分析设计每轮需多次有限元求解而计算代价极高，现有机器学习方法又多局限于二维或较小规模问题。作者希望借助连续神经网络参数化与同时分析设计范式，在避免全局刚度矩阵组装和重复有限元求解的同时，实现高分辨率、可扩展到数百万自由度且可在多GPU上高效训练的应力约束拓扑优化。

### 二、技术方案（Method）
提出同时神经拓扑优化SNTO框架，用三个定制神经网络分别表示状态场、伴随场和设计场，并在单一优化循环中联合训练；训练采用连续伴随分析与自动微分计算灵敏度，最小化由设计目标、局部应力约束聚合项和势能泛函组成的多分量物理损失。为实现大规模扩展，设计域被划分为子域并分配到多GPU，每个子域再切片为更小区域以顺序评估损失梯度并累加更新网络参数；由于场由连续神经网络表示，分区天然保持跨子域场连续性，无需额外界面损失项。

### 三、结果（Result）
在多种二维应力约束基准上，SNTO相对传统有限元方法得到超分辨率设计，表现为边界更锐利、灰度区域更小和体积分数更低；在三维大规模问题中测试到约八百万个配点并分布到最多八个GPU，摘要报告训练时间随GPU数量近似线性下降，且增加子切片数量可降低峰值GPU显存。

### 四、结论（Conclusion）
SNTO将状态、伴随和设计变量的神经网络参数化与同时优化结合，为应力约束拓扑优化提供了无需全局刚度矩阵组装、可超分辨率且可多GPU扩展的机器学习路径。结果表明该方法在有限计算资源下处理大规模应力约束问题具有可行性，并为高分辨率局部约束优化提供了新框架。

### 五、方法论与关键技术细节
关键实现包括以配点求和构成物理损失，使约束评估分辨率可独立于可训练参数数量；不组装、存储或分解全局刚度矩阵；采用能捕捉锐利梯度和边界的定制网络结构，并以应力约束聚合项控制局部约束。多GPU分区只用于计算分配，不引入需调权的界面损失，子域切片通过梯度顺序评估与累积控制显存。局限包括摘要仅给出定性对比和扩展性趋势而未列具体误差或超参数，应力聚合精度仍依赖聚合策略，当前大规模验证上限约为八百万配点和八个GPU。
