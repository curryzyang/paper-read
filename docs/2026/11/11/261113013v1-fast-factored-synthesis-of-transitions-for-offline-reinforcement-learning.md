# FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Daniel Campa, Spandan Das, Srinjoy Das
- 机构：West Virginia University, Jadavpur University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13013v1) · [PDF](https://arxiv.org/pdf/2611.13013v1)

## TLDR
FaST is a factored offline-RL transition generator that decomposes transitions into separately modeled state, action, dynamics, reward, and terminal stages with tailored estimators, enabling over 90× faster synthesis than diffusion baselines and targeted best-of-N action resampling that can improve downstream policy performance.

## Abstract
Synthetic data augmentation promises to scale offline reinforcement learning beyond fixed logged datasets, but leading diffusion-based generators model the transition tuple (state, action, next state, reward, terminal) as a monolith: no single factor can be natively redrawn in isolation. We present FaST (Factored Synthesis of Transitions), which factors transitions via the chain rule into state, action, dynamics, reward, and terminal stages, fitting each with an estimator matched to its statistical properties. Across twelve D4RL locomotion and maze benchmarks, TD3+BC and IQL agents trained on FaST transitions match the SynthER diffusion baseline while generating transitions over 90x faster. The explicit action-given-state conditional can also be re-queried for a fixed state, enabling targeted action synthesis: drawing N candidate actions per generated state and keeping the highest-advantage one under a value function fit to the same data, thereby synthesizing improved behavior during generation rather than filtering for it post-hoc. Best-of-10 synthesis beats training on real data on 11 of 12 medium and medium-replay settings (+8.9 D4RL points on average, up to +28.4), and is competitive with advantage-filtered SynthER at a fraction of its generation cost. On expert mixtures both mechanisms degrade identically, tracing the failure to the advantage estimate itself rather than to either targeting mechanism.


## 精读解读（中文）
### 一、研究动机
现有离线强化学习数据增强多用扩散模型把转移元组整体建模，无法单独重抽某个因子，生成成本高且难以在生成时控制动作质量；同时，单纯增加合成数据只会复现行为策略而未必提升策略。FaST旨在通过链式分解实现可复用、快速且可定向合成的转移生成器。

### 二、技术方案（Method）
给定真实数据集D，将转移联合分布按链式法则分解为P(S)P(A|S)P(S'|S,A)P(R|S,A,S')P(d|S,A,S',R)，并分别拟合与各因子统计形态匹配的估计器：状态用分位数-logit变换后的自回归高斯混合MDN，动作用logit空间15分量MDN，动力学用预测S'-S的7成员bootstrap集成，奖励用128×128 MLP回归，终止用Extra Trees分类。各阶段独立在真实D上训练，采样时祖先式依次生成S、A、S'、R、d；可选定向动作合成对固定生成状态从P(A|S)抽N个候选，用同一D拟合的IQL价值函数计算A_IQL=min(Q1,Q2)-V并保留最高优势动作，再继续后续阶段，N=1即普通祖先采样。

### 三、结果（Result）
在12个D4RL locomotion和maze基准上，用FaST转移训练的TD3+BC和IQL达到与SynthER扩散基线相当的下游分数，同时生成转移速度超过90倍。best-of-10定向动作合成在11/12个medium和medium-replay设置上超过真实数据训练，平均提升8.9个D4RL点，最高提升28.4，并以远低于advantage-filtered SynthER的生成成本取得有竞争力结果。专家混合数据上两种定向机制同样退化，说明失败源于优势估计而非定向机制本身。

### 四、结论（Conclusion）
FaST表明链式分解配合阶段专用估计器可在保持下游性能的同时显著降低合成成本，并把动作条件显式暴露为可控接口，使生成阶段直接合成更优行为而非事后筛选。该方法提供可复用的离线RL数据增强管线，但其定向收益依赖IQL优势估计质量，在专家混合等优势估计不可靠场景会失效。

### 五、方法论与关键技术细节
实现上各阶段仅用真实D训练，状态与动作阶段通过有界支撑变换保持合成输入在训练流形附近，动力学采用delta参数化限制S'漂移以缓解训练-采样输入不匹配；奖励阶段为128×128 MLP加MSE，动作MDN为15分量，动力学集成为7个bootstrap模型，终止器为Extra Trees，IQL优势定义min(Q1,Q2)-V。best-of-N只重抽动作阶段且不重训其他阶段，因此状态边际保持不变，但会牺牲动作多样性；单步生成没有MBRL式rollout horizon需调，但存在级联误差。局限包括逐因子独立拟合不保证级联合成联合分布精确、专家混合上优势估计失败、以及未在摘要中给出各阶段完整参数量与墙钟成本（正文附录给出）。
