# The Combined Van-and-Mopeds Routing Problem with Time Windows: Formulation, Variants, and Solution Methods

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Pedro Lameiras, Alexandre P. Francisco, Adriano Serrano, Cátia Vaz
- 机构：INESC-ID Lisboa, Instituto Politécnico de Lisboa, Universidade de Lisboa, Dingoo
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.22601v1) · [PDF](https://arxiv.org/pdf/2607.22601v1)

## TLDR
This paper introduces the Combined Van-and-Mopeds Routing Problem with Time Windows (CVMRPTW) for last-mile delivery in dense cities, proposing a MILP formulation with 22 constraint families, three operational variants, a lexicographic optimization framework, graph-sparsification preprocessing, and a Cluster-Based Combined Routing heuristic that scales to 80 customers.

## Abstract
We introduce and study the Combined Van-and-Mopeds Routing Problem with Time Windows (CVMRPTW), a novel variant of the heterogeneous fleet vehicle routing problem motivated by last-mile parcel delivery in dense European cities. In the CVMRPTW, a single van serves as a mobile base from which on-demand mopeds are deployed to reach customers located in areas inaccessible or inefficient for vans. The primary objective is to minimise the number of mopeds used while guaranteeing that all delivery time windows are met. We propose a Mixed-Integer Linear Programming (MILP) formulation that captures vehicle synchronisation, capacity tracking, and time-window compliance through 22 structured constraint families, and extend it to three operationally motivated variants: the standard model, the active-waiting-van variant, and the common-depot variant. A lexicographic two-stage optimisation framework allows secondary objectives-route duration, combined travel time, and combined distance-to be optimised without sacrificing the primary objective. Three graph-sparsification preprocessing techniques reduce the number of variables and constraints by up to 25%. For instances beyond the practical limits of exact solvers, we develop the Cluster-Based Combined Routing (CBCR) heuristic, which decomposes the problem into a clustering phase, a cluster-level exact solve, and a route-reconstruction phase. Computational experiments on real-world instances derived from OpenStreetMap data for Lisbon and Stuttgart show that the MILP solves instances with up to 48 customers to feasibility within one hour, and that the CBCR heuristic extends tractability to instances with up to 80 customers under favourable conditions.


## 精读解读（中文）
### 一、研究动机
城市最后一英里配送中，传统货车因狭窄街道、陡坡和低排放区无法到达大量客户，亟需一种结合货车和机动灵活摩托车的异构车队方案。本文受里斯本Dingoo公司运营场景启发，针对硬时间窗约束下最小化摩托车使用数量的组合路径优化问题，填补了现有车辆路径问题（如CTBRP）中多摩托车、动态结合节点和硬时间窗同时考虑的空白。

### 二、技术方案（Method）
提出CVMRPTW的混合整数线性规划（MILP）公式，包含22类约束族覆盖流守恒、车辆同步、容量追踪和时间窗满足；模型基于有向加权图，货车和摩托车各有独立边集和旅行时间，结合节点由优化内生确定。开发两阶段词典优化框架，首先最小化摩托车数量，然后在不牺牲主要目标下优化路线持续时间、总旅行时间或总距离。引入三种图稀疏化预处理技术（基于时间窗、可达性和容量约束裁剪边）将变量和约束减少最多25%。对于超过MILP求解能力的大规模实例（超过48客户），提出基于聚类的组合路由（CBCR）启发式：先通过k-medoids聚类将客户分组，再对每个聚类精确求解MILP，最后重建全局路线。实验使用基于OpenStreetMap的里斯本和斯图加特真实数据，利用Gurobi 12.0.2求解。

### 三、结果（Result）
在真实实例测试中，MILP能在1小时内求解最多48个客户的实例并达到可行性；CBCR启发式在有利条件下将可处理规模扩展到最多80个客户。图稀疏化预处理平均减少25%的决策变量和约束。新提出的性能指标（平均摩托车负载、平均同步比）为评估方案质量提供了量化依据。

### 四、结论（Conclusion）
本文首次为结合货车与摩托车的城市配送问题（CVMRPTW）提供了完整的数学模型和求解方案，证明MILP和CBCR启发式能在实际规模下有效优化摩托车数量和次要目标，为城市物流运营商制定灵活、低成本的最后一英里配送策略提供了理论支撑和实用工具。

### 五、方法论与关键技术细节
数据来源：通过OpenStreetMap提取里斯本和斯图加特的真实道路网络和客户分布。先验假设：所有客户具有硬时间窗，货车容量约50包裹，摩托车容量4-6包裹，且摩托车的装载遵循LIFO顺序（模型简化中未显式建模）。目标函数：主目标最小化摩托车使用数量，次目标按优先级可选最小化总路线时长、总旅行时间或总距离。超参：CBCR中聚类数由客户数量动态确定。复杂度：问题属NP-hard，MILP解空间随客户数指数增长，精确求解受限于48客户。局限性：CBCR在客户分布松散或时间窗紧凑时性能下降；模型未考虑实时交通变化或动态需求。
