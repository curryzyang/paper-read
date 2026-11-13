# StructRL: Model-Free Reinforcement Learning with Replay Graphs

- 区域：精读区
- 排名：4
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Ivo Nowak
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14599v1) · [PDF](https://arxiv.org/pdf/2611.14599v1)

## TLDR
StructRL improves model-free reinforcement learning by building an explicit replay graph from experience, extracting a dynamic-programming graph policy on observed transitions, and transferring it to DQN as action preferences or to SAC as shortest-path targets, yielding large success gains on sparse-reward MiniGrid and continuous PointMaze tasks.

## Abstract
StructRL turns the experience collected during reinforcement learning into an explicit replay graph. Once the graph contains a path to the task goal, dynamic programming selects actions on the observed part of the state space; these actions form a graph policy that is defined only where the required transitions have been observed. StructRL transfers these actions to model-free learners: as action preferences for a DQN Q-model and as target directions along shortest observed paths for a SAC actor. For DQN on three sparse-reward MiniGrid tasks, final success rises from 0.10 to 0.90 (DoorKey), 0.10 to 0.80 (KeyCorridor) and 0 to 0.50 (ObstructedMaze); plain DQN does not catch up with three times the budget. For SAC on continuous PointMaze, graph-derived direction labels raise final success from 0.17 to 1.0 on seven matched runs that reached the goal. Distilling the graph policy into a fresh Q-model gives a DoorKey 6x6 controller that reaches the goal from 91% of reachable states, against 38% for plain DQN. Scaling experiments identify three bottlenecks: incomplete graph support, structural aliasing, and loss of graph information in high-dimensional inputs.


## 精读解读（中文）
### 一、研究动机
稀疏奖励强化学习通常需要大量交互才能发现有用策略；在机器人和生产控制中任务目标与奖励已知，但转移动力学和通往目标的路径未知。标准回放缓冲区只把经验存为独立转移，丢失了转移之间的图结构关系。StructRL 的动机是把学习过程中已收集的转移显式组织成回放图，并相对任务目标评估这些已观测结构，以加速无模型学习。

### 二、技术方案（Method）
StructRL 将交互经验构建为显式回放图，节点是由任务知识指定的结构状态投影 phi（如位置、朝向、携带物、门状态），边来自已观测转移与动作。当图中存在通向任务目标的路径时，用动态规划在已观测状态空间上选出动作，形成仅在所需转移被观测到的图上定义的图策略 pi_G。随后把图策略动作迁移给无模型学习器：对 DQN 作为 Q 模型的动作偏好，对 SAC actor 作为沿最短已观测路径的目标方向，并可把图策略蒸馏进新的 Q 模型；推理时图策略只在支持集内给出决策。

### 三、结果（Result）
在三个稀疏奖励 MiniGrid 任务上，DQN 最终成功率从 0.10 提升到 0.90（DoorKey）、从 0.10 提升到 0.80（KeyCorridor）、从 0 提升到 0.50（ObstructedMaze），而普通 DQN 即使三倍预算也未追上。连续 PointMaze 上，SAC 使用图导出方向标签后，在七个达到目标的匹配运行中把最终成功率从 0.17 提升到 1.0。将图策略蒸馏到新 Q 模型后，DoorKey 6x6 控制器可从 91% 的可达状态到达目标，普通 DQN 为 38%。

### 四、结论（Conclusion）
StructRL 表明，把回放经验显式图化并由动态规划生成受限图策略，可以为无模型 DQN 和 SAC 提供有效的结构化监督，显著改善稀疏奖励与连续迷宫任务的成功率和策略覆盖。图策略还可蒸馏为独立控制器。方法的主要扩展瓶颈是图支持不完整、结构别名以及高维输入中图信息丢失。

### 五、方法论与关键技术细节
关键实现点是结构状态投影 phi 由任务知识指定而非学习，图策略仅在已观测转移支持上定义，动作标签来自图上动态规划或最短已观测路径；DQN 侧用动作偏好注入，SAC 侧用方向标签注入，模型仍按原无模型损失训练。实验覆盖稀疏奖励 MiniGrid 与连续 PointMaze，并用最终成功率和可达状态覆盖评估，蒸馏实验使用 DoorKey 6x6。摘要未给出具体网络结构、损失权重与超参；局限性包括支持集不足导致无决策、结构投影引发别名、以及高维输入下图信息在迁移中丢失。
