# Learning from Unreliable Trajectories: Adversarially-Robust Federated Q-Learning

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Sreejeet Maity, Aritra Mitra
- 机构：North Carolina State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06918v1) · [PDF](https://arxiv.org/pdf/2610.06918v1)

## TLDR
The paper introduces **Robust Async-Fed-Q**, an epoch-based federated Q-learning algorithm that preserves the sample-efficiency gains of collaboration among honest agents even when a fraction of agents adversarially corrupt their communications, with finite-time guarantees, nearly matching information-theoretic lower bounds, and improved communication complexity under asynchronous sampling.

## Abstract
We study federated reinforcement learning in which multiple agents interact with a common Markov decision process and communicate through a central server to collaboratively learn the optimal state-action value function. Our goal is to understand whether the sample-efficiency benefits of collaboration can be retained when a fraction of the agents behave adversarially and transmit arbitrarily corrupted information. To address this problem, we introduce Robust Async-Fed-Q, an epoch-based federated learning algorithm that combines variance-reduced estimation of the Bellman optimality operator at the agents with robust aggregation at the server. We establish high-probability finite-time guarantees showing that the proposed method preserves the statistical gains of collaboration among the honest agents while tolerating adversarial corruption. In particular, the effect of the adversarial agents decreases as the amount of data collected by each honest agent grows and eventually vanishes in the infinite-sample limit. We complement these guarantees with information-theoretic lower bounds that characterize the unavoidable statistical cost of adversarial corruption, leading to the first nearly matching upper and lower bounds for adversarially robust federated reinforcement learning. We further extend our framework to accommodate single-trajectory Markovian sampling and heterogeneous partial coverage, where different agents may explore different regions of the state-action space and learning relies on their collective coverage. Finally, our epoch-based design substantially improves the best known communication complexity for federated Q-learning under asynchronous sampling.


## 精读解读（中文）
### 一、研究动机
联邦强化学习通过多智能体协作提升样本效率，但现有理论与算法大多假设所有智能体可靠且常要求全覆盖，现实中部分智能体可能故障或被对抗性操纵并发送任意损坏信息。核心张力是协作既能降方差也可能引入偏差，因此需要回答更多数据到底帮助还是损害学习，以及能否在异步采样、部分覆盖和低通信成本下保持协作收益。

### 二、技术方案（Method）
本文提出 Robust Async-Fed-Q，一种基于 epoch 的联邦 Q-learning 算法：多个智能体与同一 MDP 交互，在单轨迹异步/Markov 采样下于每个 epoch 内收集样本，构造对 Bellman 最优算子的方差缩减估计，并由服务器用鲁棒聚合规则融合各智能体估计。与传统每轮多次本地更新不同，该方法每个 epoch 只对整个 Q 表做一次同步更新，从而用异步数据实现更精确的同步方向，并扩展到 i.i.d. 采样、Markov 采样以及异构部分覆盖场景。

### 三、结果（Result）
在 i.i.d. 采样下，每智能体 T 个样本时得到高概率 l_inf 误差上界 O~(1/sqrt(λ_min N T) + ε/sqrt(λ_min T))；当 ε=0 时具有对 N 的线性加速并匹配已有联邦 Q-learning 速率，对抗性偏差随 T 增大而衰减并在无穷样本极限消失。信息论下界表明 ε/sqrt(T) 量级的腐坏代价不可避免，因而给出首个近乎匹配的对抗鲁棒联邦强化学习上下界；同时算法通信复杂度对 N 和 T 均为对数级，显著优于既有异步联邦 RL 工作。

### 四、结论（Conclusion）
该工作表明在存在任意对抗智能体时，诚实智能体仍可保留协作带来的统计增益，代价是不可避免但可随样本量消失的腐坏偏差项。它把对抗鲁棒联邦 Q-learning 从理想同步/全覆盖设定推进到异步 Markov 采样与异构部分覆盖，并提供近最优有限时间保证和基本下界，为现实不可靠轨迹数据下的联邦强化学习提供了较完整的理论图景。

### 五、方法论与关键技术细节
关键实现细节包括：对抗模型允许 ε 比例且 ε<1/2 的智能体任意外发损坏信息，MDP 为有限状态动作、折扣、奖励有界，λ_min 刻画最难访问状态动作对的访问频率；算法在每个 epoch 内用样本估计 Bellman 最优算子并做方差缩减，服务器端采用鲁棒聚合，每 epoch 仅一次 Q 表更新；Markov 单轨迹情形用耦合论证处理时间相关性，部分覆盖情形通过每个状态动作对的“信息源智能体”与信息冗余假设获得类似速率。理论贡献还包含信息论下界以刻画 ε/sqrt(T) 腐坏代价，通信复杂度对智能体数 N 和样本数 T 均为对数级；局限在于仍依赖有限 MDP、有界奖励、腐坏比例小于二分之一以及覆盖/采样假设。
