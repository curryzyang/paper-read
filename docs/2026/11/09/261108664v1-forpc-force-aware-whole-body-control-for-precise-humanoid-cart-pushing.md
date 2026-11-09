# ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：ZhenYu Zou, Xing Liu, ShiChuang Wang, YunLong Dong, LiNan Deng, Feng Hua, Jun Wan, Cheng Cheng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08664v1) · [PDF](https://arxiv.org/pdf/2611.08664v1)

## TLDR
ForPC is a force-aware whole-body control framework that uses two-stage reinforcement learning with onboard force/state latent estimation to enable humanoid robots to push carts precisely and stably—without external force sensors, human demonstrations, or payload-specific tuning—and transfers from simulation to a physical Unitree G1.

## Abstract
Humanoid robots are expected to take over strenuous material handling in manufacturing, logistics, and healthcare, where operating existing wheeled carts would let them move heavy loads without modifying the workplace. However, humanoid cart pushing remains challenging because the bimanual grasp closes a force-coupled loop in which the contact wrenches that drive the cart also disturb the robot's balance, and payload changes alter the coupled dynamics. We propose ForPC, a force-aware whole-body control framework that regulates cart velocity through two-stage reinforcement learning. A locomotion prior is first trained under varied hand loads and upper-body postures to provide balance support. A force latent and a state latent are then inferred from onboard observations, without external force sensors, and fed to a residual policy that coordinates bounded arm, waist, and leg adjustments with base-velocity commands. Multi-objective rewards penalize bimanual internal opposition, grasp slip, and actuator saturation, encouraging the policy to apply contact force on demand without human demonstrations. Sim-to-sim experiments show that ForPC reduces cart-velocity RMSE by up to 68.2% relative to a locomotion-only baseline (Loco-only) and cross-track RMSE by up to 74.2% on the multi-bend route. Trained solely in simulation, the policy also transfers to a physical Unitree G1 without real-world training or fine-tuning and, with no payload-specific adjustment, pushes a cart carrying up to 30 kg at 0.5 m/s. These results suggest that humanoid robots could eventually replace humans for efficient material handling in daily life.


## 精读解读（中文）
### 一、研究动机
人形机器人直接操作现有轮式推车可在不改造工作场所的前提下承担重物搬运，但双手抓握会形成力耦合闭环：驱动推车的接触力同时扰动机器人平衡，载荷变化又改变耦合动力学。现有方法多只估计接触力或只预测物体运动，缺少同时围绕推车速度和双手接触力闭合反馈的控制框架，因而难以在变载荷下实现精确、稳定的推车。

### 二、技术方案（Method）
ForPC采用两阶段强化学习实现力感知全身控制：第一阶段在不同手部载荷和上肢姿态偏移下预训练抗交互扰动的运动先验，并冻结以提供平衡支撑；第二阶段用教师—学生估计器从关节运动学历史、上肢关节力矩和视觉观测的相对推车朝向中推断力潜变量与状态潜变量，无需外部力传感器，再输入残差策略输出有界的臂、腰、腿关节残差并调制基座速度命令。训练中使用多目标奖励惩罚双臂内耗对顶、抓握滑移和执行器饱和，使策略在无人类演示条件下按需施加接触力。

### 三、结果（Result）
仿真到仿真实验中，ForPC相对仅运动控制基线Loco-only将推车速度RMSE最多降低68.2%，在多弯道路线上将横向跟踪RMSE最多降低74.2%。仅用仿真训练的策略零样本迁移到实体Unitree G1，无需真实世界训练或微调，且不做载荷专用调整即可以0.5 m/s推动载重达30 kg的推车。

### 四、结论（Conclusion）
结果表明，将人形机器人与推车视为紧耦合动力学系统，并通过机载观测估计交互力与状态、以残差全身控制协调双臂和下肢，可显著提升变载荷推车的速度与路径跟踪精度。该框架展示了人形机器人零样本执行实际物料搬运任务的潜力，为替代人类完成高强度推运提供可行路径。

### 五、方法论与关键技术细节
方法关键在于冻结的抗扰动运动先验、基于历史观测的力/状态潜变量估计、有界残差动作空间以及针对双臂内耗、抓握滑移和执行器饱和的多目标奖励；控制不依赖腕部力/力矩传感器或人类演示，依赖仿真训练和教师—学生蒸馏。已验证单平台Unitree G1与最高30 kg、0.5 m/s工况，超参数、估计器网络结构和更广载荷/地形下的鲁棒性及长期实机稳定性仍需进一步核验。
