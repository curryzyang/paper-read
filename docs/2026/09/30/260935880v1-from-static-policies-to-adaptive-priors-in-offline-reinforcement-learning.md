# From Static Policies to Adaptive Priors in Offline Reinforcement Learning

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Tianwei Ni, Vineet Jain, Akash Karthikeyan, Pierre-Luc Bacon
- 机构：Université de Montréal, Mila - Quebec AI Institute, McGill University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35880v1) · [PDF](https://arxiv.org/pdf/2609.35880v1)

## TLDR
This position paper argues that offline reinforcement learning should move beyond static, conservative policies for direct deployment and instead learn adaptive policy priors—formalized as adaptive offline reinforcement learning (AORL)—that preserve memory, exploration, and self-correction for later test-time or online adaptation, with Bayesian offline RL as a principled direction.

## Abstract
Offline reinforcement learning (RL) has traditionally focused on learning policies for direct deployment under conservative objectives, where uncertainty outside the offline dataset is treated pessimistically to ensure robustness. We argue that this formulation becomes incomplete when an offline-trained policy is subsequently updated through online interaction, as increasingly occurs in modern intelligent systems through test-time adaptation and online fine-tuning. This position paper argues that, in such settings, the objective of offline RL should extend beyond immediate deployment and instead prioritize learning adaptive policy priors: policies that preserve the capacity to improve during subsequent interaction through memory, exploration, and self-correction. We formalize this perspective as adaptive offline reinforcement learning (AORL), distinguish it from offline-to-online RL, and explain why adaptability becomes important under distributional shift, limited dataset coverage, and changing test-time conditions. We further discuss Bayesian offline RL as one principled direction for constructing adaptive policy priors by preserving epistemic uncertainty over plausible environments. Finally, we outline connections, open challenges, and research directions for treating offline RL as preparation for future experience rather than as a static deployment problem.


## 精读解读（中文）
### 一、研究动机
传统离线强化学习通常面向直接部署，以保守目标对离线数据之外的不确定性进行悲观处理，以保证策略安全与鲁棒。但本文指出，当离线训练得到的策略还要通过测试时适配或在线微调继续改进时，这种静态部署式表述并不完整，会因过度保守而牺牲后续适应能力。在分布偏移、离线数据覆盖不足以及测试条件变化等场景下，离线阶段应优先学习可继续改进的自适应策略先验，而不仅是固定策略。

### 二、技术方案（Method）
本文将问题形式化为自适应离线强化学习（AORL）：输入为静态离线数据集D和未知MDP M*，离线阶段不与环境交互，只学习策略先验，再用行为支持supp_D(s)刻画覆盖不足并保留对P*、R*的认知不确定性。核心方案是让策略先验具备记忆、探索和自我纠正三要素，通过历史依赖策略π:H_t→Δ(A)或隐式潜变量、规划、参数适配实现记忆，并通过保留对不确定但潜在有价值动作的概率实现探索与纠错。在线测试阶段可组合使用四类适配机制：测试时上下文学习、测试时规划、测试时训练和在线RL微调；其中上下文学习和规划不更新参数，测试时训练只做临时更新，在线微调做持续更新。作为原则性方向，贝叶斯离线RL把离线学习视为认知POMDP，在合理MDP上保持后验，使策略基于在线历史条件化，从而先探索不确定动作再转向利用。

### 三、结果（Result）
本文的核心论证是：经典离线RL的保守性在策略后续会继续交互改进时会产生机会成本，离线阶段应优化可适应性而非仅优化部署鲁棒性。文中通过对比表指出，经典离线RL通常采用马尔可夫决策、限制在离线支持内、只关注离线阶段，而AORL要求历史依赖、保留灵活性、协同离线与测试时阶段，并具备记忆、探索和自我纠正能力。论文还区分了AORL与offline-to-online RL：后者是一种具体适配流程，AORL关注的是离线阶段本身应保留可适应性，只有当下游离线阶段显式增强测试时适应性时，offline-to-online方法才实例化AORL。本文为立场论文，未提供定量实验指标，其可复现结论主要体现在概念框架、性质对比和适配机制分类上。

### 四、结论（Conclusion）
结论是，当离线训练得到的策略将随后续交互继续改进时，离线RL的目标应从学习静态策略转向学习自适应策略先验，把离线数据学习视为未来经验的准备而非最终部署问题。贝叶斯离线RL被视为构建此类自适应先验的原则性方向，因为它通过保持对合理环境的认知不确定性，使策略能够在测试时通过历史条件化进行探索和自我纠正。未来研究需要围绕离线优化与测试时适配的协同设计，重新定义离线RL的评价标准、算法目标和开放挑战。

### 五、方法论与关键技术细节
关键实现细节上，本文将标准无限时域折扣MDP扩展为可含POMDP的设定，定义历史h_t、行为支持supp_D(s)={a|Pr_D(a|s)>ε}，并把离线覆盖之外的动作视为认知不确定性来源而非固有坏动作。方法强调不应对所有OOD动作施加零概率或强惩罚，而应保留足够行为灵活性以支持探索和纠错，同时通过记忆机制让同一状态在不同历史信念下选择不同动作。适配机制按在线数据量、是否更新参数和机制类型区分：上下文学习为隐式推断，规划为显式推断，测试时训练为临时参数更新，在线RL微调为持续参数更新。贝叶斯视角通过对合理MDP保持后验来实现自适应先验，但本文属于立场论文，未给出具体算法、损失函数、超参数、复杂度分析或实证结果，局限在于框架仍偏概念化，分布偏移、有限高质量覆盖、测试条件变化及多种适配机制的组合仍是开放挑战。
