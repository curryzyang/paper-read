# Parameter-Free Interval-Dynamic Regret under Heavy-Tailed Noise

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Vaneet Aggarwal
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02258v1) · [PDF](https://arxiv.org/pdf/2610.02258v1)

## TLDR
This paper develops a parameter-free online convex optimization learner that achieves interval-dynamic regret guarantees under heavy-tailed noise with unknown finite \(p\)th moments, adapting to comparator complexity and interval length while separating mean-gradient and noise exponents and proving matching logarithmic-cost lower bounds.

## Abstract
We study online convex optimization with one unbiased stochastic subgradient per round and an unknown finite conditional $p$th noise moment, $1<p\le2$. For every fixed interval $I$ of length $n$ and comparator path with $Λ_I=1+P_I/D$, one learner achieves
  \[ E[Regret_I(u)]\le\min(GDn, C[GD\sqrt{n(Λ_I+\log^2(2T))} +σDn^{1/p}(Λ_I+\log^2(2T))^{(p-1)/p}]). \]
  The learner uses none of $G,σ,p,I,P_I$, and the constant is universal. Interval adaptation adds to comparator complexity, preserving the distinct mean-gradient and noise exponents. The analysis controls calibration in expectation and limits the cost of observation-scale changes. Its general theorem compares to distributions over predictably available experts with relative-entropy dependence on a nonuniform prior. A common prior favors long windows and long restart lengths. With the statistics supplied, the interval cost becomes $1+\log(T/n)$, including the optimal full-horizon static rate. A change-of-measure lower bound identifies the noise power of this logarithm for learners retaining a full-horizon optimal guarantee, under explicit conditions. Static comparisons and deterministic partitions follow from the same decisions.


## 精读解读（中文）
### 一、研究动机
研究在线凸优化中评估窗口事后选定、比较器随时间变化且噪声重尾（仅有未知有限 p 阶条件矩，1<p≤2）的场景。全时域保证可能掩盖短窗口内跟踪失败，而未知 G、σ、p、区间和比较器路径长度使区间动态遗憾的参数自由化困难。目标是给出无需调参、对每个固定区间和可比路径均成立的动态遗憾上界，并厘清局部评估的统计代价。

### 二、技术方案（Method）
设定每轮仅收到一个无偏随机次梯度，满足条件矩假设；用区间动态遗憾度量固定区间内与移动比较器的累积损失差。算法维护 N+1 条共享梯度的 AdaGrad 轨迹，按 dyadic 窗口和重启层级构造可预测专家记录 (j,J)，每个专家仅在窗口 J 内活跃并给出对应轨迹预测；使用多速率乘法聚合与有界乘子 F(z)=1+clip(z,-1/2,1/2) 进行在线加权，校准条件期望并由指数检验控制超调。先验 π 把质量偏向长窗口和长重启长度，窗口位置均匀；局部抽取通过尺度变化触发和路径计数器将相对熵复杂度 KL(ν||π) 限制在 O(L^2) 量级，每轮只需 O(log T) 次投影。若 G、σ、p 已知，则将 log^2(2T) 替换为 χ_T(n)=1+log(T/n) 得到更紧界，下界用三元 oracle 和变化测度构造。

### 三、结果（Result）
主要定理给出期望区间动态遗憾不超过 min{GDn, C[GD√(n(Λ_I+log^2(2T))) + σ D n^{1/p}(Λ_I+log^2(2T))^{(p-1)/p}]}，等价于 O(B_I(Λ_I+L^2)) 且被 GDn 截断，其中 L=log(2T)、B_I(q)=GD√(nq)+σD n^{1/p}q^{(p-1)/p}。该界不需要 G、σ、p、I、P_I，区间自适应仅以加法进入比较器复杂度；当 Λ_I≥L^2 时可吸收进给定窗口动态率，p=3/2 时噪声项适应因子为 L^{2/3}，均值梯度项为 L。已知统计量时区间代价变为 1+log(T/n)，并保持全时域静态最优率；变化测度下界说明在要求全时域最优保证时，噪声代价 σD n^{1/p} log(T/n)^ρ 在显式条件下是必要的。

### 四、结论（Conclusion）
论文实现了重尾噪声下参数自由的区间动态遗憾，统一了静态、动态、区间和全时域保证，并分离了学习噪声统计量的额外上界代价与局部评估的统计下界。结果表明长窗口和长重启优先的先验能自然覆盖区间比较，且已知 G、σ、p 时额外代价仅为对数级 χ_T(n)。局限在于假设每轮一个无偏次梯度、均匀条件 p 阶矩、凸闭域和可用投影，且下界在显式条件下成立，常数虽通用但通常较大。

### 五、方法论与关键技术细节
关键细节包括条件矩假设 E[g_t|F_{t-1}]=v_t、||v_t||≤G、E[||ε_t||^p|F_{t-1}]≤σ^p（1<p≤2），遗憾定义中的 P_I=Σ||u_t-u_{t-1}|| 和 Λ_I=1+P_I/D，以及基准 B_I(q)。算法细节为 dyadic 覆盖、每层 AdaGrad 重启轨迹 V_t^{(j)}=Σ_{r=s}^t||g_r||^2、步长 D/√(2V_t^{(j)})、专家先验 π_{(j,J)}=τ_k ζ_{j|k}/m_k（偏向长窗口和长重启），以及 O(log T) 投影每轮。证明细节包括有界乘子的切线超额与对数缺陷界 min{2z^2,|z|}、条件期望校准界 4η^2(DG)^2+4η^p(Dσ)^p、指数检验控制期望超调、观测尺度变化时 T^3b 触发与 2||g_t||/T^2 重置、每阶段 O(L^2) 对数势预算和相对熵 KL(ν||π) 比较。已知统计量时使用 χ_T(n)=1+log(T/n)；下界使用三元 oracle 与零假设对窗口的变化测度；算法不使用函数值，仅用梯度反馈，区间和比较器固定但学习者事先不知道。
