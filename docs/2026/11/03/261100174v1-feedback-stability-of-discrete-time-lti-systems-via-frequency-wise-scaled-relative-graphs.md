# Feedback Stability of Discrete-Time LTI Systems via Frequency-Wise Scaled Relative Graphs

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Guoming Shi, Eder Baron-Prada, Fredy Ruiz
- 机构：Austrian Institute of Technology, Politecnico di Milano
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00174v1) · [PDF](https://arxiv.org/pdf/2611.00174v1)

## TLDR
The paper develops a frequency-wise scaled-relative-graph condition that certifies well-posedness and ℓ₂-stability of negative-feedback interconnections of stable discrete-time LTI SISO/MIMO systems without requiring the chord property or nonsingular frequency-response matrices, and shows it is less conservative than an operator-level SRG condition.

## Abstract
This paper studies the stability of negative-feedback interconnections of proper, stable discrete-time multivariable linear time-invariant (LTI) systems using scaled relative graphs (SRGs). We propose a frequency-wise condition that compares the SRGs of the two subsystems'frequency-response matrices only at the same frequency along a feedback-scaling homotopy. We prove that this condition guarantees well-posedness along the homotopy and $\ell_2$-stability for both single-input single-output (SISO) and multi-input multi-output (MIMO) subsystems, without requiring the chord property or nonsingular frequency-response matrices. An equivalent form exchanges scaling and geometric inversion. We also derive an operator-level condition from the SRG closures of the convolution operators and show that it implies the frequency-wise condition. Numerical examples show that the operator-level condition is more conservative because it depends on intersections between responses at different frequencies.


## 精读解读（中文）
### 一、研究动机
连续时间LTI系统已有基于SRG的频率逐点反馈稳定性条件，但离散时间SRG研究主要集中于计算，缺乏面向离散时间反馈互联的稳定性判据；同时数据驱动控制中常需在模型不精确时认证闭环稳定性，而离散时间LTI系统的SRG可由输入输出数据计算，因此需要建立离散时间频率逐点SRG稳定性条件作为数据驱动控制器分析的基础。

### 二、技术方案（Method）
针对两个proper、稳定的离散时间多变量LTI子系统H1和H2构成的负反馈互联，提出对每个频率θ∈[0,π]及同伦参数τ∈(0,1]检验SRG(H1(e^{jθ}))^{-1}与-τSRG(H2(e^{jθ}))不相交的频率逐点条件；通过反馈缩放同伦将H2替换为τH2，证明该条件保证同伦路径上的适定性和ℓ2稳定性，并给出交换缩放与几何逆的等价形式，即τSRG(H1(e^{jθ}))与-SRG(H2(e^{jθ}))^{-1}不相交。进一步从卷积算子的SRG闭包构造算子级条件，并证明其蕴含频率逐点条件；矩阵SRG通过Beltrami–Klein变换将频率响应矩阵映射到数值范围后计算。

### 三、结果（Result）
理论结果表明，所提频率逐点条件对SISO和MIMO离散时间LTI反馈系统均能保证同伦适定性与ℓ2稳定性，且不要求弦性质或频率响应矩阵非奇异；等价形式表明缩放与SRG集合的几何逆可交换，无需构造逆子系统。数值算例显示算子级条件蕴含但比频率逐点条件更保守，其原因在于算子级条件依赖不同频率响应之间的交集。

### 四、结论（Conclusion）
论文为proper、稳定离散时间LTI反馈互联建立了一套频率逐点SRG稳定性判据，扩展了SRG频率域稳定性分析到离散时间情形，并为后续数据驱动控制器的闭环稳定性认证提供了理论基础；相较算子级SRG闭包条件，频率逐点条件保守性更低，但当前框架仍限定于稳定、proper的子系统。

### 五、方法论与关键技术细节
关键假设是H1、H2属于离散时间proper、实有理、稳定传递矩阵集合，频率只需检查[0,π]，并利用实系数带来的共轭对称性；同伦适定性对应直接项满足det(I+τD1D2)≠0。SRG矩阵计算依赖Beltrami–Klein映射f_bk及数值范围，几何逆按z↦1/z̄作用于SRG集合而非构造逆系统，因此可处理严格proper系统。主要局限包括：条件不直接覆盖不稳定、非proper或无界子系统，含未抵消积分器的情形需环路变换或更一般框架；算子级条件因跨频率响应交集而更保守。
