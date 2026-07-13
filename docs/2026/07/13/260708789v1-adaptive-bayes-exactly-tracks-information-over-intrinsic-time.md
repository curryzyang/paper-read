# Adaptive Bayes exactly tracks information over intrinsic time

- 区域：精读区
- 排名：4
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Akshay Balsubramani
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08789v1) · [PDF](https://arxiv.org/pdf/2607.08789v1)

## TLDR
Bayesian and multiplicative-weights updates satisfy an exact information-accounting identity for regret, where each round’s excess loss decomposes into an immediate payment for uncertainty and a reduction in information-distance to the comparator, cumulatively defining an intrinsic time that yields exact instead of worst-case regret bounds across a wide range of sequential decision-making settings.

## Abstract
Bayesian and multiplicative-weights updates reweight experts, models, or actions from sequential feedback. We show that the regret of any such update obeys an exact information-accounting identity. On each round, the learner's excess loss to any chosen comparator is the sum of an immediate payment for the uncertainty exposed by the round and a reduction in the information distance from the learner's current weights to the comparator. The cumulative payment defines a pathwise uncertainty clock, the \emph{intrinsic time} of the realized sequence. Summing one-step balances yields two exact adaptive decompositions of cumulative regret, one for each natural way of composing the update across rounds. Because the decompositions are exact rather than upper bounds, favorable stochastic or low-noise regimes appear as self-bounding properties of the realized intrinsic time, not as slack in worst-case analyses. The same calculus covers Hedge, optimistic and side-information variants, continuous priors, boosting, online convex optimization, contextual bandits, and repeated games: the pathwise account is the same in every case.


## 精读解读（中文）
### 一、研究动机
现有贝叶斯和乘法权重更新在序列反馈中的遗憾分析通常采用上界，未能精确揭示更新过程的信息结构。本文旨在建立一个精确的信息核算恒等式，将超额损失分解为即时支付和信息距离减少，从而为自适应算法提供统一框架。

### 二、技术方案（Method）
基于一步信息平衡恒等式，将每轮超额损失拆分为即时支付δ_t(c)和信息距离减少项。通过两种方式累积：先验回火更新从原始先验π和累计得分C_t以当前温度η_t重计算后验p_t；局部更新仅从当前权重p_t和当前得分c_t更新。学习率调度包括平方根时钟（η_t ∝ 1/√V_{t-1}）和压力目标（解方程∑ p_t(i) e^{-η_t(c_t(i)-a_t)}=1）。该恒等式适用于Hedge、乐观变体、边信息（通过复合损失c_t=ℓ_t+u_t）等。关键步骤为每轮计算当前分布p_t，观察损失c_t，更新累积量并调度下一温度。

### 三、结果（Result）
对于任意比较器ρ和任意时间T，累计遗憾R_T^c(ρ)精确等于内在时间支付∑ η_t Q_t(c)加温度变化漂移D_T加终端比较器信息B_T(ρ)。内在时间V_T(c)=∑ Q_t(c)完全由算法和路径决定。平方根时钟调度可实现O(√V_T)遗憾，压力目标调度可实现自我界定的更紧速率。该恒等式覆盖了Hedge、乐观更新、上下文赌博机、重复博弈等多种算法，且无近似松弛。

### 四、结论（Conclusion）
贝叶斯和乘法权重更新本质上遵循一个精确的信息核算，将遗憾分解为可解释的组件。这种视角统一了看似不同的在线学习算法和权衡（如困难/容易序列、一阶/二阶界、不同比较器类等），并为设计自适应算法提供了清晰原理。

### 五、方法论与关键技术细节
内在时间增量Q_t(c)定义为有限温度下当前分布的倾斜累积量，可通过一阶条件计算；平方根调度使用常数C=1/√2；压力目标调度中a_t为自由能水平；先验回火更新需每次完全重计算，复杂度为O(K)；局部更新更高效但需实时求解η_t；二次松弛W_t(c)=1/2∑ Var_{i~p_t}(c_t(i))作为Q_t(c)的近似；算法要求损失c_t使得指数矩有限；局限性包括未处理无限专家集或连续非凸问题，但框架可扩展。
