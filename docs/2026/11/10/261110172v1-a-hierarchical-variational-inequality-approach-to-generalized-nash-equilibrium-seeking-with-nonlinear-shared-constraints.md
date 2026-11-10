# A Hierarchical Variational Inequality Approach to Generalized Nash Equilibrium Seeking with Nonlinear Shared Constraints

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Tatiana Tatarenko, Puya Latafat, Alberto Bemporad
- 机构：IMT School for Advanced Studies Lucca, Technical University of Darmstadt
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10172v1) · [PDF](https://arxiv.org/pdf/2611.10172v1)

## TLDR
The paper reformulates variational generalized Nash equilibrium seeking under nonlinear shared constraints as a hierarchical variational inequality with a penalty-based lower level, enabling primal-space centralized and distributed projection algorithms with last-iterate convergence guarantees.

## Abstract
We study the computation of variational generalized Nash equilibria (v-GNE) in games with strongly monotone pseudo-gradients and nonlinear convex shared constraints. We show that the v-GNE problem is exactly equivalent to a hierarchical variational inequality, whose lower level is given by the gradient of a smooth convex penalty of the constraint violation over the local action sets. Building on this reformulation, we propose a hierarchical regularization scheme that operates entirely in the primal space and requires only projections onto the local action sets. In the centralized setting, we prove last-iterate squared distance convergence to the v-GNE with rate $O(1/t^{\scriptscriptstyle 2/3})$ under a local error bound condition, which holds, e.g., under Slater's condition, improved to $O(1/t)$ under a global error bound condition. We then extend the scheme to the partial-decision information setting, where the agents communicate over a network and maintain local estimates of the joint action. We derive a distributed algorithm with a constant stepsize operating in the primal space and converging to the v-GNE with rate $O(1/t)$.


## 精读解读（中文）
### 一、研究动机
广义纳什均衡问题中，智能体既通过代价函数耦合，也通过共享约束耦合；实际系统如电力网络、充电协调和交通网络常具有非线性共享约束，且智能体只能获得局部信息。现有基于KKT条件的原始-对偶方法需要维护和协调对偶变量，并在非线性约束下失去全局Lipschitz性、常步长保证或需集中式线搜索，因此需要一种完全在原始空间、仅依赖局部动作集投影的均衡求解方法。

### 二、技术方案（Method）
论文针对强单调伪梯度和非线性凸共享约束的博弈，证明v-GNE问题等价于一个分层变分不等式：上层为博弈伪梯度，下层为约束违反的某个光滑凸罚函数梯度在局部动作集上的变分不等式。基于此提出集中式分层正则化格式，每步仅对局部动作集做投影，不引入对偶变量；随后扩展到部分决策信息场景，智能体在连通无向图上通信并维护联合动作的局部估计，采用常步长的分布式原始空间算法，通过局部估计一致性与投影更新逼近v-GNE。

### 三、结果（Result）
在集中式设置下，作者证明末迭代平方距离收敛到v-GNE：局部误差界条件（例如Slater条件成立时）下速率为O(1/t^{2/3})，全局误差界条件（例如线性共享约束与多面体局部集）下提升为O(1/t)。在部分决策信息设置下，分布式常步长算法在局部误差界条件和有界动作集下以O(1/t)速率收敛到v-GNE；实验在随机非线性网络约束和多智能体线性共享约束问题上验证性能，并与基于KKT的提升原始-对偶方法进行比较。

### 四、结论（Conclusion）
该工作给出了v-GNE的精确分层变分不等式重构，说明无需对偶变量或耦合可行集投影即可在原始空间求解非线性共享约束下的广义纳什均衡。所提集中式与分布式算法分别具有可证明的末迭代收敛速率，分布式版本避免对偶变量通信并降低计算与通信负担，为局部信息下的GNE寻求提供了新框架。

### 五、方法论与关键技术细节
关键假设包括博弈为凸博弈、伪梯度强单调、共享约束函数凸且连续可微、局部动作集投影易计算；集中式分析依赖局部或全局误差界条件，分布式分析还要求连通无向图和有界动作集。方法的核心是先验结构是把耦合可行集刻画为光滑凸罚函数的最小点集，从而下层VI对应凸优化并支持末迭代分析；算法仅使用局部动作集投影和常步长，不需要对偶变量共识或集中式线搜索。局限在于收敛速率依赖误差界/Slater类条件，分布式结果需有界动作集，且集中式方案仍需全局算子信息，实验主要覆盖随机实例和线性共享约束对比。
