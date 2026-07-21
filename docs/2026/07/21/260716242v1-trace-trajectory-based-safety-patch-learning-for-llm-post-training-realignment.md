# TRACE: Trajectory-Based Safety Patch Learning for LLM Post-Training Realignment

- 区域：精读区
- 排名：4
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Changyue Li, Jiaming He, Youliang Yuan, Jialin Wu, Boxi Yu, Zhicong Huang, Pinjia He
- 机构：Ant Group, University of Limerick, The Chinese University of Hong Kong, Shenzhen
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16242v1) · [PDF](https://arxiv.org/pdf/2607.16242v1)

## TLDR
TRACE is a trajectory-based safety patch learning framework that simulates harmful fine-tuning trajectories to learn a disentangled patch, enabling LLMs to recover nearly 100% safety without degrading downstream task utility.

## Abstract
Fine-Tuning-as-a-Service (FTaaS) platforms let users train large language models (LLMs) on customized tasks, but this pipeline could erode models' safety alignment. In practice, service providers need to recover models' safety without re-running full alignment, or destroying the utility gained from customized tasks. A line of existing work refers to model parameter merging, which adds a safety patch on the fine-tuned model parameters to shift the model away from unsafe tendencies. However, this merging-based paradigm is fundamentally bottlenecked by task-safety update entanglement: downstream task updates and the safety patch often overlap in their dominant directions, so the merge strength is intrinsically hard to calibrate. If the safety vector is scaled too weakly, harmful components could still dominate, preventing the model from returning to a safe region; if it is scaled too aggressively, it suppresses task-relevant directions and degrades utility.
  To solve this problem, we shift the focus of merging-based methods from designing online merging operators to offline patch learning, and seek a safety patch that minimally interferes with task-relevant directions while retaining decisive control over unsafe behaviors. We propose TRACE, a trajectory-based safety patch learning framework that (i) simulates harmful tuning trajectories to generate progressively corrupted states, and (ii) optimizes a plug-in patch to recover safety while maintaining utility across varying corrupted base states.
  Across six benchmarks and two models, TRACE consistently dominates the safety-utility frontier. TRACE reaches nearly 100% safety on all settings, while maintaining comparable utility to the undefended fine-tuned model.


## 精读解读（中文）
### 一、研究动机
现有的基于参数合并的后训练安全恢复方法受制于任务-安全更新纠缠问题：下游任务更新和安全补丁在主导方向上重叠，导致合并强度难以校准。安全向量缩放过弱则无法消除有害行为，过强则抑制任务相关方向并降低效用。因此需要一种新的范式，学习一个与任务更新方向解耦且具有决定性控制能力的安全补丁。

### 二、技术方案（Method）
TRACE 提出基于轨迹的安全补丁学习框架，包含两个步骤：(i) 模拟有害微调轨迹，通过逐步对基础模型进行有害数据微调生成从安全到逐渐被破坏的模型状态序列；(ii) 在这些不同破坏程度的基座上优化一个通用可插拔补丁（采用低秩适配器形式），通过最小化安全损失和任务效用损失的联合目标，使得该补丁能够一致地恢复安全同时不干扰下游任务性能。训练完成后，该补丁可直接通过标准参数合并（如加权加法）应用于任何微调模型，无需在线逐用户调整合并系数。

### 三、结果（Result）
在六个基准（三个有害数据集：Shadow、FineTuning、PKU-SafeRLHF；三个效用基准：SAMSum、SQL-Create-Context、GSM8K）和两个模型（Llama-3.1-8B-Instruct、Qwen2.5-7B-Instruct）上，TRACE 在所有设置下达到接近100%的安全率，同时保持了与未防御微调模型相当的效用，在安全-效用前沿上全面优于现有合并方法（如 RESTA、SafeLoRA、SafeDelta 等）。

### 四、结论（Conclusion）
TRACE 通过将合并范式从在线合并操作转变为离线补丁学习，有效解决了任务-安全更新纠缠问题。它学习到的解耦且决定性的安全补丁能够在不牺牲下游任务性能的前提下高效恢复安全性，为 FTaaS 平台提供了一种鲁棒、高效且无需逐用户校准的后训练安全恢复机制。

### 五、方法论与关键技术细节
方法核心是模拟-恢复策略：离线模拟用户不同训练强度导致的有害微调轨迹，生成覆盖安全到不安全状态的模型序列；补丁优化同时使用安全拒绝数据和任务数据，通过联合损失确保补丁在不同基座上的一致性。超参数包括轨迹步数、适配器秩等，实验中使用 LoRA 秩为16；计算开销低（约0.5秒在线合并），且兼容其他干预阶段的方法。局限性：依赖离线模拟轨迹的代表性，如果用户训练强度超出模拟范围可能效果下降；另外对安全数据质量有一定要求。
