# $\mathcal{C}^\infty$ Smooth Trajectory Planning with Application to Soft Robots

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Reinhard M. Grassmann, Abdulaziz Y. Alkayas, Lingyun Chen, Sami Haddadin
- 机构：Mohamed bin Zayed University of Artificial Intelligence
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05615v1) · [PDF](https://arxiv.org/pdf/2611.05615v1)

## TLDR
The paper introduces a \(\mathcal{C}^\infty\)-smooth trajectory generator based on an infinitely differentiable path primitive that respects kinematic limits, enabling vibration-avoiding motion for soft continuum robots and other flexible systems, with validation in simulation and on hardware.

## Abstract
High motion performance and avoiding structural vibrations rely on smooth trajectory planning. The smoothness requirement depends on the robot's complexity in terms of the number of degrees of freedom and system order due to the flexibility of the joints and links. For industrial robots, the smoothness requirements have been determined and subsequently taken into account. Although unknown for soft continuum robots, the exact smoothness requirement can potentially be much larger than previously considered ones such as $\mathbf{\mathcal{C}^4}$ for collaborative robots and $\mathbf{\mathcal{C}^5}$ for quadcopter drones. To address this gap, we introduce a $\mathbf{\mathcal{C}^\infty}$-smooth trajectory generator that respects defined kinematic limits and generates infinitely differentiable trajectories. The generated path addresses and generalizes to all smoothness requirements, where a transition between sequential states is needed. Therefore, all trajectories have continuous velocity, acceleration, jerk, snap, crackle, pop, etc. Of particular interest is the case of null boundary conditions, i.e., all derivatives at the start and end of the trajectory are equal to zero. We verified and evaluated our proposed approach in simulations and on hardware.


## 精读解读（中文）
### 一、研究动机
软连续体机器人自由度和柔性环节近似无限，结构振动抑制与高跟踪性能要求轨迹具有任意阶连续导数；现有工业、协作机器人和无人机轨迹多为C3至C5平滑，软体机器人常用线性插值或位置控制且常未指定平滑性，已有C∞基元经几何缩放后仍可能不满足端点任意阶导数为零，因此需要一种尊重运动学限制、适用于顺序状态过渡的C∞轨迹生成器。

### 二、技术方案（Method）
在归一化时间τ∈[0,1]上构造路径基元：先用平坦函数ψ(τ)=exp(-1/τ)（τ>0）、0（τ≤0），再经归一化φ(τ)=ψ(τ)/(ψ(τ)+ψ(1-τ))得到满足φ(0)=0、φ(1)=1、端点各阶导数为零、单调且点对称的C∞路径基元s(τ)；通过几何缩放q(t)=qs+(qg-qs)s(τ)，导数按q^(k)=Δq/(Δt)^k s^(k)(τ)计算，并用最大速度、加速度、加加速度等运动学限制确定持续时间Δt，从而生成关节空间点到点轨迹；实现上采用分段定义和稳健求导处理τ=0处，可同步多状态并支持零边界条件。

### 三、结果（Result）
提出的基元产生的轨迹速度、加速度、jerk、snap、crackle、pop等直至任意阶均连续，满足C∞平滑和零边界条件，并能通过调整持续时间遵守给定运动学限制；与多项式基元及Havercosine、指数、逻辑函数等对比，后者分别存在平滑阶次有限、端点导数跳变或路径跳变等问题；作者在肌腱驱动软体机器人仿真和7自由度FR3机械臂硬件上验证了方法，摘要未报告具体数值误差或速度指标。

### 四、结论（Conclusion）
该工作提供了可工程实现的C∞平滑点到点轨迹生成框架，将软连续体机器人对无穷阶平滑的潜在需求转化为简单的归一化路径基元加几何缩放方案，并证明其可推广到柔性关节或连杆机器人、无人机等需要高阶平滑过渡的场景；其主要意义在于以低实现成本替代线性插值和低阶多项式轨迹，降低振动并改善跟踪，但当前范围限于关节空间直线路径且定量性能仍待更全面评估。

### 五、方法论与关键技术细节
关键实现点包括：输入为起止关节状态和速度、加速度、加加速度上限，无学习训练过程；ψ为在0处平坦的非解析光滑函数，φ由ψ与其时间反转组合归一化，保证端点全阶导数为零、单调、点对称和φ(τ)=1-φ(1-τ)；路径采用直线几何缩放，曲线路径可化为角度等标量插值；持续时间由运动学限制缩放得到，多轴可同步；数值上需处理τ=0附近exp(-1/τ)下溢和分段导数，复杂度为逐点闭式求值、较低；局限是主要讨论关节空间点到点直线轨迹，硬件和仿真验证规模有限，摘要未给出与低阶方法的具体定量对比。
