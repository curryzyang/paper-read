# Dynamic Regret and Tightened Constraint Violation for Communication-Efficient Distributed Online Bilevel Optimization

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Fan Li, Xinlei Yi, Guanghui Wen, Yang Shi, Tao Yang
- 机构：Southeast University, Northeastern University, University of Victoria, Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26911v1) · [PDF](https://arxiv.org/pdf/2610.26911v1)

## TLDR
The paper proposes communication-compressed distributed online bilevel optimization algorithms—a single-loop primal–dual method and an adaptive multi-loop variant—that achieve dynamic regret and tightened cumulative constraint violation, with the latter removing dependence on inner-level and gradient path variation.

## Abstract
This paper investigates the distributed online bilevel optimization problem with time-varying inequality constraints. In this setting, a multi-agent network is confronted with a hierarchical decision-making task characterized by coupling between the inner and outer optimization levels. We first propose a communication-efficient single-loop distributed online primal--dual algorithm based on communication compression, which tracks both the inner-level solution and the Hessian-inverse-vector product using only one update per-round. We show that this algorithm achieves a dynamic network regret bound of $\mathcal{O}(T^{\max\{θ_1,1-θ_1\}}+T^{θ_1 } P_T+H_{1,T}+E_{1,T})$, where~$θ_1 \in (0,1)$, $P_T$ is the outer-level path variation, $H_{1,T}$ is the inner-level path variation, and $E_{1,T}$ is the gradient path variation alongside a network cumulative constraint violation bound of $\mathcal{O}(T^{1-θ_1/2})$, which is further reduced to $\mathcal{O}(T^{1-θ_1})$ under Slater's condition. Furthermore, to eliminate the dependence of regret on the inner-level and gradient path variation, we propose a novel adaptive multi-loop distributed online algorithm to control the inner-level approximation accuracy at each round. By dynamically adjusting the number of inner-level updates based on a gradient-norm tolerance condition, this algorithm yields an improved dynamic network regret bound of $\mathcal{O}(T^{\max\{θ_1,1-θ_1\}}+T^{θ_1 } P_T)$ which depends solely on the outer-level path variation while maintaining the same network cumulative constraint violation bound. Finally, numerical simulations verify the effectiveness of the proposed algorithms.


## 精读解读（中文）
### 一、研究动机
论文针对多智能体网络中的分布式在线双层优化问题，该问题具有内外层耦合、环境时变和时变不等式约束，现有分布式双层算法多面向静态环境且依赖嵌套循环，集中式在线双层算法又未同时处理网络不一致、约束满足和通信压缩；因此需要设计通信高效且具有动态遗憾与累计约束违反保证的分布式在线算法。

### 二、技术方案（Method）
在凸外层、强凸内层和时变不等式约束设定下，将多智能体分层在线决策建模为分布式在线双层优化。首先提出基于通信压缩的单环分布式在线原始-对偶算法：每轮每个智能体仅执行一次内层解跟踪更新和一次 Hessian-逆向量积近似跟踪，并与压缩后的网络共识及原始-对偶约束更新耦合。随后提出自适应多环算法，根据梯度范数容忍条件动态调整每轮内层更新次数以控制内层近似精度，同时保持压缩通信和约束对偶更新。

### 三、结果（Result）
理论分析表明，单环算法达到动态网络遗憾 O(T^{max{θ1,1-θ1}}+T^{θ1}P_T+H_{1,T}+E_{1,T}) 和网络累计约束违反 O(T^{1-θ1/2})，在 Slater 条件下约束违反界收紧为 O(T^{1-θ1})。自适应多环算法将动态网络遗憾改进为 O(T^{max{θ1,1-θ1}}+T^{θ1}P_T)，仅依赖外层路径变化 P_T，并保持相同的累计约束违反界；数值仿真验证了两种算法的有效性。

### 四、结论（Conclusion）
论文首次在分布式在线双层优化中同时实现通信压缩、时变不等式约束处理以及 Slater 条件下的约束违反收紧，并通过自适应内层精度消除遗憾对内层路径变化和梯度路径变化的显式依赖，为通信受限动态网络中的分层在线决策提供了可证明的算法框架。

### 五、方法论与关键技术细节
关键点包括：通信压缩作用于智能体间信息交换，但压缩扰动会经外层迭代传播到内层解跟踪和 Hessian-逆向量积近似，因此需在原始-对偶与跟踪模块中联合分析；Slater 条件下的收紧依赖在正则化拉格朗日中保留原始约束以利用严格可行裕度；超参 θ1∈(0,1) 调节遗憾与约束违反的权衡，路径变化由 P_T、H_{1,T}、E_{1,T} 刻画。复杂度上单环算法梯度查询和 HvP 均为 O(T)，自适应多环约为 O(T log(√T)+H_{1,T}) 与 O(T log T)。局限性在于理论依赖凸外层、强凸内层等假设，且主要用数值仿真验证。
