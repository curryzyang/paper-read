# Steeringless Drifting: Differential-Torque Control of a Four-Wheel Independently Driven Vehicle

- 区域：精读区
- 排名：8
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Sheng Zhao, Zexin Wu, Dongyang Zhou, Bolin Zhao, Xiaodong Wu
- 机构：Nanyang Technological University, Shanghai Jiao Tong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24863v1) · [PDF](https://arxiv.org/pdf/2607.24863v1)

## TLDR
This paper proposes and validates a differential-torque drift control method for a steering-free four-wheel independently driven vehicle, demonstrating that steady circular and figure-eight drifting with large sideslip angles can be achieved using only wheel torques without mechanical steering.

## Abstract
Control methods for emerging vehicle chassis architectures are important for autonomous driving near handling limits. Unlike conventional drift control, which relies on mechanical steering and rear-tire saturation, a steering-free four-wheel independently driven (4WID) vehicle can generate direct yaw moment through differential wheel torques. This paper proposes a differential-torque drift control method for such a vehicle. A double-track vehicle model incorporating four-wheel differential actuation is established, based on which a drift-equilibrium calculation method and a closed-loop drift controller are developed. The proposed approach is validated through simulations and experiments on a 1:10-scale vehicle. The results show that the vehicle can achieve steady circular drifting with a sideslip angle of approximately 20$^\circ$ and perform figure-eight drift tracking. This study demonstrates the feasibility of drift control using only differential wheel torques and provides a new perspective on near-limit control for steering-free vehicle architectures.


## 精读解读（中文）
### 一、研究动机
传统漂移控制依赖机械转向和后轮轮胎饱和，而对于无转向的四轮独立驱动(4WID)车辆，能否仅通过差动扭矩产生直接横摆力矩并实现漂移，是一个尚未解决的问题。本文旨在提出首个针对无转向4WID车辆的漂移控制框架，验证仅通过轮端扭矩实现稳定漂移的可行性。

### 二、技术方案（Method）
建立无转向四轮独立驱动车辆的双轨动力学模型，包含三自由度刚体动力学(纵向、横向、横摆)、轮胎摩擦圆约束(考虑纵向与横向力耦合)以及电机一阶动态模型(带幅值与速率限制)。离线阶段，基于目标纵向速度、侧偏角和横摆率参数化期望平衡状态，通过多起点序列二次规划求解约束优化问题(平衡残差为零，目标为最小化扭矩二范数和轮胎利用率六次方加权和)得到平衡扭矩向量。在线阶段，设计脉冲-保持控制器：利用纵向速度和横摆率反馈生成标量扭矩修正，叠加至平衡扭矩后经约束处理分配至四个车轮；脉冲信号用于漂移起始或状态切换，侧偏角不参与在线反馈。在1:10比例RC车辆平台进行仿真与实验验证。

### 三、结果（Result）
仿真与实验结果表明，车辆能够在无转向输入下实现侧偏角约20度的稳定圆形漂移，并能执行八字形轨迹漂移跟踪，且漂移过程中仅通过四个车轮的差动扭矩进行控制。该结果验证了所提方法的有效性，证明了纯差动扭矩漂移控制的可行性。

### 四、结论（Conclusion）
本研究证明了无转向四轮独立驱动车辆仅依靠差动扭矩即可实现稳定漂移控制，为无转向底盘架构的极限操控提供了新的控制思路。

### 五、方法论与关键技术细节
关键细节：(1)轮胎模型采用摩擦圆约束，利用atan2计算零转向角下的侧偏角，并使用饱和度函数限制纵向力与横向力，其耦合效应通过摩擦圆平方根关系体现。(2)平衡点优化中，目标函数包含扭矩归一化二范数(权重0.25)和轮胎利用率六次方(权重0.50，指数6)，通过多起点初始化避免局部最优，并确保左右对称车辆交换扭矩方向后仍需重新验证平衡残差。(3)控制器为脉冲-保持结构：脉冲信号仅用于漂移触发，在线反馈仅使用纵向速度和横摆率误差，侧偏角不纳入闭环。(4)电机模型考虑一阶滞后和幅值/速率约束(Tm固定，τ_max和τ_dot_max设置)。(5)仿真与实验在1:10比例车辆上进行，未考虑悬架运动、载荷转移和滚动阻力，且轮胎力模型为静态简化，可能影响高精度应用。
