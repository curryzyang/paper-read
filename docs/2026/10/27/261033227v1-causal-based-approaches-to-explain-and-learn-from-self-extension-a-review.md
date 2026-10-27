# Causal-based approaches to explain and learn from self-extension - A review

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Rebeca Marfil, Pablo Bustos, Antonio Bandera
- 机构：Universidad de Málaga, Universidad de Extremadura
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33227v1) · [PDF](https://arxiv.org/pdf/2610.33227v1)

## TLDR
This review examines causal-reasoning-based approaches that enable self-aware, self-evolving robots to generate explanations for their actions and perceptual anomalies, validate them with humans, and incorporate them into their knowledge base to improve future behavior and trustworthiness.

## Abstract
The last decades have seen a revolution in autonomous robotics. Deep learning approaches and their hardware implementations have made it possible to endow robots with extraordinary perceptual capabilities. In addition, they can also benefit from advances in Automated Planning, allowing them to autonomously solve complex tasks. However, on many occasions, the robot still acts without internalising and understanding the reasons behind a perception or an action, beyond an immediate response to a current state of the context. This gap results in limitations that affect its performance, reliability and trustworthiness. Deep learning alone cannot bridge this gap, because the reasons behind behaviour, when it emanates from a model in which the world is a black-box, are not accessible. What is really needed is an underlying architecture based on deeper reasoning. Among other issues, this architecture should enable the robot to generate explanations, allowing people to know why the robot is performing, or has performed, a certain action, or the reasons that may have caused a certain plan failure or perceptual anomaly. Furthermore, when these explanations arise from a cognitive process and are shared, and thus validated, with people, the robot should be able to incorporate these explanations into its knowledge base, and thus use this understanding to improve future behaviour. Our article looks at recent advances in the development of self-aware, self-evolving robots. These robots are designed to provide the necessary explanations to their human counterparts, thereby enhancing their functional capabilities, in the quest to gain their trust.


## 精读解读（中文）
### 一、研究动机
自主机器人在深度学习与自动规划推动下具备强感知和复杂任务求解能力，但其行为多是对当前情境的即时响应，缺乏对感知与行动背后原因的内部理解，导致性能、可靠性和人类信任受限。仅靠黑箱深度学习无法弥合这一缺口，机器人需要更深层推理架构来生成解释，并在与人类共享和验证解释后更新知识库、改进未来行为。本文因此聚焦可自我理解、自我扩展并能为人类提供因果解释的机器人研究进展。

### 二、技术方案（Method）
本文是一篇综述，围绕因果推理和可解释自主机器人组织文献：以Pearl因果阶梯的关联、干预、反事实三层为分析框架，梳理知识表示与可解释规划方法，包括And-Or图、行为树、PDDL及E/D因果链接、扩展PDDL2.1、贝叶斯网络、本体、分层任务组织和线性模型树等。文章分别讨论无约束解释、受约束或反事实计划解释，以及感知异常的自我理解与通过仿真器进行想象重放以定位原因。其方法核心是比较不同表示如何支撑机器人回答做什么、怎么做、为什么做、为何不这样做以及如果状态不同会怎样等问题，并分析解释如何进入机器人知识库以支持自我扩展。

### 三、结果（Result）
综述指出，现有机器人系统已能较好完成关联层感知和部分干预层可解释规划，多数工作集中在解释当前计划、行动选择和失败原因，常用图结构、规划领域描述、贝叶斯网络和本体等表示。反事实解释、感知异常的内部化重放以及解释经人类验证后回写知识库的自我扩展仍较薄弱，且各方法分散、缺少统一基准和可复现定量指标。核心对比结论是知识表示与因果层级决定了解释能力上限，仅靠数据驱动的XAI不足以支撑目标驱动的机器人解释。

### 四、结论（Conclusion）
作者认为，可信自主机器人需要将因果发现、因果推理、解释生成、人机沟通和知识更新整合进认知架构，使机器人不仅能解释当前或过去行为，还能在人类反馈验证后吸收解释并自我扩展。未来研究应重点推进反事实与想象式推理、感知异常归因、开放式环境中的知识维护以及解释质量和人类信任的评估。

### 五、方法论与关键技术细节
关键方法论点包括区分XAI的数据驱动解释与XAR的目标驱动解释，强调解释是填补因果历史并回应反事实问题的认知过程；知识表示覆盖And-Or图、行为树、PDDL/E-D链接、扩展PDDL2.1、贝叶斯网络、本体、三层分层组织和线性模型树等，并映射到因果阶梯不同层级。实现上多依赖手工调整模型或领域先验，部分方法用自编码器聚类、可达性约束和稀疏多步图学习世界模型，感知异常解释可能需要仿真器重放；局限是综述本身无实验数据、无损失函数与超参数结论，现有方案在开放世界泛化、解释验证、知识回写和信任度量上仍不充分。
