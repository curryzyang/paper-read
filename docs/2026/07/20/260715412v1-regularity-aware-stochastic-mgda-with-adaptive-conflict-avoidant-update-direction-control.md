# Regularity-Aware Stochastic MGDA with Adaptive Conflict-Avoidant Update Direction Control

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Chentong Huang, Lisha Chen
- 机构：University of Rochester
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15412v1) · [PDF](https://arxiv.org/pdf/2607.15412v1)

## TLDR
The paper proposes a regularity-aware stochastic multi-gradient descent method (MoRe) that achieves an improved convergence rate of \(\widetilde{\mathcal O}(T^{-1/2})\) from \(\widetilde{\mathcal O}(T^{-1/4})\) by exploiting Lipschitz continuity of the conflict-avoidant direction under nondegeneracy and switching to linear scalarization otherwise, with per-iterate conflict-avoidance guarantees.

## Abstract
Multi-objective learning (MOL) aims to optimize multiple objectives simultaneously. The multi-gradient descent algorithm (MGDA) is a workhorse that iteratively updates along a common descent or conflict-avoidant (CA) direction across objectives. In stochastic settings, however, the vanilla stochastic MGDA method, SMG, lacks a fast convergence rate because mini-batch sampling introduces noise in the gradients. This causes bias in the update direction, which is controlled by the CA direction continuity. In this paper, we show that the CA direction is $1/2$-Holder continuous with respect to the Jacobian matrix, and the exponent $1/2$ cannot be improved in the worst case. This leads to a suboptimal convergence rate for vanilla stochastic MGDA in prior works. Nevertheless, under additional regularity conditions, we show this can be improved to Lipschitz continuity. Based on this insight, we propose a stochastic multi-objective regularity-aware (MoRe) method that exploits the Lipschitz continuity of the CA direction when the subproblem is regular, and switches to a fixed scalarization weight otherwise. Intuitively, the proposed algorithm employs CA direction update when the gradient conflict is large, and linear scalarization update otherwise. Theoretically, our method improves the convergence rate of SMG in the nonconvex setting from $\widetilde{\mathcal O}(T^{-1/4})$ to $\widetilde{\mathcal O}(T^{-1/2})$, where $\widetilde{\mathcal O}(\cdot)$ hides logarithmic factors. Meanwhile, we also establish the per-iterate conflict-avoidance guarantees. Empirically, experiments demonstrate its effectiveness in multi-task performance and verify convergence behavior consistent with the established theoretical rate.


## 精读解读（中文）
### 一、研究动机
现有随机多梯度下降（SMG）方法在多目标学习中因小批量梯度噪声导致冲突避免（CA）方向偏差，收敛率仅为O~(T^{-1/4})。研究表明CA方向仅满足1/2-Hölder连续性，最坏情况下不可改进，但该连续性限制了算法在随机设置下的稳定性与速率。本文旨在探索CA方向何时能获得更强的Lipschitz连续性，并设计利用正则性的算法以加速收敛。

### 二、技术方案（Method）
输入为从小批量Z_t采样得到的随机梯度矩阵Q_t。建模为求解CA方向子问题：min_{λ∈Δ^M} ||Q_tλ||^2，得到方向d_t=-Q_tλ*。关键模块是检测子问题是否满足μ-非退化条件：当||Q_t^⊤Q_t P||_F或相关量保证CA方向Lipschitz连续时，使用CA方向更新；否则切换到固定标量化权重（如等权重）。训练流程中，采用小批量大小|Z_t|=Θ(t+1)和步长α=Θ(T^{-1/2})，迭代更新参数x_{t+1}=x_t+α d_t。该算法称为MoRe（多目标正则性感知）。

### 三、结果（Result）
理论证明在非凸经验目标上，MoRe的收敛率达到O~(T^{-1/2})，显著优于SMG的O~(T^{-1/4})。同时建立了逐次迭代的CA方向距离上界，保证冲突避免能力。实验在多任务学习基准上验证了MoRe在模型性能和收敛行为上与理论一致，实际收敛速率匹配O~(T^{-1/2})。

### 四、结论（Conclusion）
本文通过精细分析CA方向连续性，揭示了非退化条件下Lipschitz连续性的存在，并据此提出MoRe算法。该算法自适应切换CA方向与标量化更新，在理论上将随机MOL的收敛率从O~(T^{-1/4})提升至O~(T^{-1/2})，同时保持冲突避免性质，实验证实其有效性和理论匹配。

### 五、方法论与关键技术细节
关键点包括：1）μ-非退化条件定义（投影矩阵P=I-M^{-1}11^⊤，以及梯度矩阵Q的相关条件），该条件使CA方向成为Lipschitz连续；2）证明若子问题不合格，CA方向仅为1/2-Hölder连续且sharp；3）小批量大小随迭代t线性增长，步长α=O(T^{-1/2})，收敛率中隐藏对数因子；4）算法需在每次迭代检测非退化条件，可能增加开销；5）限制优化器为p×M梯度矩阵，未考虑高维模型或结构化先验，且只针对经验目标，未讨论泛化界。
