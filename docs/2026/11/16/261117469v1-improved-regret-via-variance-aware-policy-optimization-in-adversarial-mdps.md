# Improved Regret via Variance-Aware Policy Optimization in Adversarial MDPs

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ofir Schlisselberg, Alon Cohen, Yishay Mansour
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17469v1) · [PDF](https://arxiv.org/pdf/2611.17469v1)

## TLDR
This paper introduces a variance-aware policy optimization algorithm, VOPO, with a Stability-Matching Bonus and a downstream-dependent unknown-to-known dynamics reduction, achieving improved regret \(\widetilde O(\sqrt{H^3SAK})\) for adversarial MDPs with unknown dynamics and full-information rewards.

## Abstract
We study episodic adversarial MDPs with unknown dynamics and full-information rewards and achieve regret with leading term $\widetilde O(\sqrt{H^3SAK})$. Here $H$ is the horizon, $S$ the total number of states across decision layers, $A$ the number of actions, and $K$ the number of episodes. This improves the two incomparable prior leading terms by factors $\sqrt{S/H}$ and $\sqrt{H^3}$, leaving a factor $\sqrt H$ to the lower-bound scale. We give a reduction from unknown to known dynamics for \emph{downstream-dependent} algorithms, whose policy at step $h$ is computed only from information at steps $h+1$ and onward. This reduces the remaining leading-order gap to finding a downstream-dependent known-dynamics algorithm with $\widetilde O(H\sqrt K)$ regret, which would yield the tight $\widetilde O(H\sqrt{SAK})$ leading term for unknown dynamics. We instantiate the reduction with VOPO, a policy optimization (PO) algorithm. Its improved guarantees follow from a variance-aware analysis enabled by a novel bonus, which we call the Stability-Matching Bonus (SMB). VOPO achieves $\widetilde O(\sqrt{H^3K})$ regret under known dynamics with full information; its $\sqrt H$ gap to the target $H\sqrt K$ rate is inherited by our unknown-dynamics guarantee. We also show that with known dynamics and trajectory bandit feedback, VOPO achieves $\widetilde O(\sqrt{H^2SAK})$ regret. Both known-dynamics guarantees improve the corresponding state-of-the-art PO bounds by a factor $\sqrt H$. A matching lower bound establishes that the full-information rate is tight in one parameter regime.


## 精读解读（中文）
### 一、研究动机
论文针对未知动力学、全信息奖励的回合制对抗性MDP，目标是改进遗憾界并缩小与标准下界Omega(H√(SAK))的差距。此前两个最优领先项O(HS√(AK))与O(√(H^6SAK))互不可比，因此需要新的方差感知策略优化分析来同时改善状态数和视野依赖。

### 二、技术方案（Method）
方法先给出从未知动力学到已知动力学的归约，适用于“下游依赖”算法，即第h步策略仅由h+1步及以后的信息计算。内层采用VOPO策略优化算法，交替进行策略评估与局部软策略改进，并引入新的Stability-Matching Bonus（SMB）精确匹配局部更新中的稳定性项；结合方差敏感分析、Profiles处理模型偏差以及适配的quasi-optimism型bonus控制探索，反向计算保证归约所需的下游依赖性。

### 三、结果（Result）
在未知动力学与全信息奖励下取得领先项Õ(√(H^3SAK))的期望遗憾，较O(HS√(AK))改进√(S/H)，较O(√(H^6SAK))改进√(H^3)，距下界尺度仅差√H。已知动力学全信息下VOPO达到Õ(√(H^3K))，轨迹bandit反馈下达到Õ(√(H^2SAK))，均较对应策略优化界改进√H；全信息情形还给出匹配下界，说明该速率在一个参数区域是紧的。

### 四、结论（Conclusion）
论文通过未知到已知动力学的归约和VOPO的方差感知策略优化，显著改进了对抗性MDP未知动力学遗憾界，并把剩余差距具体化为寻找下游依赖的已知动力学Õ(H√K)算法。SMB与方差敏感稳定性分析是获得改进视野依赖的关键，已知动力学策略优化保证也具有独立价值。

### 五、方法论与关键技术细节
关键设定为无环回合制MDP、oblivious对抗奖励、S为各决策层状态总数、A为动作数、H为视野、K为回合数，奖励为全信息或轨迹bandit反馈。技术要点包括下游依赖归约、VOPO局部软策略改进、SMB与稳定性项匹配、方差敏感分析、Profiles控制模型偏差和适配quasi-optimism型bonus；理论工作无实验超参，复杂度以忽略对数因子的遗憾标度表述。局限性是未知动力学结果仍比Omega(H√(SAK))多√H因子，归约依赖尚未实现的下游依赖Õ(H√K)已知动力学算法。
