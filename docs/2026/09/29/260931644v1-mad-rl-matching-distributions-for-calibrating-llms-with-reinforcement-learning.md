# MaD-RL: Matching Distributions for Calibrating LLMs with Reinforcement Learning

- 区域：精读区
- 排名：1
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Sourabh Kulkarni, Ksheeraj Sai Vepuri, Basar Demir, Jason Bohrer, Emily Shen, Jianfa Chen, Nan Jiang, Ankit Jain, Harihar Subramanyam, Mannat Singh, Chirag Nagpal
- 机构：Meta Superintelligence Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31644v1) · [PDF](https://arxiv.org/pdf/2609.31644v1)

## TLDR
MaD-RL is a general reinforcement-learning framework that calibrates LLMs by matching the distribution of a latent categorical attribute in their outputs to a specified target distribution, addressing diversity collapse in methods like GRPO via theoretically motivated reward functions for divergences such as KL and Jensen-Shannon, with experiments in mathematical reasoning and programming.

## Abstract
Reinforcement learning (RL) is widely used in language-model post-training to maximize rewards assigned to individual model outputs, such as scores from binary verifiers or reward models trained on human feedback. However, applications such as synthetic-data generation, fairness-related constraint satisfaction, and policy exploration require controlling the distribution of outputs across model generations rather than only maximizing expected reward. We propose a general RL-based framework for \textit{Distribution Matching} allowing matching the distribution of a latent categorical attribute of model outputs to a specified target distribution. Empirically, we demonstrate that dominant post-training recipes such as Group Relative Policy Optimization (GRPO) reduce output diversity by concentrating policy probability towards a single mode. Entropy regularization and sampling temperature can improve the spread of the distribution but have constrained effectiveness, limited to apply only in token space and toward uniform distributions. We show that prior work in this area is a specific case of Distribution Matching involving the $L_2$ divergence. We then propose reward functions for other divergences such as KL and Jensen-Shannon and motivate them with theoretical justification. Finally, we demonstrate the effectiveness of our approach on a set of experiments involving mathematical reasoning and programming.


## 精读解读（中文）
### 一、研究动机
现有RL后训练方法如GRPO主要最大化单条输出的期望奖励，容易把策略概率集中到单一模式并降低输出多样性；而合成数据生成、公平性约束满足和策略探索等任务需要控制模型输出在潜在类别属性上的整体分布，而非仅提高平均奖励。因此，论文提出MaD-RL，用分布匹配来校准LLM的输出分布。

### 二、技术方案（Method）
MaD-RL是一个通用RL式分布匹配框架：给定提示集，从当前策略采样多条输出，用属性识别器或分类器抽取每条输出的潜在类别属性，统计当前生成分布，并与指定目标分布比较；将L2、KL、Jensen-Shannon等散度构造成可优化的奖励函数，插入GRPO等策略优化流程，以优势估计和策略梯度更新LLM。其关键模块包括潜在属性定义与分类、经验分布估计、散度奖励计算、策略采样与优化；训练目标是让模型输出属性分布逼近目标分布。

### 三、结果（Result）
实验发现，GRPO等主流后训练配方会显著降低输出多样性，使策略概率向单一模式集中；熵正则和采样温度虽能改善分布展宽，但效果有限，且主要作用于token空间并趋向均匀分布。MaD-RL在数学推理和编程任务上验证有效，KL与Jensen-Shannon散度奖励可泛化已有L2散度特例，并更灵活地匹配目标分布。

### 四、结论（Conclusion）
分布匹配可作为RL后训练中控制LLM输出属性分布的通用目标，MaD-RL为超越单纯奖励最大化提供了理论依据和可操作的奖励设计。该框架有望用于需要多样性、公平约束或探索控制的生成场景，并扩展至更多潜在属性与目标分布。

### 五、方法论与关键技术细节
关键点在于把输出潜在类别属性的经验分布与目标分布对齐，并将散度作为奖励驱动策略优化；L2散度对应已有工作特例，KL/JS散度带有理论动机。实现上依赖属性分类器可靠性、目标分布设定、散度估计方差、采样预算与计算开销；熵正则与温度只能在token空间和均匀分布附近有限调节。局限性是摘要未给出完整超参、数据规模和具体数值，且实验任务集中在数学推理与编程。
