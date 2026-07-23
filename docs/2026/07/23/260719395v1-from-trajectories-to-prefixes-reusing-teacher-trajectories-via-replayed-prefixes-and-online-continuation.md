# From Trajectories to Prefixes: Reusing Teacher Trajectories via Replayed Prefixes and Online Continuation

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Yihan Wang, Zhong Guan, Haoran Sun, Jiale Huang, Likang Wu, Hongke Zhao
- 机构：Tianjin University of Technology, Tianjin University, ai-deepcube.com, Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19395v1) · [PDF](https://arxiv.org/pdf/2607.19395v1)

## TLDR
Prefix-GRPO improves small-model interactive agents by decomposing teacher trajectories into replayable prefix queries and optimizing both the replayed teacher prefix tokens and online student continuations under a unified clipped reinforcement learning objective.

## Abstract
Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets. This is inefficient in long-horizon environments, where early decisions shape later states and rewards. We propose Prefix-GRPO, a reinforcement learning framework that decomposes teacher trajectories into replay-aligned prefix queries and online continuations. Each prefix is replayed in the environment to recover a valid intermediate state, after which the student continues online interaction and receives task reward. Unlike response-only GRPO, Prefix-GRPO also applies clipped policy updates to historical assistant tokens inside the replayed prefix, using a policy-distilled SFT checkpoint to estimate their old log-probabilities. This unifies prefix learning and continuation learning within the same policy-optimization form. Experiments on TextCraft, BabyAI, and ALFWorld show that Prefix-GRPO improves small-model agents over distillation and standard RL baselines, while ablations show that replay alone is insufficient without explicit prefix-token optimization. The implementation and reproduction scripts are available at https://github.com/HappynessI/Prefix_GRPO.


## 精读解读（中文）
### 一、研究动机
小语言模型作为交互代理骨干具有低延迟和部署优势，但直接蒸馏教师轨迹会将丰富多轮行为转化为单次模仿目标，在长程环境中早期决策影响后续状态和奖励，导致蒸馏模型学习决策动态失效，效率低下。

### 二、技术方案（Method）
Prefix-GRPO框架将教师轨迹分解为多个可重放前缀查询和在线延续：首先基于熵变化信号从教师轨迹中选取关键令牌位置作为切点，形成组查询；每个查询在环境中回放以恢复有效中间状态，并通过规范化为系统指令、前缀历史和切点观察的提示；对重放前缀中的历史助手令牌，使用策略蒸馏SFT检查点估计旧对数概率，并通过前缀掩码指定优化位置；统一优化目标采用裁剪策略比率，延续分支使用在线滚动的组相对优势，前缀分支使用延续优势幅度作为锚，两者通过权重系数λ_pre结合。

### 三、结果（Result）
在TextCraft、BabyAI和ALFWorld三个长程交互环境上的实验表明，Prefix-GRPO相比直接蒸馏（SFT）和标准强化学习基线（GRPO、GRPO-MIS、DAPO）显著提升了小模型代理的Avg@8和Pass@8指标，消融实验证实单纯回放前缀而不进行显式令牌优化是不够的，验证了前缀令牌优化对提升效果的贡献。

### 四、结论（Conclusion）
Prefix-GRPO通过将教师轨迹分解为重放前缀和在线延续，并统一优化前缀和延续令牌，有效提高了教师轨迹的利用率，超越了单次蒸馏和标准强化学习方法，为小模型多轮代理提供了更高效的训练范式。

### 五、方法论与关键技术细节
组查询构建基于教师强制熵变化信号，仅对助手交互令牌评分，每个轨迹最多保留三个前缀查询和一个无前缀查询；回放验证要求重放后观测与延续侧共享结构字段匹配，否则丢弃；前缀优化使用延续令牌组优势的绝对值作为锚定信号，不赋予符号信用；损失函数中前缀项系数λ_pre平衡前缀和延续学习；复杂性在于需要回放验证和缓存前缀旧对数概率，局限性包括对教师轨迹质量和环境可重放性的依赖。
