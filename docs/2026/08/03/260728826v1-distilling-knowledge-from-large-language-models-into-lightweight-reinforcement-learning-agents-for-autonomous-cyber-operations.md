# Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Konur Tholl, François Rivest, Mariam El Mezouar, Adrian Taylor, Ranwa Al Mallah
- 机构：Royal Military College of Canada, Polytechnique Montreal, Defence Research and Development Canada
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28826v1) · [PDF](https://arxiv.org/pdf/2607.28826v1)

## TLDR
A large cybersecurity-focused LLM can be distilled via online policy distillation into a lightweight RL agent (64,910 parameters) that maintains effective defensive performance in CybORG, offering a scalable path for autonomous cyber operations.

## Abstract
Autonomous Cyber Operations (ACO) are increasingly important for defending enterprise networks as cyber threats continue to evolve in sophistication. ACO applications commonly employ Reinforcement Learning (RL) agents to learn defensive behaviors through interaction with environments. However, RL agents typically require extensive exploration during training, often resulting in unstable behavior and poor initial decision-making before converging toward effective defense strategies.
  In this work, we investigate the use of a Large Language Model (LLM) to improve autonomous defensive decision-making within an ACO environment. Through prompt engineering rather than fine-tuning, we demonstrate that an 8-billion parameter LLM pretrained on cybersecurity data can outperform a baseline RL agent in a modified CybORG CAGE Challenge 2 environment. We then propose an online policy distillation framework that transfers the LLM's defensive policy into a lightweight RL agent containing only 64,910 parameters, reducing model size by several orders of magnitude while maintaining effective defensive capabilities. This provides a pathway toward operationalizing frontier cybersecurity models within lightweight, deployable agents.
  To evaluate transferability, we construct CybORG scenarios ranging from 4 to 12 hosts and assess the approach across varying network configurations. We also evaluate teacher-guided RL stabilization strategies and observe that none consistently surpass the optimized teacher policy, suggesting policy-alignment limitations between reward-driven RL optimization and teacher-guided defense strategies.
  Our results demonstrate the potential of cybersecurity-focused LLMs as sources of expertise for autonomous cyber defense, while policy distillation provides a practical path toward operationalizing frontier cybersecurity models within efficient, scalable agents.


## 精读解读（中文）
### 一、研究动机
自主网络作战（ACO）中，强化学习（RL）智能体通常需要大量探索，导致训练初期决策不稳定且效果差；在网络安全环境中，错误决策可能造成严重后果。同时，大语言模型（LLM）虽具备强大防御决策能力，但参数量大、推理成本高，难以直接部署。因此，本文旨在将8B参数的网络安全LLM的防御策略蒸馏为仅6.5万参数的轻量级RL智能体，在保持防御性能的同时显著降低模型规模，为前沿模型在资源受限环境中的实际部署提供可行路径。

### 二、技术方案（Method）
本文提出在线策略蒸馏框架，分为三个阶段。首先，通过提示工程优化一个在网络安全数据上预训练的8B参数LLM（Cyber Risk Llama），使用角色设定、零样本学习、规则语义和约束链式思维（chain-of-thought scaffolding）构造提示词，仅基于现实可获取的CybORG状态信息生成防御动作，并通过正则匹配与语义相似度提取可执行动作。其次，在蒸馏阶段，LLM作为教师，其推荐动作通过动作掩码（action masking）强制学生RL智能体（仅包含64,910个参数）执行，同时使用教师交叉熵损失L=-log(π_θ(a^teacher|s))更新学生策略，使学生的动作概率分布逐渐对齐教师策略；该过程持续240个回合，之后完全移除教师指导，仅由学生自主决策。最后，为评估可迁移性，构造了4到12台主机共9种不同规模的CybORG场景，保持相同LLM与提示结构，仅调整蒸馏回合数，并与基线PPO智能体、教师引导RL策略进行对比。

### 三、结果（Result）
优化后的提示相比标准提示在CybORG环境中平均奖励约为70，性能提升约35%；蒸馏得到的轻量级智能体（6480回合内，参数仅64,910）在2,000回合内的平均奖励优于基线PPO智能体和教师引导RL智能体。教师引导智能体在初期性能与蒸馏智能体相近，但随训练进行性能明显下降并最终收敛到基线水平，表明奖励驱动的RL优化与教师防御策略之间存在策略对齐问题。在50,000回合（160万时间步）的长训练中，基线PPO的均值性能始终未稳定超越蒸馏智能体，且训练波动大；蒸馏智能体则保持持续稳定。在4到12主机的多种网络拓扑下，蒸馏方法均表现出有效转移性。

### 四、结论（Conclusion）
本文验证了网络安全聚焦的LLM可以作为自主网络防御的专家知识源，并通过在线策略蒸馏有效转移到轻量级RL智能体中，模型规模缩小数个数量级，同时保持与教师相当甚至更优的防御性能。研究还表明，教师引导RL的多种稳定化策略均无法一致超越优化后的教师策略，说明传统奖励驱动的RL优化与教师防御策略之间存在固有的策略对齐局限。该工作为将计算开销大的前沿网络安全模型部署到轻量级、可扩展的智能体中提供了可行途径，并公开了代码与配置以支持复现。

### 五、方法论与关键技术细节
关键细节包括：教师LLM为8B参数的Cyber Risk Llama，学生RL智能体仅含64,910个参数；蒸馏使用动作掩码确保学生始终执行教师推荐的动作，同时用教师交叉熵损失进行参数更新，训练240个回合后停止教师影响；提示工程采用约束链式思维模板，仅包含人类防御者可获得的现实信息，不纳入特权模拟器状态或攻击方TTP；动作提取通过正则匹配和语义相似度回退实现；评估环境为修改的CybORG CAGE Challenge 2，并扩展到4-12主机的9种网络拓扑；蒸馏回合数随网络规模减小而减少；基线采用PPO算法（10次独立运行，50,000回合）；结果显示教师引导RL（逐步衰减教师损失）最终性能退化至基线，验证了策略对齐问题；计算复杂度方面，LLM推理成本远高于学生智能体，但蒸馏后仅需轻量部署。
