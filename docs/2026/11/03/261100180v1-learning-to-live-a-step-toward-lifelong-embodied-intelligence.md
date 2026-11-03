# Learning to Live: A Step Toward Lifelong Embodied Intelligence

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Lirong Che, Peidong Wang, Yimeng Su, Jiong Wang, Yang Chen, Wenbo Fu, Zhenyu Huang, Tiancheng Xu, Yuzhe Yang, Dongli Xie, Xu Cao, Chuang Wang, Daqi Liu, Jian Su
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00180v1) · [PDF](https://arxiv.org/pdf/2611.00180v1)

## TLDR
LIFE is a framework for lifelong embodied intelligence in which a robot continuously observes its changing world, selectively records useful experiences in a persistent plastic memory, and converts problem-solving experience into reusable tools and skills to become more capable over time.

## Abstract
Embodied agents are usually organized around individual tasks, yet the physical world keeps changing between tasks and during execution. We introduce LIFE (Lifelong Intelligence from Experience), a framework in which a robot observes continuously, remembers selectively, and turns experience into new capabilities. RoboBeats, a family of lightweight streaming gates, tracks conditions set by the agent and discovers new events, deciding when an observation warrants a response or a memory write. Selected observations enter Plastic Memory, a flat store of images and structured records that keeps the source evidence, so new fields and indexes can be added when later questions need them. When existing tools fall short, Explore-Distill-Mount (EDM) turns solutions found during problem solving into validated, reusable tools and skills. Under matched protocols, RoboBeats substantially improves condition tracking over its base models and, at the same writing budget, retains more useful evidence for memory question answering than uniform sampling. A case study of limited scale, replaying 24 hours of continuous video recorded by a real robot, illustrates how the integrated system builds memory from a day of experience and uses it to answer everyday questions. LIFE takes a step toward robots that become more familiar with their surroundings and more capable through experience: learning not only to complete tasks, but to live in the world.


## 精读解读（中文）
### 一、研究动机
现有具身智能体多围绕用户指定任务组织，但物理世界在任务间和执行中持续变化，离散推理和工具调用难以匹配连续演化环境。机器人需要持续观察、选择性记忆，并在长期运行中把经验转化为新能力，从而像在一栋建筑中生活百日一样逐渐熟悉人和物。

### 二、技术方案（Method）
LIFE框架把主动感知、长期记忆、推理行动和自主学习连成闭环：RoboBeats作为基于Qwen3.5的0.8B/2B/4B轻量流式门控，以时间戳图像和自然语言条件为输入，因果处理视频流，对每个条件读取true/false单token logits得到保持概率，并将连续激活观测组成区间以触发响应或记忆写入；训练时冻结视觉编码器、用LoRA更新语言模型，多条件共享帧并独立计算损失，采用边界权重为三的加权BCE和软IoU间隔监督，每组最多八个条件。被选观测进入Plastic Memory，以扁平文件保存源图像及含时间、位姿和结构化字段的JSON记录，支持按人、地点、物体和事件检索，并可在后续问题需要时用程序从源图像扩展字段和索引。现有工具不足时，EDM通过探索、蒸馏、挂载把问题求解中形成的方法验证为可复用工具或技能并注册到共享能力层。

### 三、结果（Result）
在匹配协议下，RoboBeats在Charades-STA、StreamingBench、SPOT-Bench、ESTP-Bench、OVO-Bench和SSS-Bench等流式感知与记忆问答评测中显著提升条件跟踪能力，优于其基座模型；在相同记忆写入预算下，其选择性写入比均匀采样保留更多对记忆问答有用的证据。一个有限规模案例回放真实机器人连续录制的24小时视频，说明集成系统能从一天经验中构建记忆并回答关于人、物体和活动的日常问题。

### 四、结论（Conclusion）
LIFE将主动门控感知、保留源证据的可扩展记忆和工具技能积累结合起来，使机器人能够在任务之外持续观察世界、选择性保留经验并用历史证据支持当前决策。该工作朝终身具身智能迈出一步，目标是让机器人不仅学会完成任务，也学会在真实世界中长期生活并随经验变得更熟悉环境、更有能力。

### 五、方法论与关键技术细节
感知训练数据由公共视频和标注经筛选、按来源分组、去重和时间对齐构成连续片段，条件跟踪沿用原生动作区间，事件发现由教师模型标出从事件开始到视觉证据充分的窗口并合并为正区间，随后做数据平衡、格式与时间戳检查及人工目检。RoboBeats默认以1 Hz因果处理帧，复用缓存注意力和循环状态，以重叠分块限制上下文；分数在场景变化时会波动，需由触发状态更新和区间分组稳定输出。Plastic Memory保留原始图像以支持记录时未预见的问题，并依靠普通文件操作添加字段和索引；EDM强调只有验证后的方法才进入能力层。局限包括24小时案例规模有限、长期在线计算与记忆冗余约束、未来问题未知时的记忆选择权衡，以及多条件训练每组最多八个条件的工程限制。
