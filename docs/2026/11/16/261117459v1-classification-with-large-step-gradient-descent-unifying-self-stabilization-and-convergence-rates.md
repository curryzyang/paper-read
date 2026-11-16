# Classification with Large-Step Gradient Descent: Unifying Self-Stabilization and Convergence Rates

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Salma Tarmoun, Lachlan Ewen MacDonald, Konstantinos Emmanouilidis, Ziqing Xu, René Vidal
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17459v1) · [PDF](https://arxiv.org/pdf/2611.17459v1)

## TLDR
This paper unifies self-stabilization and convergence-rate analysis for large-step gradient descent in separable linear classification with exponential-tail losses, using a curvature-defined reference subspace to derive explicit iterate bounds and reveal a transient large-step implicit bias toward the max-margin direction.

## Abstract
Neural networks are often trained with gradient descent (GD) using step sizes that exceed classical stability thresholds, a regime where standard convergence theory no longer applies. Despite exhibiting non-monotonic loss and oscillatory dynamics, this regime frequently leads to faster convergence and better generalization. Existing theoretical perspectives offer complementary but incomplete insights: one identifies a self-stabilization mechanism that drives GD toward flat regions but does not yield convergence rates; another derives rigorous rates for specific losses but does not explain the underlying stabilization mechanism; and a third unifies these views for overparameterized least squares, but relies on the existence of a minimizer manifold, which is absent in classification settings. In this work, we extend this unified geometric perspective to exponential-tail losses, including logistic and cross-entropy losses in separable linear classification, where the loss infimum is not attained at any finite parameter. We identify a curvature-defined reference subspace that replaces the role of the minimizer manifold, yielding a coupled dynamical system in which orthogonal oscillations are damped by parallel progress along directions of decreasing sharpness. Under regularity conditions, which we verify for logistic and multiclass cross-entropy losses on symmetric data models, we derive explicit bounds for the iterates, not just the loss, covering both the unstable and stable regimes, and revealing a three-phase damping structure in the latter. Our analysis further uncovers a transient implicit bias induced by large step sizes: although GD converges asymptotically to the max-margin direction, large steps can leave persistent orthogonal residuals and, in certain geometries, amplify them, affecting finite-time alignment with the max-margin direction.


## 精读解读（中文）
### 一、研究动机
大步长梯度下降常突破经典稳定阈值，虽损失非单调且轨迹振荡，却常带来更快收敛和更好泛化，但现有理论各执一端：自稳定机制缺乏收敛率，特定损失的速率分析不解释稳定化机制，最小二乘的统一分析又依赖分类问题中不存在的极小值流形。本文旨在把统一的几何视角推广到指数尾损失，为可分离线性分类中的大步长GD同时刻画自稳定机制与迭代收敛率。

### 二、技术方案（Method）
论文研究可分离线性分类中的逻辑损失和多类交叉熵等指数尾损失，其下确界不在任何有限参数处达到；作者用由损失曲率定义的参考子空间替代极小值流形，将GD轨迹分解为平行于该子空间的分量和正交振荡分量，得到一个耦合动力系统，其中正交振荡被沿低锐度方向的平行推进所阻尼，三阶耦合对应曲率的隐式梯度下降。作者在正则条件下推导迭代点而非仅损失的显式上界，覆盖不稳定与稳定两类步长区间，并在对称数据模型上验证逻辑损失和多类交叉熵损失满足条件，同时用实验检验理论预测。

### 三、结果（Result）
分析给出迭代点的显式收敛界，并在稳定区揭示振荡阻尼的三相结构；同时发现大步长会引入瞬态隐式偏置：尽管GD渐近收敛到最大间隔方向，有限时间仍可能留下持续的正交残差，并在某些数据几何下放大这些残差，从而影响与最大间隔方向的有限时间对齐。

### 四、结论（Conclusion）
该工作将大步长GD的自稳定机制与收敛率统一到指数尾损失的几何分析框架中，说明曲率参考子空间可替代分类设定中缺失的极小值流形，并揭示稳定区的三相阻尼和由步长与几何决定的瞬态隐式偏置。其结论为理解大学习率下分类训练的快速收敛、振荡行为及有限时间方向偏置提供了可检验的理论依据。

### 五、方法论与关键技术细节
关键实现依赖曲率定义的参考子空间、平行-正交分解以及三阶耦合项，核心假设包括谷几何和衰减剖面等正则条件，并在对称可分离数据的逻辑回归与多类交叉熵上验证；分析同时给出不稳定与稳定步长区的迭代界，而不只约束损失值。局限在于理论主要覆盖指数尾损失和满足正则条件的对称数据模型，尚未直接适用于一般深度网络或任意数据几何，且大步长导致的正交残差和有限时间最大间隔对齐偏差是几何相关的瞬态现象。
