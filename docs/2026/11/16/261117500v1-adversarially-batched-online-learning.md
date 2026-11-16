# Adversarially Batched Online Learning

- 区域：精读区
- 排名：10
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Mingda Qiao, Kerui Wu
- 机构：University of Massachusetts Amherst
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17500v1) · [PDF](https://arxiv.org/pdf/2611.17500v1)

## TLDR
The paper introduces adversarially batched online learning, where a learner can update only at adversarially chosen batch boundaries, and characterizes the resulting regret for stochastic bandits, OCO, experts, and adversarial bandits via batch-structure complexity measures, with matching bounds showing that optimal regret is governed by relative batch growth for stochastic bandits and by the 2-norm of batch lengths for the other problems.

## Abstract
We introduce adversarially batched online learning, where the learner may update its decision rule only at a restricted set of time steps. Equivalently, the time horizon is partitioned into batches, within which the learner must use a fixed policy. We study this model for four canonical problems: stochastic bandits, online convex optimization, prediction with expert advice, and adversarial bandits. For stochastic bandits, we identify a universal complexity measure based on relative batch growth and establish both gap-dependent and gap-independent regret bounds. We show that the multiplicative penalty relative to the standard gap-dependent complexity can grow superlinearly in batch hardness. For the remaining three, we show that the optimal regret is tightly characterized by the 2-norm of the batch-length sequence. The upper bound is achieved by a batch-oblivious learner who does not know the batch structure, via a generic adaptive doubling trick tailored to this complexity measure. In contrast, the lower bound holds even for batch-aware learners.


## 精读解读（中文）
### 一、研究动机
标准在线学习通常假设每轮后都能立即更新策略，但临床试验、众包标注、分布式系统同步等场景只在少数时间点提供反馈或允许部署更新，策略必须在批内保持不变。已有 batched 学习多由学习者自行设计批次以权衡后悔与批数，本文转而研究更新时点由环境或对手决定且不可更改的 adversarially batched 情形，刻画批次结构对可学习性的根本影响。

### 二、技术方案（Method）
作者把时间域划分为长度 b_1,...,b_B 的批次，学习者在每个批次内使用固定策略或动作，仅在批末获得累计反馈并更新，并区分预先知道批次结构的 batch-aware 与只知道当前批结束、不知道未来边界的 batch-oblivious。针对随机多臂老虎机定义批次硬度 α=max_j b_j/t_{j-1}（t_{j-1} 为此前累计长度），提出带合并操作的逐次消除算法并给出 gap-dependent 与 gap-independent 分析；针对 OCO、专家建议和对抗老虎机，分别用 OGD、Hedge、EXP3 等凸优化或在线学习算法处理批内累计损失或次梯度，并用面向 2-范数复杂度的通用自适应倍增技巧实现 batch-oblivious 上界。下界侧通过对对手构造和批次结构实例化，证明即使允许学习者知道批次结构也无法突破相应复杂度。

### 三、结果（Result）
随机老虎机得到 gap-dependent 期望后悔 O(min{T, α^2 log(NT) Σ_{i:Δ_i>0}1/Δ_i}) 与 gap-independent 后悔 Õ(min{T,√(αTN)})；下界在适当条件下给出 Ω(α Σ1/Δ) 与 Ω(√(αNT))，并进一步构造 Ω(α^{3/2}Σ1/Δ) 的 gap-dependent 下界，说明相对标准 UCB 复杂度的乘性惩罚可随批次硬度超线性增长。对 OCO、专家问题和对抗老虎机，最优后悔被批次长度序列的 2-范数 ∥b∥_2 紧致刻画，上界由不知道未来批次边界的 batch-oblivious 学习器通过自适应倍增达到，下界即使对 batch-aware 学习器也成立；当批次硬度为常数时，随机老虎机结果可恢复非批处理速率（最多多对数因子），且相比已有工作适用于任意批次结构并把 N/Δ_min 型依赖改进为 UCB 型 gap 求和。

### 四、结论（Conclusion）
该文表明，在更新受外部批次约束的在线学习中，批次结构不是常数级修正，而是决定后悔阶的核心复杂度：随机老虎机由相对批次增长 α 控制，凸优化型三类问题由批次长度 2-范数控制。结果同时说明，学习者在不知道未来更新时点的情况下，借助自适应倍增仍可达到与 batch-aware 下界近匹配的最优速率，为反馈延迟和部署受限的实际系统提供了理论依据。

### 五、方法论与关键技术细节
关键细节包括：随机老虎机奖励在 [0,1]、对抗老虎机损失在 [0,1]、OCO 的动作集紧凸且损失 G-Lipschitz，后悔分别按伪后悔或静态最优固定动作定义；α 取最大 b_j/t_{j-1} 并约定 t_0=1，非批处理对应 ∥b∥_2=√T 而单批次对应线性上界；算法上随机老虎机采用逐次消除与批次合并，其他问题采用 OGD、Hedge、EXP3 加自适应倍增，学习率或步长不需预知完整批次结构；下界构造覆盖 batch-aware 学习者并依赖 t_{j*-1}≥CN、t_{j*-1}≥C_2T/α 等条件；局限是随机老虎机 gap-dependent 的 α^2 上界与 α^{3/2} 下界之间仍有差距，文中还指出其分析会带来 Ω(α^{7/4}) 因子，且结论依赖有界损失或奖励与 Lipschitz 等标准假设。
