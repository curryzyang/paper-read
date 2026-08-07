# Katz Centrality-Based Security Allocation in Positive Networks

- 区域：精读区
- 排名：8
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Anh Tung Nguyen, Sribalaji C. Anand, André M. H. Teixeira
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05360v1) · [PDF](https://arxiv.org/pdf/2608.05360v1)

## TLDR
This paper develops a Katz centrality-based security allocation framework for positive networked control systems under stealthy false data injection attacks, showing that worst-case performance loss is bounded by a tractable SDP problem and linked to Katz centrality to enable scalable, optimization-free selection of monitor nodes.

## Abstract
This paper deals with security allocation challenges for networked control systems represented by positive-weighted digraphs under stealthy false data injection attacks. These systems consist of interconnected subsystems, referred to as nodes in the underlying digraph, where an adversary aims to maximize network performance loss by stealthily attacking specific nodes. Meanwhile, a defender monitors several nodes to impose stealthiness constraints on the adversary's actions, thereby minimizing the network performance loss. We analyze the worst-case network performance loss of these stealthy attacks and make the following contributions: we (i) show that the worst-case network performance loss is upper-bounded by a tractable semi-definite programming (SDP) problem; (ii) establish the relationship between the SDP problem and the Katz centrality measure of the underlying digraph under a sufficient condition, resulting in a network-size-independent optimization problem; and (iii) provide a heuristic search based on the Katz centrality measure of the underlying digraph for selecting sub-optimal monitor nodes against all admissible attack scenarios without solving optimization problems. These results offer practical insights for safeguarding large-scale networked control systems against stealthy false data injection attacks. The obtained results are validated via extensive simulations on Erdos-Renyi random graphs with different network sizes.


## 精读解读（中文）
### 一、研究动机
针对正加权有向图表示的网络化控制系统在隐秘虚假数据注入攻击下的安全资源分配问题，现有安全度量在大规模网络中计算复杂且缺乏图论解释，难以扩展，需要更高效且具有图论洞察的安全评估与防御资源分配方法。

### 二、技术方案（Method）
将系统建模为正加权有向图，节点为子系统，攻击者选择若干节点注入隐秘攻击信号以最大化性能损失，防御者监控若干节点施加隐匿约束以最小化损失。首先利用耗散系统理论将最坏情况性能损失上界转化为可处理的半定规划（SDP）问题；然后在充分鲁棒性条件下证明该上界与SDP解相等，并利用正系统特性将SDP简化为与网络规模无关的优化问题；进一步引入两种适配Katz中心性度量，建立几何条件判定SDP有限解的存在性，并基于该条件设计启发式搜索算法，无需求解优化问题即可选择次优监控节点。

### 三、结果（Result）
通过不同规模的Erdős–Rényi随机图仿真验证：所提SDP上界在满足充分条件时精确等于最坏情况损失；Katz中心性为基础的几何条件能够有效判定安全性；启发式搜索可快速选择有效监控节点，且计算复杂度不随网络规模增长，适用于大规模网络。

### 四、结论（Conclusion）
论文建立了安全度量与Katz中心性之间的关联，提供了可扩展的安全评估框架和基于中心性的防御资源分配策略，为大规模正网络控制系统抵御隐秘虚假数据注入攻击提供了实用工具。

### 五、方法论与关键技术细节
关键点包括：系统状态非负性（正系统）与KYP引理在简化SDP中的作用；充分鲁棒性条件是保证SDP解与最坏损失相等的前提；两种Katz中心性变体考虑了网络邻接矩阵和自环增益；几何条件本质上是关于监控节点集合的中心性覆盖条件；启发式搜索基于中心性排序选择监控节点，避免求解优化问题；局限性在于结果依赖于充分条件和启发式搜索的次优性，且未考虑完全对抗性场景的证明保证。
