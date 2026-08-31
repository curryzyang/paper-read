# An Adaptive Augmented Lagrangian Method for Deterministic and Stochastic Nonconvex Optimization

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Tianzhu Liu, Michael J. O'Neill
- 机构：University of North Carolina at Chapel Hill
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27676v1) · [PDF](https://arxiv.org/pdf/2608.27676v1)

## TLDR
This paper introduces an inexact augmented Lagrangian method that uses adaptive penalty updates and full dual stepsizes, achieving best-known worst-case complexity guarantees (up to logarithmic factors) for deterministic and stochastic nonconvex optimization and demonstrating practical gains over non-adaptive alternatives in experiments.

## Abstract
We present an inexact Augmented Lagrangian algorithm for solving nonlinear, non-convex optimization problems. Unlike most recently proposed Augmented Lagrangian methods with worst-case complexity guarantees, we utilize adaptive penalty parameter updates and full dual stepsizes. We show that the method matches the best known worst-case complexity results for Augmented Lagrangian methods (up to logarithmic factors) when both the function and constraints are deterministic, when the function is stochastic and the constraints are deterministic, and when both are stochastic. Experiments on CUTEst test problems confirm the practical advantages of the proposed approach over Augmented Lagrangian methods with non-adaptive penalty parameters and/or short dual step sizes in the deterministic setting. Numerical results on stochastic constrained optimization problems in machine learning also confirm these findings.


## 精读解读（中文）
### 一、研究动机
现有带最坏情况复杂度保证的增广拉格朗日方法通常采用固定罚参数增长调度和短对偶步长，前者会让子问题严重病态、实际求解困难，后者破坏增广拉格朗日与对偶近端点法的等价性。本文旨在设计一种自适应罚参数并采用完整对偶步长的非精确增广拉格朗日算法，使其在保持最优复杂度担保的同时更贴近经典ALM的实用行为。

### 二、技术方案（Method）
输入为 min f(x)+g(x) s.t. c(x)=0，其中 f 与 c 光滑且可为确定性或随机期望形式，g 为凸非光滑函数。算法构造增广拉格朗日函数 Lβ(x,y)=f(x)+c(x)^T y + β/2||c(x)||²；外层迭代中先非精确求解原始子问题 min_x Lβ_k(x,y_k)+g(x)，再根据约束违反度的实际下降比例自适应更新罚参数 β_k：若违反度获得充分下降则保持 β_k，否则增大 β_k。对偶更新使用完整步长 y_{k+1}=P_Y(y_k+β_k c(x_{k+1}))，其中 P_Y 为投影到有界对偶球；随机情形下在子问题内部采用简单随机/方差缩减型内循环估计梯度并求解近似最小点。终止条件为 dist(-∇_x L(x,y),∂g(x))+||c(x)||≤ε。

### 三、结果（Result）
在CUTEst/PyCUTEst确定性测试集上，自适应罚参数与完整对偶步长显著优于固定罚参数和短对偶步长的增广拉格朗日方法；在机器学习随机约束问题（如Neyman-Pearson分类）上数值结果同样验证了优势。理论上，方法在确定性目标/确定约束、随机目标/确定约束、两者均随机三类设置下均达到已知最优增广拉格朗日复杂度（对数因子内）：确定性情形为 O~(ε^{-3})，随机目标/确定约束为 O~(ε^{-6})，两者随机为 O~(ε^{-7})；加入更强方差缩减型内层后分别可改进至 O~(ε^{-4}) 与 O~(ε^{-5})。

### 四、结论（Conclusion）
自适应罚参数更新与完整对偶步长既能提供与最优已有复杂度匹配的理论保证，又能避免固定调度导致的病态子问题。该方法更接近经典增广拉格朗日/对偶近端解释，在确定性与随机非凸约束优化中均有实际与理论优势。

### 五、方法论与关键技术细节
关键假设包括 f,c,J 的 Lipschitz光滑性与有界性，以及正则性条件 ν||c(x_{k+1})||≤dist(-J(x_{k+1})^T c(x_{k+1}),∂g(x_{k+1})/β_k)，该条件在LICQ下成立。对偶变量通过投影限制在固定半径球内，从而保证有界性；罚参数更新采用ALGENCAN式启发规则，若 β_k 不超过阈值则外迭代为 O(log ε^{-1})，否则可借助Sahin式分析得到多项式复杂度。随机情形使用随机/方差缩减内层求解器，复杂性以高概率成立，且自适应性的额外代价仅为相关因子的对数项。局限性包括对偶投影半径和子问题求解容差需要适当设置，随机复杂度依赖内层求解器的精度与方差缩减策略。
