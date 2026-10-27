# Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Yichu Zhou, Qinyi Chen, Fei Feng, Jacob Loh, Mehdi Ben Ayed, Lin Yang, Andrei Curelea, Jiajing Xu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33248v1) · [PDF](https://arxiv.org/pdf/2610.33248v1)

## TLDR
RLBP is a deployed hybrid system at Pinterest that uses reinforcement learning as a daily meta-controller to tune campaign-specific PID bidding parameters while retaining PID for high-frequency bid adjustments, achieving statistically significant eCPC reductions without revenue loss.

## Abstract
Auto-bidding systems in online advertising must balance competing objectives-maximizing budget delivery while minimizing cost per action-across heterogeneous campaigns under non-stationary market conditions. This trade-off evolves over campaign lifespans: early on, cost optimization dominates when budgets roll over; near deadlines, budget delivery becomes urgent. While PID controllers are widely used in production for their stability and interpretability, fixed tunings cannot adapt to diverse campaigns and shifting traffic patterns. We present RLBP (Reinforcement Learning for Bidding Parameters), a hybrid architecture deployed at Pinterest that uses RL as a meta-controller to select campaign-specific PID parameters daily while retaining PID for high-frequency bid adjustments. RLBP trains a multi-head Q-network using a relative-lift reward formulation normalized against the production baseline, and performs inference-time fusion that adapts the cost-delivery trade-off to campaign states without retraining. Through online A/B testing at Pinterest, RLBP achieves a statistically significant reduction in effective cost-per-click (eCPC) with no revenue degradation, and two months of post-rollout measurements against a holdout also show consistent cost reductions. These results demonstrate that meta-controller RL can successfully augment production control systems at scale.


## 精读解读（中文）
### 一、研究动机
在线广告自动出价需要在非平稳市场和多类广告主之间同时兼顾预算交付与成本效率，且这种权衡会随广告活动生命周期变化：初期预算滚动时更重成本优化，临近截止时预算交付更紧迫。生产中常用的PID控制器虽稳定可解释，但固定调参难以适配不同广告活动和流量波动，因此需要一种能按活动状态自适应调整控制参数的方法。

### 二、技术方案（Method）
论文提出并在Pinterest部署RLBP（Reinforcement Learning for Bidding Parameters）混合架构：RL作为元控制器，按日为每个广告活动选择特定的PID参数，底层PID仍负责高频出价调整。模型采用多head Q网络，以相对于生产基线归一化的相对提升作为奖励，并在推理阶段进行融合，使成本与交付的权衡能随广告活动状态自适应，而无需重新训练。

### 三、结果（Result）
Pinterest在线A/B测试显示，RLBP在收入不下降的前提下实现了统计显著的有效每次点击成本（eCPC）降低；上线后两个月对holdout的持续测量也显示一致的成本下降。这些结果表明该元控制器方案在真实生产规模上可稳定改善成本效率。

### 四、结论（Conclusion）
RLBP证明将强化学习作为元控制器、保留PID作为底层高频控制器，是增强大规模生产自动出价系统的可行路径。该方法能在不牺牲收入的情况下改善成本指标，并具备上线后的持续收益，说明元控制RL可与现有控制架构互补落地。

### 五、方法论与关键技术细节
关键实现点包括：控制频率分层，RL仅做日级PID参数选择，PID承担高频出价调整；奖励采用相对生产基线归一化的相对提升，降低不同活动间绝对量纲差异的影响；多head Q网络支持面向广告活动状态的自适应决策；推理时融合可在不重训练的情况下调整成本—交付权衡。局限性在于RL只优化日级参数空间，效果受PID参数化与日级更新约束，具体网络输入和训练超参需参考论文正文。
