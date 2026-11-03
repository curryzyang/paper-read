# Parameter-Free First-Order Method for Constrained Variational Inequalities

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Yan Wu, Qi Luo, Yuyuan Ouyang
- 机构：University of Iowa, Clemson University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00229v1) · [PDF](https://arxiv.org/pdf/2611.00229v1)

## TLDR
The paper proposes a parameter-free accelerated operator sliding (PFAOS) method, extended to multi-constraint settings, for monotone constrained variational inequalities that achieves \(\mathcal{O}(1/\varepsilon)\) operator evaluation and \(\mathcal{O}(1/\sqrt{\varepsilon})\) constraint-gradient evaluation complexities without requiring prior knowledge of Lipschitz or smoothness constants.

## Abstract
Constrained variational inequalities (VIs) provide a general framework for modeling and solving complementarity and equilibrium problems with functional constraints. In this paper, we propose a parameter-free accelerated operator sliding (PFAOS) method for solving monotone VIs with convex smooth constraints. For a single constraint, PFAOS achieves an operator evaluation complexity of $\mathcal{O}(1/\varepsilon)$ and a constraint gradient evaluation complexity of $\mathcal{O}(1/\sqrt{\varepsilon})$, without requiring prior knowledge of the Lipschitz constant of the VI operator or the smoothness constant of the constraint function. We further extend PFAOS to multiple constraints by incorporating a primal-dual hybrid gradient update, yielding a multi-constrained PFAOS (MC-PFAOS) method that preserves the same evaluation complexities.
  Finally, numerical experiments are conducted on large-scale games with coupling constraints to validate the efficiency and effectiveness of the proposed algorithms.


## 精读解读（中文）
### 一、研究动机
带功能约束的变分不等式可统一建模互补与均衡问题，但现有一阶方法常需向约束集投影或预先知道算子Lipschitz常数与约束光滑常数，且约束梯度复杂度多为O(1/ε)。本文受光滑凸优化与梯度滑动思想启发，试图分离算子评估与约束梯度评估成本，设计无需投影和先验参数的算法，在保持O(1/ε)算子复杂度的同时把约束梯度复杂度降到O(1/√ε)。

### 二、技术方案（Method）
针对单调Lipschitz算子F与凸光滑约束g，提出三层结构的无参数加速算子滑动法PFAOS：外层生成加速序列，中层对约束曲率参数η做倍增线搜索，内层执行算子滑动并自适应估计F的局部Lipschitz常数。每个内层子问题在简单凸集X上求解强凸二次规划，目标含外推的F评估与两个二次正则项，约束采用在当前λ点处的仿射线性化并在内层复用，随后通过加权平均形成候选外层点并用约束线性化接受检验。多约束情形MC-PFAOS引入原始-对偶混合梯度更新处理多个约束，保持相同的评估复杂度且不向约束集投影。

### 三、结果（Result）
理论结果表明，单约束PFAOS达到O(1/ε)的算子评估复杂度和O(1/√ε)的约束梯度评估复杂度；多约束MC-PFAOS保持O(1/ε)算子评估与O(1/√ε) Jacobian评估复杂度。两种方法均不需要预先知道F的Lipschitz常数、约束光滑常数或J(x)在X上的统一上界，也不需向功能约束集投影。相比已有CVI方法，约束梯度复杂度由O(1/ε)改进到O(1/√ε)，同时保留无约束VI最优的算子复杂度阶；大规模耦合约束博弈实验验证了效率和有效性。

### 四、结论（Conclusion）
PFAOS与MC-PFAOS为单调约束变分不等式提供了一类无参数一阶算法，在不向约束集投影和不依赖先验光滑常数的条件下，同时获得更优的约束梯度/Jacobian复杂度与最优算子复杂度。该工作说明通过算子滑动与约束线性化可有效分离两类oracle成本，并为带功能约束的均衡与互补问题提供可扩展求解框架；文中还给出任意小初始估计与无需集合直径的自动停止规则等实用扩展。

### 五、方法论与关键技术细节
方法假设F单调且Lipschitz、各g_i凸可微且梯度L_i-Lipschitz、X为投影廉价的紧凸集，并采用Slater条件与原始-对偶解存在性假设。实现上以初始L0∈(0,L]和Λ>0构造M0=2ΛL0，中层用2的幂次调整η，内层用整数q倍增局部Lipschitz估计M，子问题为含线性化约束的强凸二次规划，并以1/M权重做加权平均。复杂度为算子O(1/ε)、约束梯度或Jacobian O(1/√ε)，且无需J(x)统一界；局限性包括仍需高效求解X上的子问题、依赖凸光滑约束与Slater型条件，实验主要为大规模耦合约束博弈。
