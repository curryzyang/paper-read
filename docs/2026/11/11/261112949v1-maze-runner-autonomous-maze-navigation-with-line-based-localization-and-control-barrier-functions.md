# Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Alvaro J. Gaona, Lucas Gómez-Velayos, Peter Pasuy-Quevedo
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.12949v1) · [PDF](https://arxiv.org/pdf/2611.12949v1)

## TLDR
**TLDR:** Maze Runner is an open ROS 2 autonomy stack for simulated maze navigation that combines line-based EKF localization/SLAM, grid and Hybrid A* planning, and NMPC with control barrier functions for safety, achieving a 135 m autonomous route with 1.0 cm localization RMSE and real-time planning/control performance.

## Abstract
Maze navigation requires localization from sparse, repetitive geometry, planning through narrow corridors, and control that stays safe when the estimate or the map is wrong. We present Maze Runner, an open autonomy stack in C++ and ROS 2 that addresses these needs end to end on a simulated Husarion ROSbot XL with a 2D LiDAR in Gazebo. Perception extracts wall lines from each scan with RANSAC and total least squares, with per-line uncertainty. The same line front end feeds two estimators: an Extended Kalman Filter (EKF) that localizes against a line map built from the maze mesh, and an EKF SLAM variant that builds the line map online. Planning runs online on an inflated occupancy grid with A* plus line-of-sight shortcutting, or with a forward-only Hybrid A*. A nonlinear Model Predictive Controller (NMPC) tracks the plan while discrete-time Control Barrier Functions (CBFs) on world-frame LiDAR points keep the robot clear of walls and unmapped obstacles. The algorithms live in a ROS-free, unit-tested core library, and the whole stack builds and runs from a single reproducible environment. In simulation, the robot drives a 135 m route through the maze with 1.0 cm localization RMSE against the known map and 24 cm in SLAM mode, the planner returns a path in 6 ms, and the NMPC solves in 11.7 ms on average, never exceeding its 80 ms budget.


## 精读解读（中文）
### 一、研究动机
迷宫导航同时面临稀疏重复几何下的实时定位、狭窄走廊中的可行路径规划，以及估计或地图出错时仍保持安全的控制问题。本文旨在提供一个开源、可复现的端到端自主导航栈，在仿真平台上统一解决感知、定位与建图、规划和安全控制。

### 二、技术方案（Method）
系统在Gazebo中以搭载2D LiDAR的Husarion ROSbot XL为平台，采用C++和ROS 2实现，算法置于无ROS依赖且单元测试的核心库。感知端用RANSAC从每帧扫描提取墙面线并做总体最小二乘精化及逐线不确定性估计；同一线特征前端同时驱动两种估计器：基于迷宫网格生成线地图的EKF定位，以及在线构建线地图的EKF SLAM。规划在膨胀占据栅格上运行8邻接A*加视线捷径化，或采用仅前进的Hybrid A*；控制层用NMPC跟踪参考路径，并以作用在世界坐标系LiDAR点上的离散时间CBF约束保证避墙和避让未建图障碍，且通过扇区式障碍选择限制问题规模。

### 三、结果（Result）
仿真中机器人完成了135 m的迷宫路线；对已知地图定位RMSE为1.0 cm，SLAM模式下为24 cm；规划器约6 ms返回路径；NMPC平均求解11.7 ms，且从未超过80 ms预算。

### 四、结论（Conclusion）
结果表明，基于线特征的EKF定位/SLAM、在线栅格规划和带离散时间CBF约束的NMPC可以组成实时、端到端且可复现的迷宫自主导航栈，并在定位精度、规划速度和控制实时性上满足仿真实验要求。

### 五、方法论与关键技术细节
线地图用Hesse法向式表示，由迷宫网格中竖向且水平跨度足够的墙面提取并合并共线重复线，运行时按机器人预测位置调整线的可见朝向；EKF预测采用中点圆弧里程计模型，并在过程噪声中加入随运动增长的横向与航向滑移项以适配滑移平台。RANSAC参数为每轮30次采样、点对最小间距5 cm、内点阈值3 cm、最少10个内点，固定随机种子保证确定性；参考生成按0.5 m/s和0.1 s控制周期加密路径，并采用前向窗口路径跟踪防止跨墙跳点。规划栅格分辨率0.1 m、膨胀半径0.6 m，Hybrid A*用5条0.3 m前进弧、最小转弯半径1 m、72个航向分箱及障碍感知Dijkstra启发式；主要局限是仅在Gazebo仿真验证，依赖LiDAR线特征与已知或在线构建的几何地图，真实平台上的动态障碍、噪声和计算约束仍需进一步评估。
