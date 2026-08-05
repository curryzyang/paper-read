# Biconvex Optimization for Smooth Minimum-Time Trajectories around Convex Obstacles

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Peter Werner, Tobia Marcucci, Daniela Rus
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02834v1) · [PDF](https://arxiv.org/pdf/2608.02834v1)

## TLDR
A biconvex optimization approach for minimum-time motion planning around convex obstacles that guarantees convergence, supports arbitrary-order derivative constraints, and robustly produces high-quality trajectories via alternating between separating-plane computation and trajectory optimization.

## Abstract
We present a biconvex approach for minimum-time motion planning around convex obstacles that is guaranteed to converge, is anytime, and supports derivative constraints to arbitrary order. We jointly convexify the minimum-time objective and all derivative constraints through a change of variables, and handle collision avoidance via time-varying separating planes, reducing the problem to a biconvex program. This program is solved by alternating between computing maximum-margin separating planes and optimizing the trajectory. By only adding planes for obstacles that the current iterate collides with, the trajectory can jump around obstacles and escape local minima. The method is guaranteed to converge starting from a simple collision-free polygonal curve. In our experiments on drone navigation and dual-arm bin unloading, we find that the proposed method reliably produces high-quality trajectories with computation times comparable to state-of-the-art decomposition-based motion planners, while handling a larger class of problems and being substantially more robust to bad initialization. Project page:https://wernerpe.github.io/bmtp-website/


## 精读解读（中文）
### 一、研究动机
现有运动规划方法中，采样规划器产生锯齿状路径且难以原生编码平滑度与导数约束，而局部轨迹优化方法受非凸碰撞约束影响容易陷入局部极小、运行时间不稳定且依赖精心初始化。基于分解的运动规划器虽然可靠，但需预先计算自由空间的凸分解，且难以在凸框架下同时支持任意阶导数约束和连续性约束。本文旨在提出一种无需预先凸分解、保证收敛、支持任意阶导数约束且对初始化鲁棒的最小时间轨迹规划方法。

### 二、技术方案（Method）
提出一种双凸最小时间规划器（BMTP）。输入为起点、终点、凸障碍集合及导数约束集。轨迹用贝塞尔曲线表示，通过变量替换将最小时间目标与所有导数约束共同凸化，支持任意阶导数约束和任意有限阶连续性约束。碰撞避免通过时变分离半空间实现，将问题转化为双凸规划。求解时交替执行两个步骤：固定当前轨迹，为当前发生碰撞的障碍计算最大间隔分离平面；固定分离平面，优化轨迹。仅对当前迭代碰撞的障碍添加平面，使轨迹能够绕过障碍并逃离局部极小。算法从简单的无碰撞多边形曲线初始化，可随时输出当前最优解并保证收敛。

### 三、结果（Result）
在无人机导航与双臂卸货箱实验中，所提方法稳定生成高质量轨迹，计算时间与最先进的基于分解的运动规划器相当，同时处理更大的问题类别，并对不良初始化显著更鲁棒。方法从简单无碰撞折线即可保证收敛，具备任意时间特性。

### 四、结论（Conclusion）
提出了一种保证收敛、任意时间、支持任意阶导数约束的双凸最小时间轨迹规划方法，无需昂贵的自由空间凸分解。该规划器在保持可靠性和可预测运行时的同时提高了轨迹质量，适用于无人机导航和双臂操作等场景，可作为现有启发式或策略后处理的替代方案。

### 五、方法论与关键技术细节
关键细节包括：使用贝塞尔曲线离散化轨迹以实现有限维数值求解；通过变量替换联合凸化最小时间目标与全部导数约束；碰撞避免采用时变分离平面，每个平面在每时刻将对应轨迹点与障碍分离；仅添加当前碰撞障碍的分离平面以帮助跳出局部极小；初始化只需简单多边形曲线，可由手工设计或采样规划器生成；方法保证从无碰撞初始曲线收敛。局限性包括障碍物需为凸集或可分解为凸集，以及未预先给出完整凸分解，依赖迭代生成分离平面。
