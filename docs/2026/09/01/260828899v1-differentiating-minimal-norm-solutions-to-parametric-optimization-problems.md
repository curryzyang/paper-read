# Differentiating Minimal-Norm Solutions to Parametric Optimization Problems

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Baptiste Plaquevent-Jourdain, Jalal Fadili, Antonio Silveti-Falls
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28899v1) · [PDF](https://arxiv.org/pdf/2608.28899v1)

## TLDR
The paper extends implicit differentiation of parametric optimization problems to ill-posed settings with multiple solutions by relaxing the implicit function theorem's invertibility condition to a uniform range condition, using limiting Tikhonov regularization and conservative set-valued field theory to justify pseudoinverse-based generalized derivatives for minimal-norm solution mappings, with applications to nonsmooth composite problems like Least-Squares, Huber regression, and LASSO.

## Abstract
Differentiating through parametric optimization problems is central to bilevel programming and meta-learning, often accomplished using approximate implicit differentiation. The implicit function theorem requires inverting a partial Jacobian of the optimality condition, which fails when there are many solutions. Nonetheless, in such cases it is possible to relax invertibility to a strictly weaker uniform range condition, under which it is shown that the minimal-norm solution mapping admits generalized derivatives by using a limiting Tikhonov regularization argument and conservative set-valued field theory. With additional control on the eigenvalues of the generalized Hessians, a pseudoinverse formula is justified. This is established for a class of smooth convex objectives and extended to nonsmooth composite problems. These assumptions are verified for Least-Squares, Huber regression and LASSO. The resulting extension of nonsmooth implicit differentiation to ill-posed settings is examined experimentally on data poisoning and data hypercleaning problems.


## 精读解读（中文）
### 一、研究动机
在双层优化与元学习中，常需对参数化优化问题求导，现有方法多依赖近似隐式微分。隐函数定理要求最优性条件的偏雅可比矩阵可逆，当问题存在多个解时这一条件失效，导致梯度无法定义。本文旨在解决多解（病态）情形下最小范数解映射的求导问题。

### 二、技术方案（Method）
以参数化优化问题的最小范数解映射为求导对象，其中外层参数为输入，内层目标为光滑凸函数（复合情形为光滑损失加非光滑正则）。建模上放弃偏雅可比矩阵的可逆性假设，改设更弱的均匀值域条件；通过引入极限Tikhonov正则化项使内层解唯一化，再利用保守集值场论对正则化解映射取正则参数趋于零的极限，从而得到最小范数解的广义导数；当广义Hessian特征值可控时，进一步推导出伪逆公式作为可计算的导数形式。整体流程为：验证均匀值域条件、构造正则化内层问题、求解唯一正则化解、取极限获得保守Jacobian、用伪逆公式回传梯度；该框架在最小二乘、Huber回归与LASSO上逐一验证适用条件，并在数据投毒与数据超清洗双层任务中实现端到端梯度计算。

### 三、结果（Result）
证明了在均匀值域条件下，即使偏雅可比矩阵不可逆，最小范数解映射仍存在良定义的广义导数（保守Jacobian），并在广义Hessian特征值有界时伪逆公式成立。该结论先对光滑凸目标建立，再推广到光滑加非光滑正则的复合问题；最小二乘、Huber回归与LASSO均被验证满足理论前提。在数据投毒与数据超清洗实验中，该方法在病态多解场景下相比标准隐式微分获得更稳定有效的梯度，给出可复现的对比结论。

### 四、结论（Conclusion）
本文将隐式微分从解唯一的良态情形推进到解不唯一的病态情形，以均匀值域条件替代雅可比可逆假设，为非光滑复合参数优化问题的梯度计算奠定了理论与算法基础。这为双层优化、元学习及数据清洗等应用提供了在病态设定下仍可用的求导工具，并明确了适用边界。

### 五、方法论与关键技术细节
核心假设是均匀值域条件，它弱于可逆性且便于在具体模型上验证；极限Tikhonov正则化是推导枢纽，要求正则参数单调趋于零并处理极限交换；保守集值场论提供非光滑广义导数的严格定义，绕开单值切导数可能不存在的问题；伪逆公式需要额外控制广义Hessian的特征值。方法限于凸目标，非光滑复合情形要求正则项（如LASSO的ℓ1范数）满足次微分规则性与近端可计算条件；实验采用数据投毒与数据超清洗两个典型病态双层任务，展示实用性，但也暴露了对目标凸性和条件验证的依赖等局限。
