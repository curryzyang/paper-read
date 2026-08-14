# Excitation-Supervised Closed-Loop Self-Calibration and Target Seeking for an Unknown-Pose Range-Bearing Relay

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Yash Bagla
- 机构：Michigan State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12528v1) · [PDF](https://arxiv.org/pdf/2608.12528v1)

## TLDR
TLDR: The paper introduces an excitation-supervised closed-loop controller that uses a single trajectory-spread margin to certify when an unknown-pose range-bearing relay is sufficiently self-calibrated, retriggering exploratory motion when excitation is insufficient and enabling provably finite-time calibration acquisition, accuracy-driven threshold selection, and reliable target seeking validated in simulation, Monte Carlo sweeps, and ROS 2/Gazebo experiments.

## Abstract
A vehicle seeking a hidden target through a range-bearing relay of unknown position and yaw must decide, online, whether its own motion has already made the relay calibration trustworthy, and what to do when it has not. Two distinct vehicle-relative observations are known to remove the calibration gauge and make the target's relay-local packet globally actionable (arXiv:2608.09464), but that statement is static: it classifies a stored window only after the fact. This paper supplies the closed-loop layer: we show that the trajectory-spread margin $S_v$ that governs identifiability is simultaneously a finite-noise seed-accuracy bound, a local-vector variance decomposition, and a circle-geometry excitation budget, and we use it to supervise an excitation-reset controller. An excitation-supervised algorithm retriggers exploratory motion whenever the spread certificate is insufficient, projecting the target-seeking input away from the excitation's push, and otherwise proceeds to unrestricted target seeking. Under explicit sampling assumptions the supervision rule provably acquires any required excitation in finite time; in the noiseless local regime with positive excitation decay, estimator convergence yields target-seeking convergence after certification; and the threshold is selected from a desired calibration-accuracy level rather than chosen heuristically. Closed-loop simulation, paired Monte Carlo comparisons, a spread-threshold ablation, and a ROS 2/Gazebo software-in-the-loop experiment with sensing delay validate the approach. A decay-rate sweep shows that supervision matters when a fixed schedule's decay outruns the unknown time-to-adequate-excitation: over 100 paired trials the fixed baseline's yaw RMSE rises from 0.010 to 0.065 rad and success falls to 56%, while target-tracking error remains insensitive; supervision keeps yaw RMSE between 0.0095 and 0.0191 rad with 100% success.


## 精读解读（中文）
### 一、研究动机
车辆通过未知位姿的测距-测向中继（range-bearing relay）寻找隐藏目标时，中继的位置和偏航未知且目标仅以中继局部坐标系报告。已有工作证明两类车辆相对观测可消除标定自由度，但该结论是静态的：只能在事后判断已存储轨迹窗口是否充分激励。本文要解决在线闭环问题：车辆在每一步必须决定自身运动是否已使中继标定可信，若不足则应继续探索，否则才进行目标追踪。作者希望将轨迹扩展裕度S_v从静态可辨识条件转化为可在线监督的标定激励判据，从而避免固定探索时间表在未知标定时间下失效。

### 二、技术方案（Method）
本文提出一种激励监督的闭环自标定与目标搜寻算法。系统模型为：隐藏目标p和中继x,yaw未知，车辆在每个位姿q_k收到中继返回的局部坐标系下的含噪距离-方位包，状态z=(p,x,ψ)，通过最小化加权批量残差J(z)进行估计。核心方法是利用轨迹扩展裕度S_v=Σ||ℓ_k^v-ℓ̄^v||²（噪声情形下等于Σ||q_k-q̄||²）作为监督信号。算法流程为：控制器在每一步检查S_v是否超过阈值S̄；若不足，则重新触发探索运动（如圆形旋转包络），同时将目标追踪输入投影到探索推动方向的垂直方向以避免干扰标定；若超过阈值，则停止探索并切换到无限制目标追踪。阈值S̄由期望标定精度推导：由var(ψ̂)=σ²/S_v，给定所需偏航标准差ε_ψ，选取S̄≥σ²/ε_ψ²，对应最少圆上位姿数K≥σ²/(ρ²ε_ψ²)。理论上证明：在显式采样假设下，监督规则能有限时间内累积所需激励；在无噪声局部区域且正激励衰减下，估计器收敛可带来标定后目标追踪收敛。验证通过闭环仿真、配对蒙特卡洛、阈值消融以及含传感延迟的ROS 2/Gazebo软件在环实验完成。

### 三、结果（Result）
核心发现：S_v同时作为有限噪声种子精度界、局部向量方差分解和圆形几何激励预算。理论结果包括：构造性种子误差界中，偏航误差|ψ̂-ψ|≤2πε/d_v，位置误差随1/√S_v或1/S_v缩放；线性化模型下var(ψ̂)=σ²/S_v，目标估计协方差分解为(σ²/K)I（平均项）和B F_ζ^{-1}B^T（标定传播项）；圆上等距K个位姿时S_v=Kρ²，达到阈值S̄最多需⌈S̄/ρ²⌉个位姿。实验方面，100次配对试验的衰减率扫描显示：当固定激励时间表的指数衰减快于未知的达到充分激励所需时间时，固定基线的偏航RMSE从0.010升至0.065 rad，成功率降至56%，而监督方法保持偏航RMSE在0.0095–0.0191 rad之间且成功率100%；目标追踪误差对两种方法不敏感。阈值消融验证了精度驱动阈值可作为总体RMSE目标，并量化了其激励代价。

### 四、结论（Conclusion）
本文证明轨迹扩展裕度S_v不仅是可辨识性条件，更是可在闭环中在线监督的标定质量证书。通过将静态可辨识性转换为由S_v触发的探索-重置控制律，算法能自适应地决定何时停止探索并切换到目标追踪，消除了固定时间表在未知标定时间下的脆弱性。理论保证与仿真、蒙特卡洛和软件在环实验共同表明，监督机制在有限时间内获取所需激励，且在标定后目标追踪收敛。结论是：当普通闭环运动难以自然提供足够激励时，激励监督对保证标定精度和成功率至关重要，而阈值可根据目标标定精度而非启发式选取。

### 五、方法论与关键技术细节
关键细节：(1) 测量噪声模型为各向同性高斯噪声，精度矩阵W=diag(σ_r^{-2},σ_θ^{-2},σ_r^{-2},σ_θ^{-2})；(2) 种子构建利用两帧车辆相对观测，要求d_v≥4ε以保证角度误差有界；(3) 方差分解中目标包对(x,ψ)的Fisher信息为零（当p可自由吸收变化），因此标定信息完全来自车辆包，yaw信息量F_ψ=S_v/σ²；(4) 圆形激励预算S_v=Kρ²(1-||ū||²)，等分圆周时ū=0；(5) 阈值设计规则S̄=σ²/ε_ψ²，允许从期望偏航精度反推最少位姿数；(6) 算法实现中欠激励阶段将目标追踪输入投影到探索推动方向的垂直方向以避免冲突；(7) 监督规则在显式采样假设下有限时间获取所需激励，无需预先知晓达到充分激励所需时间；(8) 局限性：局部收敛结论在无噪声模型下证明，噪声下的全局收敛依赖高斯-牛顿收敛域；监督对目标追踪误差影响不显著，说明其价值主要在于维护标定质量而非目标估计本身。代码与数据开源。
