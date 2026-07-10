# Principled Analysis of Deep Reinforcement Learning Evaluation and Design Paradigms

- 区域：精读区
- 排名：4
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Ezgi Korkmaz
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07769v1) · [PDF](https://arxiv.org/pdf/2607.07769v1)

## TLDR
This paper theoretically and empirically demonstrates that standard evaluation and design paradigms in deep reinforcement learning can lead to incorrect conclusions due to non-monotonic scaling relationships with data.

## Abstract
Starting from the utilization of deep neural networks to approximate the state-action value function that led to winning one of the most challenging games, to algorithmic advancements that allowed solving problems without even explicitly stating the rules of the challenge at hand, reinforcement learning research has been the center of remarkable scientific progress for the past decade. In this paper, we focus on the key ingredients of this research progress and we analyze the canonical evaluation and design paradigms in reinforcement learning. We introduce the theoretical foundations of scaling laws in reinforcement learning and show that the asymptotic performance of reinforcement learning algorithms does not have a monotone relationship between performance rankings and data-regimes. We conduct large-scale experiments and our results demonstrate that a line of reinforcement learning research under the canonical design and evaluation paradigms resulted in incorrect conclusions. Our analysis and results provide a core analysis on scaling, capacity and complexity of deep reinforcement learning.


## 精读解读（中文）
### 一、研究动机
当前深度强化学习的评价与设计范式可能存在系统性偏差，导致研究结论不可靠。本文旨在通过理论分析与大规模实验，揭示规范范式下算法性能排名与数据区域之间的非单调关系，从而纠正错误结论。

### 二、技术方案（Method）
首先建立强化学习缩放定律的数学理论基础，推导算法渐近性能与数据规模的关联形式。然后设计大规模实验，在多种任务（如Atari、MuJoCo等）上比较不同深度强化学习算法（如DQN、PPO、SAC等）在不同数据规模（从少样本到极大样本）下的性能表现，记录排名随数据量的变化。通过对比分析，检验现有评价范式下结论的稳定性。

### 三、结果（Result）
实验表明，强化学习算法的渐近性能与数据区域之间不存在单调关系：在数据量较小时排名靠前的算法，在大数据量下性能可能落后；反之亦然。这意味着大量基于单一数据规模的对比研究得出了误导性结论，整体上规范评价范式存在重大缺陷。

### 四、结论（Conclusion）
当前深度强化学习的标准评价与设计范式未能考虑缩放效应，导致许多公开结论不可靠。研究者应重新审视这些范式，引入基于缩放定律的多尺度评估方法，以确保算法比较和设计选择的鲁棒性。

### 五、方法论与关键技术细节
关键细节包括：缩放定律的理论推导基于统计学习理论，假设模型容量与数据规模匹配；实验覆盖了从少量（如10万帧）到海量（如2亿帧）的数据量范围；性能排名反转现象在多个任务中一致出现；该方法揭示了现有基准（如Atari 100k）的局限性，但结论可能受限于训练计算资源和环境多样性，未来需在更广泛领域验证。
