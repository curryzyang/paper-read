# Training and Evaluating Ethical Reinforcement Learning Agents on Per-Episode Distributions

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Prabhjyot Singh, Majid Ghasemi, Mark Crowley
- 机构：University of Waterloo
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14642v1) · [PDF](https://arxiv.org/pdf/2608.14642v1)

## TLDR
TLDR: Training ethical RL agents with a per-episode, non-compensatory ESR objective instead of mean-based or linear-scalarized objectives prevents ethical violations from being averaged away across episodes, and in Craftax it holds the stated per-episode violation budget at no cost to mean return—so both training and evaluation should target per-episode distributions rather than means.

## Abstract
Reinforcement Learning (RL) agents trained on a single reward signal exploit the gap between the designed reward and the intended behavior. This is particularly a problem when we are trying to imbue ethical behavior into RL agents. An agent can look ethical on average while concentrating its violations in a few bad episodes, and a creature in the environment harmed in one episode is not restored by good conduct in another. We compare four ways of training ethical behavior in Craftax, an open-ended survival benchmark. The four are: scalar penalties with termination, a linear multi-objective weight sweep, an adaptive Lagrangian constraint, and a non-compensatory utility optimized per episode under the Expected Scalarized Returns (ESR) criterion. All are evaluated under a single detector-based protocol that counts every violation in every episode without censoring. On the frontier of mean return against mean violation rate, the four methods are indistinguishable; per episode they separate sharply. At matched mean return, the ESR agent holds its stated budget of one violation in effectively every episode (worst-decile 1.04 +/- 0.07 violations), the Lagrangian leaks past the same budget (1.14 +/- 0.03), and the weight sweep's worst episodes double it (2.20 +/- 0.20). An observation-augmentation control attributes the separation to the training objective rather than to what the agent observes, and the per-episode guarantee costs nothing on the mean frontier. When ethical violations do not average away across episodes, we argue both training and evaluation must target the per-episode distribution rather than the mean.


## 精读解读（中文）
### 一、研究动机
强化学习智能体在单一奖励信号下会利用设计奖励与真实意图之间的差距，这在赋予智能体伦理行为时尤为严重。一个智能体可能在平均意义上看起来合伦理，却将违规集中在少数恶劣回合中；环境中的一个生物在一个回合中被伤害，并不会因另一个回合中的良好行为而得到弥补。因此当伦理违规不能跨回合平均抵消时，训练和评估都必须针对每个回合的分布而非均值。

### 二、技术方案（Method）
在Craftax开放世界生存基准上比较四种伦理训练方法：带终止的标量惩罚、线性多目标权重扫描、自适应拉格朗日约束、以及基于每回合期望标量化回报（ESR）的非补偿效用。环境奖励为双分量向量[r_ext, r_eth]，其中r_eth在发生违规时为-10；定义三种困境（禁止杀戮、可持续性、比例武力）。ESR-PPO通过回合内累计回报的效用增量作为telescoping伪奖励，使用平滑阈值字典序效用u_TLO = sigma(s*(tau_tol - v))*R_ext - rho_u*v，并可选通过Bradley-Terry偏好学习蒸馏该效用；拉格朗日基线采用对偶上升更新约束乘子。所有方法在共享检测器环境中评估，不删减任何步骤，统计每个回合的违规分布。

### 三、结果（Result）
在平均回报对平均违规率的前沿上四种方法无法区分，但按每回合分布则清晰分离。在匹配的平均回报下，ESR智能体几乎在每个回合都保持其声明的预算（最差十分位1.04±0.07违规），拉格朗日略超预算（1.14±0.03），权重扫描的最差回合翻倍（2.20±0.20）。观察增强对照表明分离来自训练目标而非观察内容，且每回合保证在平均前沿上不产生代价。

### 四、结论（Conclusion）
当伦理违规不能跨回合平均抵消时，训练和评估必须针对每回合分布而不是均值。非补偿效用目标能在不牺牲平均回报的前提下将每回合违规数控制在预算内，优于平均约束方法，且该结论在方法论上归因于目标设计而非观测信息。

### 五、方法论与关键技术细节
关键实现细节包括：道德惩罚为事件触发且每回合固定-10，不提供正塑形；效用u_TLO使用逻辑门控sigma(s*(tau_tol-v))，sharpness s=12，容差tau_tol=0.5（严格）或k+0.5（容忍k次违规），每违规额外成本rho_u=10或1；ESR与SER的区别在于期望与效用顺序，线性效用下二者等价；评估采用共享检测器环境，无删减的逐步计数，报告标准差、任意违规概率和CVaR（最差十分位均值）等分布指标；随机策略和环境意味着不能保证完全干净回合；线性于状态-动作占用测度的统计量（如均值前沿）无法区分每回合目标与期望目标，分离必须出现在高阶矩。蒸馏变体从已训练智能体的回合返回池中生成偏好对，用Bradley-Terry损失拟合MLP，输出重标定到游戏回报单位。拉格朗日预算d在{0.5,1,2,4}中扫描，权重扫描w_eth在{0.1,0.3,1,3,10}中。
