# GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Bohan Lin, Liyi Chen, Zhuoning Guo, Muyang Li, Qimeng Wang, Yan Gao, Yao Hu, Yudong Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08959v1) · [PDF](https://arxiv.org/pdf/2610.08959v1)

## TLDR
GraphOPD augments on-policy distillation for LLM agents with a step-dependency graph derived from environment state changes, scoring each step via a random-walk stationary distribution and fusing this structural credit with teacher-student divergence to focus supervision on high-impact steps, outperforming eleven baselines on ALFWorld, WebShop, and SearchQA by up to +5.8 pp.

## Abstract
On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory. Existing instantiations allocate this guidance by the size of the teacher-student divergence at each step, on the single-turn intuition that a large disagreement marks a mistake worth correcting. Once decisions chain over many turns, that rule misfires, since an early drift enters every later context both policies condition on, leaving the teacher consistent with the drifted trajectory instead of flagging its cause, while interchangeable steps register large but outcome-irrelevant divergences. We demonstrate this on an agentic benchmark, where distilling the highest-divergence steps brings no consistent benefit over random selection. To this end, we introduce GraphOPD, the first method to bring graph-based structural augmentation into on-policy distillation for agent capabilities. It reads which steps enabled which later ones from the environment's own record of state changes, immune to the drift that corrupts the teacher-student gap, organizes them into a dependency graph, scores each step by a random-walk stationary distribution over it, and fuses that structural credit with the divergence signal into a trajectory-relative mask concentrating supervision on each rollout's highest-aptitude steps. Across three model scales and eleven baselines on ALFWorld, WebShop, and SearchQA, GraphOPD shows competitive performance throughout, improving over the strongest baseline by up to +5.8 pp. An executed-replay audit further shows that this structural credit score tracks true causal impact far above chance, that both fused signals are independently necessary, and that the same signal transfers to out-of-domain tool-integrated reasoning.


## 精读解读（中文）
### 一、研究动机
当强化学习奖励稀疏且只在轨迹结束时给出时，on-policy distillation 依赖教师策略提供逐步密集监督，但现有方法按教师-学生每步散度大小分配指导，默认高散度处就是值得纠正的错误。该单轮直觉在多轮 agent 中失效：早期偏差会进入后续所有上下文，使教师与已漂移轨迹保持一致而不再标记根因，同时可交换步骤会产生大但无关结果的散度。作者在 agentic benchmark 上验证，蒸馏最高散度步骤相对随机选择并无稳定收益。

### 二、技术方案（Method）
GraphOPD 将图结构增强首次引入面向 agent 能力的 on-policy distillation：它以学生 agent 与环境交互产生的 rollout 为输入，从环境自身记录的状态变化中读取哪些步骤使能了哪些后续步骤，从而构建步骤级依赖图。每个步骤作为节点，若前一步的状态变化为后一步创造了条件则连边，不依赖教师-学生散度，因此不受上下文漂移污染。随后在依赖图上做随机游走并计算平稳分布，作为该步骤的结构信用分数。最后将该结构信用与教师-学生散度信号融合，形成轨迹相对的掩码，把监督集中在每条 rollout 中“能力适配度”最高的步骤上，用于 on-policy 蒸馏训练。

### 三、结果（Result）
在 ALFWorld、WebShop 和 SearchQA 上，覆盖三种模型规模和十一种基线，GraphOPD 整体表现有竞争力，相对最强基线最高提升 +5.8 个百分点。执行重放审计进一步显示，结构信用分数对真实因果影响的追踪显著高于随机水平；融合中的结构信号与散度信号均独立必要；同一信号还能迁移到域外的工具集成推理任务。

### 四、结论（Conclusion）
GraphOPD 表明，多轮 LLM agent 的 on-policy distillation 不应只依赖教师-学生散度来分配逐步监督，而应利用环境状态变化提供的结构因果信息。通过依赖图与随机游走平稳分布对步骤进行信用评分，并与散度融合成轨迹相对掩码，可更稳定地提升 agent 后训练效果。该方法在多个基准和模型规模上优于强基线，并具备跨域迁移潜力。

### 五、方法论与关键技术细节
关键实现点包括：以环境状态变化记录构建步骤依赖图，避免使用可能被漂移污染的 teacher-student divergence 作为唯一依据；用随机游走平稳分布量化步骤结构信用；将结构信用与散度信号融合为 trajectory-relative mask，仅在每条 rollout 内选择高适配步骤施加蒸馏监督。评估覆盖三种模型规模、十一种基线、ALFWorld/WebShop/SearchQA，并用 executed-replay audit 验证因果追踪、两信号独立必要性与域外工具集成推理迁移。局限性在于方法依赖环境可提供可靠的状态变化记录，图构建与随机游走带来额外复杂度，融合权重与掩码阈值等超参可能影响效果，且对无状态记录或噪声环境未必适用。
