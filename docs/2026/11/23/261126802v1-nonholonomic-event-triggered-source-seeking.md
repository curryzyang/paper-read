# Nonholonomic Event-Triggered Source Seeking

- 区域：精读区
- 排名：1
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Victor Hugo Pereira Rodrigues, Tiago Roux Oliveira, Miroslav Krstic
- 机构：State University of Rio de Janeiro, University of California San Diego
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26802v1) · [PDF](https://arxiv.org/pdf/2611.26802v1)

## TLDR
The paper proposes an event-triggered source-seeking controller for nonholonomic unicycle vehicles that keeps continuous probing active while aperiodically updating the source-seeking correction from a filtered gradient estimate, guaranteeing practical exponential convergence to the unknown source, a positive minimum dwell time excluding Zeno behavior, and applicability to anisotropic quadratic source fields.

## Abstract
This paper introduces an event-triggered source seeking control (ET-SSC) strategy for autonomous vehicles modeled as nonholonomic unicycles. The key feature of the proposed design is the separation between the continuous probing motion required for gradient extraction and the event-triggered update of the source-seeking correction. This separation enables aperiodic computation and transmission of the correction while the periodic probing signals remain continuously active. The triggering mechanism acts on a low-pass-filtered gradient estimate, obtained by high-pass (washout) filtering, demodulation, and low-pass filtering of the measured signal, and combines a relative and an absolute threshold. Stability is proved with a time-periodic Lyapunov function constructed along the exponentially stable periodic solution of the filtered closed loop, establishing practical exponential convergence of the vehicle to a neighborhood of the unknown source. The guaranteed minimum dwell time is strictly positive and independent of the probing frequency, which excludes Zeno behavior. Unlike available Lie-bracket analyses of the forward-velocity design, the proposed averaging-based analysis accommodates anisotropic quadratic source fields with distinct spatial curvatures. The resulting ET-SSC framework therefore provides a resource-aware implementation in which the source-seeking correction is updated aperiodically while the information-generating probing motion remains continuous.


## 精读解读（中文）
### 一、研究动机
非完整无人车在GPS拒止环境中只能依靠局部标量场测量寻找未知源，而现有源搜索控制通常需要连续或快速周期更新控制修正；事件触发控制可降低计算与通信资源，但如何在不打断用于提取梯度的连续探测运动的前提下实现非周期修正更新，仍缺乏理论框架。论文旨在解决非完整独轮车源搜索中探测运动连续性与修正更新事件触发化之间的耦合问题。

### 二、技术方案（Method）
将被控对象建模为独轮车，采用前向速度调谐方案：角速度恒定为omega0，线速度由小振幅周期抖动和事件触发修正项组成，即v=a1 omega1 cos(omega1 t)+2L^T u，其中L由omega0 t+theta0构造，探测频率满足omega1=mu omega0且mu>3。车辆测得标量场信号后，先经高通洗出滤波、与探测信号解调，再经低通滤波得到梯度估计；触发机制作用于该低通滤波后的梯度估计，结合相对阈值与绝对阈值决定是否非周期地计算并传输源搜索修正u，而周期探测信号始终连续运行。稳定性分析采用平均化方法，并沿滤波闭环的指数稳定周期解构造时间周期Lyapunov函数，证明车辆位置实用指数收敛到未知源邻域。

### 三、结果（Result）
理论结果表明，在未知各向异性二次源场中，即使两个空间方向曲率不同，所提ET-SSC仍能保证车辆实用指数收敛到源点附近的小邻域。触发机制保证的最小驻留时间严格为正且与探测频率无关，从而排除Zeno行为；与依赖Lie括号分析的前向速度设计相比，该平均化分析可直接容纳具有不同空间曲率的方向异性二次场。

### 四、结论（Conclusion）
论文给出了首个面向非完整车辆的 event-triggered source-seeking 框架，使控制器侧源搜索修正可以非周期更新且具有可保证的最小更新间隔，同时保持用于信息生成的快速探测运动连续。该框架实现了资源感知的源搜索：节省的是修正的计算与通信资源，而不是车辆探测运动本身。

### 五、方法论与关键技术细节
关键实现细节包括：源场建模为具有唯一未知最大值的各向异性二次函数，Hessian为diag(-fx,-fy)；假设源位置、强度和曲率未知；探测频率比mu>3、抖动振幅a1和角速度omega0需满足平均化与收敛条件。触发判据基于低通滤波后的梯度估计而非含快速旋转的解调信号，因此最小驻留时间不随探测频率缩小。证明采用平均化与时间周期Lyapunov函数，依赖滤波闭环周期解的指数稳定性；主要局限是源场局部二次、参数调谐和传感器中心布置假设，且方法只降低修正更新频率，不减少连续探测能耗。
