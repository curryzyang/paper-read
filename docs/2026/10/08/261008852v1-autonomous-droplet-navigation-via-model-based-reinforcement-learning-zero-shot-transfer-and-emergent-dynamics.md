# Autonomous Droplet Navigation via Model-Based Reinforcement Learning: Zero-Shot Transfer and Emergent Dynamics

- 区域：精读区
- 排名：6
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Rajneesh Anand, Mayuresh V. Kothare
- 机构：Lehigh University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08852v1) · [PDF](https://arxiv.org/pdf/2610.08852v1)

## TLDR
This paper presents the first robotic platform for closed-loop autonomous navigation of deformable droplets on an open surface using model-based reinforcement learning, trained offline from only 50–150 physical episodes without simulation or analytical models, achieving zero-shot transfer to unseen geometries, autonomously discovering an oscillatory depinning strategy, and completing training in under 90 minutes.

## Abstract
Self-driving laboratories (SDLs) are transforming chemical and materials discovery through closed-loop automation, yet automated infrastructure for physical manipulation of soft, deformable matter remains beyond current robotic platforms. A critical instance is autonomous droplet transport on an open surface, where contact-angle hysteresis, capillary pinning, and surface heterogeneity produce partially observable dynamics that pose significant challenges for classical model-based controllers. We introduce the first robotic platform for closed-loop autonomous liquid droplet navigation on an open, unconfined surface using model-based reinforcement learning. A two-axis tilting board coated with a thin silicone oil film drives the droplet, while an overhead camera provides real-time feedback. A learned policy was trained on just 50 to 150 physical episodes depending on geometric complexity, without simulation or analytical models. Beyond performance alone, the platform demonstrates three capabilities of interest to the SDL community: it robustly transfers zero-shot to unseen geometries; it autonomously discovers an oscillatory depinning strategy to free the droplet when it sticks; and it completes its full training pipeline in under 90 minutes. These results extend reinforcement-learning manipulation from rigid microrobots to deformable soft-matter systems for next-generation SDLs.


## 精读解读（中文）
### 一、研究动机
自驱动实验室正在通过闭环自动化改变化学与材料发现，但软、可变形物质的物理操作自动化仍超出当前机器人平台能力。开放表面上的液滴运输是关键实例，其受接触角滞后、毛细钉扎和表面异质性影响，产生部分可观测动力学，使经典基于模型的控制器面临显著挑战。现有液滴运输平台多依赖预编程驱动序列或手动控制，因此需要实现开放无约束表面上的自主液滴导航。

### 二、技术方案（Method）
平台为 DropletRunner：将 BRIO Labyrinth 板改造成带定制 3D 打印 PLA 通道的板面，并涂覆薄硅油膜，用两个 Dynamixel 电机提供两轴重力倾斜驱动，顶置 See3CAM_24CUG 相机以 1920×1200、60 fps 提供 RGB 视觉反馈，红色染色水滴作为被控对象。控制单元采用双计算机架构，CPU 笔记本运行 ROS2 控制环和 U2D2 电机通信，GPU 平台用于离线训练，episode 在两者间传输，训练好的策略回传评估以避免训练延迟干扰实时控制。算法采用 DreamerV3 潜在世界模型进行基于模型的强化学习，完全离线在实验数据上训练，不使用模拟器或解析模型，在 50 到 150 个物理 episode 上学习策略，并以 20 Hz 闭环执行感知-动作控制。

### 三、结果（Result）
材料显示 MBRL 策略在复杂度递增的几何中达到 100% 成功率（数字在预览中截断），并与 PID 基线在五种几何的成功率图中进行对比；从 I 形训练出的策略零样本迁移到未见几何达到 95% 成功率（数字在预览中截断）。智能体还在几何收缩处自主发现交替极性的振荡脱钉策略，当液滴粘住时会升级幅度，该行为未经奖励塑形或编程，与振动诱导脱钉一致。整个训练流水线在 90 分钟内完成，且仅需 50 到 150 个物理 episode。

### 四、结论（Conclusion）
该工作提出首个用于开放、无约束表面上闭环自主液滴导航的机器人平台，用基于模型的强化学习控制可变形液体代理，将强化学习操作从刚体微机器人扩展到软物质系统。它证明无需仿真或解析模型即可在真实实验数据上离线训练世界模型策略，并具备零样本迁移和涌现物理策略，未来计划开源硬件与软件，作为低成本、低硬件复杂度的重力驱动油拖曳液滴导航真实世界基准。

### 五、方法论与关键技术细节
关键实现包括 BRIO Labyrinth 改造、3D 打印 PLA 通道、薄硅油膜（厚度不可观测）、两轴 Dynamixel 倾斜驱动、顶置 1920×1200 60 fps 相机、ROS2 控制环 20 Hz、U2D2 通信；训练在 CPU 控制与 GPU 离线训练解耦的双机架构上完成，episode 传输后策略回传。方法使用 DreamerV3 潜在世界模型，完全离线于 50 到 150 个物理 episode，无仿真或解析模型，材料未列出具体损失函数、网络结构与超参数。局限性包括接触角滞后、毛细钉扎、表面异质性和油膜厚度不可观测导致的部分可观测动力学，经典 MPC 难以建模；物理训练数据量小，且预览中成功率数值被截断，具体结果需查原文确认。评估几何包括直线 I 形、L 内/外、Arc 内/外，贡献部分另提及 Staircase 新几何。
