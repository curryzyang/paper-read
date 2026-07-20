# Stochastic Reset Pathfinding: Path-Level Regret for Cascading Bandits over Graph Paths

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Guni Sharon, Wei Zhang
- 机构：Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15440v1) · [PDF](https://arxiv.org/pdf/2607.15440v1)

## TLDR
This paper introduces Stochastic Reset Pathfinding (SRP), an episodic learning problem on a known graph with unknown edge success probabilities where any failure resets to the source, proposes Log-Dijkstra-based UCB and Thompson Sampling algorithms, and proves a path-level regret bound for PathUCB that decomposes regret via per-path complexity.

## Abstract
We introduce Stochastic Reset Pathfinding (SRP), an episodic learning problem on a known directed graph with unknown stationary edge success probabilities. In each episode, the agent commits to a source-to-goal path, and any edge failure during execution resets it to the source. SRP captures settings such as entanglement distribution in quantum repeater networks, payment routing on the Lightning Network, and delivery in unreliable mesh networks. We show that the global-reset structure makes the optimal policy open-loop, placing SRP within the combinatorial cascading bandit (CCB) framework. We propose a Log-Dijkstra meta-algorithm with UCB (PathUCB) and Thompson Sampling (PathTS) instantiations. Our main technical result is a path-level regret bound for PathUCB that decomposes regret over suboptimal paths via a per-path complexity C(pi) combining each edge's prefix and suffix reliability. The bound is complementary to the edge-level CCB bound and more informative on structured graphs with polynomially many source-to-goal paths. Experiments on quantum-network, layered-DAG, grid-world, and Erdos-Renyi domains support the theory and show that PathTS typically achieves the best empirical performance among the algorithms tested. We then exhibit an adversarial instance on which PathTS fails to converge, consistent with a known exponential obstruction for combinatorial Thompson Sampling on multiplicative-reward problems. We recommend PathTS as the practical default while cautioning that adversarial instances exist.


## 精读解读（中文）
### 一、研究动机
许多现实世界的网络决策问题（如量子中继网络中的纠缠分发、闪电网络中的支付路由、不可靠mesh网络中的投递）要求代理遍历一个已知有向图，其中边的成功概率未知且静止，任何边失败都会导致代理从源节点重新开始。现有方法（如随机最短路径强化学习）因为全局重置结构使得最优策略是开环的而不适用，因此需要将问题建模为组合级联bandit并发展新的路径级遗憾分析。

### 二、技术方案（Method）
本文提出Log-Dijkstra元算法：在每个回合t，基于当前边成功概率估计值p̂_e(t)，使用Dijkstra算法在权重w_t(e) = -log p̂_e(t)上计算从源v_s到目标v_g的最短路径作为选择路径π_t；随后尝试遍历π_t，按顺序观察每条边的结果直到第一次失败或全部成功，并更新前K条边的估计。算法有两种实例：PathUCB采用UCB估计，初始设p̂_e=1，对已探索边使用clip(̄p_e + sqrt(ρ ln t / N_e), p_min, 1)以保持乐观；PathTS采用Beta-Bernoulli后验采样，从Beta(α_e, β_e)中采样后clip到p_min，默认先验为Beta(1,1)。元算法循环执行选择、遍历、更新过程，直至T个回合结束。

### 三、结果（Result）
主要理论结果是PathUCB的路径级遗憾界：R(T) ≤ ∑_{π∉Ψ^*} (C(π)^2 ln T) / Δ(π)，其中C(π)是路径复杂度，结合每条边的前缀可靠性（观测到该边的概率）和后缀可靠性（估计误差对后续边的影响），Δ(π)是路径π与最优路径的可靠性差距。实验在量子网络、分层有向无环图、网格世界和Erdos-Renyi随机图四个领域上进行，显示PathTS通常取得最佳经验性能，而PathUCB次之；但存在一个对抗实例使得PathTS线性遗憾，验证了组合Thompson Sampling在乘性奖励上的指数障碍。

### 四、结论（Conclusion）
本文形式化并解决了随机重置寻路问题，证明了开环策略的最优性，将其归入组合级联bandit框架，并设计出基于Log-Dijkstra的PathUCB和PathTS算法。PathUCB提供了新颖的路径级遗憾界，优于边级界；PathTS在实践中表现优异，但存在对抗脆弱性。推荐PathTS作为默认选择，同时建议用户注意其在对实例下的风险。

### 五、方法论与关键技术细节
关键细节包括：边成功概率下界p_min > 0确保权重有限；PathUCB探索参数ρ ≥ 2足够保证遗憾界；PathTS使用无信息Beta(1,1)先验，采样后下界裁剪到p_min作为安全网；路径复杂度C(π)依赖前缀可靠性和后缀影响，分解遗憾时考虑了观测概率和下游误差传播；算法的计算复杂度由Dijkstra主导，适合路径数量为多项式的图；局限性在于PathTS缺乏理论遗憾界且存在对抗失败实例，PathUCB的界保守且依赖p_min已知；实验中的对抗实例使用三路径构造，乘性奖励导致TS指数级探索困难。
