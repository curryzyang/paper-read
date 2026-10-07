# RMRRT: Riemannian Barrier Metric RRT for Inequality-Aware Steering on Equality Manifolds

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Minhyeong Kang, Sanghyun Kim
- 机构：Kyung Hee University, Advanced Institute of Convergence Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06863v1) · [PDF](https://arxiv.org/pdf/2610.06863v1)

## TLDR
RMRRT is a sampling-based motion planner that unifies equality and inequality constraints by constructing a barrier-induced Riemannian tangent-space metric on equality-constrained manifolds and using it consistently in steering and nearest-neighbor selection to bias exploration away from inequality boundaries while preserving equality feasibility, yielding faster and more reliable constrained manipulation planning.

## Abstract
This paper presents a motion planning framework that unifies equality and inequality constraints within a single geometric formulation for sampling-based planning in high-dimensional robotic systems. In conventional sampling-based planners, equality constraints are typically enforced through projection, whereas inequality constraints are handled separately through binary validity checks such as collision testing, often leading to inefficient exploration. To address this limitation, we propose Riemannian Barrier Metric RRT (RMRRT), which constructs a unified local geometry for planning on equality-constrained manifolds. RMRRT first builds an ambient barrier metric from inequality-sensitive barrier terms and then induces a tangent-space metric via a (G)-orthogonal projection associated with the equality constraints. The resulting tangent-space metric is used consistently in both steering and nearest-neighbor selection, biasing exploration away from nearby inequality boundaries while preserving first-order equality consistency. In this work, the metric is instantiated from signed-distance-based geometric proxy inequalities to provide collision-informative tangent-space directions; hard feasibility is enforced separately through standard validity checks. Experimental results show that RMRRT achieves a 100% success rate across diverse constrained manipulation tasks in both simulation and real-world settings, while reducing planning time relative to representative constrained planning baselines. Ablation studies further demonstrate that the proposed metric improves exploration quality by reducing rejected samples and shortening path length. Experiment videos and source code are available at: https://rmrrt-anonymous.github.io


## 精读解读（中文）
### 一、研究动机
在高维机器人采样规划中，等式约束通常通过投影维持，而不等式约束往往只在碰撞检测等二值有效性检查中事后处理，二者分离导致样本拒绝率高、转向不稳定，尤其在可行域狭窄或碎片化的环境中探索效率低下。因此，本文旨在为等式约束流形上的规划构建一个同时满足一阶等式一致性和不等式边界感知的统一局部几何框架。

### 二、技术方案（Method）
RMRRT首先利用不等式敏感的对数障碍项，从基于符号距离的几何代理不等式构造环境空间障碍度量；随后结合等式约束雅可比J(q)，通过G-正交投影将该环境度量诱导到切空间，得到切空间度量。该切空间度量在最近邻选择、局部转向和流形校正中一致使用：转向时选择朝目标有进展且远离邻近不等式边界的方向，最近邻选择也按同一度量衡量局部可连接性，从而在保持一阶等式一致性的同时使探索远离障碍边界。规划器采用双向RRT式树扩展，输入为配置q、等式约束g(q)=0、不等式h_i(q)>0，以及若干机体固定代理点p_j(q)及其到障碍物的符号距离d_j(q)和代理点雅可比J_j(q)；实际硬可行性仍由标准状态有效性与边有效性检查独立保证，因此该度量作为探索偏置而非硬约束。

### 三、结果（Result）
实验在多种受约束操作任务中验证，包括仿真与真实世界场景，RMRRT在同时存在闭链抓取等等式约束和碰撞避免等不等式约束的任务中达到100%成功率，并相对代表性约束规划基线减少规划时间。消融研究表明，所提出的度量通过降低被拒绝样本数量、缩短路径长度来提升探索质量。真实世界示例中，三台机械臂在保持闭链抓取约束并避碰的条件下协同搬运椅子，验证了方法的实际可行性。

### 四、结论（Conclusion）
本文提出RMRRT，将环境障碍度量、G-正交投影和诱导切空间度量统一到采样规划中，使等式可行性与不等式感知探索在同一局部几何下耦合。该方法在受约束多臂与人形操作任务中表现出较高可靠性和效率，说明将不等式边界几何嵌入转向与最近邻选择可显著改善采样探索；其度量用于探索偏置，硬可行性仍由有效性检查保证。

### 五、方法论与关键技术细节
关键实现细节包括：不等式采用严格形式h_i(q)>0，使对数障碍在内部有限并在边界发散，因此硬可行性必须由状态和边有效性检查另行执行；等式约束流形要求J(q)满行秩，切空间为J(q)v=0，维数为n-m_eq；代理点为附着于运动链的机体固定点，经正运动学映射到世界坐标，其3×n雅可比和到有向包围盒的解析符号距离作为障碍度量输入；切空间度量通过与环境障碍度量兼容的G-正交投影诱导，并一致用于最近邻选择和转向；需要设置度量正则化参数λ>0及代理点数量m_proxy等超参。局限性在于该几何构造依赖可微且可计算符号距离的几何代理不等式，缺乏可微结构的不等式仍只能由有效性检查处理，且所诱导度量不改变硬可行性判定，只提供探索偏置。
