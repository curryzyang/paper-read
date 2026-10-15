# What Information Buys in Active Inference

- 区域：精读区
- 排名：2
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Melih Kandemir, Mustafa Mert Çelikok
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19046v1) · [PDF](https://arxiv.org/pdf/2610.19046v1)

## TLDR
The paper shows that Active Inference’s information gain, once square-root calibrated, serves as a reward-agnostic ℓ1 confidence set for exploration in tabular MDPs, making it preferable to value-specific methods like Bayes-UCBVI when rewards are adversarially chosen from the agent’s data but not when rewards are fixed.

## Abstract
Information-theoretic exploration is of primary interest in methodological studies of reinforcement learning (RL) and computational cognitive neuroscience, while the established RL theory builds regret guarantees on confidence sets. This situation leaves open the conditions under which the information-driven exploration found in nature is more advantageous than the exploration of the established RL theory. We put the state-of-the-art methods of these two paradigms, Active Inference (AIF) and Bayes-UCBVI, on an equal footing: both act through the same state abstraction of a tabular MDP with $S$ states, and their greedy forms differ only in the exploration term. We find that AIF's information gain decays too fast to serve as a confidence width, locking greedy agents that explore by it out of the optimal action. Calibrating the information gain by a square root yields calibrated AIF, which attains regret of order $\sqrt T$ for an exact abstraction, but no better guarantee than Bayes-UCBVI for a fixed reward. When an adversary chooses rewards from the agent's data, Bayes-UCBVI's value-specific widths lock out, whereas calibrated AIF pays a factor $\sqrt S$, which no goal-memoryless agent avoids on some MDP whose start states the adversary also chooses. Calibrated information gain thus acts as a reward-agnostic $\ell_1$ confidence set, preferable to value-specific widths when rewards are chosen from the agent's data, not when they are fixed.


## 精读解读（中文）
### 一、研究动机
信息论探索在强化学习与计算认知神经科学中备受关注，但既有强化学习理论多基于置信集给出遗憾保证，二者优劣条件尚不明确。作者因此研究在何种条件下，自然启发的信息驱动探索比基于置信集的经典探索更具优势，并特别关注探索与状态抽象之间的耦合。

### 二、技术方案（Method）
作者将主动推断（AIF）与Bayes-UCBVI放在同一框架下比较：二者都在具有S个状态的表格型分幕MDP中行动，并使用相同状态抽象，其贪心形式仅在探索项上不同。方法上分析AIF信息增益作为置信宽度的衰减速度，提出用平方根校准信息增益得到calibrated AIF，并在精确抽象、固定奖励以及对手从智能体数据中选择奖励等设定下推导遗憾界与下界。比较的核心是每轮以后验/置信宽度构造奖励上界并贪心选动作，但AIF用奖励无关的信息增益，Bayes-UCBVI用价值特定的宽度。

### 三、结果（Result）
核心发现是AIF的原始信息增益衰减过快，不能作为有效置信宽度，会使贪心智能体被锁死在非最优动作之外。用平方根校准后，calibrated AIF在精确抽象下达到O(sqrt T)遗憾，但在固定奖励下并不优于Bayes-UCBVI。当奖励由对手从智能体数据中选择时，Bayes-UCBVI的价值特定宽度会失效，而calibrated AIF需付出sqrt S因子，且在某些起始状态也由对手选择的MDP上，任何无目标记忆智能体都无法避免该因子。

### 四、结论（Conclusion）
因此，校准后的信息增益可视为一种奖励无关的l1置信集：当奖励并非固定、而是由数据或对手选择时，它比价值特定宽度更可取；当奖励固定时，经典价值特定置信宽度仍更优。该工作澄清了主动推断中信息驱动探索真正“买到”的是什么，并给出了其适用边界。

### 五、方法论与关键技术细节
关键实现点在于：同一表格型MDP与同一状态抽象保证公平比较；贪心策略只差探索项；AIF需将信息增益开平方校准；理论保证涉及精确抽象假设、O(sqrt T)遗憾、sqrt S因子以及对手选择奖励和起始状态的最坏情形。局限是固定奖励时calibrated AIF无额外优势，精确抽象条件限制强，且下界针对无目标记忆智能体；论文以理论/反例分析为主，不依赖深度网络训练或特定超参。
