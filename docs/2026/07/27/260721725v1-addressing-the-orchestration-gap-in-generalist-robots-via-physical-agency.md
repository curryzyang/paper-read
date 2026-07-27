# Addressing the Orchestration Gap in Generalist Robots via Physical Agency

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Liane Galanti, Dhruv Shah, Tri Dao
- 机构：Princeton University, Together AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21725v1) · [PDF](https://arxiv.org/pdf/2607.21725v1)

## TLDR
Pigey introduces a closed-loop, inference-time orchestrator that decomposes robotic reasoning into a high-level manager and frozen low-level skills, bridging the orchestration gap and achieving over 4x improvement on LIBERO-PRO without any extra training or data.

## Abstract
General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities into the learned policy via large-scale pre-training. Instead, we show that these capabilities can be decomposed into a general language-conditioned policy/control agent and a high-level agent manager/orchestrator. Rather than training policies to reason via pre-training, we build a closed-loop physical agent orchestrator that can do high-level planning, decompose the goal into achievable subgoals, command low-level motor commands, track and verify the outcome from low-level observations, and recover from failures. Our Physical Agency orchestrator (Pigey) can control existing vision-language-action (VLA) policies as well as parametrized skills to solve complex reasoning tasks in the real world, without any additional data collection or post-training. We evaluate Pigey extensively across simulation benchmarks and challenging real-world robotic manipulation tasks, and demonstrate significant performance improvements over existing generalist policies. On LIBERO-PRO, Pigey advances the state-of-the-art by over 4x (12.8% -> 53.3%) with no task-specific fine-tuning. On a real robot, Pigey lifts the frozen policy from near-zero to over 90% on reasoning-limited tasks. We call the difference between what frozen motor skills achieve alone and inside the agentic loop the orchestration gap.


## 精读解读（中文）
### 一、研究动机
现有通用机器人通过大规模预训练将感知、推理、规划等能力融合到单一策略中，但这种方法在处理否定、世界知识、进度跟踪和恢复等任务时存在局限，因为机器人数据和推理解决不同问题，且失败原因难以归因。作者提出将能力分解为低层语言条件控制代理和高层代理管理器，通过推理时闭环编排来弥补编排差距。

### 二、技术方案（Method）
Pigey是一个物理代理编排器，使用前沿VLM作为闭环代理：读取当前观测和交互历史，发出工具调用，选择冻结的底层后端执行子目标，验证结果并在失败时恢复。后端包括用于刚性物体精确抓取放置的TAMP规划器和用于可变形接触丰富动作的π0.5 VLA，两者均不接收抽象指令，只执行短子目标。流程包括高层规划、目标分解、命令低层电机命令、跟踪和验证观测结果、失败恢复，无需额外数据收集或后训练。

### 三、结果（Result）
在LIBERO-PRO基准上，Pigey将冻结策略的成功率从12.8%提升至53.3%，提升超过4倍且无需任务特定微调。在真实机器人上，Pigey将推理受限任务的成功率从接近零提升至超过90%。直接提示与代理条件下的性能差异清晰定义了编排差距，该差距主要出现在世界知识、条件、多步骤和恢复任务上，而简单抓取放置任务不受影响。

### 四、结论（Conclusion）
机器人数据和推理解决不同问题：演示教策略如何行动，而Pigey决定何时、为什么、以什么顺序、使用哪种技能行动。编排循环弥补了编排差距，使冻结策略在推理受限任务上显著成功，将成功归因于推理时闭环而非额外训练。

### 五、方法论与关键技术细节
使用冻结的VLM（如Gemini等）作为编排器，无需任何额外训练；后端包括TAMP规划器和π0.5 VLA，均为冻结且未为本文训练；循环中设置最大工具调用次数T_max作为停止条件；验证和恢复依赖VLM从通用预训练中获得的感知和推理能力，无需专门模块；局限性包括对VLM泛化能力的依赖、最大调用次数可能限制复杂任务、以及真实世界场景的不可预测性。
