# Tail-Likelihood Reinforcement Learning

- 区域：精读区
- 排名：4
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Shrinivas Ramasubramanian, Daman Arora, Fahim Tajwar, Guanning Zeng, Qingyang Wu, Zhongzhu Zhou, Chenfeng Xu, Haiwen Feng, Yuda Song, Aarti Singh, Ruslan Salakhutdinov, J. Andrew Bagnell, Jeff Schneider, Andrea Zanette
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02987v1) · [PDF](https://arxiv.org/pdf/2609.02987v1)

## TLDR
Tail-Likelihood Reinforcement Learning (TailRL) optimizes the log-probability of exceeding randomly chosen reward thresholds—instead of only average reward—so that generative policies retain and leverage rare, high-reward rollouts, leading to better training outcomes and greater benefits from additional samples at inference.

## Abstract
Reinforcement learning typically optimizes average reward. For generative policies, the average can hide an important distinction: two policies can achieve the same mean reward while having very different chances of producing a rare but high-reward rollout. This matters as sampling increases during training and inference, since its benefit depends on retaining probability mass on high-reward outcomes. We propose to optimize this coverage directly. Rather than considering only expected reward, we consider all of its upper tails: for each reward threshold, how likely is the policy to exceed it? This turns a continuous reward into a family of binary success events. We introduce Tail-Likelihood Reinforcement Learning (TailRL), which maximizes the log-probability of exceeding a randomly chosen reward threshold. Its gradient gives more weight to rare, high-reward rollouts and can be interpreted as a mixture of Best-of-(k) gradients. TailRL requires only a simple modification to the advantage function, making it compatible with existing reinforcement learning pipelines. Across object localization, maze navigation, GUI grounding, and code optimization, TailRL leverages rare high-reward training samples to avoid suboptimal solutions and yields models that benefit more from additional samples at inference time.


## 精读解读（中文）
### 一、研究动机
标准强化学习通常优化平均奖励，但对生成策略而言，平均奖励会掩盖关键差异：两个策略可能有相同的期望回报，却在产生稀有高回报轨迹的概率上差别很大。随着训练和推理时采样数量增加，其收益取决于是否在高奖励结果上保留概率质量，因此需要直接优化这种上尾覆盖而非仅关注均值。

### 二、技术方案（Method）
TailRL将连续奖励转化为一族二值成功事件：对每个奖励阈值，衡量策略输出超过该阈值的概率，并最大化超过随机采样阈值的对数概率。其核心仅是对优势函数做简单修改，使策略梯度给予稀有高回报轨迹更大权重；该梯度可被解释为一系列Best-of-k梯度的混合。整个方法可直接嵌入现有强化学习管线，输入为标准生成任务数据，输出为策略模型，训练使用策略梯度更新。

### 三、结果（Result）
在目标定位、迷宫导航、GUI grounding和代码优化四个任务上，TailRL能够利用稀有高奖励训练样本规避次优解，并使模型在推理时随采样数量增加获得更大的收益提升，优于仅优化平均奖励的基准方法。

### 四、结论（Conclusion）
研究表明，直接优化上尾概率而非期望奖励是更契合生成式策略采样特性的RL准则；该方法实现简单且能显著改善稀有高奖励场景下的最终性能，为后续研究提供了可扩展的新方向。

### 五、方法论与关键技术细节
关键点在于将连续奖励建模为超过随机阈值的二值事件，从而把上尾覆盖转化为一族可选目标；对优势函数的改动即插即用，兼容现有RL流程。梯度形式可视为Best-of-k梯度的混合，天然突出稀有高回报样本。局限性包括论文预览未给出具体数据集、超参数、阈值采样分布或计算复杂度，量化细节需查阅完整论文。
