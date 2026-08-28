# Stability Analysis and Data-driven Verification via Recurrent Lyapunov Functions

- 区域：精读区
- 排名：1
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Roy Siegelmann, Fernando Paganini, Enrique Mallada
- 机构：Johns Hopkins University, Universidad ORT Uruguay, Massachusetts Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26447v1) · [PDF](https://arxiv.org/pdf/2608.26447v1)

## TLDR
This paper introduces Recurrent Lyapunov Functions that relax the invariance condition of sub-level sets to recurrence, proving stability guarantees and norm-based converse theorems, along with GPU-based, trajectory-only verification algorithms that certify practical stability with logarithmic sample complexity.

## Abstract
Lyapunov's direct method is a cornerstone of stability and control, but it hinges on finding a Lyapunov function, a task demanding ingenuity or computation. A key difficulty is that every sub-level set of the function must be forward invariant, coupling its geometry to the system's trajectories. We relax this by replacing invariance with recurrence: a set is recurrent if every trajectory starting in it returns within a finite time. This yields the notion of a Recurrent Lyapunov Function (RLF), whose sub-level sets need only be recurrent. We show that, under mild conditions, RLFs guarantee stability, and we introduce stronger notions yielding asymptotic and exponential stability. We also give norm-based converse theorems: under the corresponding stability conditions, any norm is an RLF for their practical versions. We then develop GPU-based algorithms that certify (practical) stability from trajectory data alone, without a Lyapunov function. Certifying stability up to an $\varepsilon$-neighborhood needs only $O(\log(1/\varepsilon))$ trajectory evaluations, with constants growing as the certified decay rate nears the true one, exposing an intrinsic performance-cost trade-off.


## 精读解读（中文）
### 一、研究动机
传统Lyapunov直接法要求每个子水平集必须正向不变，这使函数几何与系统轨迹紧密耦合，导致Lyapunov函数构造困难。本文用回归性（recurrence）替代不变性，即每个从集合内出发的轨迹在有限时间内返回该集合，从而放松了这一关键约束，并支持仅从轨迹数据验证稳定性。

### 二、技术方案（Method）
引入Recurrent Lyapunov Function (RLF)，其子水平集只需满足回归性而非正向不变性。在局部Lipschitz向量场假设下，给出保证稳定、渐近稳定和指数稳定的RLF条件，并证明在相应稳定条件下任意范数都满足实用（ε-松弛）RLF条件。开发两个GPU并行化算法：一个在固定区域内搜索最佳衰减率，另一个在目标衰减率下增长吸引域，通过轨迹数据直接验证实用指数稳定性，全程无需显式构造Lyapunov函数；验证依赖单边Lipschitz常数、弱配对等工具。

### 三、结果（Result）
核心结果是样本复杂度：在B_R \ B_ε上验证实用指数稳定性仅需O(log(1/ε))次轨迹评估，且常数随认证衰减率接近真实衰减率而增长，揭示性能-成本权衡。与Boffi等人的Ω(ε^{-2d})样本复杂度相比，ε依赖性从多项式降为对数，但代价是常数M编码了系统指数速率λ与认证速率α之间的差距(λ-α)。

### 四、结论（Conclusion）
RLF通过以回归性代替不变性，解耦了水平集几何与向量场的瞬时对齐，仍能保证稳定、渐近稳定和指数稳定；范数逆定理表明任意范数在实用意义下都是RLF，因此无需计算Lyapunov函数即可实现基于轨迹数据的稳定性认证，并提供了可并行、可扩展的GPU验证框架。

### 五、方法论与关键技术细节
关键细节包括：系统需满足局部Lipschitz假设；RLF条件可定义在包含平衡点的任意紧集而非仅子水平集；逆定理给出的是实用（ε-松弛）版本，因此只保证实用渐近/指数稳定；样本复杂度上界为O(M^d log(R/ε))，其中d是状态维数，M与(λ-α)有关，当认证速率接近真实速率时轨迹评估需求增加；两个GPU算法分别用于固定区域最佳衰减率和目标速率下最大吸引域估计，并已通过数值实验验证；与Karafyllis等人工作相比，本文聚焦回归性联系与可并行算法，而非鲁棒稳定性的Matrosov型条件。
