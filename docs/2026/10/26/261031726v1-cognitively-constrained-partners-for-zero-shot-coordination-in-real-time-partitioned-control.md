# Cognitively Constrained Partners for Zero-Shot Coordination in Real-Time Partitioned Control

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Ash Simmons, George De Ath, Richard M. Everson
- 机构：University of Exeter
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31726v1) · [PDF](https://arxiv.org/pdf/2610.31726v1)

## TLDR
The paper proposes training zero-shot coordination agents against simulated “Cognitively Constrained Partners” whose diversity comes from human-like reaction delays and perceptual limits, rather than human data or reward shaping, and provides preliminary evidence that such partners behave more like real people and yield robust teaming performance in a partitioned Lunar Lander control task.

## Abstract
Effective human-machine teaming requires agents that coordinate with unpredictable human partners. Reinforcement learning from live human feedback or large behavioural datasets is expensive, while purely simulated training overfits to artificial conventions and fails at Zero-Shot Coordination with real people. We propose a framework for training teaming agents against Cognitively Constrained Partners: simulated partners whose diversity emerges from procedural constraints grounded in human physiological literature, specifically reaction delays and perceptual limitations, rather than from reward shaping or historical training checkpoints. In a modified Lunar Lander environment, we report preliminary evidence that these partners play more like real people than unconstrained agents do, and that agents trained against them match the strongest cross-play baselines while being the only ones whose performance does not depend on how their training partners were generated. We also describe a human-participant study designed so that its rankings can be compared directly against cross-play, testing how well that standard evaluation predicts real human-agent teaming.


## 精读解读（中文）
### 一、研究动机
人机协同要求智能体能够与不可预测的人类伙伴实时配合，但依赖真人反馈或大规模行为数据训练代价高昂，纯模拟训练又容易过拟合人工约定，在零样本协同中面对真人时性能崩溃。共享控制常把智能体降为辅助安全网，而严格分区控制下的人机协同在强化学习基准中研究不足，因此需要一种不依赖人类数据、又能产生类人多样性的伙伴训练框架。

### 二、技术方案（Method）
作者在改造的Lunar Lander中把控制权严格分区：主引擎与侧向推进器分别由两个伙伴控制，并用多离散动作包装器让双方每帧并发行动。伙伴端加入基于人类生理文献的认知约束包装器：处理延迟、机械延迟和不应期均从指数修正高斯分布采样，均值在80–110 ms、70 ms、120–150 ms区间随机初始化，动作至少持续4帧；同时对水平速度、垂直速度和倾角施加Weber定律感知阈值，并加入下限约束和斜向效应，每个伙伴采样唯一感知敏感度。由于延迟造成部分可观测，伙伴和团队智能体均采用循环PPO；先训练无包装的 solo 智能体，再从 solo 智能体部分迁移权重训练团队智能体，团队智能体只控制主引擎，并把伙伴实际执行的侧向动作作为第9维观测，每个回合从45个认知约束伙伴池中均匀抽取伙伴。基线包括FCP、PBT和MARL，训练池均匹配为45个伙伴，并在50个不相交的留出伙伴上做交叉评估。

### 三、结果（Result）
初步证据表明，认知约束伙伴的行为比无约束智能体更接近真实人类玩家；与它们训练出的团队智能体在交叉评估中达到最强基线水平，并且是唯一性能不依赖训练伙伴如何生成的方法。行为验证来自20名新玩家的非正式试点，每人完成10个固定种子的单人回合，并与45个认知约束智能体和45个无约束智能体比较；论文还描述了可直接与交叉评估排名对照的人类被试研究设计，用以检验交叉评估能否预测真实人机协同。

### 四、结论（Conclusion）
该工作表明，把反应延迟和感知限制等认知约束作为伙伴多样性的来源，可以在不收集大规模人类数据、也不依赖自博弈检查点的情况下生成更类人的训练伙伴，并训练出对伙伴生成方式更稳健的零样本协同智能体。严格分区控制迫使双方持续协调各自不可替代的输入，为搜索救援、空中交通管制和机器人手术辅助等实时人机协同场景提供了有前景的训练范式，但当前结果仍属初步，需在更多环境和真实人类实验中验证。

### 五、方法论与关键技术细节
关键实现包括：使用8维Lunar Lander状态和主引擎{0,1}、侧向{0,1,2}的多离散联合动作；共享奖励由环境势函数差分和推进器逐帧消耗组成，并加入着陆点中心惩罚；延迟分布的标准差固定为0.6/0.5/1.0，指数参数在处理和不应期取1.5、机械延迟取0.5，以保留重尾但保持感觉运动抖动较小；感知过滤只作用于水平速度、垂直速度和倾角，阈值按Weber分数4.5–8%随伙伴采样并设下限，倾角在接近垂直和水平方向更敏感；训练时伙伴策略冻结以避免“秘密握手”式共同适应，FCP和PBT采用对冻结伙伴的最佳响应，MARL保留共同适应但使用交错更新；团队智能体从solo智能体部分迁移权重，并以伙伴实际执行动作作为额外观测。局限包括试点样本小、仅一个环境、延迟随机性和人类研究结果尚未完整报告。
