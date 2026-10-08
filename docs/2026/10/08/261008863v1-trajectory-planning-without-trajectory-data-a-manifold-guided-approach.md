# Trajectory Planning without Trajectory Data: A Manifold-Guided Approach

- 区域：精读区
- 排名：8
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Silong Yong, Anji Liu, Cunxi Dai, Carl Busart, Guanya Shi, Yilun Du, Katia Sycara, Yaqi Xie
- 机构：Harvard University, DEVCOM Army Research Laboratory, National University of Singapore, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08863v1) · [PDF](https://arxiv.org/pdf/2610.08863v1)

## TLDR
Ariadne enables trajectory planning without trajectory data by learning the state-space manifold from state-only observations and using its geometry to construct feasible paths that generalize to unseen start-goal constraints.

## Abstract
A common way for trajectory planning is to leverage generative models trained on large collections of expert trajectories. At inference time, the model generates executable trajectories by conditioning on task goal constraints. However, trajectory-based methods rely on costly supervision, scale poorly with sequence length, and often generalize poorly to unseen constraints such as novel start-goal pairs. We propose an alternative to learn the underlying state-space manifold and use the geometry of the manifold for trajectory planning. This approach requires only state observations and enables generalization to unseen constraints by con- structing trajectories on the learned manifold of the state space. Experiments on Maze2D and robotic motion-planning benchmarks show that Ariadne constructs feasible paths from state-only supervision and generalizes to unseen start-goal combinations. On high-dimensional dual-arm planning, it remains competitive with trajectory-supervised and classical planners, while requiring no trajectory data for training.


## 精读解读（中文）
### 一、研究动机
现有轨迹规划生成模型依赖大规模专家轨迹，监督成本高、随序列长度扩展差，并且对未见过的起止点组合等约束泛化不足，因为轨迹空间覆盖稀疏且模型偏向训练轨迹分布。作者提出仅用状态观测学习状态空间流形，并利用其几何结构在推理时构造可行轨迹，从而规避轨迹级分布外失败。

### 二、技术方案（Method）
Ariadne 先用仅状态数据训练扩散或 score 生成模型，假设有效状态位于低维数据流形上；利用 score 函数及 score 的 Jacobian 估计每个状态的切空间与法空间，获得法空间正交基。轨迹构造被看作在流形上积分一个向量场：先沿目标方向移动，再用法空间投影把位移拉回切空间；该移动-投影过程被解释为算子分裂 ODE。为同时满足流形约束与端点约束，作者提出 Correction-Projection ODE：dx/dt = x1 - x0 + (2-4t)φ + 2t(1-t)dφ/dt，其中 φ 累积投影修正项，并用 Euler 法配合算子分裂数值积分，从给定起点到终点生成状态序列。

### 三、结果（Result）
在 Maze2D 和机器人运动规划基准上，Ariadne 仅用状态监督即可构造可行路径，并能泛化到训练中未见的起止点组合。在 6 自由度机械臂桌面避障以及两个 7 自由度机械臂互避与避障的高维任务中，其表现与轨迹监督扩散规划器和经典规划器具有竞争力，且训练阶段不需要任何轨迹数据。

### 四、结论（Conclusion）
结果表明，不学习轨迹分布而学习状态流形几何，可把规划转化为受端点约束的流形上曲线生成，从而缓解轨迹数据偏置带来的泛化问题。该方法为低成本状态数据驱动的机器人轨迹规划提供了可行路线，但在数值离散和几何估计不完美时仍有残余流形漂移与端点误差。

### 五、方法论与关键技术细节
关键实现点包括：训练输入仅为状态观测，遵循流形假设；用 score 与 score Jacobian 估计低维流形的法空间，而非只用 score 方向；投影通过减去位移在法空间正交基上的分量完成，并可从 score 导出 Riemannian 度量以稳定投影。端点约束通过 CP-ODE 的修正项 φ 显式满足，φ 含投影尺度因子 ε，Euler 离散中投影项控制流形贴合。实验覆盖 Maze2D、6DoF 桌面避障、双 7DoF 机械臂规划，并评估端点误差与流形漂移；局限性是当参考方向与法空间对齐或离散化误差累积时，流形贴合和端点到达不具严格保证。
