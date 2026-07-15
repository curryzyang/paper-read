# In-Context Reinforcement Learning under Non-Stationarity: A Survey

- 区域：精读区
- 排名：4
- 匹配度：2.7/10
- 来源：arxiv
- 作者：A Run, Ziluo Ding
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11906v1) · [PDF](https://arxiv.org/pdf/2607.11906v1)

## TLDR
This survey defines and organizes non-stationary in-context reinforcement learning, where a fixed-parameter policy must infer changing task rules from accumulated interaction context while managing stale or misleading evidence, and identifies key challenges in evaluation, context management, and theory.

## Abstract
The development of decision-pretrained transformers, algorithm distillation, long-context meta-RL, and retrieval-augmented agents has renewed interest in in-context reinforcement learning (ICRL): the ability of a pretrained or fine-tuned decision model to infer latent task rules and improve future behavior from interaction context, without test-time parameter updates. This line of work asks when trial-and-error evidence, rewards, transitions, demonstrations, feedback, or retrieved experience can make learning-like computation happen inside the context window. However, existing surveys of ICRL mainly organize the field around pretraining objectives, architectures, context formats, evaluation protocols, and theoretical mechanisms, while the non-stationary setting remains comparatively underexamined. In changing environments, accumulated context is not merely more evidence about a fixed task: the reward specification, transition kernel, observation channel, action interface, constraint model, or demonstration and memory distribution can fall out of alignment with the current regime. Previously useful context can therefore become stale, misleading, or useful again when an old regime returns. We survey non-stationary ICRL as the problem of adapting through context while deployed policy parameters remain fixed: the policy must infer both the current decision rule and which parts of its accumulated evidence still support that rule. We define non-stationary ICRL, relate it to meta-RL, decision sequence modeling, retrieval-augmented RL, value- and model-aware ICRL, and reward-feedback agents, and organize the literature along three questions: what changes, how the change unfolds, and how observable the change is to the agent.


## 精读解读（中文）
### 一、研究动机
现有ICRL综述主要围绕预训练目标、架构、上下文格式和评估协议展开，但非平稳环境下的自适应问题被严重忽视。在非平稳环境中，累积的上下文可能变得过时、误导，甚至当旧模式回归时重新有用，这对基于上下文的强化学习提出了根本性挑战。

### 二、技术方案（Method）
论文将非平稳ICRL定义为固定参数策略在部署后通过上下文进行自适应的问题，并提出一个三维分类框架：什么变化（奖励、转移、观测等）、变化如何展开（突然、渐进、循环等）、变化对智能体的可观测性（可直接观测、部分观测、隐藏）。在此基础上，综述了多种方法（算法蒸馏、决策预训练变换器、检索增强ICRL、值感知ICRL等），并通过上下文管理操作（写入、检索、压缩、信任、遗忘、隔离）进行系统分析。同时讨论了训练数据与目标（如多任务预训练、算法蒸馏数据）以及评估协议（生命周期曲线、后移恢复、动态遗憾等）。

### 三、结果（Result）
论文指出现有ICRL评估主要依赖平均回报和持有任务泛化，这些指标无法反映非平稳环境下的自适应能力。提出了更全面的评估维度：生命周期曲线、后移恢复速度、动态遗憾、陈旧上下文敏感性、检索效用、可控变化下的自适应等。同时识别出被忽视的问题，如动作语义偏移、上下文中毒、记忆隔离、不确定性校准检索和有限上下文理论。

### 四、结论（Conclusion）
非平稳ICRL需要新的设计原则和评估方法。论文呼吁建立生命周期评估、陈旧上下文压力测试、有效性感知检索、自适应遗忘机制、上下文中毒防御以及针对非平稳ICRL的有限上下文理论。未来研究方向包括统一分类法、鲁棒的上下文管理机制和更具诊断性的基准。

### 五、方法论与关键技术细节
非平稳性被定义为决策过程（如奖励函数、转移核、观测通道、动作接口、约束模型等）在智能体积累上下文的生命周期内发生变化，使得先前有效的上下文证据可能过期或误导。上下文有效性是核心概念：智能体必须能够判断哪些上下文仍然支持当前决策规则。论文强调方法层面的关键点包括：检索机制（从外部库选择相关经验）、遗忘与隔离（丢弃或抑制过时证据）、压缩与摘要（减少上下文长度）、价值/模型感知推理（在上下文中估计值或动态模型）。局限性：现有方法大多假设变化模式简单或可观测，缺乏对复杂非平稳模式（如对抗性变化、多模态循环变化）的全面处理，且缺乏理论保证。
