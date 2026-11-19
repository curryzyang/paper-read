# Neural Network-Based Modeling of Hysteretic Systems: From Prandtl and Preisach Neural Networks to Neuro-Madelung and Neuroplastic Continuous Models

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Mehrdad Shafiei Dizaji, Farzad Shafiei Dizaji
- 机构：University of Virginia
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23240v1) · [PDF](https://arxiv.org/pdf/2611.23240v1)

## TLDR
This review traces the development of specialized neural-network architectures that embed hysteresis-specific memory mechanisms—from Prandtl and Preisach neural networks to generalized, neuro-Madelung, extended Preisach, and dynamic plastic continuous models—for modeling complex path-, degradation-, and rate-dependent hysteretic systems.

## Abstract
Hysteresis is a complex nonlinear phenomenon characterized by memory dependence, path dependence, and, in many physical systems, degradation, non-congruency, asymmetry, and rate dependence. This review examines the development and capabilities of Prandtl neural networks (PNNs), Preisach neural networks (PreisachNNs), generalized Prandtl neural networks (GPNNs), the neuro-Madelung model (NMM), extended Preisach neural networks (EPNNs), and dynamic plastic continuous neural networks (DPCNNs). Particular attention is given to their mechanisms for representing memory, network architectures, activation functions, training algorithms, treatment of deterioration and rate dependence, and applications to nonlinear structural and material systems. The PNN introduced hysteretic memory directly into neural activation through stop operators and demonstrated accurate nonlinear dynamic analysis of structures. Preisach-NNs subsequently extended this concept through an additional nonlinear hidden layer to represent non-Masing hysteresis. GPNNs introduced deteriorating-stop neurons to capture stiffness and strength degradation and non-congruent hysteresis. A different generalization was provided by the NMM, which combined Madelung's hysteresis rules with multilayer feedforward neural networks to represent diverse rate-independent and rate-dependent behaviors. These developments culminated in the EPNN, which combines deteriorating hysteretic operators, nonlinear neural mappings, and input-rate information to accommodate Masing and nonMasing, symmetric and asymmetric, congruent and noncongruent, and rate-independent and rate-dependent hysteresis.


## 精读解读（中文）
### 一、研究动机
滞回系统具有记忆依赖、路径依赖以及退化、非一致性、不对称和速率依赖等复杂特征，传统前馈神经网络本质无记忆，而NARX、循环或时滞网络主要依赖历史输入输出且递归预测易误差累积。因此，需要把滞回物理机制直接嵌入神经网络结构，而不仅是做黑箱函数逼近。

### 二、技术方案（Method）
本文系统综述PNN、Preisach-NN、GPNN、NMM、EPNN和DPCNN六类模型：PNN以stop算子作为隐层神经元并采用连续遗传算法优化连接权重与屈服点；Preisach-NN在stop神经元后增加sigmoid隐层并用空间扩张次梯度法训练；GPNN用stop与play算子构造退化stop神经元，以累积滑移表征损伤并用退化参数控制刚度/强度退化；NMM用Madelung转折点与擦除规则管理记忆，剩余非线性映射由两层各15个sigmoid神经元的MLFFNN经Levenberg-Marquardt训练，输入含当前输入、相关历史转折点和输入速率；EPNN组合退化/衰减stop神经元、sigmoid映射和输入速率项，采用遗传算法与次梯度法混合训练；DPCNN则让神经元通过连续非线性塑性介质耦合，用有限元模拟波传播，并以灵敏度分析和最速下降优化神经权重及介质材料属性。

### 三、结果（Result）
PNN在白噪声训练、El Centro和Gilroy地震记录测试下能准确复现强非线性滞回 shear frame 的动力响应；Preisach-NN在非Masing算例中报告MSE约2.41×10^-5；GPNN能复现严重损伤、非一致滞回并优于原PNN；EPNN在含速率项时误差降至约7×10^-5，去除速率项误差显著增大，异频测试MSE约0.002，并能同时处理混凝土等材料的非Masing、不对称、非一致和速率相关行为；DPCNN展示了塑性连续介质中波传播与材料塑性参与学习记忆的新范式。

### 四、结论（Conclusion）
该综述表明滞回神经网络正从单纯逼近输入输出关系，转向将记忆、塑性、退化和速率依赖等物理机制直接嵌入计算模型，形成早期物理引导神经网络。不同模型在通用性与复杂度之间存在权衡：算子型网络逐步扩展至非Masing、非一致、退化和速率依赖，但训练与结构复杂度上升；DPCNN提供空间连续介质记忆的新思路，但有限元框架计算密集且理论实现仍处早期。未来方向包括可微滞回算子、自动微分与PINN/神经算子融合、不确定性量化、跨材料迁移学习及更高效可解释模型。

### 五、方法论与关键技术细节
关键实现细节包括：PNN以stop算子作为历史依赖激活，GA直接优化非光滑目标；Preisach-NN用第二sigmoid隐层实现非线性记忆组合，并以次梯度法处理大量权重；GPNN的退化stop由stop与play组合，累积滑移作为损伤指标，退化参数越大越接近普通stop；NMM依赖Madelung转折点与wipe-out规则，固定两层15个sigmoid神经元、LM训练，并可构造隐式逆模型用于开环补偿；EPNN输入含x(t)与x_dot(t)，采用GA定位参数区域后用次梯度加速收敛；DPCNN用FEM波传播与灵敏度梯度，分阶段优化连接权重和介质属性，主要局限为算子非光滑、显式历史管理、通用性增加带来结构与训练成本、DPCNN计算密集及不确定性量化与跨材料迁移尚不充分。
