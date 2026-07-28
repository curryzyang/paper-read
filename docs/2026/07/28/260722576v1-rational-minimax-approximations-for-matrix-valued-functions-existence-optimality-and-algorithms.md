# Rational Minimax Approximations for Matrix-Valued Functions: Existence, Optimality and Algorithms

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Lei-Hong Zhang, Chenkun Zhang
- 机构：Soochow University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22576v1) · [PDF](https://arxiv.org/pdf/2607.22576v1)

## TLDR
This paper generalizes scalar rational minimax approximation to matrix-valued functions with a common denominator, proving existence, establishing Kolmogorov and Ruttan optimality criteria, and linking them to a dual-based algorithm (m-d-Lawson) for certifying and computing minimax approximants.

## Abstract
In this paper, we study rational minimax approximation for continuous complex matrix-valued functions in the Frobenius norm, where all approximant entries share a common denominator. This generalizes classical scalar rational approximation, with applications in system modeling, microwave design, and nonlinear eigenvalue problems. We first prove the existence of such matrix-valued approximants on point sets dense in themselves, extending Walsh's foundational scalar result. Next, we establish characterizations of the local and global minimax approximants by deriving primal/dual matrix-valued Kolmogorov criteria and a Ruttan-type sufficient condition for global optimality. For analytic functions on a continuum, we link continuum minimax approximation to approximation on its boundary, and finite boundary samples via the maximum norm principle. We show that Ruttan's sufficient optimality condition provides a certificate under which a minimax approximant obtained from the boundary or from a discrete set of boundary nodes also solves the original continuum problem. Finally, for discrete approximation, we connect these conditions to a dual problem and the related dual-based numerical method m-d-Lawson: when the original minimax problem admits a solution, strong duality is equivalent to Ruttan's sufficient optimality condition, and, the optimality equations underlying the m-d-Lawson iteration coincide with Kolmogorov's dual criteria. These results provide a theoretical basis for certifying and computing matrix-valued rational minimax approximants.


## 精读解读（中文）
### 一、研究动机
矩阵值有理极小极大逼近在系统建模、微波设计和非线性特征值问题等场景中具有重要应用，但现有理论（如Walsh存在性定理、Kolmogorov最优性条件）主要针对标量函数，缺乏针对矩阵值函数且所有逼近项共享共同分母情形的系统研究。本文旨在建立该类逼近问题的存在性、最优性条件与数值算法的理论基础。

### 二、技术方案（Method）
论文针对定义在紧致自密集上的连续复矩阵值函数，采用所有条目共享共同分母的有理函数形式，在Frobenius范数下极小化最大逼近误差。首先，通过扩展Walsh的标量存在性证明，引入归一化分母处理，证明了矩阵值有理极小极大逼近的存在性。其次，推导了矩阵值Kolmogorov原始-对偶准则和Ruttan型充分全局最优性条件。对于解析函数，利用最大Frobenius范数原理将连续域上的逼近问题等价转换为边界或边界离散点上的问题，并证明了Ruttan条件是保证离散解同样适用于连续问题的证书。最后，对于离散逼近，建立了与对偶问题的联系，并分析了m-d-Lawson迭代方法，证明其强对偶性等价于Ruttan条件，且迭代的最优性方程对应于Kolmogorov对偶准则。

### 三、结果（Result）
论文证明了矩阵值有理极小极大逼近在自密集上的存在性，这是Walsh标量结果的自然推广。建立了局部和全局最优性的Kolmogorov型准则与Ruttan型充分条件。在解析函数情形下，揭示了连续、边界与离散逼近之间的等价性：当Ruttan条件满足时，边界或边界样本上的极小极大逼近也是原连续问题的最优解。对于离散问题，给出了强对偶性与Ruttan条件等价的理论结果，并将m-d-Lawson迭代解释为对Kolmogorov对偶准则的数值实现。这些结果为矩阵值有理极小极大逼近的认证与计算提供了完整的理论基础。

### 四、结论（Conclusion）
本文系统建立了矩阵值有理极小极大逼近的理论框架，包括存在性、最优性条件、连续-离散关系及数值算法基础。成果可直接用于指导实际应用中的逼近器构造与最优性验证，并为开发高效数值方法提供了理论支撑。

### 五、方法论与关键技术细节
关键细节包括：逼近误差采用Frobenius范数的平方度量；要求定义集是自密集（无孤立点）以保证存在性；对于解析函数，利用最大范数原理将问题域缩小至边界；离散逼近假设样本数m至少为max_{i,j}(n_{ij}+d+2)，以确保解的唯一性或收敛性；理论依赖共享分母结构，各条目次数可不同；Ruttan条件作为充分性证书避免了对全局搜索的依赖；m-d-Lawson方法基于对偶加权迭代，其合理性由强对偶性保证；未讨论分母极点的位置约束或数值稳定性等局限性。
