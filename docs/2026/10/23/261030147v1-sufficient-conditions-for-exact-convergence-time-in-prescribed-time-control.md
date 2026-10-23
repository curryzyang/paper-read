# Sufficient Conditions for Exact Convergence Time in Prescribed-Time Control

- 区域：精读区
- 排名：1
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Jiyuan Kuang
- 机构：Harbin Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30147v1) · [PDF](https://arxiv.org/pdf/2610.30147v1)

## TLDR
This paper establishes local Lipschitz, local homogeneous linear-growth, and Osgood-type sufficient conditions to rigorously exclude premature convergence in prescribed-time control, thereby proving that the settling time is exactly the prescribed time rather than merely bounded by it.

## Abstract
In this paper, we propose a series of theoretical results for prescribed-time control to rigorously prove that the closed-loop system will not reach the equilibrium point before the prescribed time. Thus, it is convenient to prove that the settling time is exactly equal to the prescribed time instant. In other words, conservative estimation of the settling time, which often accompanies classical finite-/fixed-time or prescribed-time control results, is theoretically avoided in this paper. Specifically, we introduce a local Lipschitz condition, a local homogeneous linear-growth condition, and an Osgood condition in sequence. Both reduction to absurdity and the Lyapunov method are applied to demonstrate that the system cannot converge to zero before the prescribed time instant. Finally, the proposed framework is applied to prescribed-time controllers based on adaptive backstepping, parametric Lyapunov equations, and distributed leader-following consensus, demonstrating the generality of the proposed results.


## 精读解读（中文）
### 一、研究动机
现有有限时间、固定时间和预设时间控制通常只能保证在预设时刻 T 之前或至多 T 收敛，往往给出保守的 settling time 估计；而机器人击键、航天器编队和协同打击等任务要求系统恰好在预设时刻到达平衡点。论文旨在为预设时间闭环系统建立可验证的充分条件，严格排除在 T 之前提前收敛，从而证明 settling time 精确等于 T。

### 二、技术方案（Method）
本文是纯理论控制研究，不涉及数据训练；研究对象为含时变增益的闭环系统 dot x=P0(t,x)+sum Pk(x)/Phi_k(T-t)，在 Carathéodory 条件和已知 T-finite-time stable 假设下分析精确收敛。核心步骤是先利用连续性把提前到达原点转化为原点邻域内的局部可达性问题，再依次引入局部 Lipschitz 条件、局部齐次线性增长条件和 Osgood 型增长条件，结合反证法与 Lyapunov 方法证明任意非零初值轨迹在 [0,T) 内不能到达原点。最后将该判据应用于自适应反步法、参数 Lyapunov 方程和分布式领导跟随一致性等预设时间控制器。

### 三、结果（Result）
理论结果表明，在上述充分条件下闭环系统不会在预设时刻之前到达平衡点，因此若已有结果保证不晚于 T 收敛，则 settling time 可严格等于预设时间 T，理论上避免了经典 finite/fixed/prescribed-time 控制中的保守估计。文中两个反例说明仅 T-finite-time stable 或 prescribed-time stable 并不蕴含精确 T 收敛：任意小但持续的非零扰动可使标量系统提前命中原点，二阶系统也可在 T 前收敛。三类条件按正则性由强到弱给出了逐步推广的可验证判据，并成功覆盖自适应反步、参数 Lyapunov 方程和多智能体领导跟随一致性等代表性场景。

### 四、结论（Conclusion）
论文建立了用于证明预设时间控制精确收敛的充分条件框架，将精确 T 收敛分解为不晚于 T 收敛和在 [0,T) 内不可达原点两个互补性质。该框架可用于严格认证闭环 settling time 恰为预设 T，并为时间关键的多智能体协调任务提供理论依据。其价值在于把原有预设时间稳定性结果提升为精确收敛结论，同时保持判据仅在原点邻域内验证的便利性。

### 五、方法论与关键技术细节
关键实现细节包括要求 f(t,0)=0 以保证原点不变性并排除持续非消失扰动，假设闭环系统已 T-finite-time stable 且 x(t) 有界、t→T^- 时趋于零，并在每个紧子区间满足 Carathéodory 条件以保障解的存在性；充分条件只需局部成立，局部 Lipschitz、局部齐次线性增长和 Osgood 条件依次减弱，证明依赖连续性、反证法和双侧 Lyapunov 分析。多智能体情形通过协调误差化为 disagreement dynamics 后套用同一判据。局限性在于结论依赖原点不变性和已有 T 收敛前提，主要给出定性充分条件而非鲁棒性能或收敛速度的定量刻画，且不处理持续扰动下的提前命中问题。
