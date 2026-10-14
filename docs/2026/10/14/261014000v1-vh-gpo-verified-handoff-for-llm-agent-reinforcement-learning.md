# VH-GPO: Verified Handoff for LLM Agent Reinforcement Learning

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Haoze Li, Peng Zhou, Peiyuan Wu, Weijie Zhao, Yinan Xin
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14000v1) · [PDF](https://arxiv.org/pdf/2610.14000v1)

## TLDR
VH-GPO improves group-relative LLM agent reinforcement learning by using an environment-verified teacher to repair failed rollouts only up to the earliest confirmed handoff point and then returning control to the student, raising success rates from 59.38% to 94.79% on ALFWorld and 71.62% to 77.34% on WebShop with minimal extra teacher/student tokens.

## Abstract
Group-relative reinforcement learning methods such as GRPO train large language model (LLM) agents by comparing rollouts for the same task. When every trajectory in a group fails with the same reward, relative advantages collapse toward zero, leaving no useful learning signal. A frozen teacher can recover from a student-visited state, but letting it complete the task makes the recovered suffix entirely teacher-generated. We ask: after repairing a student failure, when should control return to the student? We propose outcome-verified teacher-student handoff, instantiated in Verified Handoff for Group Policy Optimization (VH-GPO). The teacher provides enough support to reach a state from which the student can succeed, then returns control so that successful experience is again student-generated. Given an environment-verified teacher recovery, VH-GPO selects the earliest independently confirmed handoff point found within a bounded search budget. With Qwen2.5-1.5B, VH-GPO increases success rates over GRPO from 59.38% to 94.79% on ALFWorld and from 71.62% to 77.34% on WebShop. Improvements also hold with the 7B student, for which additional teacher and student output tokens amount to 1.77% and 2.61% of regular student rollout output tokens on ALFWorld and WebShop, respectively. Ablation studies demonstrate the effectiveness of the key components. These results support using verified teacher assistance to repair failures while reinforcing the student's ability to complete tasks independently.


## 精读解读（中文）
### 一、研究动机
分组相对强化学习方法如GRPO通过比较同一任务的多个rollout来训练LLM智能体，但当组内所有轨迹都失败且奖励相同时，相对优势会塌缩到零，无法提供有效学习信号。冻结教师虽可从学生失败状态恢复任务，但若让教师直接完成全部剩余步骤，成功后缀完全由教师生成，难以强化学生独立完成任务的能力。因此核心问题是：在教师修复学生失败后，应在何时把控制权交还给学生。

### 二、技术方案（Method）
VH-GPO面向LLM智能体的组相对RL训练：对同一任务采样一组学生轨迹并用环境奖励评估；若组内失败，则调用冻结教师从学生访问过的失败状态生成环境可验证的恢复轨迹。随后在教师恢复轨迹上以有界搜索预算寻找最早交接点，即从该点让当前学生继续rollout后能由环境独立验证成功；选择最早确认点，把学生前缀、教师修复段以及交接后的学生后缀组成修复成功轨迹，并纳入GRPO式组内相对优势计算与策略更新，使成功经验尽可能由学生生成。教师仅用于失败修复和交接点确认，训练与推理流程仍沿用GRPO的采样、评估、策略更新闭环。

### 三、结果（Result）
在Qwen2.5-1.5B上，VH-GPO相比GRPO将ALFWorld成功率从59.38%提升到94.79%，将WebShop成功率从71.62%提升到77.34%；7B学生也保持提升。额外教师和学生输出token仅占常规学生rollout输出token的1.77%（ALFWorld）和2.61%（WebShop）。消融研究验证了关键组件的有效性。

### 四、结论（Conclusion）
用环境验证的教师辅助修复失败，并在最早可独立成功处交还控制权，可缓解组相对优势坍塌并提升LLM智能体任务成功率，同时让成功经验仍由学生生成。结果表明验证式师生交接是一种低开销且有效的失败修复与独立能力强化机制。

### 五、方法论与关键技术细节
关键点包括环境可验证奖励、冻结教师从学生失败状态恢复、交接点需通过学生独立rollout成功确认、有界搜索预算下取最早交接点，以及避免教师生成完整成功后缀。GRPO依赖组内奖励方差，VH-GPO通过修复失败样本提供非零正样本；实验覆盖ALFWorld与WebShop及Qwen2.5-1.5B/7B，额外token开销约1.77%和2.61%。局限是依赖教师能力、环境验证器和搜索预算，交接点确认可能带来额外rollout与验证成本。
