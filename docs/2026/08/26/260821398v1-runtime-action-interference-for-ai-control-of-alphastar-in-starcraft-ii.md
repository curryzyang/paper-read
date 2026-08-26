# Runtime Action Interference for AI Control of AlphaStar in StarCraft II

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jaymari Chua, Chen Wang, Liming Zhu, Lina Yao
- 机构：CSIRO, University of New South Wales
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21398v1) · [PDF](https://arxiv.org/pdf/2608.21398v1)

## TLDR
RAI is a post-inference AI control mechanism that regulates action pacing and filters toxic action patterns without modifying policy parameters, and a human study in StarCraft II shows that disclosing versus withholding the opponent's capability claim significantly changes perceived fairness, trust, and toxicity even when the controller is identical.

## Abstract
A trained reinforcement learning policy does not determine the complete behavior that users encounter: deployment code still schedules, admits, suppresses, or replaces its proposed actions. We contribute \emph{runtime action interference} (RAI), an AI control mechanism that preserves policy parameters while regulating action pacing and filtering configured action patterns after inference. RAI releases a proposed action only when its cooldown condition is satisfied and its content detector does not flag the action; otherwise, it dispatches a no-op. The detector covers specified toxic behaviors, including worker-unit harassment, while the cooldown controls action rate. We implement RAI in a replication of AlphaStar actor.py and make the implementation and reproducibility materials available through an open source code repository. We deployed RAI in a \textit{StarCraft~II} human participant study that compared two presentations of the same opponent with high capability and rate limited actions; we withheld its capability claim in one presentation and disclosed it in the other. On response scales from 1 to 5, we observed pooled fairness, trust, and toxicity means of 3.90, 3.50, and 2.00 under claim withholding, compared with 2.62, 4.31, and 2.85 under disclosure. Disclosure corresponded with lower perceived fairness and higher perceived toxicity across every expertise group, whereas trust increased among novices and experts but decreased among intermediate participants. Our human evaluation therefore shows that perceptions of an opponent controlled through RAI can vary substantially with the capability information presented to users, even when the configured control remains constant. We conclude that human-computer evaluations must separate control within the execution stack from capability disclosure and assess fairness, trust, and toxicity as distinct dimensions of human experience.


## 精读解读（中文）
### 一、研究动机
训练后的强化学习策略并不完全决定用户遇到的行为，部署堆栈仍会在推理后调度、抑制或替换动作。因此需要一种不修改策略参数、在推理后对动作执行进行控制的机制，以调节动作节奏并过滤配置的有害行为。同时，人类评估中需要区分执行栈内的控制与能力披露对用户体验的影响。

### 二、技术方案（Method）
提出运行时动作干扰（RAI），在策略推理后、动作分发前添加确定性准入规则：维护冷却状态c_t，通过时间框架资格E_phi(c_t,t)和内容检测器T_psi(a_t^pi,h_t)两个正交谓词裁决；仅当两者均通过才释放动作，否则替换为no-op。策略参数固定，控制器参数phi和检测器配置psi决定行为。实现于AlphaStar actor.py，并记录审计事件。在星际争霸II中进行人类参与研究，比较同一高能力+RAI对手在能力声明隐藏（10人）与披露（13人）条件下的公平、信任、毒性评分，另有9人基线。

### 三、结果（Result）
在1-5评分下，能力隐藏时公平、信任、毒性池化均值分别为3.90、3.50、2.00；披露时分别为2.62、4.31、2.85。披露对应公平感降低、毒性感知提高，且在每个专家组中一致；信任在新手和专家中上升（新手+1.30，专家+1.35），但在中级参与者中下降（-0.75）。

### 四、结论（Conclusion）
人类评估必须分离执行栈中的控制与能力披露，并将公平、信任、毒性作为独立体验维度评估，因为即使控制器配置不变，能力信息也能显著改变用户感知。

### 五、方法论与关键技术细节
RAI在推理后作用于动作流，策略参数theta不变；冷却控制动作速率，内容检测器识别有毒模式（如工人单位骚扰）。审计记录包含时间戳、策略提议、冷却决策、检测器决策及原因、释放动作和控制器状态。人类研究焦点比较中，每个专家组别细胞样本量为2-5，分析为描述性，不作因果声明；提供开源实现、聚合数据和复现材料。另外，渲染器工具独立于RAI清理队列命令。
