# Consistent Model Chasing Is Minimax Optimal: The Exact Value of Scalar Adversarial Adaptive Control under Large Parametric Uncertainty

- 区域：精读区
- 排名：2
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Dimitar Ho
- 机构：California Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13651v1) · [PDF](https://arxiv.org/pdf/2608.13651v1)

## TLDR
The paper proves that for the fundamental scalar adversarial adaptive control problem with arbitrarily large unknown pole uncertainty, the exact minimax worst-case peak is \(\gamma^\star(\Delta)=1+\Delta\), and the uniquely optimal policy is certainty-equivalent deadbeat control at the midpoint of the consistent set—establishing that consistent model chasing is not just sufficient but exactly minimax optimal.

## Abstract
We solve exactly a fundamental problem of adaptive control against adversarial disturbances: regulate the scalar system $x_{t+1} = ax_t + u_t + w_t$, $x_0=0$, $\|w\|_\infty \le 1$, where the constant pole $a \in [-Δ, Δ]$ is unknown in sign and magnitude and $Δ$ is arbitrarily large. Elementary as the system looks, the least worst-case peak $\|x\|_\infty$ that a causal controller can guarantee against an adversarial pair $(a, w)$ (the value of this game) has, to our knowledge, never been determined for any adaptive control problem with parametric uncertainty of arbitrary size under this criterion; existing theory supplies stability certificates, gain bounds, and regret rates, not the value. That value is $γ^\star(Δ) = 1 + Δ$ for every $Δ>0$. The summand $1$ is the irreducible price of the disturbance, and $Δ$ the exact price of a single, unavoidable identification spike. The optimal policy is certainty-equivalent deadbeat control at the midpoint of the set-membership consistent interval, an instance of the robust oracle $\times$ consistent model chasing architecture. The architecture is forced, not merely sufficient: writing $θ_t := -u_t/x_t$ exhibits every causal controller as an oracle-selector composition, and optimality pins the selector to the midpoint at the critical histories. The standard tools, classical and modern, each fail quantifiably: probing is punished before it pays, commitment is fatal at sub-disturbance excitation once adaptation is necessary, optimism degenerates to tie-breaking or pays asymptotically at least twice the optimum, and regret certificates are blind to the worst-case peak in both directions. The optimal law contains no exploration mechanism, its learning purely passive. These results give the first exact optimality certificate for consistent model chasing as a design principle for adversarial adaptive control.


## 精读解读（中文）
### 一、研究动机
自适应控制的核心承诺是在未知且可能任意大的参数不确定性下，从第一步起就保证闭环行为。然而，对于对抗性扰动与任意大小参数不确定性并存的最坏情况峰值控制问题，现有理论只能提供稳定性、增益界或遗憾率，从未给出精确的博弈值。本文针对标量系统这一最小非平凡实例，求解其精确最小最大峰值，填补了这一空白。

### 二、技术方案（Method）
考虑标量系统 x_{t+1}=a x_t + u_t + w_t，x0=0，扰动满足 ||w||∞≤1，未知极点 a∈[-Δ,Δ]，Δ可任意大。控制器为任意因果律 u_t=K_t(x_t,...,x0)，目标是最小化最坏情况峰值 ||x||∞。最优策略是维持与观测数据一致（set-membership）的参数区间 A_t，并选择区间中点的确定性等价死拍控制 u_t=-mid(A_t)x_t。该策略属于鲁棒预言机（死拍律）乘以一致性模型追逐（中点选择）的架构，无任何主动探索机制，学习纯被动。证明过程通过写出 θ_t=-u_t/x_t，将任何因果控制器都表示为预言机-选择器组合，进而证明中点选择、被动性等是最优性的必然要求。

### 三、结果（Result）
精确的最小最大值为 γ*(Δ)=1+Δ，对所有 Δ>0 成立，且下确界与上确界均可达到。其中加数1是扰动的不可约代价，Δ是单个不可避免的辨识尖峰的精确代价。标准工具均量化失败：探测在收益前即受罚；承诺型（如先探索后利用）策略在Δ≥1时至少付出两倍最优代价，且在次扰动激励下发散；乐观主义退化为平局或渐近支付至少两倍最优（端点规则支付四倍）；遗憾界对最坏峰值不敏感。

### 四、结论（Conclusion）
该工作首次为一致性模型追逐作为对抗自适应控制的设计原则提供了精确最优性证明。该架构不仅是充分的，而且是强制的：在标量情形下，最坏情况峰值准则的精确解要求一致性区间中点选择与纯被动学习。最优控制器不含任何探索机制，证明被动学习在大不确定性对抗控制中可以是精确最优的。

### 五、方法论与关键技术细节
关键细节包括：系统模型与不确定性集合为区间[-Δ,Δ]，扰动界为1；控制律为区间中点的确定性等价死拍控制；学习通过集合成员一致性被动进行，无探测信号。证明中关键的窗口引理表明状态幅度与存活的参数不确定性在同一个预算下相互交换。局限性是标量情形，高维问题的最优值仍未解决。标准方法失败的具体原因：探测信号会被全不确定性Δ放大一步后才产生信息；承诺固定增益在激励低于扰动时会被对消对手消除辨识；乐观指标在峰值目标下对一致模型无区分度，且选择偏向端点会支付至少两倍最优。
