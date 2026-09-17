# Managing Action Preconditions in Neuro-Symbolic RL: Three Placement Strategies for Embodied Agents

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Norbert Oswald, Fabian Deuser, Thomas Bräunl
- 机构：University of the Bundeswehr Munich, The University of Western Australia
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16056v1) · [PDF](https://arxiv.org/pdf/2609.16056v1)

## TLDR
This paper compares three placements for injecting precondition Bayesian-network knowledge into neuro-symbolic RL—an inference-time symbolic verifier, a training-and-inference symbolic enforcer, and an in-network symbolic learner—showing that where the knowledge enters critically shapes solution quality, sample efficiency, and traceability on embodied planning and manipulation benchmarks.

## Abstract
Humans carry behaviour knowledge of how to act in familiar situations into every new task rather than relearning it from scratch. There is no reason a Reinforcement Learning (RL) agent shouldn't do the same: known behaviour patterns need not be learned, only applied. Neuro-symbolic RL bridges prior knowledge and RL by injecting symbolic knowledge alongside a learned policy. The point at which this knowledge is integrated is critical: a poor choice can produce, for instance, hallucinated preconditions, which surface as safety and reliability problems in agents acting in changing environments. We formalise this behavioural knowledge as a precondition Bayesian network (BN) over the agent's \emph{structural actions} - the actions whose legality depends on preconditions, such as picking up a key, grasping a block, toggling a door, or dropping an object. The BN restricts when these actions may fire, and we inject it into the RL loop at three placements: (1) a \emph{symbolic verifier}, consulted only at inference, that fires a structural action once its preconditions hold; (2) a \emph{symbolic enforcer}, active during both training and inference, that governs structural-action use throughout learning; and (3) a \emph{symbolic learner}, which folds the knowledge into the network and learns the restriction and use of structural actions itself. To test the three variants we run experiments on two benchmarks with opposite regimes: one built on long, ordered planning chains, the other on continuous manipulation. We compare against strong baselines on solution quality, sample efficiency, and traceability. The payoff is substantial. On MiniGrid, all three placements improve the \emph{solution quality} over the PPO+RND baseline, the symbolic enforcer leading at $98.2\%$ against the baseline's $88.8\%$. On Fetch, $\dots$


## 精读解读（中文）
### 一、研究动机
强化学习智能体若一切从零试错，不仅学习缓慢，在稀疏奖励或大规模环境中甚至无法学到有效策略；而人类会把熟悉情境下的行为知识带入新任务，只做应用而非重新学习。神经符号 RL 通过把符号知识注入学习策略来弥合这一差距，但知识注入的时机与位置至关重要：选择不当会产生"幻觉式前提条件"，在动态环境中表现为安全性与可靠性问题。作者因此将行为知识形式化为作用于"结构动作"（拾取钥匙、抓取方块、开关门、放下物体等其合法性依赖前提条件的动作）的前提条件贝叶斯网络，并系统研究它应在 RL 回路的哪个位置注入。

### 二、技术方案（Method）
方法将任务建模为标准 MDP，并构造一个前提条件贝叶斯网络（precondition BN）：节点包含状态量（夹爪位置、物体位姿、关节速度等）、布尔谓词（如 gripper_at_block、holding，通过阈值 τ_reach、τ_closed 等判定）、子目标（reached、grasped 等里程碑谓词）以及按效果划分的导航动作与结构动作；每个结构动作 a 配有前提函数 ρ_a，对给定状态 s 由 BN 导出合法性掩码向量 ρ(s)。基于同一套规格比较三种注入位置：(1) 符号验证器 SV，训练阶段完全不感知 BN，仅在推理时用 ρ(s) 对策略 π_θ 的输出做门控，前提成立即自动触发结构动作、否则屏蔽非法触发；(2) 符号执行器 SE，同一外挂包装器在训练与推理全程生效，持续限制动作空间；(3) 符号学习器 SL，把谓词向量 φ(s) 与子目标向量 σ(s) 作为输入特征送入监督头 P_ψ，让网络自身学会结构动作的限制与使用。三者仅在 BN 被消费的位置上不同，策略网络与监督头分别记为 π_θ 与 P_ψ。

### 三、结果（Result）
在 MiniGrid ObstructedMaze（长序列有序规划）上，三种注入方式相对 PPO+RND 基线均提升解的质量，其中符号执行器 SE 以 98.2% 领先于基线的 88.8%；在 FetchPickAndPlace（连续操作）上，SAC+HER 本身已接近约 97% 的解决率上限，收益因此转向样本效率，SE 与 SL 约提前 2 倍达到该上限。在真实街道网络上的非具身路径规划任务中，外部注入方式同样领先，并能泛化到留出实例。除性能外，符号验证器 SV 与执行器 SE 还保持了行为的可检查性：只要落地前提条件不成立，结构动作就绝不会触发。

### 四、结论（Conclusion）
知识注入的位置会实质性地决定最终效果，三种放置并非可互相替代的工程选项，而是各有适用区间的设计选择：当基线已接近任务性能上限时，符号知识主要带来样本效率收益而非解质量收益；当任务由长程有序子目标链构成时，解质量提升最为显著。外部注入（尤其是训练期即生效的执行器）在性能、样本效率与可追溯性之间取得最佳平衡，并能在具身基准之外的真实路网任务上泛化。该工作首次在同一前提条件规格下对推理期、训练期与网络级三种注入方式做正面对比，为已知领域模型的服务机器人、仓储与辅助场景提供了设计依据。

### 五、方法论与关键技术细节
该 BN 是标准贝叶斯网络的确定性特例：条件取值均为布尔量，因此求合法性掩码等价于直接做布尔函数求值，而非概率信念更新；若改用 NOTEARS 类结构学习或 NSRT 等神经符号算子学习得到概率化模型，只需把硬掩码换成软概率掩码，整套框架无需改动即成立。前提函数在实现上只依赖其在 BN 中的父节点，典型如 ρ_GRASP = fingers_open ∧ ¬holding ∧ reached。实验以 MiniGrid ObstructedMaze（离散、长有序规划链）与 FetchPickAndPlace（连续操作）两个相反范式为基准，并额外在真实街道网络的非具身路由任务上验证排序是否可迁移，对比维度为解质量、样本效率与可追溯性。主要局限在于领域模型是给定的而非从数据中发现（作者明确面向任务结构清晰的服务机器人/仓储场景），且概率化推广、软掩码下的阈值与超参行为尚未实证。
