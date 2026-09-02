# Elite-Weighted Supervised Fine-tuning for Goal-Directed Molecular Optimization

- 区域：精读区
- 排名：4
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Shiyun Wa, Yifei Wang, Anna G. Green, Simone Sciabola, Ye Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00189v1) · [PDF](https://arxiv.org/pdf/2609.00189v1)

## TLDR
TLDR: The paper proposes Elite-Weighted Supervised Fine-tuning (EW-SFT), a unified, architecture-agnostic molecular optimizer that uses rewards only to select high-scoring molecules and then fine-tunes any generator with its native pretraining loss, consistently outperforming trajectory-level RL across diverse generators, design tasks, and oracles.

## Abstract
Goal-directed optimization is essential for steering molecular generators to propose candidates with desired properties. However, it is often implemented with policy-gradient reinforcement learning, which requires a generation-trajectory log-probability whose form depends on the model architecture and generation procedure. This makes an optimizer difficult to reuse across architectures and conditional generative designs. Supervised fine-tuning needs none of that machinery, but its update is driven by a fixed dataset, so the reward never enters the update. We introduce Elite-Weighted Supervised Fine-tuning (EW-SFT), which uses reward to guide elite selection of high-scoring molecules, and updates the model by its own pretraining loss on that set. Ablations show that reward information is passed primarily through elite selection, rather than through continuous weighting within the selected set. Because the update consumes only scored molecules and the model's native loss, the same rule applies across autoregressive, masked-diffusion, and discrete-flow generators, and across de novo, motif-extension, and linker-design tasks. Under a fixed budget of 3D shape alignment oracle calls on two kinase reference compounds, EW-SFT consistently outperforms the corresponding native optimizers. It further improves goal-directed optimization under a 2D similarity oracle on four held-out references and achieves comparable performance on a sample-efficiency benchmark without a trajectory-level RL formulation. These results demonstrate that EW-SFT is a unified and effective optimizer across molecular generators, design constraints, references, and oracles.


## 精读解读（中文）
### 一、研究动机
目标导向的分子优化需要让生成模型产出具有期望性质的候选分子，但现有方法常依赖策略梯度强化学习，需要计算与模型架构和生成过程绑定的轨迹对数概率，导致优化器难以在不同架构与条件生成设计间复用；监督式微调虽然无需该机制，但其更新只由固定数据集驱动，奖励并未进入更新过程。为此提出一种统一且高效的优化方法。

### 二、技术方案（Method）
提出精英加权监督式微调（EW-SFT）：利用奖励筛选出高评分分子构成精英集合，模型仅在该集合上使用自身的预训练损失进行更新，不依赖轨迹级对数概率。消融表明奖励信息主要通过精英选择传递，而非集合内的连续加权。由于更新只消耗已评分分子与模型原生损失，同一规则可适用于自回归、掩码扩散和离散流生成器，并支持从头设计、基序扩展和连接子设计等任务。

### 三、结果（Result）
在固定3D形状对齐oracle调用预算下、针对两个激酶参考化合物，EW-SFT持续优于对应的原生优化器；在2D相似性oracle下对四个留出参考化合物进一步改进了目标导向优化，并在样本效率基准上达到与轨迹级RL相当的性能。

### 四、结论（Conclusion）
EW-SFT是一种跨分子生成器、设计约束、参考化合物和oracle均有效的统一分子优化方法，摆脱了强化学习轨迹公式化的限制，同时实现了优于或媲美原生优化器的表现。

### 五、方法论与关键技术细节
关键细节包括：精英集合由奖励排序筛选高评分分子形成；模型更新采用其预训练阶段的原生损失，不引入额外RL目标；奖励信息主要作用于顶层精英选择而非内部连续加权；方法天然兼容不同生成架构（自回归、掩码扩散、离散流）及多种分子设计任务；评估使用固定oracle调用预算，涵盖3D形状对齐和2D相似性两类oracle；局限性可能在于依赖采样分子的质量与oracle评分预算，原文未提供超参与复杂度分析的具体细节。
