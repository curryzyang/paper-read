# Prompt-Driven Exploration

- 区域：精读区
- 排名：8
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Sunshine Jiang, John Marangola, David Zhang, Raghuram Kowdeed, Ruiyang Luo, Nitish Dashora, Richard Li, Pulkit Agrawal, Zhang-Wei Hong
- 机构：Massachusetts Institute of Technology, Improbable AI Lab, MIT-IBM Computing Research Lab
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08837v1) · [PDF](https://arxiv.org/pdf/2607.08837v1)

## TLDR
Prompt-Driven Exploration (PDE) uses a vision-language model to iteratively refine natural language prompts from policy rollouts, enabling reinforcement learning to escape weak initial policies by inducing global behavioral changes rather than relying on action-level noise.

## Abstract
Exploration is essential to RL since a policy cannot improve by repeatedly sampling the behaviors it already prefers. Standard methods inject stochasticity in the action space, but such jitter only yields rollouts close to the original. Escaping a weak policy often requires global perturbations that action noise cannot produce. Large language models (LLMs) and vision-language-action (VLA) models offer a pathway: they condition the policy on a natural language prompt, and since the rollout follows from it, modifying the prompt induces global changes. The challenge is finding prompts that induce useful global changes. With a weak policy that rarely succeeds, reward is too sparse to select on. Our idea is to refine prompts from the rollouts themselves: a vision-language model (VLM) reasons over the rollout video, diagnoses how the policy responded, and rewrites the prompt to elicit better behavior next time. This procedure realizes posterior sampling, a classical RL exploration framework, at the level of prompts: the VLM maintains an implicit distribution over useful prompts and updates it from observed rollouts. We call this strategy Prompt-Driven Exploration (PDE). Across manipulation and reasoning tasks, PDE enables RL to learn successful policies even from zero-reward starts, and improves sample efficiency more broadly. Our website is available at https://xinyunsunshine.github.io/prompt-rl.


## 精读解读（中文）
### 一、研究动机
标准强化学习的探索通过在动作空间注入随机性来实现，但这仅能产生局部的行为扰动，难以从表现差的初始策略中逃脱。大型语言模型和视觉-语言-动作模型使得策略能够依据自然语言提示进行全局行为改变，但如何自动发现能引发有用改变的提示仍是一个挑战。

### 二、技术方案（Method）
本文提出提示驱动探索（PDE）方法，它利用视觉语言模型（VLM）作为提示采样器，维护一个隐式的提示分布。在每次迭代中，VLM根据任务的规范提示和已收集的轨迹历史，采样一个新的提示并执行策略，得到的轨迹和奖励被加入历史以更新提示分布。RL更新采用Proximal Policy Optimization (PPO)，并引入混合采样（以一定概率从规范提示和VLM采样的提示中选择）和混合反向传播（在PPO比率中使用两种提示下动作概率的平均值），使得探索性提示的 rollout 也能改进规范提示下的策略性能。

### 三、结果（Result）
在LIBERO、LIBERO-PRO和ManiSkill等机器人操控任务上，PDE使从近乎零成功率的弱初始策略出发的RL能够成功学习，并取得比动作空间探索高得多的成功率和样本效率。分析表明VLM的更新有效地将提示分布向能引发成功行为的提示方向移动。此外，在LLM代码生成任务上，PDE同样提升了样本效率，验证了其通用性。

### 四、结论（Conclusion）
PDE通过利用预训练VLM的语言和视觉先验，在提示空间进行后验采样式的探索，使得RL能够低成本地实现全局行为变化，从而克服动作空间探索的局限性。该方法简单且与现有RL算法兼容，为弱初始策略下的强化学习提供了一种有效的探索策略。

### 五、方法论与关键技术细节
关键细节包括：(1) 使用预训练的视觉语言模型（如GPT-4o）作为提示采样器，利用其语言先验生成合理的候选提示；(2) 混合采样系数α随训练进度逐渐增加，以逐步将训练聚焦到规范提示；(3) 混合反向传播损失迫使动作在探索提示和规范提示下都具有较高的概率，从而实现知识迁移；(4) 方法依赖VLM对轨迹的理解和改写能力，可能存在计算开销较大及对VLM质量敏感的局限性。
