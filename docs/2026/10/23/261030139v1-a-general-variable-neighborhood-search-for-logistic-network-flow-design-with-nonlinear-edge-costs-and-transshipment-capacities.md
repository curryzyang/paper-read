# A General Variable Neighborhood Search for Logistic Network Flow Design with Nonlinear Edge Costs and Transshipment Capacities

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Varvara Kovaleva, Alexander Ponomarenko
- 机构：HSE University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30139v1) · [PDF](https://arxiv.org/pdf/2610.30139v1)

## TLDR
The paper formulates a multi-commodity logistic network flow design problem with vehicle-capacity-induced nonlinear edge costs and hard transshipment capacities as arc- and path-based MILPs and proposes a path-space General Variable Neighborhood Search with three problem-specific neighborhoods, which yields near-optimal, seed-stable solutions and outperforms a time-limited exact solver by up to 55% on medium benchmark instances.

## Abstract
We study the problem of routing multiple commodities through a logistic transport network so as to minimise the joint cost of vehicle movements and of transshipment (reload) operations at intermediate storages. The problem combines two features that are common in practice but rarely treated together: edge costs that are nonlinear in the transported volume, because freight is carried by vehicles of fixed capacity, and hard upper bounds on the volume that can be reloaded at each node. We formulate the problem as a mixed integer linear program in both an arc-based and a path-based form, derive its linear relaxation, and propose a metaheuristic solver based on General Variable Neighborhood Search (GVNS). The method works in the path space and relies on three problem-specific neighborhoods that generate new candidate paths by (i) shortest paths under a reload-aware metric, (ii) edges carrying partially loaded vehicles, and (iii) detours around congested storages. We evaluate the method on our open benchmark for this problem (arXiv:2606.20653): a corpus of realistic logistic networks calibrated on real road graphs of nine European countries, five U.S. states and the European part of Russia, with near-planar topology (Zipf city sizes, a spatial-network budget model, and a doubly constrained gravity demand model). On 35 synthetic and 15 real-geometry instances with up to 150 storages, GVNS returns solutions within about one percent of the best dual bound on small networks -- a branch-and-bound lower bound substantially tighter than the LP relaxation -- is stable across random seeds, and for a comparable wall-clock budget is up to 55% better than a time-limited exact solver on the medium instances.


## 精读解读（中文）
### 一、研究动机
现实物流网络中的多商品流路由需要同时考虑固定容量车辆导致的边成本非线性（车辆数按流量向上取整）以及中转仓储的硬性换装容量；这两类特征常见但很少联合建模，且该问题为NP难，精确求解在中大规模上代价高，因此需要可扩展且高质量的启发式方法。

### 二、技术方案（Method）
论文先建立弧基与路径基等价的混合整数线性规划，并推导LP松弛，松弛后可消去车辆数变量。求解器采用路径空间的通用变邻域搜索GVNS：预处理用全图最短路补全图，并以上述松弛的直接起讫边解作初始解；N1基于含装卸成本的辅助权重建最短路，N2依据边残载量模C构造偏好未满载边的图，N3按中转节点overload比排序并删除最拥堵节点重算绕行路径。每次邻域处理为每类商品生成候选路径加入路径池，以当前流为热启动在限时MILP中重新分配流量，若目标改进则保留非零流新路径并剪除零流路径，否则丢弃；VND系统扫描邻域，Shake随机扰动，邻域变更按改进重置或推进。

### 三、结果（Result）
在包含35个合成实例和15个真实几何实例、最多150个仓储的开放基准上，GVNS在小网络上得到与最佳对偶界（分枝定界下界，明显紧于LP松弛）约1%以内的解，且跨随机种子稳定；在中等实例相同墙钟预算下，比限时精确求解器最多好55%。

### 四、结论（Conclusion）
GVNS通过路径池扩张与限时MILP再优化，配合重装成本感知、部分装载车辆和拥堵绕行三类问题特定邻域，能有效处理带非线性边成本与中转容量约束的多商品物流网络设计；结果支持其作为实际规模实例的高质量实用求解框架，并提供了与精确对偶界可比的评估。

### 五、方法论与关键技术细节
关键实现包括：边成本c_e按每车计、车辆容量C、节点单位换装成本f_v与容量W_v；路径松弛目标为每单位流量路径成本（路径边c_e/C之和加中转f_v），车辆数由y_e=ceil(总流/C)或松弛中y_e=总流/C确定。N1权重c'_{vu}=f_v+f_u+c_{vu}/C；N2用load_e=总流 mod C，满载边最不吸引且保留G'权重，否则c''_{vu}=f_v+f_u+(load_{vu}/C)(c_{vu}/C)^α（α≤1）；N3按overload_v=中转量/W_v排序删点。VND与Shake的候选路径数、拥堵阈值（0.75/0.5）和节点子集大小（约|V|/5至|V|/4或|V|/4至|V|/3）等为关键超参；局限是外层为启发式且子问题MILP需限时求解，不保证全局最优，质量依赖基准与参数设置。
