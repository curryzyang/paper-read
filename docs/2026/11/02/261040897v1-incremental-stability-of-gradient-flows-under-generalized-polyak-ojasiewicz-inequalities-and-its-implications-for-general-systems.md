# Incremental Stability of Gradient Flows under Generalized Polyak-Łojasiewicz Inequalities and Its Implications for General Systems

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Andreas Oliveira, Arthur C. B. de Oliveira, Mario Sznaier, Eduardo Sontag
- 机构：Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40897v1) · [PDF](https://arxiv.org/pdf/2610.40897v1)

## TLDR
The paper shows that nonconvex gradient flows satisfying generalized Polyak–Łojasiewicz inequalities can be incrementally stable—contracting in a state-dependent Riemannian metric when the minimizer is unique and incrementally stable when minimizers are nonunique—yielding convergence and endpoint-map continuity guarantees and extending to Heavy-Ball and Dynamical Inertial Newton flows.

## Abstract
Gradient flows of twice continuously differentiable strongly convex and convex objectives are, respectively, incrementally exponentially stable and non-expansive in the Euclidean metric. In this work, we investigate to what extent these properties extend to nonconvex objectives satisfying generalized Polyak-Łojasiewicz inequalities. For objectives with a unique minimizer, we establish conditions under which the gradient flow is contracting in a state-dependent Riemannian metric and incrementally exponentially stable. For objectives with nonunique minimizers, we generalize the non-expansivity of convex objectives to incremental stability for more general nonconvex objectives. We focus on incremental stability due to its implication to convergence to equilibrium points; when paired with a Lyapunov function it implies pointwise convergence to a minimizer and continuity of the endpoint map. Along the way, we derive new structural results for incrementally stable nonlinear systems and extend the analysis to Heavy-Ball and Dynamical Inertial Newton flows.


## 精读解读（中文）
### 一、研究动机
强凸与凸目标的梯度流分别具有增量指数稳定性和非扩张性，但非凸目标即使在广义Polyak–Łojasiewicz不等式下也只能保证目标值或梯度范数意义下的收敛，未必给出状态轨迹收敛到具体极小点的保证。本文旨在研究广义PL型梯度流在多大程度上继承增量稳定性，并借此把目标值收敛提升为状态空间中的收敛、端点映射连续性等结构性结论。

### 二、技术方案（Method）
以连续时间梯度流xdot=-∇f(x)为对象，设f为二次连续可微、下有界并达到最小值，采用广义PL不等式‖∇f(x)‖≥α(f(x)-f*)刻画梯度支配性，其中α为连续正定比较函数并可属于K、K∞或更一般的Kc类。针对唯一极小点的情形，利用收缩理论构造状态依赖的Riemannian度量，分析梯度流在该度量下的严格收缩与增量指数稳定性，并给出该度量与Euclidean度量一致等价的两种充分条件：不充分凸区域有界，或全局下曲率界配合梯度支配函数增长。针对非唯一极小点情形，转而研究增量稳定性而非严格收缩，推导增量稳定非线性系统的结构结果，并将其应用于经典PL目标和一类新的广义PL目标；随后把分析扩展到Heavy-Ball与Dynamical Inertial Newton流。

### 三、结果（Result）
在唯一极小点且极小点局部强凸时，可构造全局Riemannian收缩度量，使梯度流具有增量指数稳定性；该度量是proper且诱导Euclidean拓扑，但不一定与Euclidean度量一致等价。在不充分凸区域有界或全局下曲率界加比较函数增长条件下，该度量与Euclidean度量一致等价，从而得到Euclidean范数下的全局增量指数稳定性，通常带有非单位超调。对非唯一极小点，经典PL目标的梯度流是增量稳定的，且存在一类新的广义PL目标也具有增量稳定性，该类与经典PL类互不包含；由此得到逐点状态收敛、端点映射连续以及极小点集路径连通，而无需严格收缩或增量指数稳定。还给出一个新的对数范数判据：若系统全局渐近稳定且在一个不含平衡点的紧集之外处处无穷小收缩，则系统全局增量指数稳定；Heavy-Ball和Dynamical Inertial Newton流在所述凸性正则条件下也具增量稳定性，DIN在经典PL下亦如此。

### 四、结论（Conclusion）
本文将强凸/凸梯度流的收缩与非扩张性质推广到满足广义PL不等式的非凸目标，说明增量稳定性可作为连接目标值收敛与状态轨迹收敛、端点映射连续性和极小点集拓扑性质的关键桥梁。结果把优化动力学分析与控制理论中的增量稳定性工具相结合，并为Heavy-Ball、Dynamical Inertial Newton等惯性优化动力学提供统一分析框架。

### 五、方法论与关键技术细节
核心输入是二次连续可微目标及其梯度流，关键先验是广义PL不等式中的比较函数α、唯一极小点处的局部强凸性，以及非唯一极小点下的增量稳定性定义；稳定性度量允许为proper且与Euclidean拓扑兼容的Riemannian度量，速率κ和超调c是主要定量参数。技术上依赖Riemannian收缩度量、对数范数判据、Lyapunov函数与端点映射；在非唯一极小点情形避免要求严格收缩，改用类K函数界定的增量稳定性，并利用全局半稳定性刻画端点映射连续性和平衡集连通性。实现层面的约束包括全局收缩度量不必与Euclidean度量一致等价，只有不充分凸区域有界或全局下曲率加α增长时才得到Euclidean意义下的全局增量指数稳定性；惯性动力学结果需要相应凸性与正则性假设，且新广义PL类与经典PL类不可相互包含。
