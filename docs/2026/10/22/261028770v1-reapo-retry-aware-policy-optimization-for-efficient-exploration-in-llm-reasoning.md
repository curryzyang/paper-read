# ReAPO: Retry-Aware Policy Optimization for Efficient Exploration in LLM Reasoning

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Nghi Dao, Calder Morton-Ferguson, Noah Golowich, Adam Block
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28770v1) · [PDF](https://arxiv.org/pdf/2610.28770v1)

## TLDR
ReAPO is a simple GRPO modification that frames retry-based credit assignment as a stochastic shortest path problem, enabling additional attempts after failed reasoning trajectories so successful retries are reinforced without rewarding preceding failures, thereby improving exploration and token efficiency in LLM reasoning.

## Abstract
RLVR improves language-model reasoning, but commonly relies on independent stochastic rollouts for exploration, which can repeatedly sample similar failed strategies. Prior work has seen success with approaches that guide exploration by introducing dependence into the sampling process by including incorrect solutions in the context for subsequent attempts. Still, these methods introduce the additional question of how to assign credit to each attempt. We propose to view the credit assignment through the lens of Stochastic Shortest Paths, a framework in classical reinforcement learning that seeks to minimize the expected cumulative cost to reach a terminal state (in our case, a verified successful response). We show that, under suitable simplifying assumptions, this perspective naturally leads to a simple modification to GRPO, which we call Retry-Aware Policy Optimization (ReAPO). ReAPO allocates additional generation to failed trajectories, allowing successful retries to be reinforced without rewarding preceding failures, and assigns credit in a theoretically principled way to each attempt. Across Qwen3 and OLMo-2 models from 0.6B to 4B and eight mathematical and scientific reasoning benchmarks, ReAPO improves first-attempt performance over GRPO as well as natural recent baseline algorithms, while additional ablations demonstrate the utility of both serial sampling and ReAPO's credit assignment. On Qwen3-0.6B, ReAPO also outperforms GRPO with twice the group size or twice the training steps, reaching their peak accuracy with 39% and 31% fewer generated tokens, respectively. Taken together, our results suggest that ReAPO is a simple yet effective approach for improving LM reasoning performance through improved exploration and retry-aware credit assignment.


## 精读解读（中文）
### 一、研究动机
RLVR 能提升语言模型推理，但常见做法依赖相互独立的多条随机 rollout 进行探索，容易反复采样到相似的失败策略，导致探索效率低。已有方法通过在上下文中加入错误解来引导后续尝试，从而引入采样依赖性，但也带来如何对每次尝试进行信用分配的新问题。本文旨在用有原则的信用分配改善失败后的重试探索，并提升首次尝试推理表现。

### 二、技术方案（Method）
ReAPO 将重试式推理建模为经典强化学习中的随机最短路径问题，目标是最小化到达已验证成功终态所需的期望累计代价，并在适当简化假设下推导出对 GRPO 的简单修改。训练时对失败轨迹分配额外生成机会，把先前错误解作为后续尝试的上下文进行串行采样，仅强化成功重试而不奖励先前失败，并按理论推导对每次尝试分配信用。实验在 Qwen3 与 OLMo-2 的 0.6B 到 4B 模型上，于八个数学与科学推理基准上对比 GRPO 及近期自然基线，并通过消融检验串行采样和 ReAPO 信用分配的作用。

### 三、结果（Result）
ReAPO 在多个模型规模和八个数学与科学推理基准上提升了首次尝试性能，优于 GRPO 以及近期自然基线算法。消融表明串行采样与 ReAPO 的信用分配均有实际贡献。在 Qwen3-0.6B 上，ReAPO 还优于组大小翻倍或训练步数翻倍的 GRPO，并分别以少 39% 和少 31% 的生成 token 达到其峰值准确率。

### 四、结论（Conclusion）
ReAPO 是一种简单而有效的 LLM 推理改进方法，通过失败轨迹上的额外重试探索与理论化的重试感知信用分配，提高探索效率与首次尝试准确率。其结果说明，将重试过程纳入策略优化并避免奖励失败前缀，可在不单纯增加组大小或训练步数的情况下获得更优的 token 效率。

### 五、方法论与关键技术细节
关键实现点包括：以随机最短路径视角定义到达成功终态的期望累计代价，在简化假设下将信用分配给各次尝试；对失败轨迹追加生成以形成串行重试，仅对成功重试给予强化，不奖励此前失败；与 GRPO 结合，使用组内相对优势式更新但改变采样与信用结构。实验覆盖 Qwen3/OLMo-2 0.6B 至 4B 和八个推理基准，并报告首次尝试准确率、生成 token 效率及串行采样/信用分配消融；局限性在于理论推导依赖简化假设，且主要验证于数学与科学推理任务。
