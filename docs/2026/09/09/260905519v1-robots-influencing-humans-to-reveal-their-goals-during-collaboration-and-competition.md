# Robots Influencing Humans to Reveal their Goals during Collaboration and Competition

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Debasmita Ghose, Oz Gitelson, Michal Lewkowicz, Jake Brawer, Marynel Vazquez, Brian Scassellati
- 机构：Yale University, University of Colorado, Boulder, Massachusetts Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05519v1) · [PDF](https://arxiv.org/pdf/2609.05519v1)

## TLDR
TLDR: This paper proposes a unified robot planning framework that actively guides humans toward "Critical Decision Points"—states where competing human goals prescribe different actions—to achieve faster and more accurate goal inference in both collaborative and competitive human-robot tasks.

## Abstract
We propose a unified strategy for fast goal inference in human-robot interaction. The core idea is to drive the human toward Critical Decision Points (CDPs)-states where competing human strategies prescribe different next actions and thus maximally reveal the goal. We formalise CDPs using a goal-conditioned policy divergence measure and incorporate them into a Receding-Horizon Planner that explores future action sequences while optimizing a cost function balancing task progress and information gain. We evaluate this approach in both a collaborative, fully observable cooking task and a competitive, partially observable hide-and-seek game, each in simulation and on real robots. In both scenarios, our method infers human goals more accurately and earlier than baseline strategies.


## 精读解读（中文）
### 一、研究动机
在人与机器人共享环境的交互中，机器人需要快速推断人类的高层目标，但标准被动式贝叶斯推断在动作重叠、部分可观测或对抗性条件下收敛过慢，导致长时间的不确定性。关键洞察是某些状态比其他状态能更有效地揭示人类目标，因此提出主动引导人类到达这些“关键决策点”（CDPs）以加速目标推断。

### 二、技术方案（Method）
提出一种统一的目标推断策略，核心是用目标条件策略散度度量形式化关键决策点（CDP），即不同人类策略会规定不同下一动作的状态；将CDP纳入滚动时域规划器（Receding-Horizon Planner），通过扩展未来动作序列树，在平衡任务进度与信息获取的代价函数下选择机器人动作，主动影响人类走向CDP。在每个时间步，机器人基于观测到的人类动作用贝叶斯过滤更新对目标集合的信念，并依据策略库中的边际策略计算似然。该方法在协作、完全可观测的烹饪任务和竞争、部分可观测的捉迷藏游戏中分别以仿真和实物机器人验证；烹饪任务中人类与机器人协作制作多份餐食，捉迷藏中机器人作为搜寻者估计人类藏匿策略，CDP可在空间状态网格上预计算。

### 三、结果（Result）
在两个场景中，所提方法均比基线策略更早、更准确地推断出人类目标。烹饪任务中，主动引导人类至CDP使得机器人能更早澄清意图，从而调整自身行为以减少冗余或冲突努力；与信息增益最大化方法（如sadigh2016）和Bayesian Delegation（wu2021）相比，所提方法在目标动作序列重叠时更有效。捉迷藏游戏中，机器人引导藏匿者到CDP相比随机探索地图或仅当可见时最小化距离的基线，能更快抓住人类藏匿者。

### 四、结论（Conclusion）
研究表明，机器人可以利用共享环境中少量信息量极高的状态（CDP），通过主动影响人类行为来显著加速目标推断，该策略在协作与竞争、完全与部分可观测、动作时间依赖与独立等多种条件下均有效，是首个统一跨越合作与竞争交互的目标预测方法。

### 五、方法论与关键技术细节
关键细节包括：完整环境状态定义为s=(s_w,s_h,s_r)，机器人通过传感器接收噪声/部分观测；假设交互为回合制，机器人基于任务级状态表示规划；目标集合有限且候选策略库P_g包含多种真实人类策略，全策略库为各目标策略库的并集，人类真实目标策略在交互中恒定；信念采用均匀先验，似然通过对策略库中所有策略取平均的边际策略计算，并用贝叶斯过滤更新。CDP由目标条件策略散度形式化，RHP规划器在推断时权衡任务进度与信息增益。局限性方面，需要预先提供候选目标集合与策略库，且假设人类目标不中途切换；当前实验场景为烹饪和捉迷藏，尚需在更复杂或更大规模任务中验证可扩展性。
