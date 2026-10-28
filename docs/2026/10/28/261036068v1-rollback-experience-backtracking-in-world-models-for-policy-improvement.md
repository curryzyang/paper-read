# Rollback: Experience Backtracking in World Models for Policy Improvement

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Jiayi Luo, Yang Zhang, Liliang Chen, Nan Wang, Chen Gao, Boxiang Qiu, Zhuoxuan Li, Baorui Peng, Chuankang Li, Yuxiang Yan, Si Liu, Qingyun Sun, Shuicheng Yan, Maoqing Yao, Jianxin Li, Guanghui Ren
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36068v1) · [PDF](https://arxiv.org/pdf/2610.36068v1)

## TLDR
**TLDR:** Rollback transforms action-conditioned world models from forward-only simulators into counterfactual engines that rewind to critical decision points, branch into alternative actions, and contrast outcomes to distill action-level supervision—yielding 10.67%, 11.11%, and 11.85% absolute success-rate gains on block extraction, ball tossing, and tabletop curling, and surpassing average human performance within 8 hours of training.

## Abstract
Action-conditioned world models offer a scalable alternative to costly real-world interaction for improving robot policies. However, existing world-model-based methods largely treat world models as forward-only surrogates of the physical environment, leaving untapped a capability no physical environment affords: rewinding to past decision points to explore counterfactual futures. We introduce Rollback, a policy improvement paradigm that turns world models from passive simulators into counterfactual engines: it rolls back to critical decision points, branches into alternative actions, and contrasts their outcomes to attribute success to individual decisions. This concentrates imagination where it matters most and distills counterfactual outcomes into fine-grained, action-level supervision without a separately learned value model. We build a scalable training system that unifies distributed world-model search with asynchronous real-robot execution, forming a self-reinforcing cycle: real-world experience continually sharpens the world model, and a sharper world model in turn drives further policy improvement. We term the world-model side of this cycle test-time physics grounding, a capability that hand-built physics simulators lack: while the world model serves as the training environment, real transitions from the policy it trains correct its dynamics through a lightweight LoRA pipeline. Experiments on three challenging real-world tasks show that Rollback improves success rates over the strongest baseline by an absolute 10.67%, 11.11%, and 11.85% on block extraction, ball tossing, and tabletop curling, respectively, while achieving more stable improvement throughout training. Although initialized from teleoperated demonstrations far below human level, Rollback surpasses the average success rate of human players on both ball tossing and tabletop curling within 8 hours of training.


## 精读解读（中文）
### 一、研究动机
动作条件世界模型为机器人策略改进提供了可扩展的替代真实交互的途径，但现有方法多把世界模型当作只能前向预测的物理环境代理，忽略了真实环境不具备的能力：回退到过去决策点并探索反事实未来。作者希望把想象集中在对任务成败最关键的决定上，从而更高效地改进策略。

### 二、技术方案（Method）
Rollback 将世界模型从被动模拟器转变为反事实引擎：先回退到关键决策点，分支采样替代动作，对比不同分支结果，把成功归因到具体动作决策，并将反事实结果蒸馏为动作级细粒度监督，无需单独学习价值模型。系统层面统一分布式世界模型搜索与异步真实机器人执行，形成真实经验持续修正世界模型、更准确世界模型再驱动策略改进的自增强循环；其中“测试时物理接地”用被训练策略产生的真实转移，通过轻量 LoRA 管线校正世界模型动力学。

### 三、结果（Result）
在三个真实世界任务上，Rollback 相对最强基线分别将成功率绝对提升 10.67%、11.11% 和 11.85%（方块提取、抛球、桌面冰壶），且训练过程中提升更稳定。虽然从远低于人类水平的遥操作演示初始化，Rollback 在抛球和桌面冰壶上训练 8 小时内即超过人类玩家平均成功率。

### 四、结论（Conclusion）
结果表明，把世界模型用作可回溯、可分支的反事实引擎，能够将想象聚焦于关键决策并提供有效的动作级监督，从而显著且稳定地改进真实机器人策略。分布式世界模型搜索与异步真实执行结合形成的自增强循环，为可扩展的策略改进提供了可行范式。

### 五、方法论与关键技术细节
方法关键点包括：以关键决策点回退和替代动作分支生成反事实轨迹，通过结果对比进行动作级归因和蒸馏，不依赖独立价值模型；训练系统采用分布式世界模型搜索与异步真实机器人执行，并用轻量 LoRA 由真实转移校正世界模型动力学。实验基于遥操作演示初始化，在三个真实任务上以成功率对比最强基线，并在 8 小时内达到超过人类平均表现；主要约束是系统效果依赖世界模型保真度、真实转移校正质量以及真实机器人异步执行成本。
