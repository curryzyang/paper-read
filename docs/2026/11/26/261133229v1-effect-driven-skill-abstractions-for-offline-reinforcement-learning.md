# Effect-Driven Skill Abstractions for Offline Reinforcement Learning

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Burcu Kilic, David Drexel, Emre Ugur, Justus Piater
- 机构：Middle East Technical University, Bogazici University, University of Innsbruck
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33229v1) · [PDF](https://arxiv.org/pdf/2611.33229v1)

## TLDR
The paper introduces an effect-driven action-chunk quantization method that learns discrete, reusable skills by predicting their next-state effects, enabling improved long-horizon goal-conditioned offline reinforcement learning when paired with standard offline RL policies.

## Abstract
We seek to learn discrete skill abstractions to facilitate long-horizon, goal-conditioned reinforcement-learning (RL) tasks. Recent approaches have shown success by quantizing actions via clustering or reconstruction. However, these objectives lead to skills that are not directly related to what the current state affords or what the goal requires. Instead, we argue that goal-directed skills should be driven by \emph{how they affect the state} of the agent. To realize this, we introduce a novel quantization method for action chunks that optimizes next-state predictions conditioned on the current state and action. This objective encourages skills to be distinguished by the future states they lead to, resulting in a vocabulary that spans diverse outcomes reachable from a given state. Our framework can easily be paired with common offline RL methods by replacing their continuous actor head with a discrete one that selects among the learned skills. We can execute these skills in the environment by converting them back to continuous actions using a trained low-level controller. Experiments on benchmark navigation and manipulation tasks largely show substantial and consistent improvements over both the continuous-actor baselines and reconstruction-based discretizations. Our project page can be found at: https://burcukilic.github.io/projects/effect-driven-skill-abstractions/.


## 精读解读（中文）
### 一、研究动机
长时程目标条件离线强化学习需要可复用的时序技能抽象；现有基于聚类或重构的动作块量化方法关注动作序列本身，未直接联系当前状态可提供的结果或目标所需结果。本文主张目标导向技能应由其对状态的影响来定义，从而形成能覆盖当前状态可达多样结果的可复用离散技能词表。

### 二、技术方案（Method）
提出三阶段框架：阶段I用一维卷积编码动作块，经有限标量量化（FSQ）得到离散技能码，并由解码器在给定当前状态下预测执行该动作块后的任务相关下一状态特征，以MSE训练；阶段II训练低层控制器，将技能码与当前状态映射为单步连续动作，以MSE拟合数据动作；阶段III用阶段I编码器把全数据集转成离散转移(s_t,k,s_{t+L})，结合hindsight目标训练输出K类技能码的高层目标条件策略，并实例化为D-GCBC、D-GCIQL、D-GCIVL和D-QRL，评估时高层选码、低层控制器执行。

### 三、结果（Result）
在OGBench的Maze、Puzzle及视觉导航与操作任务、Push-T和D4RL Kitchen等基准上，该方法相较连续actor基线和基于重构的离散化方法取得一致且显著提升；学习到的技能在不同状态下对应不同方向性结果，同一低层控制器可服务四种离散离线RL变体。

### 四、结论（Conclusion）
以技能对下一状态的影响驱动动作块量化，可得到与目标条件任务更匹配、策略无关且可复用的离散技能抽象，并优于连续动作策略和重构式离散化。

### 五、方法论与关键技术细节
采用FSQ形成容量K=∏N_d的隐式码本，并用直通估计器回传梯度，避免VQ码本坍缩；仅预测任务相关下一状态特征而非完整状态，以减少与任务成功无关的噪声；阶段I编解码器只用于构造技能词表，评估时仅用高层离散策略和共享低层控制器；高层为MLP输出K类logits，训练目标因D-GCBC交叉熵、D-GCIQL/GCIVL优势加权及D-QRL拟度量值学习而异；潜在约束是技能效果依赖任务相关特征定义与离线数据覆盖。
