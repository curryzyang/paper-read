# CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Mingjia Chen, Xuewen Zhao, Philip Dames, Qi Mao, Fei Xie, Jun Chen
- 机构：Nanjing Normal University, Temple University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.12983v1) · [PDF](https://arxiv.org/pdf/2611.12983v1)

## TLDR
CAFE is a closed-loop robot autonomy framework that uses online semantic memory and a Trigger-LLM-guided Draft–Complete–Audit pipeline to discover, formulate, and execute scene-appropriate tasks without instance-specific instructions, then feeds execution outcomes back into memory for recovery and future task discovery.

## Abstract
Scene-driven robot autonomy requires selecting tasks from observations as well as executing them. We study scene-driven task formulation and execution under predefined cleaning, safety, and storage/organization categories, without instance-specific goals or action sequences. CAFE maintains online memory of objects, functional zones, and execution states. A rule-guided Trigger-LLM admits formulation from accumulated evidence; Draft, Complete, and Audit propose goals, resolve execution details, and check dependencies. Outcomes update memory for correction and subsequent discovery. Evaluation in 12 AI2-THOR scenes compares three backbones and task-complexity tiers using coverage, constraint, and execution metrics. Tri-LLM records higher GCR scores than the evaluated baselines across three backbones and task-complexity tiers. Controls examine completion, auditing, zones, feedback, triggering, and prompt examples. LimoCobot traces illustrate storage, cleanup, and recovery from a failed grasp. The study examines how shared scene state connects task discovery to execution and outcome-driven revision.


## 精读解读（中文）
### 一、研究动机
场景驱动的机器人自主性不仅要求执行任务，还要求从观察中决定该做什么；现有语言/视觉语言规划多依赖给定目标、目标清单或动作序列，难以覆盖无实例指令下的任务发现与执行衔接。CAFE针对预定义的清洁、安全和收纳/整理类别，研究如何把场景证据、可执行计划形成与执行结果修正连成闭环。

### 二、技术方案（Method）
CAFE以在线语义记忆为共享接口，记忆包含对象及状态、功能区、时间戳/置信度/执行状态，并用功能区地标在地面的包围盒把对象分配给区域。每个心跳由Trigger-LLM比较当前记忆与冻结参考，依据新增对象、对象-区域关联、状态/可供性变化和执行结果判断是否启动，规则为候选数不少于4或相对参考新增至少20个对象；启动后Draft提出包含动作、目标、区域、前置条件、优先级和几何的任务元组，Complete在单次前向中补齐目标、空间关联、几何和原子步骤，Audit检查语义一致性、对象可用性、安全与前置依赖并修复或拒绝，执行器按审计顺序执行并监控结果，成功或失败均回写记忆以支持恢复、去重和后续发现。

### 三、结果（Result）
在12个AI2-THOR场景、DeepSeek-V3/Qwen3-Max/Gemini-2.5-Pro三个骨干及简单/复合/复杂任务层级上，Tri-LLM的GCR分数高于所评估基线，覆盖度、约束满足和执行指标被联合用于比较。控制实验考察了Complete、Audit、功能区、执行反馈、触发策略和提示示例的作用；LimoCobot轨迹进一步展示了收纳、清理以及抓取失败后的恢复。

### 四、结论（Conclusion）
CAFE表明，以持久场景记忆为中心的闭环可以把任务发现、可执行计划生成和执行结果修正连接起来，使机器人在无实例级目标或动作序列时仍能按清洁、安全和收纳类别自主形成并执行任务。执行结果回写同一记忆既支持局部恢复，也影响后续任务发现与去重，说明共享场景状态是连接发现与执行的关键。

### 五、方法论与关键技术细节
评估不训练或微调模型，语义记忆从空开始，类别先验与技能固定，场景特定目标清单、参考动作序列和完整布局均不提供给机器人；12个场景每任务重复10次，控制实验使用Qwen3-Max，各变体共享观察接口、动作空间、输出格式、执行器、触发与反馈基础设施、步数预算和评测协议。触发采用冻结参考与显式阈值，失败修正可绕过发现门；关键局限是任务类别预定义、主要评估在仿真中进行，实机LimoCobot仅用于收纳、清理和抓取恢复演示。
