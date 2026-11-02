# Approximate Dynamic Programming for Link Reconfiguration to Reduce Malicious Input Controllability in Consensus Networks

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Nathaniel Mailhot, Mohammad Pirani, Davide Spinello
- 机构：University of Ottawa, Carleton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40919v1) · [PDF](https://arxiv.org/pdf/2610.40919v1)

## TLDR
This paper proposes an approximate dynamic programming method that learns which additional communication link to activate after observing the currently attacked sensor, reducing malicious-input controllability in consensus networks without constructing the full Gramian payoff matrix and achieving near-exact-DP performance.

## Abstract
Communication links influence how strongly a malicious input at one sensor affects a consensus network. We study how a defender can reduce this influence by selecting one additional link after observing the currently attacked sensor. The attacked sensor changes over time, and vulnerability is measured by the trace of a finite-horizon controllability Gramian. A prescribed local epsilon-greedy attacker response rule defines a discounted Markov decision process for the defender. Exact dynamic programming (DP) provides an optimal policy using the full Gramian payoff matrix and attacker transition model. We then introduce approximate dynamic programming (ADP) that learns from sampled attacker transitions and empirical Gramian costs estimated from measured impulse responses. Under conditionally unbiased costs and standard sampling and learning-rate conditions, the learned action-value table converges to the exact DP solution. The analysis uses Bellman contraction and bounds the effect of persistent Gramian estimation bias, establishing when measured responses recover optimal defender decisions without constructing the full payoff matrix. In simulations on 20- and 100-node graphs, empirical ADP rollout costs are within 0.23% and 1.76%, respectively, of exact DP. In a two-dimensional intruder tracking example, both policies reduce network-wide root-mean-square tracking error spread by approximately 25% relative to an unmitigated attack.


## 精读解读（中文）
### 一、研究动机
共识网络中通信链路会决定单一传感器处恶意输入对全网状态的影响强度。防御者在观测到当前被攻击传感器后，只能激活一条额外链路来降低有限时域可控性格拉姆矩阵迹所度量的脆弱性。由于被攻击传感器随时间变化且防御动作会改变下一次攻击转移，需要研究序贯链路重构策略。

### 二、技术方案（Method）
将基础共识图、候选额外链路及防御后拉普拉斯矩阵作为输入，以被攻击节点为MDP状态、额外链路为动作，并用有限时域可控性格拉姆矩阵迹构造单阶段代价；给定攻击者局部epsilon-greedy响应规则后形成带动作依赖转移概率的折扣MDP。精确方案先计算全部被攻击节点与防御动作对应的Gramian代价矩阵并求解Bellman方程得到最优策略，再引入ADP，用采样得到攻击者转移和由实测脉冲响应估计的经验Gramian代价更新动作价值表，推理时在每个被攻击状态选择最小学习动作价值对应的链路。

### 三、结果（Result）
精确DP给出利用完整Gramian代价矩阵和攻击转移模型的最优防御基准。ADP在条件无偏代价及标准采样和学习率条件下收敛到精确DP解，并能界定持续Gramian估计偏差的影响；在20节点和100节点图仿真中，经验ADP rollout代价分别与精确DP相差约0.23%和1.76%。在二维入侵者跟踪示例中，两种策略相对未缓解攻击均将全网均方根跟踪误差离散度降低约25%。

### 四、结论（Conclusion）
研究表明，防御者无需预先构造完整可控性代价矩阵，也可通过采样攻击转移和实测脉冲响应学习近最优链路重构策略。该框架把移动攻击下的链路防御表述为序贯网络重构，并在给定攻击响应规则与估计偏差足够小的条件下恢复最优防御决策。

### 五、方法论与关键技术细节
关键假设包括代价条件无偏、攻击转移可采样、标准学习率条件以及有限时域Gramian估计偏差有界；分析利用Bellman收缩性在无穷范数下证明收敛并约束持续偏差影响。实现上每阶段仅激活一条额外链路，基础边数保持不变，攻击者按局部移动半径和epsilon探索规则转移，平局选最小节点编号，且需设定折扣因子和Gramian时域。精确代价矩阵可利用共享特征分解将构造复杂度降至约O(mn^3)，而逐对Gramian实现约为O(mn^4)；局限性在于攻击者响应规则为预设、仿真规模有限且持续估计偏差会影响最优决策恢复。
