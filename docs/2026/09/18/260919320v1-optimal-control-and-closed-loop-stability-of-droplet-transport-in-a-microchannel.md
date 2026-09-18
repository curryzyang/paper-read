# Optimal Control and Closed-Loop Stability of Droplet Transport in a Microchannel

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Rajneesh Anand, Mayuresh V. Kothare
- 机构：Lehigh University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19320v1) · [PDF](https://arxiv.org/pdf/2609.19320v1)

## TLDR
This paper develops optimal control strategies for droplet transport in a microchannel using both a reduced-order ODE model solved via Pontryagin’s Maximum Principle and a full PDE model optimized by an evolutionary strategy, revealing translate–relax versus compact–translate–relax regimes and proving closed-loop exponential stability via a control Lyapunov function.

## Abstract
Understanding the efficient transport of fluid droplets in confined geometries has been a domain of interest for industrial applications in recent times. In the present work, we focus on designing control strategies that optimally steer droplet motion. Here, we apply optimal control framework to the droplet transport problem in a microchannel based on lubrication theory that minimizes viscous dissipation. Two complementary modeling routes are adopted: a reduced-order ordinary differential equation (ODE) model optimized via Pontryagin's Maximum Principle, and a full nonlinear partial differential equation (PDE) model optimized using a Covariance Matrix Adaptation-Evolutionary Strategy. By parameterizing target displacement, droplet size, and capillary number, we uncover two distinct optimal transport regimes: a "translate-relax" strategy for short distances and a "compact-translate-relax" strategy for longer targets. In continuum mechanics, the competition between surface forces and cumulative viscous dissipation decides the optimal transport strategies. We further show that the displacement range over which the reduced-order controller transfers to the continuum model is governed by capillary stiffness. We finally address closed-loop stability by adapting a control Lyapunov function (CLF) framework to the reduced-order dynamics. We demonstrate that the terminal cost which penalizes deviation from the target, serves as a cost-compatible CLF on the physical domain, and prove that the CLF-compatible feedback exponentially stabilizes the target state.


## 精读解读（中文）
### 一、研究动机
微通道内液滴的高效输运对微流控与工业应用至关重要，但现有最优控制研究多集中于具有内驱机制的活性软物质，缺少以外加压力梯度或流场为控制输入、同时兼顾最优性与闭环稳定性的工作。本文旨在基于润滑理论设计最小化黏性耗散的液滴输运控制策略，并为有限时域最优控制提供稳定性保证。

### 二、技术方案（Method）
采用润滑理论建立液滴高度场 h(x,t) 的深度平均连续性方程与通量 q=-h^3/(12μ)(γ h_xxx+∂x(Gh))，控制取 G(x,t)=G0(t)+ΔG(t)(x-xc)/R，目标为固定时间内最小化黏性耗散 W 与终端位置/尺寸偏差 T 的加权和。一路将液滴近似为抛物线剖面，用矩/Galerkin投影得到位置 X 与尺寸 R 的低维 ODE，并用 Pontryagin 最大值原理求解析/数值最优控制；另一路直接对非线性 PDE 用 CMA-ES 无梯度进化策略，以高斯分布 N(m,σ²C) 采样控制剖面、前向积分 PDE 评估代价并更新分布。最后将终端代价作为控制 Lyapunov 函数 CLF 适配到约化动力学，构造 CLF 兼容反馈并证明指数稳定。

### 三、结果（Result）
通过参数化目标位移、液滴尺寸和毛细数，发现短距离下最优策略为“平移-弛豫”TR，较长距离下为“紧凑-平移-弛豫”CTR，后者类似活性液滴的 gather-move-spread。连续介质中表面力与累积黏性耗散的竞争决定最优策略，且约化控制器可迁移到连续模型的位移范围由毛细刚度控制。PDE+CMA-ES 数值优化验证了约化模型的定性预测；终端代价在物理域上是有效 CLF，CLF 兼容反馈使目标状态指数稳定。

### 四、结论（Conclusion）
本文给出可解释的液滴输运最优控制框架，揭示了输运效率、变形与控制代价之间的权衡，并弥补了微流控液滴控制中最优控制与闭环稳定性分析之间的空白。结果可用于设计压力梯度驱动的微通道液滴输运策略，并为约化模型到连续模型的控制迁移提供毛细刚度判据。

### 五、方法论与关键技术细节
模型假设低雷诺数润滑极限 H≪W≪L、无重力、体积守恒 ∫h dx=1，PDE 中保留前驱膜/分离压以正则化接触线；控制是轴向压力梯度，空间线性变化，用有效 Ca_G 表征表面张力与驱动变形竞争。代价中 W 为剪切黏性耗散积分，终端代价为 A((X(T)-X_T)/X_T)^2+B((R(T)-R_T)/R_T)^2；PMP 适合 2 状态 2 控制、控制仿射系统并可闭式消去控制，CMA-ES 适合非凸瞬态 BVP、O(10²) 参数、各向异性敏感且无需导数。稳定性依赖无漂移控制仿射结构，终端代价作为 CLF；局限包括固定时域、约化模型忽略部分界面物理、进化优化计算代价以及润滑近似适用范围。
