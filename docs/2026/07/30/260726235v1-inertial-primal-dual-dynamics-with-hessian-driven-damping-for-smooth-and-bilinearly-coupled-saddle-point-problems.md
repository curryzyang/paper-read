# Inertial Primal Dual Dynamics with Hessian-driven Damping for Smooth and Bilinearly Coupled Saddle Point Problems

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Zepeng Wang, Juan Peypouquet
- 机构：University of Groningen
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26235v1) · [PDF](https://arxiv.org/pdf/2607.26235v1)

## TLDR
This paper introduces two inertial primal-dual dynamical systems with Hessian-driven damping that achieve fast convergence rates for smooth bilinearly coupled saddle point problems and affinely constrained convex optimization.

## Abstract
Featuring Hessian-driven damping, two inertial primal dual dynamical systems are proposed for solving smooth saddle point problems with bilinear coupling. For convex-concave functions, we establish a convergence rate $\mathcal{O}\left( \frac{1}{t^2} \right)$ for the primal dual gap; for strongly convex-strongly concave functions, we obtain an asymptotic rate $\mathcal{O}\left( \frac{1}{t^{α-1}} \right)$ ($α\ge 3$ is the damping parameter) without knowledge of the strong convexity parameters, and an accelerated linear convergence rate when the strong convexity parameters are known. As an application of the proposed inertial systems, we also consider the affinely constrained convex optimization problem, and develop an inertial system with Hessian-driven damping, which complements existing results.


## 精读解读（中文）
### 一、研究动机
现有的惯性原始对偶系统缺乏Hessian-driven damping，导致轨迹振荡和离散化困难，且在强凸情形下收敛率不理想。本文旨在引入Hessian-driven damping，以平滑轨迹、直观离散化并提升收敛速度，同时填补强凸问题中无参数先验时次线性收敛率的研究空白。

### 二、技术方案（Method）
针对光滑双线性耦合鞍点问题，提出两类惯性原始对偶动力学系统。对于凸-凹情形，构建PD-AVD-H系统：
\ddot{x} + (α/t)\dot{x} + β_f ∇_{xx}L(x,y)\dot{x} + (γ+r/t)∇_xL(x,y+θt\dot{y})=0,
\ddot{y} + (α/t)\dot{y} - β_g ∇_{yy}L(x,y)\dot{y} - (γ+r/t)∇_yL(x+θt\dot{x},y)=0,
其中α≥3, β_f,β_g,γ,r,θ>0。通过构造能量函数（含Hessian阻尼和耦合项）进行Lyapunov分析。对于强凸-强凹情形，提出PD-HBF-H系统（具有与重球法类似的结构），在已知强凸参数μ_f,μ_g时设置β与α。仿射约束问题则通过增广拉格朗日L_ρ将系统扩展。

### 三、结果（Result）
凸-凹情形下，原始对偶间隙以O(1/t^2)收敛；强凸-强凹且参数未知时，达到O(1/t^{α-1})（α≥3）渐近收敛率；若已知强凸参数，则加速为线性收敛率O(e^{-√(γ_0μ)t})（μ=min(μ_f,μ_g)）。对于仿射约束凸优化，增广拉格朗日间隙、函数值和可行性偏差均以O(1/t^2)收敛。

### 四、结论（Conclusion）
本文提出的带Hessian-driven阻尼的惯性原始对偶动力学系统，在双线性耦合鞍点问题上实现了更优的收敛率：凸-凹情形保持最优的O(1/t^2)率，强凸-强凹情形首次在无参数先验下获得O(1/t^{α-1})次线性率，并在已知参数时达到线性收敛。Hessian阻尼有效减少了轨迹振荡，为算法离散化提供了直观基础，且扩展至仿射约束问题。

### 五、方法论与关键技术细节
关键点包括：(1) 能量函数W(t)包含二阶矩、惯性项和Hessian阻尼；(2) Hessian-driven damping项β_f∇_{xx}L, β_g∇_{yy}L降低振荡并加速梯度消失；(3) 需要f,g二次连续可微且凸（强凸情形需已知或未知参数两种设定）；(4) 参数α控制惯性强度，β_f,β_g对收敛率无本质影响但改善路径；(5) 分析中利用凸性一阶条件⟨∇F, s-s^*⟩ ≥ F；(6) 复杂度：系统为二阶ODE，需数值离散化；(7) 局限性：仅适用于光滑问题，非光滑可通过降阶处理但未深入。
