# A Bellman Optimality Equation for Plasticity

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Jeremy Lucas, Doina Precup
- 机构：Mila -- Quebec Artificial Intelligence Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10776v1) · [PDF](https://arxiv.org/pdf/2609.10776v1)

## TLDR
This paper derives a Bellman optimality equation for optimizing plasticity—defined as the generalized directed information from observations to actions—within Markov decision processes, mirroring prior empowerment optimization and providing preliminary groundwork for managing the empowerment-plasticity tradeoff in continual reinforcement learning.

## Abstract
In continual reinforcement learning, carefully managing the stability-plasticity tradeoff remains a core challenge. Recent work by Abel et al. (2025) formalized this dilemma by defining plasticity as the generalized directed information from an agent's observations to its actions, and empowerment as the generalized directed information from its actions to its observations. This formulation successfully reframes the traditional stability-plasticity tradeoff as an empowerment-plasticity tradeoff. However, while extensive literature exists on optimizing for empowerment, there is currently no research addressing the optimization of plasticity under this new definition. This paper presents preliminary work toward optimizing plasticity within Markov decision processes. We show that there exists a Bellman optimality equation for optimizing plasticity similar to previous work for empowerment.


## 精读解读（中文）
### 一、研究动机
持续强化学习中稳定性-可塑性权衡是核心挑战。Abel等2025将可塑性形式化为从观测到动作的广义有向信息，将赋权定义为从动作到观测的广义有向信息，从而把传统权衡重构为赋权-可塑性权衡。赋权优化已有大量研究，但在该新定义下可塑性的优化尚属空白，本文针对这一空缺开展初步研究。

### 二、技术方案（Method）
本文在马尔可夫决策过程中推导可塑性的贝尔曼最优方程，类比Leibfried等关于赋权的统一贝尔曼框架。定义状态-动作历史下的价值函数V*(s_{t-1},a_{t-1})，以I(S_{t+1};A_{t+1}|S_t,A_t)为即时信息奖励，以γV*(s_t,a_t)为未来价值，最大化关于π的期望对数比log(π/q)，其中q为对下一状态求和的边际动作分布。理论上证明相应贝尔曼算子是压缩映射，并因q边际耦合所有下一状态的动作选择，将内层优化化为多权重背包问题，用动态规划跟踪累积权重以剪枝，进而给出表格型值迭代算法。

### 三、结果（Result）
作者证明可塑性的贝尔曼最优方程存在且算子是压缩的，策略可限制为确定性策略。在双状态双动作的Control-Gated MDP基准中，通过0.01粒度策略枚举绘制可塑性-赋权前沿，发现最大化可塑性的策略是确定性的：π*_plastic(1|0)=1且π*_plastic(0|1)=1；而最大化赋权的策略更分散，在状态0均匀行动，在状态1按一定概率选择动作。该前沿还显示可塑性上界为log2|A|比特，赋权上界为log2|S|比特。

### 四、结论（Conclusion）
本文首次在Abel等提出的信息论可塑性定义下给出了可优化的贝尔曼最优方程，为持续强化学习中主动优化和控制可塑性提供了理论基础。该结果与赋权的贝尔曼框架形成镜像，支持了稳健持续学习智能体需同时将赋权和可塑性维持在临界阈值之上的观点。未来工作可将该表格方法扩展到深度变分近似及更大规模环境。

### 五、方法论与关键技术细节
输入为已知转移概率p(s_t|s_{t-1},a_{t-1})的有限MDP，无外部奖励（α=0），策略增广为π(a_t|s_{t-1},a_{t-1},s_t)。关键损失/目标为log(π/q)，其中q(a_t|s_{t-1},a_{t-1})=Σ_{s_t} p(s_t|s_{t-1},a_{t-1})π(a_t|s_{t-1},a_{t-1},s_t)；因q共享导致动作耦合，采用多权重背包动态规划处理，原始搜索空间为|A|^{|S|}。实现细节包括值迭代初始化V=0、随机确定性策略、收敛阈值θ、折扣γ，表格基准仅2状态2动作。局限在于工作为初步研究，仅在小规模表格环境与两个扩展环境中评估，模型已知且状态动作有限，尚未给出深度或大规模场景的可行性。
