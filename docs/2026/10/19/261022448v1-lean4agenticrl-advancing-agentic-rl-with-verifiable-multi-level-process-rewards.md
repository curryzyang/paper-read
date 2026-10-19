# Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Ruida Wang, Gerald Friedland, Tong Zhang, Chris Kong
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22448v1) · [PDF](https://arxiv.org/pdf/2610.22448v1)

## TLDR
Lean4AgenticRL is a framework that formalizes problem-specific agent workflows in Lean4 to provide verifiable multi-level process rewards for agentic reinforcement learning, enabling its LAR-9B/27B models to outperform comparable baselines on software-engineering and terminal-use tasks.

## Abstract
Enhancing the agentic capabilities of Large Language Models (LLMs) to tackle complex software engineering (SWE) and general terminal-usage problems is a pressing challenge. Current state-of-the-art LLMs often go through large-scale agentic Reinforcement Learning (RL). However, they mostly rely on high-level outcome rewards, with minimal consideration of low-level toolcall and mid-level workflow-stage rewards, which makes the training less effective. To overcome this limitation, we propose **Lean4AgenticRL**, which, to the best of our knowledge, is the first framework that grounds multi-level process rewards in the unified Lean4 formalization schema for open-ended agentic RL. **Lean4AgenticRL** first builds a *problem-specific workflow* system that balances the agent's own capability and controllability during execution, laying the foundation for further verification. Subsequently, our workflow formalization and multi-level reward annotation methods enable agent behavior verification within a general harness system. It provides multi-level rewards to support more effective agentic RL with the workflow-stage-normalized GRPO algorithm. Using **Lean4AgenticRL**, we train **LAR-9B/27B**, a family of models with enhanced agentic capability. Extensive experiments indicate that our model outperforms the leading model of similar size. **LAR-27B** achieves **77.3%** on TerminalBench-2.1. On average, our models outperform the base model by **9.89%** and surpass the second-best model of comparable size we know by **5.07%**. These results indicate the potential of integrating formal methods in enhancing open-ended agentic RL.


## 精读解读（中文）
### 一、研究动机
复杂软件工程与通用终端使用任务要求大模型具备强 agentic 能力，而当前先进的 agentic RL 多依赖高层结果奖励，较少利用低层工具调用和中层工作流阶段奖励，导致训练信号稀疏、过程归因不足，训练效果受限。

### 二、技术方案（Method）
Lean4AgenticRL 首先为开放式 agentic 任务构建问题特定的工作流系统，在 agent 自主能力与执行可控性之间取得平衡；随后将工作流与多级奖励标注统一形式化到 Lean4 schema 中，并在通用 harness 系统中验证 agent 行为，提供低层工具调用、中层工作流阶段和高层结果等多级奖励；最后采用工作流阶段归一化的 GRPO 算法训练 LAR-9B/27B 模型。

### 三、结果（Result）
实验表明 LAR 系列在同类规模模型中表现领先，LAR-27B 在 TerminalBench-2.1 上达到 77.3%；平均而言，模型相对基座模型提升 9.89%，并比已知同规模第二优模型高 5.07%。

### 四、结论（Conclusion）
结果表明，将形式化方法与多级过程奖励结合到开放式 agentic RL 中，可有效提升模型在软件工程和终端使用任务上的 agentic 能力，展示了形式化验证信号用于开放式 agent 训练的潜力。

### 五、方法论与关键技术细节
核心方法是用 Lean4 统一形式化问题特定工作流和多级奖励，覆盖低层 toolcall、中层 workflow-stage 与高层 outcome，并以 workflow-stage-normalized GRPO 进行训练；关键约束包括工作流设计需兼顾自主性与可控性、奖励验证依赖通用 harness 和形式化标注质量，且问题特定工作流与 Lean4 形式化会带来额外构建与维护成本，对高度开放任务的覆盖和泛化仍需进一步验证。
