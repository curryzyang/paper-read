# First-order Optimization Methods with Generalized Smoothness for Low-rank Matrix Factorization

- 区域：精读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：A. V. Bidanets, F. S. Stonyakin
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19059v1) · [PDF](https://arxiv.org/pdf/2610.19059v1)

## TLDR
This paper proves generalized smoothness with exponent 2/3 for Burer–Monteiro low-rank matrix factorization under relaxed assumptions and uses it to develop adaptive gradient, SafeAdam, and certified projected first-order methods with global convergence and improved complexity rates, matching or outperforming Dyn-NoLips on SymNMF benchmarks without kernel tuning.

## Abstract
This paper studies several first-order methods for low-rank matrix minimization in the Burer--Monteiro form, where the target matrix is represented as the product of a nonnegative factor matrix and its transpose. Such a factorization destroys convexity of the objective function and global Lipschitz continuity of the gradient. We prove that for a quadratic objective function that is strongly convex only on the subspace of symmetric matrices, the Burer-Monteiro factorized objective possesses generalized smoothness with a fractional exponent 2/3. For a quadratic objective, the generalized smoothness property requires positive definiteness of the operator A only on the subspace of symmetric matrices, which relaxes the assumptions of Dragomir et al. On this basis, three methods are proposed: an adaptive gradient descent method with Armijo backtracking; an unconstrained SafeAdam method combining the Adam direction with a descent-angle certificate and a fallback to the normalized gradient; and a certified projected version for the nonnegativity constraint. Global convergence and explicit convergence rates for the proposed methods have been proved. The obtained convergence rate is better than the convergence rate of ordinary unaccelerated gradient descent in the case of a sufficiently large gradient. In the small-gradient regime, the convergence guarantee is of square-root type, and the corresponding complexity scales as the inverse square of the desired accuracy. In the large-gradient regime, the convergence guarantee is of three-quarters type, and the corresponding complexity is proportional to the inverse of the accuracy raised to the power of 4/3. Experiments on SymNMF using the TDT2, Reuters and CBCL datasets, which are standard benchmarks for document and image clustering, show that the methods match or outperform Dyn-NoLips without tuning the relative-smoothness kernel parameters.


## 精读解读（中文）
### 一、研究动机
低秩矩阵分解常写为Burer-Monteiro形式 X≈HH^T，但该分解破坏目标凸性与梯度全局Lipschitz连续性，导致经典一阶优化收敛分析失效。本文旨在为仅在有对称矩阵子空间上强凸的二次目标建立广义光滑性，并设计无需精细调参的一阶方法。

### 二、技术方案（Method）
研究对象为二次目标下的对称非负矩阵分解（SymNMF），输入为相似度/核矩阵A，建模为 A≈HH^T，H为非负因子矩阵。作者证明BM分解后的目标具有指数为2/3的广义光滑性，仅要求算子A在对称矩阵子空间上正定，从而放松Dragomir等条件。据此提出三类算法：带Armijo回溯的自适应梯度下降；结合Adam方向、下降角证书与归一化梯度回退的无约束SafeAdam；以及面向非负约束的带证书投影版本。优化流程为迭代更新H，使用回溯/证书判断步长或方向安全性，必要时切换为归一化梯度或投影以保持下降与可行性。

### 三、结果（Result）
理论上获得全局收敛性与显式收敛率：梯度较大时优于普通未加速梯度下降；小梯度区域为平方根型保证，复杂度随目标精度ε反平方即O(ε^-2)；大梯度区域为三分之四型保证，复杂度为O(ε^-4/3)。在TDT2、Reuters和CBCL三个文档/图像聚类标准基准上的SymNMF实验表明，所提方法在未调相对光滑核参数的情况下达到或超过Dyn-NoLips。

### 四、结论（Conclusion）
作者表明，利用二次目标在对称子空间上的强凸性即可建立2/3指数广义光滑性，并据此得到可证明收敛且实际表现有竞争力的一阶优化框架。该框架统一处理无约束与带非负约束的BM低秩分解，并在标准聚类基准上验证了无需调核参数的优势。

### 五、方法论与关键技术细节
关键细节包括：目标为二次型，仅要求算子A在对称矩阵子空间上正定；BM因子化为X=HH^T且H非负；广义光滑指数为2/3；算法含Armijo回溯、Adam方向、下降角证书、归一化梯度回退与投影操作。复杂度方面，小梯度域O(ε^-2)，大梯度域O(ε^-4/3)，优于普通未加速GD的条件是梯度足够大。实验使用TDT2、Reuters、CBCL三个SymNMF基准，且不调相对光滑核参数。局限是理论主要针对二次目标与对称BM形式，非负约束需投影版本，非凸分解的全局最优性仍受初始化与问题结构影响。
