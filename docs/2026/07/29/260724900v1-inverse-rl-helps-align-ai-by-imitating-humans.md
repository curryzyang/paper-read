# Inverse RL Helps Align AI by Imitating Humans

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Michał Wiliński, Liu Leqi, Chirag Nagpal
- 机构：The University of Texas at Austin, Independent Researcher, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24900v1) · [PDF](https://arxiv.org/pdf/2607.24900v1)

## TLDR
PARED introduces an inverse reinforcement learning approach that recovers an explicit, inspectable reward solely from expert demonstrations—without requiring preference annotations—to align AI via inference-time reranking and on-policy reinforcement learning.

## Abstract
Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following. Current approaches typically use supervised fine-tuning on demonstrations or reinforcement learning with rewards derived from verifiers or human feedback. These paradigms leave an important question underexplored: can demonstrations alone yield an implicit reward that can be inspected, reused, and optimized on-policy to align AI? Motivated by inverse reinforcement learning, we introduce Projected Alignment Reward Estimated from Demonstrations (PARED). PARED recovers the implicit reward underlying expert demonstrations as an explicit function over a small set of response-level features, learned by a lightweight discriminator that separates demonstrations from the policy's own samples in this feature space. Unlike a standard reward model, PARED requires no task-specific preference annotations: demonstrations provide the task-specific supervision, which can be augmented with AI feedback as additional dimensions of supervision. Through experiments involving inference-time reranking and adversarial on-policy RL, we show that the recovered reward improves a base policy without a supervised loss and yields further gains when optimized after standard supervised fine-tuning. Additionally, we demonstrate that PARED can be used for contextual alignment, in which a single policy can be tailored to the preferences of different audiences.


## 精读解读（中文）
### 一、研究动机
当前语言模型对齐方法主要通过监督微调或基于偏好的强化学习，但专家示范仅被用于模仿输出，未能恢复可检查、可复用、可策略优化的隐式奖励。逆强化学习可以推断奖励，但传统方法恢复的奖励往往不透明。PARED 旨在利用逆强化学习从示范中恢复紧凑、可解释的奖励，支持推理时选择和策略优化。

### 二、技术方案（Method）
PARED 使用专家示范和当前策略样本，将每个响应级轨迹 (x, y) 映射到由帮助性、无害性以及 LDA 主题分布构成的 7 维特征空间。一个轻量级逻辑回归判别器在二度多项式展开特征上区分专家与策略样本，其专家似然得分定义为奖励。判别器初始拟合后可在策略优化期间在线重拟合。奖励用于 best-of-N 重排（推理时选择）或作为 KL 正则化的 GRPO 奖励进行 on-policy RL。上下文对齐中为不同受众独立学习判别器，共享策略面向各受众优化对应奖励。

### 三、结果（Result）
在 best-of-N 重排和 on-policy RL 实验中，PARED 奖励改善了基策略（零样本指令微调模型），并在标准监督微调后进一步取得增益。在上下文对齐设置中，单一策略可针对成人和儿童两个受众分别调整，两个受众均获得提升，未发现受众间存在权衡。

### 四、结论（Conclusion）
PARED 通过逆强化学习从专家示范中恢复显式、可解释的奖励，无需任务特定的偏好标注。该奖励可审计、可复用，在推理选择和策略训练中提升对齐，并支持面向不同受众的上下文对齐，为利用示范进行对齐提供了一种新的范式。

### 五、方法论与关键技术细节
特征空间为 7 维（排除长度以避免策略优化中的捷径），使用 L2 正则化逻辑回归作为判别器，在度 2 多项式展开特征上实现特征匹配。在线更新时固定 TF-IDF 和 LDA 变换，仅重拟合判别器权重。RL 使用 GRPO 优化，KL 正则化系数 β 控制偏离参考策略的程度。局限性包括：奖励质量依赖于所选特征空间，且需为每个受众独立训练判别器；示范质量直接影响奖励效用。
