# Forward Tangent-Centered Sinkhorn DRO: Exact Nominal Recovery from Optimal Transport to KL

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Junjie Guo
- 机构：Rutgers University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30144v1) · [PDF](https://arxiv.org/pdf/2610.30144v1)

## TLDR
The paper proposes a forward tangent-centered Sinkhorn discrepancy for distributionally robust optimization that subtracts the nominal-law tangent from entropy-regularized optimal transport, ensuring exact recovery of the nominal distribution while preserving a tractable log-sum-exp dual and interpolating between optimal transport and KL divergence across temperature regimes.

## Abstract
Fixed-reference entropy-regularized transport yields smooth distributionally robust optimization (DRO) objectives, but its value as a function of the adversarial marginal is generally minimized at a kernel-smoothed law rather than at the nominal distribution. Consequently, the smallest raw ambiguity set need not recover nominal risk. Building on prior information-geometric plan-KL orientations, we study the forward tangent-centered discrepancy obtained by subtracting the value and first variation at the nominal law. This is the unique affine recentering, up to the simplex gauge; for symmetric costs, its plan-KL representation coincides with the forward candidate noted by Amari et al. (2018). The representation shows that the discrepancy dominates marginal KL, is uniquely zero at the nominal law, and is strongly convex in total variation. The resulting DRO problem retains a scalar log-sum-exp dual and closed-form conditional adversarial weights. On finite supports with symmetric zero-diagonal costs, the discrepancy converges uniformly to the unregularized transport cost at low temperature; for any finite cost, its rescaled value converges uniformly to marginal KL at high temperature. We derive its exact local Hessian, an explicit finite-sample containment radius, and a generalized chi-square calibration for multinomial data. Controlled simulations verify nominal centering, both limiting regimes, and practical plug-in coverage.


## 精读解读（中文）
### 一、研究动机
固定参考熵正则最优传输虽使Sinkhorn DRO目标光滑易解，但其关于对抗边际的最小点通常是名义分布的核平滑版本，而非名义分布本身，因此最小的原始模糊集不必然恢复名义风险。本文旨在去除这种固定参考漂移，同时保留DRO所需的凸性与log-sum-exp可解结构。

### 二、技术方案（Method）
在有限支撑上定义熵正则传输值Tγ(q,p)，先刻画其原始最小点为核平滑qγ°(p)，再对q↦Tγ(q,p)在名义p处减去值与一阶变分，构造前向切中心差异Dγ^TC(q||p)=F(q)-F(p)-ν^T(q-p)，并证明其是单纯形上唯一的仿射重新中心。方法核心包括：利用最优传输计划得到Dγ^TC=γKL(Πγ^{q,p}||Πγ^{p,p})及边际KL链式分解；将DRO鲁棒风险写为Dγ^TC≤ρ约束下的线性损失最大化，推导仅含标量传输乘子的强对偶和闭式条件最坏耦合/对抗权重；进而分析低温OT极限、高温KL极限，并用条件softmax协方差给出局部Hessian、有限样本包含半径和多项数据的广义卡方校准，最后以受控仿真验证名义居中、两温度极限和插件覆盖。

### 三、结果（Result）
理论结果显示Dγ^TC唯一在p处为零、支配边际KL并在全变差下强凸，故ρ=0时鲁棒风险精确等于名义风险p^T L(θ)，实现精确名义恢复。对有限支撑对称零对角成本，低温下Dγ^TC一致收敛到未正则传输成本，误差界为εγ=2γ[1+2log m+log(√m/p_min)]；任意有限成本高温下Dγ^TC/γ一致收敛到边际KL，且非退化KL极限需取ρ=γτ。鲁棒风险也有一致收敛界，如低温下与Wasserstein型DRO风险的差异不超过2Bεγ/ρ；仿真验证了名义居中、两个极限 regime 及插件式覆盖。

### 四、结论（Conclusion）
前向切中心化可在不牺牲Sinkhorn DRO凸性和标量对偶可解性的前提下，消除固定参考熵正则造成的名义分布漂移，使模糊集真正以名义分布为中心。该构造在低温端连接离散最优传输、在高温端连接KL-DRO，提供了一个由温度控制的建模连续谱，并给出可操作的局部校准与有限样本半径。

### 五、方法论与关键技术细节
关键实现点包括：熵以计数测度为参考，固定参考矩阵经正行列缩放或成本加行列势不改变Dγ^TC；名义p需在单纯形内部，成本有限，理论主要覆盖有限维分类/情景约简/加权支撑。对偶每次评估为O(m^2)的稠密核log-sum-exp，名义自势由一次Sinkhorn缩放预计算；ρ=0无需求解即得名义风险，ρ>0需一维乘子优化。高温柔性依赖ρ=γτ缩放，固定ρ会收缩到{p}；局部几何由条件softmax协方差刻画，并给出多项数据广义卡方校准。局限性是未提供连续支撑采样定理，也不处理学习得到的支撑或ground cost。
