# SWAP: Stepwise Action Policy Routing for Vision-Language-Action Models

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Mousumi Das, Aditeya Prajapati, Abrar Anwar, Jesse Thomason
- 机构：University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06926v1) · [PDF](https://arxiv.org/pdf/2610.06926v1)

## TLDR
SWAP is an offline reinforcement learning framework that learns a routing critic to dynamically select among multiple Vision-Language-Action policies at each execution step, improving real-world manipulation success by up to 33% and reducing successful trajectory length by 28.3% over fixed-policy and routing baselines.

## Abstract
Robot manipulation systems using Vision-Language-Action (VLA) model backbones typically use just one VLA for task execution. However, individual VLAs do not perform well across different task states and environments. We introduce a framework for dynamically composing multiple VLA policies during execution: StepWise Action Policy Routing (SWAP). SWAP formulates policy routing as an offline reinforcement learning problem, learning a routing critic that selects the most appropriate policy at each decision step given the current observation. SWAP enables robots to select new policies to execute online rather than committing to a single policy for the duration of an episode. We evaluate SWAP on both real-world DROID manipulation tasks and LIBERO simulation experiments. SWAP improves over fixed-policy execution and routing baselines, giving absolute improvements in real-world task success up to 33% while reducing successful trajectory robot action step length by 28.3%.


## 精读解读（中文）
### 一、研究动机
现有 VLA 机器人系统通常在整个 episode 中固定执行单一策略，但单个 VLA 难以在不同任务状态、场景分布和接触/恢复阶段中始终最优，因此需要多个互补策略的动态组合。SWAP 的核心动机是把机器人操作中的策略选择建模为逐步策略路由问题，而不是在回合开始时一次性选定控制器，从而让机器人在线切换最适合当前观测的策略。

### 二、技术方案（Method）
SWAP 将策略路由形式化为离散动作空间上的离线强化学习：给定候选 VLA 策略库 P={π1,...,πK}，机器人以底层 VLA 的 action chunk 为路由粒度，构建离线路由数据集 D={(o_t,z_t,r_t,o_{t+c},d_t)}，其中 o_t 为 chunk 起始观测，z_t 为所选策略，r_t 为稀疏二值成功奖励，o_{t+c} 为执行 c 步后的观测，d_t 为终止标志。训练时用冻结的 Qwen2.5-VL-3B 将当前视觉观测和语言指令编码为 2048 维嵌入，拼接可学习的候选策略身份嵌入后送入轻量 double-Q MLP 和独立 value 网络，并用 IQL 通过 TD 损失学习 Q1、Q2，再用 expectile 回归拟合 V，取 min(Q1,Q2) 抑制高估。推理时，SWAP 在当前观测下评估所有候选策略的 Q 值，选择 z_t=argmax_z min(Q1(o_t,z),Q2(o_t,z))，执行被选策略产生的短时 action chunk，随后重复该过程，实现执行中的在线策略切换；在真实 DROID 上还对多相机视角的 Q 值进行聚合以增强鲁棒性。

### 三、结果（Result）
在真实 DROID Franka 操作任务上，SWAP 平均成功率从最佳固定策略 π0-FAST 的 63.3% 提升到 96.7%，绝对提升约 33 个百分点，并优于随机路由的 66.7%；三个任务中 Marker→Bowl 和 Cube on Cloth→Bowl 达到 100%，Cube→Cup 达到 90%。同时，在成功轨迹中 SWAP 将机器人动作步长减少 28.3%，说明动态路由不仅提高成功率，也能选择更高效的下游策略。LIBERO 仿真实验（LIBERO-Plus spatial 子集）进一步验证了学习式策略路由在分布外任务变化下的有效性。

### 四、结论（Conclusion）
SWAP 表明，稳健的机器人执行不必只依赖更强的单体 VLA，而可以通过学习如何在多个已有 VLA 之间进行逐步路由来获得互补优势。该方法把策略路由作为离线 RL 问题，在部署时在线选择策略，不重训底层专家，能够提高真实操作成功率并缩短成功轨迹长度。这为构建可组合、可扩展的 VLA 策略库和测试时策略选择机制提供了可行方向。

### 五、方法论与关键技术细节
关键实现细节包括：候选策略被视为固定黑盒，只学习路由器，因此无需重训各 VLA 专家；离线数据需覆盖所有候选策略的成功与失败轨迹，奖励为稀疏二值信号；路由在底层 VLA 的 action chunk 级别进行，不打断 chunk，也不增加额外策略查询；IQL 使用双 Q 网络、min 双 Q 保守估计和 expectile 回归 value 函数；视觉语言骨干为冻结的 Qwen2.5-VL-3B，输出 2048 维嵌入，策略身份用可学习嵌入表示；真实 DROID 采用 7-DoF Franka 与多相机观测，推理时聚合多视角 Q 值；局限在于依赖离线数据对候选策略行为空间的覆盖，稀疏奖励导致长期信用分配困难，策略库固定时扩展新策略可能需要补充路由数据，且每个 chunk 需评估 K 个候选策略带来一定推理开销。
