# Navigating the Proximity-Safety Balance: Constraint Decomposition for Human Following in Pedestrian Crowds

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Shiting Gong, Jianpeng Yao, Jinfeng Wang, Marco Pavone, Jiachen Li
- 机构：University of Pennsylvania, Stanford University, University of California, Riverside, NVIDIA Research, Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10056v1) · [PDF](https://arxiv.org/pdf/2608.10056v1)

## TLDR
The paper proposes a multi-constraint reinforcement learning framework that decomposes human-following into a sparse reward and independent, behaviorally interpretable safety cost constraints with uncertainty-aware costs, enabling an explicit and tunable proximity-safety trade-off in dense pedestrian crowds.

## Abstract
Following a target human in crowded environments involves an inherent conflict between staying close to the target and navigating safely among surrounding pedestrians and obstacles. This conflict becomes more severe in dense scenarios, where aggressive following risks collisions and conservative margins lead to target loss, especially when pedestrian behaviors are unfamiliar or unpredictable. Existing reinforcement learning (RL) methods typically encode these competing objectives into a single dense reward, but the resulting proximity-safety balance is implicit and difficult to adjust across conditions. To address this, we decompose the human-following task into a sparse task reward and independent cost constraints within a multi-constraint RL formulation, where each constraint is managed through cost thresholds with direct behavioral meaning rather than implicit reward weight ratios, allowing explicit and tunable control over the trade-off. We further quantify the prediction uncertainty of human motions and integrate these estimates into the RL costs to enhance safety under unpredictable conditions. Extensive experiments across both in-distribution and out-of-distribution settings demonstrate that our method achieves an effective proximity-safety balance compared to baselines. Real-robot deployment further validates the feasibility of our method in real-world scenarios. More details are available on our project page: https://nav-ps-balance.github.io/.


## 精读解读（中文）
### 一、研究动机
在拥挤环境中跟随目标行人需要同时满足‘靠近目标’与‘安全避障’两个内在冲突的目标，密集场景下激进跟随易导致碰撞，保守间距又易丢失目标。现有强化学习方法通常将竞争目标编码为单一稠密奖励，其折中关系隐含在权重比中，难以跨场景调节，且面对不可预测行人行为时泛化不足。因此需要一种能显式、可调地控制接近-安全平衡的决策框架。

### 二、技术方案（Method）
将人类跟随任务建模为带约束的马尔可夫决策过程（CMDP），采用稀疏任务奖励和三个独立成本约束：跟随成本（等式约束）、行人碰撞成本（不等式约束）、静态障碍碰撞成本（不等式约束），并通过PPO-Lagrangian联合优化。输入状态包括机器人自身状态、附近行人的当前位置与预测轨迹、由自适应共形推断（ACI）估计的各预测时域不确定性，以及最近5帧的局部占据栅格图。策略网络采用早融合Transformer架构：3D CNN提取占据栅格特征，机器人、目标、障碍物与行人各自生成token，经正弦位置编码与未检测行人掩码后输入Transformer编码器，取机器人token经MLP得到特征，输出二维速度动作(vx, vy)。训练中四个critic分别估计奖励与三个成本的GAE优势，通过动态拉格朗日乘子满足约束；推理时仅需一次前向传播即可生成动作。

### 三、结果（Result）
在分布内与分布外（OOD）场景下，包括不同人群密度、行人行为和环境布局，该方法相比优化式基线和消融变体取得了更高的任务成功率与更低的碰撞率。真实机器人ROS 2部署进一步验证了算法在真实世界中的可行性与有效性，表明约束分解和不确定性感知能实现有效的接近-安全折中。

### 四、结论（Conclusion）
将目标跟随分解为稀疏任务奖励与具有行为语义阈值的独立成本约束，能够替代隐式奖励权重比，显式且可调地控制接近-安全平衡；将行人运动预测不确定性量化并融入成本设计，可增强不可预测条件下的安全性。仿真与真实机器人实验均证明了该框架的有效性和可部署性。

### 五、方法论与关键技术细节
关键细节包括：ACI使用M个并行估计器在线维护每个行人每个预测时域的误差界，更新公式为δ(t+1)=δ(t)+γ*(1[δ(t)>δ(t)]-α)，最终通过自适应加权采样选择输出；人类安全成本在行人的当前位置周围使用半径r_ego+r_h+r_buf的固定安全区，在前K'个预测位置周围使用半径r_ego+r_h+δ_hat(t)的不确定感知安全区，成本与最大侵入深度成正比；跟随成本仅在距离超过个人空间阈值d_personal时惩罚，障碍成本则基于最小表面距离与安全阈值d_safe_o的偏差；奖励只在成功、碰撞、目标丢失三种终端事件时给出稀疏信号。训练采用PPO-Lagrangian，每类成本有独立critic和GAE，拉格朗日乘子动态调整，其中跟随约束为等式约束以维持期望距离而非最小化距离，安全约束为不等式。人体token按距机器人距离排序，掩码处理未检测行人；局限性包括依赖上游预测器质量，且对极端OOD行人行为仍可能不够鲁棒。
