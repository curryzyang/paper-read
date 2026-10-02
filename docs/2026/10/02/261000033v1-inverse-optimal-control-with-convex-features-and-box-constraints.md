# Inverse Optimal Control with Convex Features and Box Constraints

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Jiguang Yu, Louis Shuo Wang
- 机构：Boston University, Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00033v1) · [PDF](https://arxiv.org/pdf/2610.00033v1)

## TLDR
This paper studies an inverse optimal-control problem for identifying nonnegative weights in a convex-feature lower-level objective with box constraints, proving well-posedness, Lipschitz stability, value-function concavity and exact relaxation, local identifiability and noise stability, and C-stationarity through a KKT/MPCC reformulation.

## Abstract
We study an inverse optimal-control problem for identifying nonnegative weights in a convex-feature lower-level objective. The resulting model is an optimistic bilevel optimal-control problem whose lower level is a strongly convex, linearly constrained control problem with box constraints in \(L^2\). For the reduced response map \(x\mapsto (y_x,u_x)\), we prove global single-valuedness and an explicit Lipschitz estimate, without assuming differentiability of active sets. Exploiting the affine dependence of the lower-level functional on \(x\), we show that the value function is concave and Lipschitz and derive an asymptotically exact optimal-value relaxation. We further establish local identifiability and \(O(δ)\) noise stability by a gradient-free argument based on second-order growth. Finally, a KKT reformulation yields a function-space MPCC; Scholtes relaxation gives C-stationarity under uniform multiplier boundedness. A decoupled scalar example provides an explicit strict-complementarity certificate via finiteness of threshold contacts.


## 精读解读（中文）
### 一、研究动机
在机器人、生物力学和成像等场景中，人们能观测受控系统的最优状态与控制轨迹，却常不知道其目标函数及各项权重，逆最优控制或变分模型参数学习正试图从数据恢复这些权重。该问题本质上是上层数据拟合、下层参数化最优控制嵌套的乐观双层规划，而控制盒约束会导致下层解映射通常非光滑，给存在性、稳定性、可辨识性和最优性条件带来困难。本文针对下层目标为非负凸特征加权和且控制受L2盒约束的结构化实例，研究其适定性、值函数结构、松弛精确性与MPCC稳定性。

### 二、技术方案（Method）
把未知特征权重记为 x∈Xad⊂R^n_+，下层对每个 x 求解 min_{y,u} x·j(y)+σ/2||u||_U^2，约束为线性状态方程 dot y=Ay+Bu、y(0)=y0 与盒约束 u∈Uad={u∈L^2(0,T;R^m): u_a(t)≤u(t)≤u_b(t) a.e.}。利用控制到状态仿射映射 y=Su 将下层约化为仅含控制的 P_red(x): min_{u∈Uad} x·j(Su)+σ/2||u||^2，再研究响应映射 x↦(y_x,u_x)。上层采用 F(x,y,u)=1/2||y-y^obs||^2+β/2||u-u^obs||^2+R(x)，形成乐观双层问题；分析路线包括证明下层强凸适定性并估计响应Lipschitz界，利用x的仿射依赖证明值函数凹性与Lipschitz性，构造渐近精确的值函数ε松弛，并在局部二阶增长条件下给出可辨识性与噪声稳定性；最后将下层替换为KKT系统得到函数空间MPCC，并用Scholtes型松弛证明C-平稳性，另用二次与解耦标量两智能体特例给出严格互补证书。

### 三、结果（Result）
核心结论是：在凸C^2特征、σ>0和盒约束下，每个x对应唯一下层解，约化响应映射全局单值且具有显式Lipschitz估计，无需假设活跃集可微；下层值函数φ在Xad上凹且Lipschitz，j(y_x)为其凹超梯度，值函数松弛在ε↓0时渐近精确，松弛全局极小点沿子列收敛到原双层问题全局极小点。在单射敏感性条件下可得局部可辨识性，在二阶增长条件下噪声观测带来O(δ)稳定性；KKT重构因下层凸而与原问题等价，Scholtes松弛在乘子一致有界时给出C-平稳性。解耦标量例子进一步证明：当耦合权重消失时，阈值接触次数有限，从而严格互补几乎处处成立（对L2法锥），无需非退化条件，尽管活跃弧可正测度。

### 四、结论（Conclusion）
本文为凸特征加权、盒约束下的逆最优控制提供了较完整的理论框架，说明即使下层响应因控制约束而可能非光滑，仍可通过值函数凹性获得精确松弛，并通过函数空间MPCC获得可验证的C-平稳性。其意义在于把逆最优控制或变分参数学习纳入双层最优控制与MPCC理论，并为实际求解提供值函数松弛和Scholtes松弛两类可选路径。局限是通常只能得到C-平稳性而非M-或S-平稳性，约束情形一般没有C^1光滑性，严格互补证书仅对解耦标量特例给出，且结论依赖有界导数、强凸性和乘子一致有界等假设。

### 五、方法论与关键技术细节
技术细节上，状态空间取 Y=H^1(0,T;R^d)、控制空间 U=L^2(0,T;R^m)，盒约束集有界闭凸，故在自反空间中弱序列紧；特征j_l凸、C^2且非负，但非负性仅用于解释，分析真正依赖x≥0下的凸性及 j′ 在 S(Uad) 上有界（M_j<∞）以取得全局Lipschitz常数；σ>0保证下层σ-强凸，上层R在存在性中用弱下半连续、在平稳性中用C^1，β≥0为可选控制跟踪权重。值函数优化利用下层目标对x仿射依赖；噪声稳定性用基于二阶增长的免梯度论证；KKT重构把盒法锥写成逐点几乎处处互补条件，形成函数空间MPCC，Scholtes松弛需乘子一致有界（可由函数空间MPCC-MFCQ推出）才能保证极限C-平稳；标量严格互补证书只要求阈值接触有限，不要求活跃弧有限测度。主要局限包括未假设活跃集可微、一般不能升级到强平稳、理论结果未依赖数值实验指标。
