# Learning Safe Humanoid Navigation from Reduced Order Models

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：William D. Compton, Zachary Olkin, Ryan Bena, Aaron D. Ames
- 机构：Amazon Safe Autonomy Frontiers (SAF) Lab, California Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19272v1) · [PDF](https://arxiv.org/pdf/2609.19272v1)

## TLDR
The paper proposes **RoM-Nav**, a two-stage reinforcement learning pipeline that first trains a LiDAR-based navigation policy on a reduced-order humanoid model and then kickstarts a full-order humanoid policy with a frozen locomotion controller, adding a Poisson safety filter for out-of-distribution obstacle safety, enabling mapless multi-floor navigation on a Unitree G1 over 10 m vertical displacement and 100 m path length.

## Abstract
Research in humanoid robotics has achieved rapid progress in locomotion, and recent results have pushed the boundary on autonomous navigation. We demonstrate that a standard single-stage RL navigation pipeline struggles to scale to multi-level and multi-story terrain, limited by the difficulty of complex humanoid terrain interactions such as stairs. To overcome this challenge, we decompose the navigation problem into two pieces. First, we train a policy operating on the reduced order dynamics but with full 3D LiDAR observations to navigate complex, multi-story terrain. We then utilize this navigation knowledge to kickstart a policy operating on the full-order humanoid dynamics, with a frozen locomotion policy in the loop. Additionally, we demonstrate that applying a Poisson safety filter to the navigation policy output recovers safety in the presence of out-of-distribution obstacles, without dropping navigation success rate. We demonstrate the resulting RoM-Nav policy on a Unitree G1, accomplishing mapless multi-floor navigation covering trials with over 10m of vertical displacement and over 100m of path length. Project page with videos https://wdc3iii.github.io/rom-nav/ .


## 精读解读（中文）
### 一、研究动机
人形机器人运动能力快速进展，但自主导航仍受限于复杂地形交互（如楼梯）难以扩展，标准单阶段强化学习导航管线无法应对多层、多楼层地形；同时学习型导航策略缺乏碰撞保证，训练几何过于简单时在部署中遇到分布外（OOD）障碍容易违反安全约束。现有学习型导航工作（无论是人形还是四足）训练环境基本只有一个可通行层级，目标的z高度不携带平面位置以外的信息，尚无无地图学习型人形导航被命令前往建筑另一楼层的目标。

### 二、技术方案（Method）
提出两阶段训练管线 RoM-Nav。第一阶段在降阶模型（带朝向的单积分器）上训练导航策略：观测为完整 3D LiDAR 距离图（1°角像素，含距离与 LiDAR 坐标系下的 x,y,z 及有效通道）、目标观测 o_g=[d_x,d_y,log||d||/log d_max,d_z,sinγ,cosγ] 与上一动作 a_{t-1}；环境为由 3D 场景栅格化的 0.2 m 占据栅格，按楼层维护并在高度阈值处切换楼层，发生碰撞时将穿透分量投影出去沿边界滑动；从程序化生成的户外、单房间、多层建筑 tile 中采样，并以 0.3 概率在楼梯/坡道口依据步态库的随机时刻放置初始状态，否则在保证自由空间中均匀采样。第二阶段采用 kickstarting 将 RoM 导航知识迁移到全阶人形动力学策略：视觉端先用 VAE 预训练并冻结的 CNN 编码器处理 LiDAR 距离图与深度图（重建深度/XYZ 用 MSE，mask 与地面/障碍/楼梯/坡道分割用 BCE，输入加噪声与 0–80% 像素 dropout，用 1M 均匀加 1M 楼梯坡道过采样图像训练 10 个 epoch），LiDAR 特征经自注意力与 4 个学习 query 加 1 个非视觉 query 的交叉注意力，深度特征展平，二者与非视觉观测拼接后输入两层 GRU，隐状态再次拼接后经 MLP 输出 Beta 分布的 velocity 命令；训练目标为 L=L_PPO+λL_KL(π,π^R)，λ 在前 100 次迭代为 1，到 1100 次迭代衰减至 0.05 并保持，运动策略以 LIP-CLF RL 训练后冻结在环（50 Hz，前向 1 m/s、侧向 0.25 m/s、角速度 1 rad/s），导航策略 5 Hz；两阶段各 2000 次迭代、4096 个并行环境、单张 H100，分别约 12 小时与 32 小时，合计不到 45 小时。部署时在导航策略输出上叠加 Poisson 安全滤波器。

### 三、结果（Result）
单阶段 RL 导航管线在多层与多楼层地形上难以扩展，与两阶段方法的性能差距几乎完全出现在需要显著 z 高度条件的场景，例如多楼层建筑中的跨楼层目标；而两阶段得到的 RoM-Nav 策略在 Unitree G1 上实现了无地图多楼层导航，试验覆盖超过 10 m 垂直位移与超过 100 m 路径长度，并包含户外 100 m 部署。Poisson 安全滤波器在遇到分布外障碍几何时能低成本地恢复安全性，且不降低导航成功率。此外，LiDAR 编码器预训练与专门的 spawn/goal 采样被验证为解锁多楼层导航能力的关键。

### 四、结论（Conclusion）
将导航问题分解为降阶模型上的廉价预训练与全阶人形动力学上的知识迁移（kickstarting），并在环中冻结运动策略，是让人形无地图导航扩展到楼梯、多楼层等复杂地形的有效途径；再配合 Poisson 安全滤波器在线弥合环境 sim-to-real 差距，可保证面对 OOD 障碍时的安全性而不牺牲任务成功率，从而使学习型人形策略在真实多层建筑中完成长时程导航。

### 五、方法论与关键技术细节
关键实现点包括：奖励由目标跟踪（位置、朝向、高度、站立，权重各 0.2，除高度外均在 2 m 测地距离内门控触发）、进度塑形（测地线与高度的输入受限 CLF 奖励，各 0.1，且仅在达到 episode 最优时触发以避免绕圈刷分）与惩罚（碰撞 -1，动作速率系数从 -0.01 在第 1000 迭代变为 -0.1）构成，其中高度跟踪与高度进度奖励是跨楼层成功的关键；采用专门的 reset 分布（0.3 概率楼梯/坡道口步态库随机时刻）解决 z 高度依赖难以学习的问题；多层 tile 定义为同一 x,y 存在多个互不相交的可达 z 目标，占据栅格按楼层维护并在过渡区域保持局部一致；LiDAR FoV 设为前向 220°。局限性在于：RoM 训练依赖地形生成时记录的地面真值可通行性与占据栅格，运动策略在全阶训练中冻结，安全滤波基于原始占据表示且需要在线计算，策略在训练分布外的障碍几何上仍会退化，需靠滤波器兜底。
