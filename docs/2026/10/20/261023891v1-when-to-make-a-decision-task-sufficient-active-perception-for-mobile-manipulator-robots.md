# When to Make a Decision: Task-Sufficient Active Perception for Mobile Manipulator Robots

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Mariana da Silva Barros, Matthias Kerzel, Cornelius Weber, Stefan Wermter
- 机构：University of Hamburg
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23891v1) · [PDF](https://arxiv.org/pdf/2610.23891v1)

## TLDR
The paper proposes a hybrid neuro-symbolic framework that enables mobile manipulator robots to decide when task-relevant uncertainty is sufficiently resolved to act, by selecting among exploration, inspection, user clarification, and task execution in an uncertainty-aware decision loop.

## Abstract
A robotic agent operating in an unknown environment must gather sufficient task-relevant information before acting. However, determining when the available information is sufficient remains a challenge. We propose a conceptual hybrid neuro-symbolic framework for task-sufficient active perception in unknown environments. After interpreting a requested task, the agent generates an initial plan and iteratively reevaluates it as new information becomes available. At each iteration, it can acquire a more informative viewpoint, inspect or manipulate candidate objects, ask the user for clarification, or perform the task. Neural perception modules update an object-centric belief state, while a symbolic decision layer determines whether the remaining uncertainty justifies further information gathering. The framework will be implemented on a mobile manipulator comprising a humanoid torso and a mobile base, with complementary evaluation in simulation. The proposed approach aims to enable robots to determine not only how to gather additional information, but also when further perception is no longer necessary.


## 精读解读（中文）
### 一、研究动机
机器人在未知且动态的环境中执行任务前，必须收集足够的任务相关信息，但现有方法常将规划、感知、探索和交互分离，导致机器人可能收集无关信息或信息不足，核心难题是判断当前知识何时对任务执行已经充分。

### 二、技术方案（Method）
论文提出一个混合神经符号框架：用大语言模型将自然语言任务解释为结构化任务表示，用CNN或Transformer检测、语义分割及VLM视觉语言 grounding 更新以对象为中心的语义记忆信念状态；符号决策层结合神经感知不确定性、空间不确定性和任务级不确定性，在主动感知（基于Next-Best-View选择期望降低语义不确定性的视角）、对象检查或操作、向用户澄清、执行任务之间迭代选择，并用行为树组织决策与重规划。系统计划在NVIDIA Isaac Sim和由人形躯干与移动底座组成的移动操作机器人上实现，并用域适应进行仿真到现实迁移。

### 三、结果（Result）
本文是概念性框架论文，尚未给出实际实验结果或可复现的定量对比；计划评估任务成功率、路径与动作计划、达到目标所需步数，以及探索、检查或澄清后神经感知不确定性如何变化，并考察机器人是否避免依据低置信度或歧义预测行动。

### 四、结论（Conclusion）
该工作旨在让移动操作机器人不仅知道如何收集更多信息，还能判断进一步感知何时不再必要，从而以任务充分而非完整场景理解为目标，在遮挡、感知歧义和任务说明不完整等可复现场景中提升未知环境下的鲁棒性。

### 五、方法论与关键技术细节
关键实现点包括对象中心信念状态记录位置、语义类别、检测置信度、观测历史和视觉语言嵌入，任务充分性判据融合检测置信度、空间与任务级不确定性并设置执行阈值，主动感知以期望语义不确定性降低选择视角，决策采用符号行为树并复用ELMiRA的人机交互结构；任务覆盖物体搜索、取回和导航，仿真包含遮挡、相似物体和歧义指令。局限性是当前仅为概念与计划，缺少实证结果，阈值校准、异构信息收集动作的成本与风险比较、仿真到现实迁移及真实平台验证仍需后续完成。
