# Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Nolan Fey, Khai Nguyen, Yash Prabhu, Gabriel B. Margolis, Pulkit Agrawal
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18991v1) · [PDF](https://arxiv.org/pdf/2610.18991v1)

## TLDR
Contact-UAN is an unsupervised actuator-network residual world model that uses proprioception-based contact-consistent replay initialization to correct actuator sim-to-real discrepancies in simulation, enabling humanoid policies trained on 6.5 minutes of real walking data to transfer force-sensitive behaviors with 20% lower running torque and 43% lower force-tracking error.

## Abstract
Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness to impacts. This failure can arise from actuator sim-to-real gaps because forces depend on actuator torques. We introduce Contact-UAN, a residual world model that preserves a simulator's physics priors while correcting actuator dynamics to align simulated rollouts with recorded hardware rollouts. For humanoid motion with contact, this requires contact-consistent replay: if hardware playback in simulation begins with misaligned contact wrenches, the residual model learns to correct reset artifacts rather than actuator discrepancies. Using only onboard proprioception, Contact-UAN infers the simulator-side stance-foot pose needed to initialize replay with consistent contact forces. We show that a UAN trained on 6.5 minutes of real-world walking data generalizes to tasks that benefit from accurate force and impulse regulation and produces policies that transfer seamlessly to the real world, yielding 20% lower running torque, 43% lower force-tracking error, extreme compliance, accurate impedance control, and dynamic, robust jumps.


## 精读解读（中文）
### 一、研究动机
仿真训练的人形策略虽能定性迁移到硬件，但往往无法迁移力交互，导致扭矩效率低、负载调节差和冲击鲁棒性不足。其根源是执行器动力学存在 sim-to-real 差距，因为地面力、外力和冲量都通过关节扭矩介导。已有域随机化或系统辨识难以同时保留模拟器物理先验并精确校正执行器，且许多平台没有可靠扭矩传感标签。

### 二、技术方案（Method）
Contact-UAN 分三阶段：先用本体感觉短历史估计接触概率、支撑脚位姿和基座线速度，仅对置信支撑样本回归模拟器侧穿透高度与倾角，并通过正运动学与接触概率融合得到接触一致的回放初始状态。随后把 UAN 作为残差世界模型只作用于执行器命令通道，输入各关节目标位置误差和关节速度短历史，按执行器类型共享两层 MLP 和 ELU，在 PPO 重放环境中用关节位置 MSE、关节速度 MSE 与残差速率惩罚训练，使模拟 rollout 匹配硬件轨迹而保留模拟器刚体动力学、接触求解和积分。最后冻结 UAN，将校正后的目标注入下游任务训练，策略输出关节位置目标，部署时只运行任务策略而 UAN 不参与。数据上先训练 WTW 行走策略并变步态频率和摆动高度采集真实硬件本体感觉数据，重标注后用于 UAN 训练。

### 三、结果（Result）
在 29 自由度 Unitree G1 上，Contact-UAN 使开环重放的全关节 commanded torque 聚合失配降低 69.2%，且在相同命令和初始化下把 ground-truth 初始化后的关节位置 RMSE 从 0.0720 降到 0.0184 rad，说明收益来自执行器建模改进而非重置伪影补偿。硬件 running 策略保持速度跟踪的同时降低扭矩使用 20%，力控制策略将测力计力跟踪误差降低 43%，并实现零力指令下的柔顺和仅本体感觉的阻抗位置控制。跳跃任务中参考跟踪策略均可迁移，但任务奖励微调提高跳高后无 UAN 策略落地失败，有 UAN 策略可稳定落地并抗推。仅用 6.5 分钟真实行走数据训练的 UAN 可泛化到跑步、力和跳跃任务，接触一致初始化把 sim-to-sim 下游 20 秒存活率从 49.8% 提升到 96.7%，接近 oracle 重置。

### 四、结论（Conclusion）
Contact-UAN 表明，保留模拟器物理先验并只学习执行器通道残差，配合接触一致的回放初始化，可以显著缩小人形机器人力与冲量层面的 sim-to-real 差距。该方法仅依赖 onboard proprioception 和短时真实行走数据，无需扭矩传感或额外机器人系统辨识，且训练后的 UAN 可冻结复用到多个下游任务。因此，对于运行、力调节、阻抗控制和动态跳跃等执行器敏感行为，执行器残差世界模型是一种有效且可迁移的仿真增强方案。

### 五、方法论与关键技术细节
实现上使用 29-DoF Unitree G1 和 BeyondMimic G1 名义模拟器参数，不额外执行机器人特定 SysID；接触位姿估计器在仿真训练并假设平地形，采用 root 与 yaw 不变帧，且刻意从观测中移除绝对基座高度以避免估计器复制高度而非学习负载相关线索。UAN 训练用 4096 个并行环境、24 步重放时域和同长度 PPO rollout，残差网络按相同执行器硬件共享参数；下游训练移除机器人特定域随机化，但仍随机化地形网格、地面摩擦和外力推力。主要超参与约束包括 6.5 分钟真实行走数据、5 分钟 WTW 与 5 分钟 running 的 sim-to-sim 数据设置、位置残差可避免扭矩监督并保留部署位置控制接口。局限是当前模型不捕捉耦合执行器效应和电机温度依赖效应，后者因温度慢变需要热建模或额外传感器。
