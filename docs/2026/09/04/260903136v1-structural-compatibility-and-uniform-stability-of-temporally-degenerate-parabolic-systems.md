# Structural Compatibility and Uniform Stability of Temporally Degenerate Parabolic Systems

- 区域：精读区
- 排名：1
- 匹配度：5.7/10
- 来源：arxiv
- 作者：Amadou Cissé
- 机构：University of Lorraine
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03136v1) · [PDF](https://arxiv.org/pdf/2609.03136v1)

## TLDR
Temporally degenerate parabolic systems admit well-posed feedback interconnections only under an operator compatibility condition linking the singular reaction operator to the actuator and observation operators, which enables regularization, uniform exponential stability certification, and constructive static output feedback synthesis.

## Abstract
Modern feedback design for distributed parameter systems presupposes that the closed-loop dynamics define a well-posed evolution problem. This presupposition becomes nontrivial for temporally degenerate parabolic systems, where temporal degeneracy affects not only the analytical properties of the evolution equation but also the mathematical formulation of the feedback interconnection itself. It is shown that admissible feedback interconnections for temporally degenerate parabolic systems are completely characterized by an operator compatibility condition linking the singular reaction operator with the actuator and observation operators. This characterization removes the singular component of the closed-loop dynamics and reduces the degenerate evolution equation to a regular evolution equation. Building upon this regularized formulation, a critical--residual decomposition yields a uniform exponential stability certificate, which is subsequently extended to the original infinite-dimensional evolution through a finite-to-infinite lifting theorem. A constructive static output feedback synthesis is finally obtained as a consequence of these results. Numerical experiments illustrate the regularization mechanism, validate the stability certificate, and confirm the finite-to-infinite lifting.


## 精读解读（中文）
### 一、研究动机
现代分布参数系统反馈设计默认闭环动力学是良定的，但时间退化抛物系统中乘在时间导数前的系数 α(t) 在 t=0 处退化，使得反馈互连本身的良定性不再平凡。强退化使 1/α 不可积，闭环方程出现无法视为有界摄动的奇异反应项；因此必须首先刻画什么样的反馈连接在结构上是可容许的，之后才能讨论镇定与综合问题。

### 二、技术方案（Method）
以希尔伯特空间 X 上的抽象发展方程 α(t)ż+β(t)A0z+A1z+α(t)Arz=Bu、y=Cz 为对象，状态空间为 X，控制与观测空间分别为 R^m 与 R^p；α(0)=0 且 1/α 非可积，β/α 有界。采用静态输出反馈 u=(K0+α(t)K1)y，代入并除以 α(t)，得到含奇异项 (1/α)(A1-BK0C)z 的闭环方程。利用迹障碍引理证明：若该奇异系统对稠密初值存在 W^{1,1} 正则解，则必须满足算子相容条件 A1=BK0C；据此选择 K0 消去奇异项，得到正则化闭环方程 ż+d(t)A0z+(Ar-BK1C)z=0。随后对 A0 作谱临界-残差分解：有限维临界子空间用 K1 镇定，残差子空间利用抛物耗散估计处理，最后通过有限到无限提升定理将有限维稳定性提升到原无穷维系统，给出静态输出反馈 K0、K1 的构造步骤。

### 三、结果（Result）
核心定理表明，时间退化抛物系统容许反馈连接的充要条件是算子相容条件 A1-BK0C=0，即反馈增益 K0 必须使 B K0 C 精确重构奇异反应算子 A1；不满足该条件时不存在对稠密初值良定的正则化闭环。满足相容条件后，退化闭环可化为正则发展方程，临界-残差分解给出一致指数稳定性证书，有限到无限提升定理保证该稳定性可推广到原无穷维系统。数值实验验证了正则化机制、稳定性证书以及有限到无限提升结论的有效性。

### 四、结论（Conclusion）
时间退化首先对反馈连接施加结构约束，而不是一个普通的稳定性问题。只有满足 A1=BK0C 的反馈才能消去奇异分量并使闭环进入经典无穷维控制框架；在该前提下，利用抛物算子的临界-残差分解可以实现一致指数稳定并构造静态输出反馈。该结果将退化系统控制设计转化为先验证算子相容性、再做有限维镇定与无穷维提升的清晰步骤。

### 五、方法论与关键技术细节
关键设定包括 X=L2(Ω)、A0=-a²Δ、D(A0)=H2(Ω)∩H0¹(Ω) 及 Dirichlet 边界条件；A0 自伴、严格正且具有紧预解式。强退化条件为 ∫0δ dt/α(t)=∞，且存在常数 0<d−≤β/α≤d+。相容条件 A1=BK0C 是算子等式，意味着 A1 必须能被 B、C 和 K0 因子化；若该等式不可满足，则不存在对稠密初值良定的正则化闭环，这是主要局限性。稳定性证书依赖于 A0 谱投影给出的临界-残差分解，并需要对残差子空间建立一致衰减估计；有限到无限提升定理利用残差部分的抛物耗散控制无穷维耦合。数值验证应对比满足与不满足相容条件时的闭环轨迹，并检查提升定理给出的一致指数衰减上界。
