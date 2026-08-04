# Motion Planning for Mobile Manipulators Navigating Doorways via Model Predictive Control

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Kasra Sinaei, Kasun Weerakoon, Christopher Bradley, Seyed Abolfazl Fakoorian, Donald Ebeigbe
- 机构：AlphaZ Inc., The Pennsylvania State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00206v1) · [PDF](https://arxiv.org/pdf/2608.00206v1)

## TLDR
A motion planning framework using nonlinear model predictive control with coupled robot-door dynamics and a penalty-based reachability constraint enables mobile manipulators to autonomously open and traverse push and pull doors.

## Abstract
Navigating doorways is a fundamental capability for mobile manipulators operating in human environments, requiring coordinated motion between the mobile base and manipulator arm. This paper presents a motion planning framework that generates dynamically feasible and collision-free trajectories for autonomously opening and traversing both push and pull doors. The proposed method formulates the robot and door as a coupled dynamical system within a nonlinear Model Predictive Control (MPC) optimization framework. Manipulation feasibility is enforced through a penalty-based constraint, avoiding explicit arm kinematic modeling in the planner. Simulations and a hardware experiment demonstrate that the approach successfully plans feasible trajectories for door traversal.


## 精读解读（中文）
### 一、研究动机
移动操作机器人在人类环境中自主开门并穿越门洞需要移动基座与机械臂的协调运动，现有搜索式和行为树方法将任务离散化，难以联合优化；而全身规划又维度过高。本文提出一种基于非线性模型预测控制的连续运动规划框架，在低维状态空间中联合优化基座运动与门开启过程。

### 二、技术方案（Method）
将机器人和门建模为耦合动态系统，状态为[x,y,theta_base,theta_door]，输入为[v,omega_base,omega_door]，门采用单积分器模型。用操作可行性惩罚项替代整数切换变量，通过基座与门把手距离判断是否在臂可达范围内，并将惩罚与门角速度相乘。同时用几何约束确保基座与门板最近点距离大于基座半径加安全余量。MPC目标包含控制努力、操作惩罚和终端状态代价，求解N步离散优化问题；执行时用差分逆运动学求解器（PINK）生成关节速度并支持控制障碍函数。

### 三、结果（Result）
在NVIDIA Isaac Sim高保真仿真和硬件实验中，所提方法成功规划出穿越推门和拉门的可行无碰撞轨迹，验证了框架的实用性。与搜索式方法相比，该方法在同一连续非线性规划中联合优化基座运动和开门过程。

### 四、结论（Conclusion）
该框架通过软约束避免显式臂运动学建模，保持规划状态维数低，能统一处理推门和拉门，同时施加几何离隙约束，展示了在真实机器人上应用的潜力。

### 五、方法论与关键技术细节
关键细节包括：门被建模为绕固定铰链旋转的刚体，环境为已知尺寸走廊；基座采用unicycle动力学且建模为圆形，门板为线段；操作惩罚使用r_min和r_max定义可达范围，惩罚系数高增益；碰撞约束包含安全距离d_s；MPC有控制输入和状态边界。执行层采用PINK求解器，利用控制障碍函数约束关节速度，但规划器本身不考虑完整臂运动学，且需要依赖外部定位与门检测。
