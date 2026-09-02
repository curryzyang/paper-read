# An Inexact Augmented Lagrangian Method for $(L_0, L_1)$-Smooth Convex Optimization

- 区域：精读区
- 排名：6
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Aleksandr Vyguzov, Fedor Stonyakin
- 机构：Moscow Institute of Physics and Technology, Adyghe State University, Innopolis University, V. I. Vernadsky Crimean Federal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00261v1) · [PDF](https://arxiv.org/pdf/2609.00261v1)

## TLDR
TLDR: The paper develops an inexact augmented Lagrangian method for linearly constrained convex optimization with $(L_0,L_1)$-smooth objectives, showing that the subproblems preserve this generalized smooth structure and combining it with a two-stage clipped-gradient/accelerated scheme to achieve $\mathcal{O}(K/\varepsilon)+\mathcal{O}(K)$ ergodic convergence.

## Abstract
Augmented Lagrangian methods are among the most effective approaches for solving constrained convex optimization problems. However, classical complexity analyses of first-order methods applied within the augmented Lagrangian framework usually rely on the assumption that the objective function has a Lipschitz continuous gradient. This assumption excludes an important class of generalized smooth functions whose gradients may grow unboundedly.
  In this paper, we study an inexact augmented Lagrangian method for solving linearly constrained convex optimization problems with $(L_0,L_1)$-smooth objective functions. We show that the augmented Lagrangian subproblems preserve the $(L_0,L_1)$-smooth structure, with parameters depending on the penalty coefficient. This property allows us to employ recent accelerated first-order schemes designed for generalized smooth optimization instead of classical smooth optimization methods. In particular, we combine the inexact augmented Lagrangian framework with a two-stage acceleration procedure based on clipped gradient descent and accelerated optimization.


## 精读解读（中文）
### 一、研究动机
经典增广拉格朗日方法的一阶复杂度分析通常假设目标函数具有Lipschitz连续梯度，但该假设排除了梯度可能无界增长的广义光滑函数类。实际中许多重要损失（如指数损失、logistic损失、范数函数）仅满足(L0,L1)-光滑条件，因此需要将不精确增广拉格朗日方法推广到这类更一般的凸优化问题。

### 二、技术方案（Method）
本文针对线性约束凸优化问题 min f(x) s.t. Ax=b，在f为凸(L0,L1)-光滑函数的假设下，采用不精确增广拉格朗日方法（iALM）。外循环每次生成增广拉格朗日子问题 L_β_k(x,y^k)，允许以可控精度ε_k近似求解，随后按 y^{k+1}=y^k+β_k(Ax^{k+1}-b) 更新对偶变量；内循环使用两阶段加速过程求解子问题：先用裁剪梯度下降（步长可取三种形式之一）使函数次优性降至 L0/(5L1^2)，此时目标退化为有效2L0-光滑，再切换至AGMsDR加速算法以达到ε_k精度。参数选取为 β_k=ρ_k=Cβ/(Kε)，并要求累积精度满足 Σ ρ_k ε_k ≤ Cε/2。

### 三、结果（Result）
证明了增广拉格朗日子问题保持(L0,L1)-光滑结构，且其L0参数随惩罚系数β_k增加而增大。基于iALM的遍历收敛分析，得到目标误差和可行性误差的复杂度为 O(K/ε)+O(K)，其中K为外迭代次数；同时表明常数惩罚参数序列在迭代次数意义下最优，但为缓解病态性可选择递增序列如 β_{k+1}=β_g σ^k。

### 四、结论（Conclusion）
本文首次将不精确增广拉格朗日框架与针对(L0,L1)-光滑函数设计的加速一阶方法结合，解决了经典L-光滑假设无法覆盖的广义光滑线性约束凸优化问题，给出了可证明的遍历收敛率，拓展了增广拉格朗日方法的适用性和理论边界。

### 五、方法论与关键技术细节
关键点包括：(L0,L1)-光滑定义为 ||∇²f(x)|| ≤ L0+L1||∇f(x)||，当L1=0时退化为经典L-光滑；裁剪梯度下降步长备选 η_k^cl = min{1/(2L0), 1/(3L1||∇f||)} 等；两阶段切换条件为 f(x)-f* ≤ L0/(5L1^2)，之后函数表现为2L0-光滑；外层复杂度依赖 K 和精度 ε，总内迭代复杂度为 O(K/ε)+O(K)；假设KKT点存在且每步子问题可解；常数β策略虽迭代最优但可能导致子问题病态，递增β可在复杂度和数值稳定性间权衡。
