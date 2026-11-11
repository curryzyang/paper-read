# State-constrained optimal control with the theory of functional connections: squared slacks and junction exponents

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Emmanuel Tr{é}lat, Daniele Mortari
- 机构：Texas A&M University, Sorbonne Université
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13047v1) · [PDF](https://arxiv.org/pdf/2611.13047v1)

## TLDR
The paper combines the theory of functional connections with squared-slack substitutions to enforce affine state constraints identically in optimal control, introduces a multiple-arc TFC method with unknown junction times and junction exponents that can represent optimal trajectories exactly with geometric convergence, and benchmarks it against direct collocation and indirect shooting on Bryson–Denham, rendezvous, and shuttle reentry examples.

## Abstract
For optimal control problems with an affine state constraint, we combine the theory of functional connections (TFC), which writes every function satisfying prescribed linear conditions as an explicit expression in terms of a free function, with the squared-slack substitution $b - a^\top x(t) = s(t)^2$. Every trial trajectory then satisfies the endpoint conditions and the path constraint identically. The accuracy depends on the regularity of the slack function at the junctions with a boundary arc. Along an optimal trajectory, the constraint residual vanishes like $(t_1 - t)^m$, where the junction exponent $m$ is equal to the order $p$ of the constraint if and only if the $p$-th derivative of the constraint jumps at the junction, and thus a single polynomial slack converges algebraically. The \emph{multiple-arc TFC method} that we introduce, with unknown junction times and with residuals $(t_1 - t)^m σ(t)^2$ on the free arcs, represents the optimal trajectory exactly and converges geometrically when the arcs are analytic. In a linear-quadratic class, an exact cost identity shows that the cost of every trial trajectory is an upper bound of the optimal cost. We compare both approaches with direct collocation and indirect shooting on the Bryson-Denham problem, on a rendezvous problem with an approach corridor and on the six-dimensional atmospheric reentry of a space shuttle with three state constraints.


## 精读解读（中文）
### 一、研究动机
带仿射状态约束的最优控制广泛存在于航空航天任务中，其最优解常包含未知交会时刻连接的边界弧与自由弧，直接法受离散精度限制且节点间约束不受控，间接法依赖弧结构和好的协态初值。作者希望利用TFC把端点条件与路径约束显式嵌入试探轨迹，并用平方松弛处理不等式，从而同时获得可行轨迹表示、高精度和可分析的收敛性。

### 二、技术方案（Method）
对仿射约束a^T x(t)≤b作适配坐标变换y=b-a^T x≥0并引入平方松弛y=s(t)^2，再用TFC约束表达式构造满足端点条件和路径约束的显式轨迹，自由函数用多项式基展开并由最小二乘/优化确定。单弧TFC在整个时域用一个松弛函数，分析其在边界弧交会处的正则性，证明约束残差按(t1-t)^m消失并定义交会指数m；多弧TFC在未知交会时刻切分时域，边界弧精确满足约束，自由弧采用(t1-t)^m σ(t)^2残差并联合求解未知交会时刻。流程上先用单弧法及松弛阈值粗略定位边界弧数量与交会时刻，再初始化多弧法，并在Bryson-Denham、带接近走廊的交会及航天飞机六维再入算例上与直接配点（IpOpt/CasADi）和间接打靶比较。

### 三、结果（Result）
核心发现是单弧法中多项式松弛对最优松弛的逼近受交会指数控制，最优一致误差约为N^{-m/2}，因而仅代数收敛；若约束在交会处第p阶导数发生跳变，则m=p，否则m>p。提出的多弧TFC在解析弧段上可精确表示最优轨迹并实现几何收敛；在线性二次类中，精确代价恒等式表明每个试探轨迹的代价都是最优代价的上界，且自由弧上的平方残差必须保持非负而不仅是交会处相切。三个算例验证了两种TFC方法与直接配点、间接打靶的对比表现及约束表示能力。

### 四、结论（Conclusion）
将平方松弛与TFC结合可使试探轨迹在构造上满足端点条件和仿射状态约束，其精度关键取决于松弛函数在交会处的正则性，交会指数决定了单弧多项式表示的收敛阶。多弧TFC通过未知交会时刻和带交会指数的残差表示克服单弧法在表示、精度和条件数上的障碍，在解析情形下几何收敛；虽然非线性非LQ情形下试探轨迹不再必然可行、代价上界性质丢失，但仍可精确表示各约束在相邻弧段上的结构，并可由单弧残差形式或直接法/几何分析获得弧结构初值。

### 五、方法论与关键技术细节
关键细节包括：约束阶p与交会指数m满足m≥p，且m=p当且仅当约束沿轨迹的第p阶导数在交会处跳变，最优松弛s=√y表现为(t1-t)^{m/2}的Hölder正则性；适配坐标用a^⊥的正交基Q消去法向，端点条件经Hermite型TFC切换函数处理，活动端点对应s=0且需注意平方参数化在边界处的一阶奇异性和乘子符号的二阶恢复；有限维中给出二阶平稳性与KKT条件的对应引理。实现上自由函数的多项式阶数N、单弧松弛阈值、交会时刻初值以及交会指数候选选择是关键超参/先验，多弧法需预先知道边界弧数量、顺序和指数，非线性情形下试探轨迹不保证可行且失去代价上界，这是主要局限性。
