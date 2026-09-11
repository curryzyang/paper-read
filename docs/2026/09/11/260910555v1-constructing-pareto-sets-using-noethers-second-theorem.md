# Constructing Pareto Sets Using Noether's Second Theorem

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Evgeny Nikulchev
- 机构：MIREA -- Russian Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10555v1) · [PDF](https://arxiv.org/pdf/2609.10555v1)

## TLDR
This paper uses Noether’s second theorem to show that gauge symmetries of a multiobjective variational control system determine the Pareto set as a conservation law, enabling analytical construction and dimension reduction via gauge regularization, with numerical examples for an LQR problem and ZDT1.

## Abstract
This paper presents an analytical approach to constructing the Pareto set in multiobjective variational control problems, based on Noether's second theorem. A fundamental connection is established between the gauge symmetries of the dynamical system describing the plant and the structure of the Pareto set. It is shown that the Pareto front can be interpreted as a conservation law arising from the invariance of the system and the quality criteria with respect to a symmetry group. A gauge regularization concept is proposed, which allows eliminating variables that do not affect the criteria without changing the Pareto set, thereby reducing the dimension of the solution space. Numerical examples are provided for the linear-quadratic regulator with two conflicting criteria and for the standard ZDT1 test problem.


## 精读解读（中文）
### 一、研究动机
多目标控制与设计问题需要同时优化多个冲突指标，Pareto集搜索常受解空间高维、约束和系统对称性影响，传统数值方法效率有限。作者提出以Noether第二定理为基础，把系统规范对称性与Pareto前沿结构联系起来，从而解析构造并降维Pareto集。

### 二、技术方案（Method）
将对象描述为 dx=f(x,u) 的动力系统，并在其解空间上定义k个泛函 J_i=∫L_i(x,u,u_(1),...,u_(r))dt，要求系统与各准则对同一规范Lie群G不变。利用Pareto最优的广义KKT条件 Σλ_iE_i(L_i)=0 和Noether第二定理给出的Bianchi恒等式，约束并消去权重λ_i，导出与权重无关的前沿方程Φ(J_1,...,J_k)=0。规范变量可通过惩罚项 μΣz_j^2 固定而不改变Pareto集；LQR例子用Riccati方程逐λ求解，ZDT1用于标准测试对比。

### 三、结果（Result）
核心发现是Pareto前沿可解释为由系统对称性产生的守恒律，权重可由对称性解析导出而非经验选择；规范正则化可删除不影响准则的变量并降低解空间维度。标量LQR中由守恒律得到 J1=λJ2，与Riccati解析解一致，并在λ∈[0.01,10]对数尺度上给出50个前沿点；三维LQR也通过Riccati方程构造前沿，ZDT1与已发表精度数据进行了比较。

### 四、结论（Conclusion）
该工作把Noether第二定理引入多目标变分控制，给出解析构造Pareto集的框架，并可与现代Pareto前沿算法结合以提升可靠性和降维能力。结论强调Pareto前沿并非任意折中，而是系统与准则共同对称性的不变量；当对称性不足或仅正则部分可解析时，仍需结合数值方法。

### 五、方法论与关键技术细节
关键点包括：输入为状态方程、积分型/二次型准则及规范Lie群；核心对象为变分导数E_i(L_i)、加权Euler-Lagrange方程 Σλ_iE_i(L_i)=0、Bianchi恒等式和前沿方程Φ(J)=0。主要假设是各准则在同一解空间上对同一规范群不变，λ_i≥0且正则点满足KKT；惩罚参数μ仅作规范固定，可任取如μ=1。局限在于结果主要覆盖具有规范对称性的系统与Pareto集正则部分，ZDT1等非控制问题需按标准测试验证，证明细节依赖Noether第二定理的标准框架。
