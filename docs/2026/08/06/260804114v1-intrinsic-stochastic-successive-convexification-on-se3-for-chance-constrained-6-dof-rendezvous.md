# Intrinsic Stochastic Successive Convexification on SE(3) for Chance Constrained 6-DOF Rendezvous

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Fabio D'Onofrio, Renato Zanetti
- 机构：The University of Texas at Austin
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04114v1) · [PDF](https://arxiv.org/pdf/2608.04114v1)

## TLDR
The paper introduces an intrinsic stochastic successive convexification method on SE(3) that jointly optimizes the nominal trajectory, covariance, and feedback law for chance-constrained 6-DOF spacecraft rendezvous, capturing coupled translational–rotational uncertainty to improve probabilistic constraint satisfaction.

## Abstract
This work presents an intrinsic stochastic successive convexification method formulated on the Special Euclidean group SE(3) for six degrees of freedom spacecraft rendezvous trajectory optimization. The proposed approach extends stochastic successive convexification, originally developed for Euclidean state spaces, to the nonlinear manifold of SE(3), thereby enabling a consistent covariance steering and chance constrained optimization of rigid body pose trajectories. While conventional trajectory optimization methods often treat position and attitude separately, or account for stochastic dispersion only after a deterministic reference trajectory has been generated, the proposed SE(3)-based formulation captures the intrinsic coupling between translational and rotational motion uncertainty. This coupling is especially important for rendezvous problems with safety constraints that depend on the full relative pose, including collision avoidance, docking corridor, camera field of view, and probabilistic force and torque bounds. Numerical simulations show that jointly optimizing the nominal trajectory, covariance, and feedback law shapes the closed loop dispersion and improves probabilistic constraint satisfaction relative to tracking a deterministic reference with a feedback linearization controller.


## 精读解读（中文）
### 一、研究动机
传统六自由度交会轨迹优化方法常将位置与姿态分离处理，或仅在确定性参考轨迹生成后才加入随机散布，因而无法捕获平动与转动运动不确定性之间的内在耦合。这种耦合对依赖完整相对位姿的安全约束（如碰撞规避、对接走廊、相机视场、概率力/力矩界）至关重要，因此需要在SE(3)流形上建立一致的协方差控制和机会约束优化框架。

### 二、技术方案（Method）
本文提出一种在SE(3)上的内蕴随机逐次凸化方法。完整状态定义为乘积群SE(3)×ℝ^{n_c}，其中SE(3)表示位姿，ℝ^{n_c}表示欧氏速度分量。使用左不变逆回缩（boxminus）将位姿扰动映射到李代数切空间，用左回缩（boxplus）将切空间修正映射回流形，以此保持标称轨迹在流形上。在每次迭代中，将非线性动力学在切空间线性化，并结合集中高斯分布假设在切空间传播协方差，形成关于标称轨迹、协方差序列和仿射反馈增益的凸子问题。机会约束通过切空间协方差投影转写为确定性凸约束，并采用虚拟控制和信任域机制避免人工不可行性与无界性。算法迭代求解凸子问题直至收敛，实现同时优化标称轨迹、协方差与反馈律。实现采用齐次矩阵，但亦可推广到对偶四元数表示。

### 三、结果（Result）
数值仿真表明，联合优化标称轨迹、协方差与反馈律能够主动塑造闭环散布，相比先求确定性参考再用反馈线性化控制器跟踪的方法，显著提高了概率约束满足度。该方法在碰撞规避、对接走廊、相机视场和概率力/力矩界等依赖完整相对位姿的约束下均表现出更好的一致性。

### 四、结论（Conclusion）
本文在SE(3)上建立了几何一致的随机顺序凸优化框架，使位姿更新、不确定性模型、反馈策略和概率约束全部表达在SE(3)的李代数中，从而在六自由度交会问题中实现了平动与转动不确定性的内在耦合优化。该方法拓展了随机逐次凸化到非线性流形的适用范围，为位姿级随机轨迹优化提供了可行且高效的工具。

### 五、方法论与关键技术细节
关键点包括：采用左集中高斯分布假设，概率质量集中于对数映射良定义的邻域，因此可在李代数中使用欧氏协方差代数；使用左群理论均值而非Fréchet均值；位姿扰动采用左不变逆回缩，更新采用左回缩，保证均值在流形上；完整状态为SE(3)×ℝ^{n_c}，速度部分使用常规向量加法；机会约束利用切空间协方差投影转为高斯分位数约束；迭代凸化过程需要虚拟控制变量和信任域以保证可行性和收敛性；实现使用齐次矩阵，但推导同样适用于对偶四元数。局限性在于集中分布假设要求不确定性足够小，且未提供具体超参设置与复杂度分析。
