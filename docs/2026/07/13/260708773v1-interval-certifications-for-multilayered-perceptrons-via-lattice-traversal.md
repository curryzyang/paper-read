# Interval Certifications for Multilayered Perceptrons via Lattice Traversal

- 区域：精读区
- 排名：5
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Merkouris Papamichail, Konstantinos Varsos, Giorgos Flouris, João Marques-Silva
- 机构：Foundation for Reasearch and Technology - Hellas, Heraklion, Greece, Catalan Institution for Research and Advanced Studies, Barcelona, Spain, University of Lleida, Lleida, Spain, University of Crete, Heraklion, Greece
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08773v1) · [PDF](https://arxiv.org/pdf/2607.08773v1)

## TLDR
This paper provides a rigorous theoretical framework for adversarial robustness in multilayered perceptrons by reducing it to a lattice traversal problem, enabling the computation of maximally sound and minimally complete interval certifications through novel lattice traversal operators and a refine-and-verify scheme.

## Abstract
In this work we present a rigorous theoretical framework to a foundational problem of AI safety, namely adversarial robustness. In particular, we show that the adversarial robustness problem can be reduced to a lattice traversal problem. Each element of this lattice corresponds to an interval, i.e., an axis-aligned hyper-rectangle, containing an input point $\mathbf{x}$. Consider a multilayered perceptron classifier (MLP). An interval $I$ constitutes a sound certification if $\mathbf{x} \in I$ and $\mathbf{x}$ can be freely perturbed in $I$ without changing the MLP's prediction. Complementarily, an interval $I$ constitutes a complete certification if $\mathbf{x} \in I$ and when $\mathbf{x}$ moves outside of $I$ the MLP's prediction is guaranteed to change. While the sound certification problem corresponds to the well-studied adversarial robustness, complete certifications have not been examined in the literature. We develop lattice traversal operators, which we apply in a refine & verify iterative scheme. Using formal MLP verifiers, sound maximality and complete minimality are guaranteed. Moreover, we examine objective optimization problems. There we discover some interesting asymmetries. For complete certifications, the minimum solution is obtained in polynomial oracle calls. This does not hold for sound certifications, where we prove strong intractability results. Additionally, we examine optimization problems in symmetric intervals (i.e., $\ell_\infty$-spheres), where we provide logarithmic algorithms. Finally, we present an empirical evaluation, using the novel ParallelepipedoNN system.


## 精读解读（中文）
### 一、研究动机
现有对抗鲁棒性方法主要依赖凸松弛或MILP求解，但缺乏对区间认证最大性/最小性的保证，且完全认证（complete certification）尚未被研究。本文旨在建立严格的区间认证理论框架，并将鲁棒性问题归约为格遍历问题，以同时处理声音认证（sound certification）和完全认证。

### 二、技术方案（Method）
将MLP分类器的对抗鲁棒性建模为格遍历问题，其中每个格元素对应一个包含输入点x的轴对齐超矩形（区间）。定义声音认证（区间内任意扰动不改变预测）和完全认证（区间外任意移动必然改变预测）。开发格遍历算子（lattice traversal operators），结合细化-验证（refine & verify）迭代方案，利用形式化MLP验证器（如Marabou）保证声音区间的最大性和完全区间的最小性。针对对称区间（ℓ∞球），提出对数复杂度优化算法。实现ParallelepipedoNN系统进行实验。

### 三、结果（Result）
完全认证的最小化问题可在多项式次oracle调用内求解，而声音认证的最优化问题被证明是强NP难（intractable）。对称区间（ℓ∞球）的优化问题存在对数时间算法。实验表明，ParallelepipedoNN系统能够有效计算最大声音区间和最小完全区间，且相比现有方法提供非平凡性保证。

### 四、结论（Conclusion）
本文建立了区间认证的严格理论框架，揭示了声音认证与完全认证在优化复杂性上的本质不对称性。通过格遍历和形式化验证，首次实现了最大声音区间和最小完全区间的计算，并为对称区间提供了高效算法，推动了对抗鲁棒性认证的理论与实用进展。

### 五、方法论与关键技术细节
输入为MLP分类器及输入点x；建模为区间格（轴对齐超矩形）上的遍历；核心模块包括格遍历算子、形式化验证器（MILP oracle）以及细化-验证循环；优化目标为最小边缘长度（即ℓ∞半径）；复杂度方面，完全认证问题可在O(poly)次oracle调用内解决，声音认证为NP-hard；局限性在于当前工作主要基于理论分析，实验规模可能受限，且依赖外部验证器的效率。
