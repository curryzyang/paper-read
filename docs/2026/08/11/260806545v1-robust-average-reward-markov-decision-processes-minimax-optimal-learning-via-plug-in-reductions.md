# Robust Average-Reward Markov Decision Processes: Minimax-Optimal Learning via Plug-in Reductions

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Yuepeng Yang, Yuxin Chen, Yuejie Chi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06545v1) · [PDF](https://arxiv.org/pdf/2608.06545v1)

## TLDR
This paper establishes minimax-optimal sample complexity for learning ε-optimal robust policies in average-reward Markov decision processes under total-variation uncertainty, identifying a perturbation-scale threshold that separates two regimes and proposing reduction-based plug-in algorithms that achieve these rates.

## Abstract
Distributionally robust Markov decision processes provide a principled framework for sequential decision making under model uncertainty. We study how many samples are necessary and sufficient to learn an $\varepsilon$-optimal robust policy under the average-reward criterion. A generative model provides samples from the nominal transition kernel, whereas policy performance is evaluated over $(s,a)$-rectangular total-variation uncertainty sets of radius at most $σ$.
  Let $H_0$ and $H_σ$ denote the nominal and robust optimal bias spans, respectively. We identify $σH_0$ as the perturbation scale separating high- and low-tolerance regimes. Our matching upper and lower bounds show that, up to logarithmic factors, the minimax total sample complexity is $$ NSA \asymp \frac{SA}{\varepsilon^2}\begin{cases} \min\{H_0,H_σ\}, & \varepsilon\gtrsimσH_0,\\ \min\{H_0,H_σ\}+σH_σ^2, & \varepsilon\lesssimσH_0. \end{cases} $$ Here $S$ and $A$ are the numbers of states and actions, and $N$ is the number of samples per state-action pair. The sample complexity consists of a linear-span term that resembles the nominal AMDP results and a robustness-specific term that appears only in the low-tolerance regime. We attain these rates using reduction-based plug-in procedures that select the reduction---nominal or robust---and its discount factor: a span-informed procedure that makes these choices using known span parameters, and a span-agnostic procedure that calibrates both choices from data.


## 精读解读（中文）
### 一、研究动机
长期平均奖励准则更适合持续学习任务，但标准强化学习依赖固定转移核，环境偏差可能使学到的策略失效。分布鲁棒平均奖励MDP通过在名义转移核周围定义不确定集来保证最坏情况下的可靠性能，然而其最小样本复杂度尚不清晰：已有鲁棒方法仅给出关于鲁棒span参数的二次上界，与名义AMDP的线性最优率存在明显差距。本文旨在回答生成模型下，为学到epsilon最优鲁棒平均奖励策略，究竟需要多少样本。

### 二、技术方案（Method）
输入为生成模型对每个状态-动作对采样的N条名义转移样本，以经验转移核作为名义模型P0的plug-in估计，并在(s,a)-矩形全变差不确定集（半径不超过sigma）上评估鲁棒平均奖励。建模上基于鲁棒平均奖励Bellman方程，将鲁棒AMDP求解归约为选择合适的reduction类型（名义或鲁棒）及其折扣因子，再对相应鲁棒折扣MDP进行plug-in求解。关键模块包括两种算法：span-informed过程在已知名义和鲁棒最优偏差跨度H0、Hsigma时直接选择reduction与折扣因子；span-agnostic过程则从数据中校准这两个选择，从而无需预先知道span参数。算法通过经验模型上的鲁棒策略优化输出策略。

### 三、结果（Result）
该文给出了匹配的上下界，证明到对数因子为止的极小极大总样本复杂度为NSA与SA/eps^2乘以分段因子：在高容忍区间eps约大于等于sigma H0时，复杂度为min{H0,Hsigma}；在低容忍区间eps约小于等于sigma H0时，复杂度为min{H0,Hsigma}+sigma Hsigma^2。高容忍区间中，求解名义AMDP即可达到标准率SAH0/eps^2，而采用鲁棒reduction在Hsigma<=H0时可将率改进为SAHsigma/eps^2；低容忍区间则必须计入鲁棒性带来的额外项sigma Hsigma^2。这些结果将此前鲁棒AMDP的二次span上界改进为匹配的极小最优率。

### 四、结论（Conclusion）
该工作完整刻画了分布鲁棒平均奖励MDP在生成模型下的极小极大样本复杂度，识别出sigma H0作为高容忍与低容忍机制的分界尺度，并证明名义与鲁棒span参数H0、Hsigma相互独立、不能互相控制。文中提出的span-informed与span-agnostic两种plug-in reduction算法均可达到最优样本率，说明分布鲁棒性在高容忍区间不产生额外统计代价，仅在低容忍区间需要付出与sigma Hsigma^2相关的额外代价。

### 五、方法论与关键技术细节
关键设定是生成模型提供每个状态-动作对N条独立名义转移样本，总样本数为NSA；性能在(s,a)-矩形全变差不确定集上评估，半径至多sigma。核心参数包括状态数S、动作数A、名义最优偏差跨度H0、鲁棒最优偏差跨度Hsigma和不确定半径sigma，且H0与Hsigma至少为1且彼此独立。算法依赖从鲁棒AMDP到鲁棒折扣MDP的reduction，折扣因子的选择是决定样本率的关键，span-informed算法需要已知span参数，span-agnostic算法通过数据校准折扣因子和reduction类型。方法假设底层MDP满足unichain结构，且结论在总变差不确定性集下成立；复杂度表达均忽略对数因子，并强调低容忍机制中的sigma Hsigma^2项是鲁棒性特有的统计代价。
