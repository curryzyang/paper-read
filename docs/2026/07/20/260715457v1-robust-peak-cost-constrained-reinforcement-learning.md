# Robust Peak-cost Constrained Reinforcement Learning

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Shilpa Mukhopadhyay, Sourav Ganguly, Santosh Mohan Rajkumar, Honghao Wei, Debdipta Goswami, Arnob Ghosh
- 机构：The Ohio State University, NJIT, Washington State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15457v1) · [PDF](https://arxiv.org/pdf/2607.15457v1)

## TLDR
The paper introduces a robust peak-cost constrained reinforcement learning framework to maximize reward while limiting the maximum trajectory cost, reveals that peak-cost MDPs may not have zero duality gap, and proposes a surrogate optimization method with integral probability metric-based robust value estimation that ensures safety under dynamics perturbations with bounded constraint violation.

## Abstract
We study robust peak-cost constrained reinforcement learning (RP-CRL), where the objective is to maximize expected reward while controlling the maximum cost encountered along a trajectory. This setting is motivated by safety-critical applications in which a single large violation can be catastrophic and therefore cannot be adequately captured by the standard CMDP framework based on expected cumulative cost. Existing reachability-constrained RL methods adopt Lagrangian-based approaches, yet the underlying duality properties of peak-cost constrained MDPs remain unclear. We show that, unlike standard CMDPs, peak-cost constrained MDPs may not admit zero duality gap. We further consider a robust formulation to address simulator-to-real-world mismatch in the transition dynamics. To solve this problem, we develop a surrogate optimization framework and a robust value estimation method based on integral probability metrics. We prove that, with appropriate hyperparameter choices, the surrogate solution attains the same robust reward value as the original problem while violating the constraint by at most epsilon. Experiments show that the proposed method effectively enforces safety under dynamics perturbations while retaining strong reward performance.


## 精读解读（中文）
### 一、研究动机
现有约束强化学习（CMDP）基于期望累积成本，无法捕捉单次大违规带来的灾难性后果，而峰值成本约束（如最大即时成本低于阈值）更符合安全关键应用。现有基于可达性的方法采用拉格朗日对偶，但尚未证明对偶间隙为零；同时缺乏对模拟到真实动力学失配的鲁棒性。

### 二、技术方案（Method）
构建鲁棒峰值成本约束MDP，采用基于积分概率指标（IPM）的矩形不确定性集描述动力学扰动。提出代理优化问题min_π max{ max_P J_r^{π,P}/β, (max_{P,s∈S^{π,P}} V_{c,peak}^{π,P}(s)-b) }，其中峰值成本价值函数通过折扣递归定义并采用Log-Sum-Exp平滑max操作。算法为Actor-Critic框架：actor使用PPO裁剪目标，critic分别对奖励和峰值成本进行IPM鲁棒化TD误差估计，TD误差中加入ρ||w_{2:d}||_2项；利用GAE计算优势函数。

### 三、结果（Result）
理论证明峰值成本约束MDP即使在两状态场景下也可能不具备零对偶间隙（与标准CMDP本质不同）。代理优化在β≥C_max/ϵ时，最优解可达到与原鲁棒问题相同的鲁棒奖励值，且约束违反不超过ϵ。实验表明方法在动力学扰动下能有效保持峰值成本约束，同时获得高奖励。

### 四、结论（Conclusion）
本文首次揭示峰值成本约束MDP对偶间隙非零，提出了鲁棒峰值成本约束RL的代理优化框架和基于IPM的鲁棒价值估计方法，理论保证与实验验证共同说明该方法在模拟到真实迁移中具有可靠的安全性。

### 五、方法论与关键技术细节
关键点：1) 对偶间隙非零原因在于峰值成本约束不满足状态-动作占用度量的凸性；2) IPM鲁棒贝尔曼算子形式为L_P V = (1-γ)c + γ V + ρ||w_{2:d}||_2；3) 代理目标中β控制约束违反容忍度，需满足β≥C_max/ϵ；4) 采用LSE近似max以保证可微；5) 不确定性集基于IPM通用距离，适用于连续状态空间；6) 局限性：理论保证依赖于矩形不确定性集假设，且β选择可能需要领域知识。
