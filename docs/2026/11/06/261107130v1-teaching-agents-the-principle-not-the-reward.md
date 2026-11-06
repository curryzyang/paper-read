# Teaching Agents the "Principle", Not the "Reward"

- 区域：精读区
- 排名：2
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Shan Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07130v1) · [PDF](https://arxiv.org/pdf/2611.07130v1)

## TLDR
The paper proposes prescriptive policy learning (PPL), which teaches agents higher-level behavioral principles via stepwise key quantities and references instead of reward signals, enabling better, more generalizable policies with fewer samples and no reward.

## Abstract
Reinforcement learning has achieved strong performance in many tasks by letting agents learn from nothing more than a reward signal. However, in more complex tasks, agents still struggle to learn good, generalizable policies, even with carefully designed rewards and abundant samples. We argue that this difficulty stems from the reward decoding burden: designers encode their knowledge of the desired behavior into rewards and penalties, and agents must infer this knowledge from long sequences of noisy scalars. To address this burden, we propose prescriptive policy learning (PPL), which directly teaches agents higher-level knowledge about the tasks, termed principles of behavior, such as how to maintain balance, how to accumulate energy, and how to land smoothly. Through appropriately selected key quantities and references, PPL can directly indicate at every step whether the agent follows the principles and to what extent. Our experiments show that agents can learn good, generalizable policies without any reward. Taught only simple heuristic principles, PPL agents outperform reward-based methods with far fewer samples. Their policies also transfer directly to harder settings and keep performing well, demonstrating their strong generalization ability. In summary, PPL provides a new approach in which rough knowledge of the desired behavior is enough for agents to learn good, generalizable policies, even when the system dynamics cannot be accurately modeled.


## 精读解读（中文）
### 一、研究动机
强化学习依赖奖励信号，但复杂任务中设计者需把行为知识编码为奖励和惩罚，智能体再从长序列含噪标量中反推意图，形成沉重的奖励解码负担，导致策略难以学习且泛化不足。

### 二、技术方案（Method）
提出规定性策略学习（PPL），用人工选定的关键量及其参考值/期望区间构造行为原则，并在每一步评估智能体是否遵循原则及遵循程度，将该原则遵循度直接作为策略学习信号；训练时智能体与环境交互采样并据此更新策略，无需奖励函数，推理时直接执行学得策略。

### 三、结果（Result）
实验表明，仅用简单启发式原则、完全不使用奖励，PPL智能体就能以远少于奖励基线的样本学到较好策略，并超过奖励基线的表现；其策略还能直接迁移到更难设置并保持良好性能，显示出强泛化能力。

### 四、结论（Conclusion）
PPL将教学重点从设计奖励转向直接传授行为原则，说明即使系统动力学无法精确建模，粗略的期望行为知识也足以让智能体学习良好且可泛化的策略，为复杂任务提供了一条不依赖奖励的新路径。

### 五、方法论与关键技术细节
关键先验是用少量关键量和参考值表达行为原则，如保持平衡、积累能量、平滑着陆，并在每步计算遵循程度；方法不依赖奖励塑形，原则可较粗略，适用于动力学难精确建模的场景；具体损失、超参和复杂度摘要未披露，且原则与关键量的选择仍需人工设计，可能构成应用局限。
