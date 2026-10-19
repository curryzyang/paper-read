# Local Projected Controllability of Nonlocal Continuity Equations

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Elena Goncharova, Nikolay Pogodaev, Maxim Staritsyn
- 机构：Siberian Branch of the Russian Academy of Sciences, Universidade do Porto
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22550v1) · [PDF](https://arxiv.org/pdf/2610.22550v1)

## TLDR
The paper develops a Lie-bracket-based sufficient condition for local projected controllability of controlled nonlocal continuity equations on probability measures by lifting the measure dynamics to an ODE on a Banach space of maps, motivated by finite-dimensional feature observations in self-interacting machine-learning models.

## Abstract
We formulate and study the problem of local projected controllability (LPC) for characteristic solutions of controlled nonlocal continuity (transport) equations on the space of probability measures over a separable Banach space. The task is motivated in particular by self-interacting models in machine learning, whose action can be represented as controlled dynamics of the probability distribution over input data, while the actual output is given by a finite-dimensional vector of features extracted from the terminal distribution by a possibly nonlinear observation map. Given a fixed finite family of velocity fields which may depend on the transported measure, we ask whether the reachable values of the observable vector fill a neighborhood of its reference value. Our approach is to lift the transport equation in the space of measures to an ordinary differential equation on a Banach space of maps. This representation makes it possible to employ the machinery of Lie brackets developed for Banach manifolds, while the resulting sufficient condition for LPC can be formulated directly on the space of measures.


## 精读解读（中文）
### 一、研究动机
论文关注无限维概率测度空间上的受控非局部连续性方程：实际应用往往不要求控制整个测度，而只要求由终末分布经观测映射提取的有限维特征达到参考值附近。该问题受机器学习中自交互模型（如 Transformer 自注意力）启发，其中输入数据分布按非局部速度场演化，输出是有限维特征向量，因此需要判定可观测向量的可达集是否覆盖参考值的邻域。

### 二、技术方案（Method）
在可分 Banach 空间 Q 的概率测度空间 P(Q) 上，考虑由有限个可能依赖当前测度的速度场 V_j 生成的控制线性非局部连续性方程，控制取自紧集 U 上的 L∞ 函数，并给定光滑观测 g:P(Q)→R^N。作者将测度层面的输运方程提升为 Banach 空间 C_b(Q;Q) 中位移映射的常微分方程，由提升方程的解重构特征线和测度曲线，再在 Banach 流形框架下使用 Lie 括号技术；最终把充分条件表述为：对非局部速度场诱导的算子 L_{V_j} 及其迭代交换子作用于观测，在参考测度处投影后的方向张成 R^N。

### 三、结果（Result）
主要结果是 LPC 的一个充分条件：若 Lie 代数中存在 W_i 使 {Dg(μ0)[W_i(μ0)]} 张成 R^N，则足够小时间 T 内由分段常值控制得到的观测值 g(μ_T) 覆盖 g(μ0) 的邻域，从而系统在 μ0 处关于 g 局部投影可控。该定理把 Hermes 的观测局部可控性判据推广到 Banach 流形上具有向量值控制的无漂移 ODE，并给出可直接在测度空间检验的交换子秩条件；示例表明 Transformer 代理模型中缺失的投影方向可由一阶交换子补足，而在平移或旋转等变约束下，局部速度场无法改变观测，合适的非局部速度场才能达到所需投影秩。

### 四、结论（Conclusion）
论文说明即使概率测度空间缺乏自然的 Banach 流形结构，也可以通过提升到位移映射空间并借助 Lie 括号几何控制工具来研究有限维观测的可控性。其贡献是为非局部连续性方程提供了一套可计算的 LPC 充分判据，并揭示了非局部性与对称性约束对投影可控性的关键作用。

### 五、方法论与关键技术细节
关键细节包括：Q 为可分实 Banach 空间，状态为 Borel 概率测度，速度场可写成 V(q,μ) 且可能非局部依赖 μ；控制为 L∞([0,T];U)，U 为含 [-1,1]^m 的紧集，解按特征解理解；光滑性通过对非局部速度场提升和观测的局部 Fréchet 光滑性假设保证，积分型泛函与有界核情形可由引理推出。判据使用 Lie 括号约定 [F1,F2]φ=F1(F2φ)-F2(F1φ) 及算子 L_V 的迭代交换子，若有限个泛函在 L_{V_j} 下封闭则可精确降维；对积分泛函和核型非局部场，交换子有核的显式公式。局限在于高阶括号需要更多切换且位移量级更小，缺乏括号长度通用上界，数值误差和切换限制会影响可实现深度；此外同时控制任意大有限族观测不蕴含无限维可控性，因为时间窗口和邻域未必一致。
