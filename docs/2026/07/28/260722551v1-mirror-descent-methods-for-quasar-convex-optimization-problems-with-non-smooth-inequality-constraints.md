# Mirror Descent Methods for Quasar Convex Optimization Problems With Non-Smooth Inequality Constraints

- 区域：精读区
- 排名：4
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Mohammad Alkousa
- 机构：Innopolis University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22551v1) · [PDF](https://arxiv.org/pdf/2607.22551v1)

## TLDR
This paper presents two groups of mirror descent algorithms, including deterministic and stochastic variants, for solving non-smooth quasar convex optimization problems with non-smooth inequality constraints and establishes their convergence rates.

## Abstract
In this paper, we consider constraint optimization problems subject to non-smooth convex functional (inequality-type) constraints, wherein the objective function is non-smooth and quasar convex. We propose and analyze two groups of algorithms, each consisting of a standard version and a modified variant, that operate by switching between two types of iteration points: productive and non-productive. Within each group, we develop distinct mirror descent-type algorithms for both deterministic and stochastic settings, and we establish their convergence rates.


## 精读解读（中文）
### 一、研究动机
非光滑quasar凸函数在机器学习中广泛应用，例如线性动力学系统学习和相位恢复，但现有研究多集中于光滑情形，非光滑带功能约束的问题尚未充分探索。本文旨在填补这一空白，提出有效的镜面下降算法。

### 二、技术方案（Method）
考虑问题min_{g(x)<=0, x in Q} f(x)，其中f为γ-quasar凸且非光滑，g凸非光滑。提出两组镜面下降算法，每组包括标准版和修改版，在确定性和随机设置下均适用。算法基于productive（满足g<=ε）和non-productive（不满足）步骤切换：productive步使用f的子梯度更新，non-productive步使用g的子梯度更新。步长h_k自适应为Θ_0(∑_{i=0}^k M_i^2)^{-1/2}，其中M_i为当前子梯度的对偶范数。最终输出productive迭代中f值最小的点。

### 三、结果（Result）
对于确定性算法（Group I定理1），迭代复杂度为O(max{M_f^2, M_g^2} Θ_0^2 (1+1/γ)^2 / ε^2)，输出点同时满足f(hat{x})-f(x*)≤ε和g(hat{x})≤ε。随机设置类似，建立了相应的收敛速率。

### 四、结论（Conclusion）
本文提出了两类针对非光滑quasar凸约束优化问题的镜面下降算法，在确定性和随机环境中均建立了收敛保证，扩展了quasar凸优化的理论框架至更实际的带约束场景。

### 五、方法论与关键技术细节
关键假设包括：f为γ-quasar凸（γ∈(0,1]），f和g均为Lipschitz连续（常数M_f, M_g），Bregman散度有界（≤Θ_0^2）。步长自适应且非增，通过productive/non-productive机制处理约束。算法需要已知Θ_0，但无需问题精确解信息。随机设置中使用无偏随机子梯度。局限性可能包括对于大规模问题的计算成本以及对Θ_0的依赖。
