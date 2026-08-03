# Hypergradient-based Bilevel Reinforcement Learning with Improved Sample Complexity

- 区域：精读区
- 排名：5
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Naman Saxena, Mudit Gaur, Vaneet Aggarwal
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28849v1) · [PDF](https://arxiv.org/pdf/2607.28849v1)

## TLDR
This paper proposes a Hessian-free hypergradient-based bilevel reinforcement learning algorithm that achieves state-of-the-art sample complexity \(\tilde{O}(\epsilon^{-2})\) while removing the Polyak-Łojasiewicz condition on the outer-level objective.

## Abstract
Bilevel reinforcement learning (RL) is an important framework within the literature of RL that can be used to formalize various categories of problems, such as meta-learning, hierarchical task decomposition, and reinforcement learning from human feedback (RL-HF). Most of the bilevel RL algorithms are either not scalable because of using hypergradient with Hessian, or they suffer from high sample complexity because of using penalty-based approximation methods. In this work, we propose a hypergradient-based bilevel RL algorithm using the optimality of the Boltzmann policy for the entropy regularized discounted RL objective function. Our proposed algorithm is Hessian-free and obtains an iteration complexity of $O(ε^{-1})$ and state-of-the-art sample complexity of $\tilde{O}(ε^{-2})$ under mild regularity conditions. Further, in our convergence analysis, we are able to remove the assumption of the Polyak-Lojasiewicz (PL) condition on the outer-level objective function present in the prior state-of-the-art sample complexity work.


## 精读解读（中文）
### 一、研究动机
现有双层强化学习算法要么因使用含Hessian的hypergradient而难以扩展到大规模参数化策略，要么基于罚方法近似外层梯度导致样本复杂度较高；同时先前最优样本复杂度工作还依赖外层目标的Polyak-Łojasiewicz条件。本文希望提出一种无需Hessian、可扩展且样本复杂度更优的双层RL算法，并去掉PL条件和内层唯一最小化假设。

### 二、技术方案（Method）
该方法以熵正则折扣回报目标作为内层RL目标，外层目标定义为策略分布下轨迹损失的期望（如RLHF中的Bradley-Terry偏好损失）。核心是利用Boltzmann策略在熵正则RL目标下的最优性，对非可实现参数化策略类引入梯度移位值函数U和W，将其作为Q函数与值函数梯度的替代，从而构造无Hessian逆项的近似hypergradient。算法AHO交替优化：内层求熵正则RL的最优策略参数，外层用该近似超梯度更新奖励参数x；整个流程不计算Hessian，也不需要PL条件或内层唯一最小化假设。

### 三、结果（Result）
理论分析给出所提AHO算法的迭代复杂度为O(ε^{-1})，样本复杂度为O˜(ε^{-2})，将先前罚方法类双层RL算法的最优样本复杂度从O˜(ε^{-3})改进到O˜(ε^{-2})。同时，算法在连续状态动作空间上成立，是Hessian-free的，并去除了外层PL条件和内层唯一最小化假设。

### 四、结论（Conclusion）
本文提出的AHO是一种可扩展的Hessian-free双层强化学习算法，在样本复杂度和假设条件上均优于已有工作，适合元学习、层次任务分解和RLHF等双层RL场景。该结果说明利用Boltzmann策略最优性可以有效构造低复杂度超梯度，为双层RL提供更实用的理论方案。

### 五、方法论与关键技术细节
关键细节包括：内层使用熵正则折扣RL目标，温度系数τ控制策略探索性；外层轨迹损失可覆盖Bradley-Terry等偏好模型；U和W分别表示以Boltzmann策略从状态或状态-动作出发的折扣奖励梯度累计。Boltzmann最优策略的闭式形式使hypergradient中不再出现Hessian逆，且所构造的近似超梯度消除了罚方法中梯度近似误差O(σ^2)与采样误差O(1/(σ^2B))之间的权衡。收敛性证明只需温和正则性条件，但不可实现参数化策略类需要额外条件以保证Boltzmann最优性的可用性。当前文稿以理论分析为主，未展示数值实验，实际应用中的函数逼近误差和常数依赖仍需进一步验证。
