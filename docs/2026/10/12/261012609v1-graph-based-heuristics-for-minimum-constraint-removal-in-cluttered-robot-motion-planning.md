# Graph-Based Heuristics for Minimum Constraint Removal in Cluttered Robot Motion Planning

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Antony Thomas, Fulvio Mastrogiovanni, Marco Baglietto
- 机构：University of Genoa, IIIT Hyderabad
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12609v1) · [PDF](https://arxiv.org/pdf/2610.12609v1)

## TLDR
This paper proposes a graph-based heuristic pipeline that combines bidirectional feasible-set generation with fixed-length searches over reduced MCR graphs to compute near-optimal, low-cardinality constraint-removal sets for cluttered robot motion planning significantly faster than exact search.

## Abstract
Humanoid and service robots operating in clut- tered human environments may encounter motion planning problems that are infeasible when all surrounding objects are treated as fixed obstacles. The Minimum Constraint Removal problem, which we refer to as MCR, addresses this situation by identifying the minimum number of constraints, such as movable objects, whose removal enables a collision-free path. However, computing an optimal MCR solution is NP-hard. In this work, we propose a graph-based heuristic pipeline that combines bidirectional feasible-set generation with fixed- length searches over reduced MCR graphs. We further derive an extended feasible-set generator for instances in which the candidates produced by the first generator do not contain a complete optimal removal set. Across six benchmarks, the evaluated pipeline matches the exact solution in three cases and, in the remaining cases, selects at most 31.25% more obstacles than the optimum, while being between 3.4 and 33.7 times faster than exact search. In one of the benchmarks, involving a manipulation task amidst clutter, selecting two rather than seven obstructing objects reduces the combined MCR, inverse- kinematics, and motion planning time from 84.72 s to 30.59 s. These results indicate that the proposed approach provides a practical compromise between computational efficiency and solution quality for motion planning among movable obstacles.


## 精读解读（中文）
### 一、研究动机
在杂乱人类环境中，人形和服务机器人常遇到将所有周围物体视为固定障碍时运动规划不可行的情况；最小约束移除问题（MCR）寻找最少可移动约束或物体子集，使其移除后存在无碰撞路径。然而最优MCR是NP-hard，精确图搜索计算昂贵，而贪婪剪枝又可能返回显著更多障碍，因此需要兼顾效率与解质量的实用方法。

### 二、技术方案（Method）
将配置空间划分为连通单元，构建带障碍标签I(v)的MCR图G=(V,E)，目标是最小化路径顶点标签并集大小。提出图启发式流水线：GFS-1从起点和终点双向探索，利用两侧搜索前沿共享的障碍标签生成候选移除集；随后Refine在约简MCR图上做固定长度路径搜索以精炼候选。GFS-2扩展可行集生成器，用于GFS-1候选未包含完整最优移除集的情况，并分析其计算复杂度。

### 三、结果（Result）
在六个基准中，GFS-1+Refine在三个实例与精确解一致；其余实例最多比最优多选31.25%的障碍，同时比精确搜索快3.4至33.7倍。一个杂乱操作任务中，选择2个而非7个遮挡物使MCR、逆运动学和运动规划总时间从84.72秒降至30.59秒。

### 四、结论（Conclusion）
该方法为可移动障碍物场景下的MCR提供了计算效率与解质量之间的实用折中，能快速生成可行低保额移除集，并显著降低下游操作规划开销。

### 五、方法论与关键技术细节
输入为已构建的MCR图，顶点对应配置空间连通单元，标签为相交障碍集合，移除代价统一为单位成本，移除抽象为将物体移出规划相关区域且不计算具体重定位。精确解用状态(v,R)的最佳优先搜索；关键难点是无标量最优子结构，同一顶点需保留多个R，局部最优前缀可能非全局最优。启发式无训练过程，核心超参为固定长度搜索的路径长度与候选集构造；局限是依赖图构建与标签，不判断物体操作难度、不规划如何何处移动物体，且只提供低保额近似而非最优保证。
