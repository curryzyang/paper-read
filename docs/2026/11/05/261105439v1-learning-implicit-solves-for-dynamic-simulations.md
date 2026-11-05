# Learning Implicit Solves for Dynamic Simulations

- 区域：精读区
- 排名：2
- 匹配度：5.7/10
- 来源：arxiv
- 作者：Chawit Kaewnuratchadasorn, Jiaji Wang, Xin Nie
- 机构：The University of Hong Kong, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05439v1) · [PDF](https://arxiv.org/pdf/2611.05439v1)

## TLDR
INOS is a reusable neural implicit solver that pretrains a neural operator on static equilibrium solutions and embeds it in Newmark-β integration to deliver accurate, efficient, zero-shot dynamic simulations without dynamic trajectory supervision.

## Abstract
High-fidelity simulation of dynamical systems is central to scientific discovery and engineering design, yet remains computationally demanding. Here we introduce the Implicit Neural Operator Solver (INOS), which learns the implicit solve and encodes a time integrator. INOS pretrains a neural operator from static equilibrium solutions and reuses it within Newmark-$β$ integration. At each time increment, the integrator forms an effective equilibrium problem, the pretrained neural operator infers the next-step solution field, and the Newmark relations advance the dynamic state. Numerical examples in linear and nonlinear elastodynamics demonstrate accurate full-field predictions without dynamic trajectory supervision. Comparative results show that INOS, evaluated zero-shot, achieves higher predictive accuracy than neural solver baselines trained on dynamic simulations. In addition, INOS delivers over 4,600$\times$ speedup in nonlinear simulations over sequential classical finite-element solvers. INOS natively accommodates changes in dynamic conditions and enables reuse of the pretrained operator across spatial and temporal discretizations. Further evaluation demonstrates a stable million-step rollout. These findings establish INOS as a reusable neural implicit solver for accurate, efficient, and robust dynamic modeling.


## 精读解读（中文）
### 一、研究动机
高保真动力系统仿真对科学发现和工程设计至关重要，但传统隐式时间积分在大规模线性和非线性问题中计算代价高，而现有神经求解器多依赖动力轨迹监督，训练成本高且跨时间离散与载荷变化的外推稳定性不足。作者希望把算子学习的表达能力与Newmark隐式积分的结构化状态更新结合，仅学习静态平衡求解并在动力 rollout 中零样本复用。

### 二、技术方案（Method）
INOS先在线性/非线性静态平衡问题上预训练神经算子，输入为附加刚度场和等效力/载荷及空间坐标，输出平衡位移场；其中静态问题采用附加节点弹簧刚度K_spring，动力问题经Newmark-β递推转化为有效平衡问题，附加刚度为a0M+a1C，在集中质量和质量比例阻尼下为对角节点系数。每个时间步由当前状态和下一时刻外载构造有效力，预训练算子一次性预测下一时刻位移，再由Newmark关系更新速度和加速度，仅平衡映射被学习，时间积分和输入构造均按预设格式执行；结构化网格用FNO，非结构化网格用Transolver，静态标签由Newton法生成。

### 三、结果（Result）
在线性和非线性弹性动力学基准上，INOS无需动力轨迹监督即可零样本给出全场预测，并在相同骨干家族内多数IID、OOD(F)和OOD(H)设置下取得低于轨迹训练神经基线的误差；非线性仿真相对顺序有限元求解取得超过4600倍加速，并展示百万步稳定rollout。对比也显示个别极端外推情形仍有不足，例如1D Transolver版INOS在力幅外推下误差高于轨迹训练的FNO。

### 四、结论（Conclusion）
INOS表明，将静态平衡神经算子嵌入Newmark隐式积分可形成可复用、可微且模块化的神经隐式求解器，在不依赖动力轨迹训练的情况下实现准确、高效和较稳健的动力仿真。其性能依赖静态预训练对有效平衡输入空间的覆盖，并为跨空间/时间离散复用和长时程rollout提供了可行路径。

### 五、方法论与关键技术细节
关键实现包括：用静态平衡数据预训练，动力测试对轨迹监督为零样本；Newmark有效平衡中的附加刚度由a0M+a1C给出，采用集中质量和质量比例阻尼使其对角化并以节点系数输入；每个非线性基准使用与所选Δt匹配的固定附加刚度场，且该场作为算子输入；局部平衡预测误差会随自回归步累积，因此预训练覆盖、载荷外推和时间步变化是主要约束，OOD力幅/时域和固定Δt设置构成局限性。
