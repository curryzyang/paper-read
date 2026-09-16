# Conflict-Predictive Variable Horizons in Multi-Drone Distributed Model Predictive Control

- 区域：精读区
- 排名：5
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Linda Mümken, Michael Schwung, Stefan Lier, Andreas Schwung
- 机构：Ruhr University Bochum, South Westphalia University of Applied Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13270v1) · [PDF](https://arxiv.org/pdf/2609.13270v1)

## TLDR
The paper proposes a conflict-predictive variable prediction horizon for multi-drone distributed MPC, where each drone locally lengthens its horizon only when lightweight neighbor extrapolation with confidence funnels predicts an upcoming conflict, preserving recursive feasibility and stability while reducing computation and maintaining collision separation.

## Abstract
In distributed model predictive control for multi-drone collision avoidance, a fixed prediction horizon forces a compromise: a short horizon is inexpensive but reacts late to approaching neighbors, whereas a long one anticipates conflicts at a per-step cost that grows superlinearly with its length. We propose a conflict-predictive variable horizon that each drone sets locally, leaving the distributed model predictive control itself unchanged. From a short history of observed positions, a drone extrapolates the flight lines of its neighbors, tests each against its own using confidence funnels that narrow with prediction range, and obtains each time to conflict in closed form. The horizon is then the smallest admissible value whose planning window covers the farthest predicted conflict. It collapses to its minimum in clear airspace and grows only when a conflict lies ahead. Provided this minimum meets a single computable feasibility bound, we prove that recursive feasibility and asymptotic stability are preserved for every horizon the policy can select. These guarantees hold for a linear model, and a cascaded inner loop reduces each quadrotor's translational dynamics to a perturbed double integrator, so they carry over to the linearized quadrotor model and, as practical stability, to the full nonlinear one. In simulation on dense antipodal-swap benchmarks, the variable horizon reduces both per-step solver cost and total computation well below those of a long fixed horizon, and it maintains separation in every run, which a short fixed horizon of comparable per-step cost does not.


## 精读解读（中文）
### 一、研究动机
在多无人机分布式模型预测控制（DMPC）避撞中，预测时域是决定成败的核心参数：短时域计算便宜但对逼近的邻居反应太迟，长时域能提前化解冲突但每步优化代价随时域长度超线性增长。然而冲突在时空上是间歇且稀疏的，无人机大部分时间处于清空空域，固定时域却必须按最坏密集度设定，从而在每一步都付出前瞻代价。现有动态时域方法要么把时域作为优化变量造成非凸/混合整数负担，要么依据受控系统自身状态而非邻居几何来调整，且没有把安全保证与自适应信号解耦。

### 二、技术方案（Method）
提出冲突预测型可变时域，由每架无人机本地设定，完全不改动分布式MPC本身，仅替换其核心参数H。每个控制步，无人机用轻量线性预测器从一段短滚动观测历史中外推各邻居的飞行直线，并用随预测距离收窄的置信漏斗（容差管）将其与自身航线做检验，从而对每个邻居以闭式解得到冲突时间；时域取最小的可行值，使其规划窗口刚好覆盖最远的预测冲突，在空域清空时收缩到最小值H_min，仅在检测到冲突时才向H_max增长。为把结论推广到旋翼平台，采用级联内环将四旋翼平动动力学约化为带扰动的双积分器，底层DMPC沿用速度相关安全球、成对间隔约束与异步Gauss–Seidel迭代。

### 三、结果（Result）
理论方面证明：只要最小可容许时域H_min满足单一可计算的可行性界H_min^feas，则策略可能选择的每一个时域都保持递归可行性与渐近稳定性；时域仅通过有限时域近似残差进入分析，该残差在[H_min,H_max]上一致有界，并被一个仅依赖无人机物理状态的证书吸收。仿真方面，在稠密对跖交换（antipodal-swap）基准上，可变时域把每步求解代价与总计算量显著降到长固定时域之下，完成了长固定时域无法完成的交换任务，并在每次运行中都保持安全间隔，而每步代价相当的短固定时域则做不到。

### 四、结论（Conclusion）
由于可行性与稳定性建立在与冲突预测无关的时域下界之上，预测失误只会削弱前瞻能力并损失效率，绝不会危及安全，这使该时域策略与保证解耦，区别于现有动态时域方案。该保证对线性模型严格成立，并经由级联内环传递到线性化四旋翼模型（渐近稳定）以及完整非线性模型（实用稳定），且自适应安全半径与原有分布式控制器公式均无需修改。

### 五、方法论与关键技术细节
输入为机载感知或广播获得的时间戳邻居位置，无人机维护短滚动历史，邻居速度与自适应半径均由这些位置计算得到，避撞采用速度相关安全球与成对间隔约束。置信漏斗是随预测范围单调收窄的容差管，使得冲突判定可闭式求时间，冲突越远越需要更贴近才计为重叠。算法保持线性预测以保证轻量，并兼容可学习预测器而不影响保证。关键条件是H_min≥H_min^feas这一可计算界；底层分析依赖异步Gauss–Seidel/ADMM的分布式MPC、收缩论证与基于物理能量的Lyapunov函数。局限包括：线性外推的误预测只能降低前瞻性，理论结果对非线性动力学仅为实用稳定，验证目前限于仿真而非实飞，且性能受H_min、H_max与漏斗参数选择影响。
