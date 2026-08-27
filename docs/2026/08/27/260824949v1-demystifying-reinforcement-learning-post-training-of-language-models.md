# Demystifying Reinforcement Learning Post-Training of Language Models

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Donovan Clay, Saket Gollapudi, Sankar Harilal, Min Jang, Jacob Morrison, Sewoong Oh, Natasha Jaques
- 机构：Allen Institute for AI, University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24949v1) · [PDF](https://arxiv.org/pdf/2608.24949v1)

## TLDR
This paper demystifies RL post-training for LLMs by deconstructing its components in controlled experiments, showing how base model priors, reward granularity, prompt diversity, and scale interact to determine success—demonstrating, for example, that spurious rewards' effects depend on prompt distribution and that dense rewards can overcome sparse-reward limitations on learning new behaviors.

## Abstract
Reinforcement learning (RL) post-training has emerged as a powerful framework for enhancing the capabilities of large language models (LLMs), enabling impressive reasoning, math, and coding capabilities. Yet for many researchers and practitioners, the principles behind classical RL remain a "black box". In this work, we deconstruct the RL post-training algorithm, investigating each step to clarify what is actually happening beneath the surface. By isolating the mechanics of RL with Verifiable Rewards in a controlled and simplified environment, we examine how RL outcomes are shaped by the base model's prior distribution, the granularity of the reward signal, the diversity of the prompt distribution, and model scale. We use the entropy of the policy's output distribution as a lens to compare the distributions learned through pretraining, SFT, and RL post-training, revealing how each stage shapes model certainty. Our investigation sheds light on how these choices interact to affect post-training success. For example, we show that the effect of so-called 'spurious rewards' depends on the prompt distribution used for post-training. We also provide insight into why the success of RL post-training depends on whether the base model already places sufficient probability mass on the desired behavior, linking it to the classical concept of exploration in RL. Ultimately, we provide this primer as a resource to those in the NLP community wishing to incorporate RL as a tool in their toolbox.


## 精读解读（中文）
### 一、研究动机
强化学习后训练虽已显著提升大语言模型的推理、数学和编程能力，但其背后的经典强化学习原理对许多研究者和实践者而言仍是“黑箱”，导致文献中出现了相互矛盾或误导性的结论。本文旨在通过受控实验解构RL后训练的每个步骤，澄清基础模型先验分布、奖励信号粒度、提示分布多样性和模型规模如何共同影响后训练的成功率，并为NLP社区提供一份可理解的RL入门资源。

### 二、技术方案（Method）
在受控的序列生成与数学推理环境中，作者系统性地操纵基础模型分布、奖励函数和提示分布三个组件。首先通过SFT+（在目标行为上微调以提高先验概率）和SFT-（在目标行为上最大化交叉熵以抑制概率）构造不同的基础模型初始化，包括目标字符串生成（如电影台词）和AIME 2025数学问题。奖励函数涵盖稀疏的二元验证器、基于Levenshtein距离的密集奖励，以及用于数学推理的过程奖励模型（PRM）。提示分布包括窄域的推理数据集和Tulu-3使用的广泛预训练分布。训练使用带KL约束的RL目标，并以策略输出分布的熵作为透镜，比较预训练、SFT和RL后训练各阶段对模型确定性的影响，同时测量目标行为的概率质量变化。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
RL后训练并非凭空创造新行为，而是对基础模型先验分布进行概率质量再分配；其成功与否取决于基础模型是否已在目标行为上放置足够概率质量，以及奖励信号能否有效引导探索。该研究调和了近期关于“虚假奖励”和“RL是否真能学习新行为”的矛盾结论，为理解RL后训练机制提供了系统性视角，并为构建更有效的后训练流程提供了实用指南。

### 五、方法论与关键技术细节
关键细节包括：使用Base、SFT+、SFT-三种初始化变体分别表示原始基础模型、人工抬高目标先验的模型和人为压制目标概率的模型；目标字符串任务可精确测量行为概率，数学任务使用AIME 2025问题并验证正确答案；稀疏奖励为二元正确性加上长度惩罚，密集奖励使用Levenshtein距离或由LLM-as-judge构建的PRM；训练目标包含KL散度约束以防止语言漂移；提示分布分为窄域（仅数学）和宽域（Tulu-3预训练分布）；采用策略熵作为衡量分布变化的指标；实验基于OLMo 3、Qwen2-7B、Qwen3-1.7B、Qwen2.5-7B-Instruct等不同规模模型。局限性在于实验环境为简化受控场景，可能无法完全反映真实大规模LLM后训练的复杂性。
