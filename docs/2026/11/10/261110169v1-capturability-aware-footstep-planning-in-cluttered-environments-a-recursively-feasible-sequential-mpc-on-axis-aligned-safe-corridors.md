# Capturability-Aware Footstep Planning in Cluttered Environments: A Recursively Feasible Sequential MPC on Axis-Aligned Safe Corridors

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Athanasios Kyriakopoulos, Shubham S. Kumbhar, Kunal S. Narkhede, Abhijeet M. Kulkarni, Ioannis Poulakakis
- 机构：University of Delaware, National Technical University of Athens, Athena Research Center, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10169v1) · [PDF](https://arxiv.org/pdf/2611.10169v1)

## TLDR
This paper proposes a capturability-aware sequential MPC framework for LIP-based humanoid footstep planning that uses axis-aligned safe corridors to jointly ensure obstacle avoidance and locomotion stability with recursive feasibility, enabling autonomous in-place walking when forward motion is blocked and validating the approach on the humanoid robot Digit.

## Abstract
A fundamental aspect of humanoid footstep planning is to jointly guarantee obstacle avoidance and locomotion stability. This paper presents a capturability-aware sequential Model Predictive Control (MPC) framework for Linear Inverted Pendulum (LIP)-based humanoid footstep planning in the presence of obstacles. The proposed method combines obstacle avoidance with capturability constraints through safe corridors constructed as sequences of intersecting rectangles, yielding a sequential MPC framework with recursive feasibility guarantees for the LIP-based planning layer. The planner autonomously adapts to constrained scenarios, switching to in-place walking when obstructions---such as doors assumed to be open during planning but unexpectedly found to be closed during execution---block forward motion. Performance is largely independent of the prediction horizon, allowing high success rates while keeping the computational cost low. The approach is validated in high-fidelity simulations with the humanoid robot Digit, demonstrating a practical solution for capturable humanoid footstep planning in cluttered environments.


## 精读解读（中文）
### 一、研究动机
人形机器人在杂乱、以人为中心的环境中导航时，足步规划必须同时保证避障与运动稳定性，但现有基于降阶模型的方法往往只生成无碰撞路径而缺乏显式可捕获性保证，而强调步态稳定的方法又常忽略障碍约束。本文针对这一空白，研究在障碍环境中具有递归可行性的可捕获性感知足步规划。

### 二、技术方案（Method）
方法以线性倒立摆（LIP）为规划模型，将状态分解为发散运动分量（DCM）与收敛运动分量（CCM），并采用步到步动力学、足端可达集和N步捕获区域约束；将自由空间表示为轴对齐安全走廊（AASC），即一串相交矩形，并在每个矩形内构造内接的可行足步区域，使足步限制在该区域内时同时保证COM不越界和N步可捕获。随后沿走廊构建顺序MPC：每个局部MPC只优化当前矩形内的足步，并通过捕获区域/终端约束与矩形间切换策略保持递归可行性；当检测到前进受阻（例如规划时假定打开但执行时关闭的门）时，规划器自动减速并切换为原地踏步。

### 三、结果（Result）
在高保真MuJoCo仿真中以Digit人形机器人验证，并在随机生成的轴对齐矩形障碍环境中与Narkhede2022方法比较；结果表明该方法能在保持高成功率的同时显著降低对预测时域的依赖，计算成本较低。关键发现是显式可捕获性约束带来内在安全性和优雅降级：当前进路径被意外阻塞时，机器人会自主减速并原地踏步，而仅依赖纯几何安全走廊的方法难以提供这种保证。

### 四、结论（Conclusion）
本文提出了一种将避障与可捕获性统一到顺序MPC中的足步规划框架，通过轴对齐安全走廊及其内接可捕获足步区域，为基于LIP的人形机器人规划层提供递归可行性保证。该方法在杂乱环境中兼顾无碰撞导航与可捕获步态，并在受阻场景中表现出安全退化能力，为实际人形机器人足步规划提供了有前景的解决方案。

### 五、方法论与关键技术细节
关键实现包括：以LIP常高COM模型和DCM/CCM分解建立离散步态动力学，使用步长T、固有频率ωo=√(g/H)、足端可达边界以及递归计算的N步捕获区域；安全走廊由可分离的轴对齐矩形组成，便于高效碰撞检测和盒约束，每个矩形内再求内接足步区域，并依据DCM偏移位于捕获区域、CCM偏移有界来保证约束一致性；顺序MPC沿走廊局部求解，配合矩形切换条件和捕获区域终端约束保证递归可行性，因而计算复杂度较低且性能对预测时域不敏感。局限包括依赖轴对齐矩形障碍近似、采用降阶LIP模型、主要在MuJoCo仿真中验证，以及走廊构造与切换策略对复杂非矩形环境的适用性仍需进一步检验。
