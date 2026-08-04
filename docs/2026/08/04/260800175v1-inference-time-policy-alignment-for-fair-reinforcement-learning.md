# Inference-Time Policy Alignment for Fair Reinforcement Learning

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Umer Siddique, Peilang Li, Conor Wallace, Yongcan Cao
- 机构：University of Texas at San Antonio
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00175v1) · [PDF](https://arxiv.org/pdf/2608.00175v1)

## TLDR
The paper introduces an inference-time fairness alignment framework for reinforcement learning that steers a frozen, pretrained policy toward welfare-based fairness objectives via multiplicative policy shaping with a learned critic (QFair), improving fairness without retraining or sacrificing core task performance.

## Abstract
Deep reinforcement learning (RL) agents achieve strong performance by optimizing scalar reward functions. However, once deployed, the policies of these RL agents are often rigid and costly to adapt to new performance criteria. For instance, an agent trained to maximize expected cumulative reward may not accommodate previously unknown stakeholder preferences. Existing approaches to achieve fairness, a type of preference, in RL typically assume that such preferences are known a priori and require complete retraining of the policy under a fairness-oriented metric. Inspired by inference-time alignment in large language models, we investigate the problem of steering a pretrained RL policy toward welfare-based fairness objectives at inference time without updating the base policy's parameters. We formalize inference-time fairness alignment as a policy shaping problem and propose a multiplicative policy shaping framework that adjusts action probabilities using action-dependent welfare scores, thus requiring no modification to the base policy. Our framework is general and compatible with any deep RL agent. Through extensive experiments across multiple domains, we demonstrate that inference-time policy shaping substantially improves welfare-based fairness objectives while preserving core task performance.


## 精读解读（中文）
### 一、研究动机
深度强化学习智能体通过优化标量奖励函数获得强性能，但部署后策略僵化，难以适应新的性能标准（如公平性）。现有公平RL方法通常假设公平偏好已知，并需要完全重训练策略，成本高昂且不适应部署后偏好变化。受大语言模型推理时对齐启发，本文研究在不更新基策略参数的情况下，在推理阶段将预训练RL策略引导至基于福利的公平目标，以降低重新训练成本并提升部署适应性。

### 二、技术方案（Method）
提出乘法策略塑形框架，形式化推理时公平对齐为策略塑形问题。首先构造福利增强MDP，通过引入追踪累积奖励向量的增强状态来恢复非线性福利函数的马尔可夫性；然后离线从基策略rollouts（含轻探索）学习一个轻量级公平评论员QFair网络，该网络以当前状态和累积奖励向量为输入，输出动作相关的福利分数；推理时保持基策略参数冻结，将基策略的动作概率与QFair产生的福利分数相乘并归一化，得到塑形后的策略。该塑形过程还通过KL正则化约束，闭式解为基策略的指数重加权形式，保证福利改善下界。

### 三、结果（Result）
在多个领域的广泛实验中，推理时策略塑形大幅提升了基于福利的公平目标（如广义基尼福利函数），同时保持了核心任务回报，相比直接部署冻结基策略和需要重训练的公平RL方法，实现了无需更新基策略参数的公平对齐。

### 四、结论（Conclusion）
本文首次将推理时对齐范式扩展到具有轨迹级公平目标的顺序决策RL中，证明通过轻量级离线训练的公平评论员进行乘法策略塑形，可在部署时有效引导预训练策略满足福利公平约束，同时保持基性能，为低成本适应新公平偏好提供了新途径。

### 五、方法论与关键技术细节
关键点包括：1) 问题设定为有限视野多目标MDP，标量训练奖励取向量奖励各部分之和；2) 非线性福利函数依赖整个轨迹的累积奖励向量，导致策略非平稳，通过状态增强（附加累积奖励向量）恢复马尔可夫性；3) 训练离线进行，仅需基策略生成的数据和少量探索，无需福利驱动的环境交互，避免昂贵或不安全的训练；4) 塑形策略由闭式指数重加权得到，含KL正则化参数；5) 框架与任意深度RL智能体兼容，动作空间需有限；局限性包括：依赖奖励可分解为多个目标、未考虑状态空间连续性/大动作空间挑战，且公平目标需能表达为福利函数。
