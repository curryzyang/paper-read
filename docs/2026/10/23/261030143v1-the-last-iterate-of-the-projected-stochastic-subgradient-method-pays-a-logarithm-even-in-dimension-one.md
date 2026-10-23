# The Last Iterate of the Projected Stochastic Subgradient Method Pays a Logarithm, Even in Dimension One

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Guglielmo Beretta, Tommaso Cesari, Roberto Colomboni
- 机构：University of Ottawa, University of Bristol, Aarhus University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30143v1) · [PDF](https://arxiv.org/pdf/2610.30143v1)

## TLDR
The paper proves that the projected stochastic subgradient method with standard anytime stepsizes \(\eta_t=\gamma/\sqrt t\) can incur expected last-iterate error of order \((\log n)/\sqrt n\) even in one dimension, establishing this as the sharp worst-case rate.

## Abstract
We prove that the projected stochastic subgradient method with the standard anytime stepsizes $η_t = γ/\sqrt t$ can suffer expected last-iterate optimization error of order $(\log n)/\sqrt n$ already on the real line. Combined with the classical in-expectation upper bound, this establishes the sharp worst-case order of the projected stochastic subgradient method.


## 精读解读（中文）
### 一、研究动机
投影随机次梯度方法在条件无偏且二阶矩有界的随机一阶 oracle 下，使用 anytime 步长 η_t=γ/√t 时，last iterate 的期望优化误差已知有 O(log n/√n) 上界，但该上界是否最坏情形紧、对数因子是否必要尚不明确。本文旨在证明该上界在实数轴一维情形已经紧，从而确定算法的尖锐最坏阶，并辨析对数损失来自 anytime 步长调度而非噪声假设。

### 二、技术方案（Method）
对任意 b,γ>0 和 n≥2，构造一维凸目标 f(x)=ε|x|（唯一极小点 0、ε-Lipschitz）及次梯度选择 g(x)=ε sign(x)（g(0)=0），噪声取 W_t=(b-ε)ξ_t，其中 ξ_t 为 i.i.d. Rademacher，更新为 X_{t+1}=X_t-(γ/√t)(g(X_t)+W_t)，X_1=0。展开第 n 步迭代，用三角不等式控制 g 项，并用 Khintchine-Szarek 不等式估计 μ=E|Σ_{t=1}^{n-1}ξ_t/√t|，再选取 ε=(b/2)μ/(μ+s)，s=Σ_{t=1}^{n-1}1/√t，最后用调和和与积分估计把下界化为对数除以根号 n 的形式。

### 三、结果（Result）
证明对每个 b,γ>0 和 n≥2，存在满足 f 的 Lipschitz 常数≤b/2、噪声为幅度≤b 的 i.i.d. 缩放 Rademacher 的实例，使随机次梯度 g(X_t)+W_t 一致有界于 b，且第 n 次迭代满足 E[f(X_n)-min f]≥(γb²/24)(log n/√n)。这与经典期望上界 O(log n/√n) 合并，得到投影随机次梯度方法在最坏情形下的精确阶 Θ(log n/√n)，即使在一维也成立。

### 四、结论（Conclusion）
投影随机次梯度方法的 anytime 步长 η_t=γ/√t 的 last-iterate 最坏期望误差确实为 Θ(log n/√n)，经典上界不可去掉对数因子。该下界在加性、状态无关、一致有界 i.i.d. 噪声这一良性设置下已出现，说明对数损失可归因于 anytime 步长调度本身；相较之下，固定时域常数步长 γ/√n 在一维同类噪声下可达到 O(n^{-1/2})，无对数因子。

### 五、方法论与关键技术细节
关键构造是 f(x)=ε|x| 与 W_t=(b-ε)ξ_t，且 ε 依 n、b 和 μ,s 选取，保证 0<ε<b/2 并平衡噪声主导项与次梯度累积项。证明使用 Khintchine-Szarek 不等式得到 μ²≥h/2、μ≤√h（h=Σ_{t=1}^{n-1}1/t），并用 h≥log n、s≤2√n、h≤n 推出常数 1/24；核心限制是结论针对期望 last iterate、一维构造和加性状态无关有界 i.i.d. 缩放 Rademacher 噪声，且 Lipschitz 上界 b/2 与噪声幅度 b 分别设定。
