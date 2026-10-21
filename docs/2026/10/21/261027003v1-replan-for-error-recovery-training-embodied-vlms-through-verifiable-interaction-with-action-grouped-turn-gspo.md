# Replan for Error Recovery: Training Embodied VLMs through Verifiable Interaction with Action-Grouped Turn-GSPO

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Zhuoran Wang, Keqing Fan, Yang Li, Jinbo Su, Ke Wang, Sijia Luo, Yuanzheng Tan, Junken Peng, Jing Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27003v1) · [PDF](https://arxiv.org/pdf/2610.27003v1)

## TLDR
The paper introduces ERR-Env and ERR-Bench for verifiable error-recovery learning, proposes Action-Grouped Turn-GSPO to train a compact 2B embodied VLM (ERR-VLM), and reports gains of 10.25 points in Strict Success Rate and 22.95 points in Recovery Rate on ERR-Bench.

## Abstract
Embodied VLMs can execute increasingly complex manipulation tasks, yet execution errors can leave the environment in states that require replanning for recovery. Existing recovery methods either rely on inference-time mechanisms with fixed policies or learn from failure examples and reference corrections rather than verified action outcomes. To enable recovery learning through verifiable interaction, we introduce the Embodied Replanning for Recovery Environment (ERR-Env), which provides feedback on task progress and execution errors. We further construct ERR-Bench, a benchmark with held-out tasks spanning nominal, intermediate, and error states for evaluating recovery capability and execution reliability. We then propose Action-Grouped Turn-GSPO (AGT-GSPO), an online reinforcement learning method combining turn-level rewards for task progress and error states with action-grouped advantage estimation, and use it to train ERR-VLM, a compact 2B embodied VLM. Evaluation on ERR-Bench reveals a mismatch between task progress and execution reliability across diverse VLMs. AGT-GSPO improves ERR-VLM by 10.25 percentage points in Strict Success Rate for error-free completion and 22.95 percentage points in Recovery Rate, while ablations and zero-shot transfer further validate the effectiveness of our method.


## 精读解读（中文）
### 一、研究动机
具身视觉语言模型已能执行复杂操作任务，但执行错误会使环境进入需要重新规划才能恢复的状态。现有恢复方法要么依赖推理时的固定策略，要么从失败样例和参考纠正中学习，而不是从可验证的动作结果中学习，因此需要一种通过可验证交互来训练恢复能力的方法。

### 二、技术方案（Method）
论文提出ERR-Env环境，为任务进展和执行错误提供反馈，并构建ERR-Bench基准，覆盖留出任务以及正常、中间和错误状态，用于评估恢复能力与执行可靠性。随后提出AGT-GSPO在线强化学习方法，将面向任务进展和错误状态的轮级奖励与按动作组聚合的优势估计相结合，并用于训练紧凑的2B具身视觉语言模型ERR-VLM，使其通过与环境交互学习重规划恢复。

### 三、结果（Result）
ERR-Bench评估显示多种视觉语言模型在任务进展与执行可靠性之间存在不匹配。AGT-GSPO使ERR-VLM在无误完成任务的严格成功率上提升10.25个百分点，在恢复率上提升22.95个百分点；消融实验和零样本迁移进一步验证了该方法的有效性。

### 四、结论（Conclusion）
通过可验证交互学习恢复，并结合轮级奖励和动作组优势估计的在线强化学习，能够同时提升紧凑具身视觉语言模型的任务执行可靠性和错误恢复能力。该工作表明恢复能力不应仅依赖推理时机制或参考纠正，而可由环境反馈驱动的策略学习获得。

### 五、方法论与关键技术细节
关键设计在于ERR-Env提供任务进展与执行错误两类可验证反馈，ERR-Bench按正常、中间和错误状态组织留出任务以分离评估执行可靠性与恢复能力，AGT-GSPO以轮级奖励建模任务进展和错误状态并用动作组优势估计匹配操作序列的信用分配。摘要层面未给出具体损失函数、超参数和训练规模等实现细节，方法有效性依赖可验证环境反馈，零样本迁移虽有验证，但跨环境和真实场景的泛化与反馈获取成本仍是潜在约束。
