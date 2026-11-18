# Asymptotic analysis of sample average approximations for optimal control problems with uncertain dynamics

- 区域：精读区
- 排名：1
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Maria Soledad Aronna, João Miguel Machado, Oscar Sierra Fonseca
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21831v1) · [PDF](https://arxiv.org/pdf/2611.21831v1)

## TLDR
This paper develops a second-order asymptotic theory for sample average approximations of control-affine optimal control problems with uncertain parameters, establishing differentiability and well-posedness, almost sure consistency with dimension-free \(M^{-1/2}\) convergence rates, central limit theorems and asymptotic distributions for optimal values and minimizers, and confidence intervals for linear functionals of the optimal control.

## Abstract
We study sample average approximations (SAA) of optimal control problems with control-affine dynamics depending on an uncertain parameter. The objective is an expected terminal cost plus a Tikhonov regularization term, and the controls are square-integrable functions subject to pointwise convex constraints. We show that the reduced objective is twice continuously differentiable in the square-integrable topology, so that no two-norm discrepancy arises, and that its Hessian is a Hilbert--Schmidt perturbation of a multiple of the identity. This yields Lipschitz regularity of stationary controls and second-order conditions without gap for polyhedral constraints. For the SAA scheme with sample size $M$, we prove almost sure uniform consistency of the empirical minimizers, convergence rates of order $M^{-1/2}$ for the optimal values, independent of the dimension of the parameter space. We then derive the asymptotic distributions. The optimal values satisfy a central limit theorem, obtained from a functional central limit theorem for the SAA objective. The empirical minimizers are asymptotically Gaussian when the constraints are inactive; under polyhedral constraints, their limit solves a quadratic problem on the critical cone with a Gaussian linear term. We also derive confidence intervals for linear functionals of the optimal control and illustrate the results on two numerical examples.


## 精读解读（中文）
### 一、研究动机
实际最优控制问题中，动力学参数、初始状态或模型系数往往只能以概率分布描述，因此需要设计一个对整族系统都表现良好的开环控制，即最小化期望终端代价的平均（风险中性/ensemble）最优控制问题。但该分布通常未知或不可解，只能用数据构造的经验测度近似，于是样本平均近似（SAA）成为自然的求解与统计推断工具。已有工作多只给出 epi-收敛意义下的定性收敛结论，缺少收敛速率、渐近分布与置信区间等定量结果，本文正是为补足这一缺口。

### 二、技术方案（Method）
研究对象是控制仿射、依赖不确定参数的动力学系统，控制取为 L^2([0,T];R^m) 中满足逐点凸约束的函数，目标为期望终端代价加 Tikhonov 正则项。作者先把状态对控制的依赖代入，得到约化目标泛函，并证明它在 L^2 拓扑下二次连续可微、不存在 two-norm discrepancy，且 Hessian 是恒等算子常数倍加上一个 Hilbert–Schmidt 扰动；由此推出驻点控制的 Lipschitz 正则性，以及多面体约束下无间隙的二阶充分条件。随后构造样本量 M 的 SAA：用 i.i.d. 样本的经验测度替换真实分布，求解经验问题的最优值与前 minimizer，先证几乎必然一致收敛与 M^{-1/2} 速率，再对 SAA 目标建立泛函中心极限定理，导出最优值的 CLT 与经验 minimizer 的渐近分布（约束不起作用时为高斯；多面体约束下为临界锥上带高斯线性项的二次规划解），并据此给出最优控制线性泛函的置信区间，最后用两个数值算例验证。

### 三、结果（Result）
论文证明了经验 minimizer 几乎必然一致收敛，最优值的收敛速率为 M^{-1/2} 且与不确定参数空间的维数无关；最优值满足中心极限定理，经验 minimizer 在约束不起作用时渐近高斯，在多面体约束下其极限是临界锥上一个带高斯线性项的二次规划问题的解。基于这些极限分布构造的线性泛函置信区间在两个数值算例上得到验证，表明理论分布可用于实际的区间估计。

### 四、结论（Conclusion）
对带不确定动力学的控制仿射最优控制问题，SAA 不仅有定性的一致性，还具备与参数维数无关的定量收敛速率和可显式刻画的渐近分布，因此可以直接支撑样本量选择、误差评估与最优控制的统计推断。约化目标在 L^2 下的二阶结构与 Hilbert–Schmidt 型 Hessian 是这些结论成立的核心机制。

### 五、方法论与关键技术细节
关键点包括：依赖于 Tikhonov 正则项与 Hessian 的 Hilbert–Schmidt 结构，才在 L^2 拓扑下获得二次连续可微并避免 two-norm discrepancy；收敛速率与参数维数无关源于 Hillbert–Schmidt/迹类性质对维数不敏感；分布层面要求 i.i.d. 采样，约束为逐点凸集（多面体情形可给出无间隙二阶条件与临界锥刻画）。局限在于结果只覆盖控制仿射动力学、开环控制、凸约束与可微终端代价，且正则项不可省略，对非凸问题、状态约束与反馈策略等情形尚未涵盖。
