# KernelOnet: An Interpretable Neural Operator Based on Kernel Functions

- 区域：精读区
- 排名：1
- 匹配度：6.2/10
- 来源：arxiv
- 作者：Yuan Guo, Hanshu Chen, Qiang Xi, Timon Rabczuk, Zhuojia Fu
- 机构：Bauhaus-University Weimar, Hohai University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35938v1) · [PDF](https://arxiv.org/pdf/2609.35938v1)

## TLDR
KernelOnet is an interpretable neural operator that replaces DeepONet’s implicit trunk network with explicit data-driven, physics-informed, or hybrid kernel functions, enabling more accurate and parameter-efficient PDE solution learning, unsupervised boundary-only training, and effective handling of unbounded exterior acoustic propagation.

## Abstract
This paper proposes an interpretable neural operator framework, the Kernel Operator Network (KernelOnet), which incorporates kernel functions explicitly into the neural operator architecture, so that the operator structure matches the kernel-expansion form used in boundary-type kernel-expansion methods. Unlike traditional neural operators such as DeepONet, which learn basis functions implicitly through deep networks, KernelOnet replaces the trunk network with explicit kernels and offers three complementary kernels: a data-driven learnable kernel, in which a neural network parameterizes a radial basis function learned from data, and which for constant-coefficient linear problems can be regarded as a non-singular fundamental solution; a physics-informed kernel, which embeds physical information such as analytic fundamental solutions into the network structure, so that the expansion satisfies the governing equation automatically and can be trained without supervision on boundary conditions alone, with no interior solution data; and a hybrid kernel, which splits the solution, according to the linear principal part of the governing equation, into a homogeneous part spanned by analytic fundamental solutions and a source part carried by low-rank learned correction kernels, thereby balancing physical priors against data fitting on nonlinear problems lacking an analytic fundamental solution. On three benchmarks and one engineering problem in a shallow-water waveguide, KernelOnet attains high accuracy; where comparable with DeepONet, it is more accurate with fewer learnable parameters. Its unsupervised configuration needs no interior solution labels, and its per-query inference cost is far below that of per-instance solvers, offering an effective route to acoustic propagation in unbounded exterior domains that general-purpose neural operators struggle to handle.


## 精读解读（中文）
### 一、研究动机
现有神经算子（如 DeepONet、FNO）依赖深度网络隐式学习基函数，其结构缺乏与具体控制方程的显式联系，导致可解释性差、物理一致性不足，且通常需要大量高保真数据、小样本泛化受限。与之相对，MFS、Trefftz、BEM 等边界型核展开数值方法从一开始就用显式核（如基本解）作基函数，兼具物理解释性与高效性，但依赖人工选择核函数与源点布局，难以自动适应复杂非线性问题。本文正是要在这两条路线之间架桥，把显式核函数引入神经算子架构。

### 二、技术方案（Method）
KernelOnet 是对 DeepONet 的直接改造：分支网络仍将输入函数（边界点离散值）映射为系数 β_k(a)，但把 trunk 网络替换为显式核函数，输出写成核展开形式 Σ_k β_k(a) K(x, y_k) + b_0，从而与边界型核展开方法的算子结构一致。作者给出三种核构造策略：数据驱动可学习核（KernelOnet-RBF）用浅层网络参数化径向基函数并从数据学习，常系数线性问题下可视为非奇异基本解；物理信息核（KernelOnet-PIKF）直接把控制方程的解析基本解嵌入网络，使展开自动满足控制方程，仅用边界条件即可无监督训练、不需任何内部解标签；混合核（KernelOnet-HK）按方程线性主部把解拆为解析基本解张成的齐次部分与 K_c 个低秩可学习修正核张成的源项部分，前者精确满足线性主部，后者承载无法用核函数表达的非线性源项。训练时监督配置最小化内部评估点上的数据均方误差，物理/无监督配置则最小化边界条件残差，对照的 PI-DeepONet 则以 λ_PDE 和 λ_BC 加权组合 PDE 残差（借助自动微分求高阶导数）与边界残差。

### 三、结果（Result）
在圆域 Laplace 方程、星形域非线性修正 Helmholtz 方程、无界外域复 Helmholtz 方程三个基准以及浅水波导中球壳振动引起的水下声辐射与传播工程问题上，KernelOnet 均取得高精度解。在与 DeepONet 可直接对比的算例上，它以更少的可学习参数获得更高精度；其无监督配置完全不需要内部解标签，且单次查询推理成本远低于逐实例求解器。针对浅水波导，作者分别用 Pekeris 核与简正模核构造核函数，使近场与远场都能无监督求解，并在多种声速剖面下表现出良好鲁棒性。

### 四、结论（Conclusion）
KernelOnet 通过把显式核函数嵌入神经算子，建立了神经算子与基于核展开的边界型数值方法之间的内在联系，在精度、可解释性和参数效率上同时取得收益，并为通用神经算子难以处理的无界外域声传播问题提供了有效途径。其关键前提是：物理信息核与混合核都要求控制方程或其线性主部存在可用的解析基本解，这正是该框架发挥作用的适用条件。

### 五、方法论与关键技术细节
输入为输入函数（边界条件/源项/初值）在离散点上的采样值，输出为任意空间坐标处的解值，分支网络输出展开系数、核中心（源点）位置可固定或学习，并保留可学习偏置 b_0，DeepONet 基线中 trunk 输出经 tanh 保证有界。损失设计分三类：监督用内部评估点均方误差，无监督用边界条件残差（PIKF 完全不用内部解标签），混合核与 PI-DeepONet 对照中涉及 λ_PDE、λ_BC 权重调节以及自动微分计算 PDE 残差所需的高阶导数。关键超参包括展开项数/核个数 p、混合核中的低秩修正核数 K_c 及权重组，计算上核展开使参数量显著少于隐式 trunk，但核中心布局、虚拟边界选择与无界域截断仍影响精度；物理先验主要来自解析基本解、浅水波导的 Pekeris 核与简正模核。主要局限在于 PIKF 与 HK 依赖解析基本解，DeepONet 分支网络对固定传感器布局的依赖也使输入侧分辨率无关性受限，而 PI-DeepONet 的软约束权重需人工调参且高阶级数计算代价大。
