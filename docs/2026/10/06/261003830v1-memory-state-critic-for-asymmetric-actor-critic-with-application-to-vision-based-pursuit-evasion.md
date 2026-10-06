# Memory-State Critic for Asymmetric Actor-Critic with Application to Vision-Based Pursuit-Evasion

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Arthur Louette, Alejandro Sánchez Roncero, Gaspard Lambrechts, Pascal Leroy, Julien Hansen, Petter Ögren, Damien Ernst
- 机构：McGill University, Belerion, Mila Québec AI Institute, KTH Royal Institute of Technology, University of Liège
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03830v1) · [PDF](https://arxiv.org/pdf/2610.03830v1)

## TLDR
This paper introduces the memory-state critic for asymmetric actor-critic in POMDPs, which conditions the critic on the privileged state and the policy’s own recurrent memory—without backpropagating through it—to yield unbiased policy gradients while removing the need for a second recurrent history encoder, and demonstrates faster, competitive performance on vision-based quadrotor pursuit-evasion.

## Abstract
In partially observable Markov decision processes, the optimal policy generally depends on the history of observations and past actions. Asymmetric actor-critic methods have become popular to learn such policies when additional information, such as the true state of the environment, is available during training. The critic, which is not needed at execution, is given access to the state. A critic conditioned on the state alone is generally ill-defined and yields biased policy gradients. Conditioning on the state and the history, the history-state critic restores both. In this paper, we show that conditioning the critic on the state and the policy's own memory, i.e., the internal representation of the history through which the policy selects its actions, is already well-defined and gives unbiased policy gradients, removing the need for a second recurrent approximator of the history. We call it the memory state critic. It follows that a critic based on the policy's memory need not backpropagate its loss into that memory, even though the memory is a lossy encoding of the history. We evaluate the memory-state critic in a vision-based pursuit-evasion environment between two quadrotors across two arena types. The pursuer is the learning agent, and the evader is sampled per episode from a fixed pool of heuristic behaviours. The results show that the memory-state critic outperforms the history-state critic and converges faster. In addition to being unbiased compared to the state-only critic, it maintains a slight edge in the wall arena, where the actor's history carries information that the privileged state alone does not.


## 精读解读（中文）
### 一、研究动机
在部分可观测马尔可夫决策过程中，最优策略依赖观测与动作历史；非对称 actor-critic 在训练时让 critic 访问仿真中的真实状态以缓解部分可观测问题。然而仅以状态为条件的 critic 通常定义不良并产生有偏策略梯度，而以状态和历史为条件的 history-state critic 虽无偏却需要额外的循环编码器，增加训练时计算与表示学习负担。本文希望证明直接复用策略自身记忆即可消除第二个历史编码器，同时保持 critic 的无偏性。

### 二、技术方案（Method）
论文定义 memory-state critic，令策略的循环编码器输出记忆 z_t^a=f_θ(h_t)，critic 以特权状态 s_t 和 z_t^a 为输入，即 V_ψ(s_t,z_t^a)，并在该输入上使用 stop-gradient，使 critic 损失不反传到策略编码器，编码器仅由策略梯度更新。理论部分在确定性循环编码器和策略分解 π_θ(a|h)=g_θ(a|z^a) 下证明：给定 (s_t,z_t^a) 与给定 (s_t,h_t) 诱导的未来轨迹分布在策略上相同，因此 V、Q 与 history-state 版本逐点相等，V(s,z^a) 对 s 取期望回历史价值，优势函数也相等，故非对称策略梯度仍无偏。实现上 actor 用 RNN 维护记忆，critic 价值头用 MLP 读取 s 与策略记忆，训练时共享前向但不共享梯度。实验在 IsaacLab 与 skrl 中构建两架四旋翼的视觉追逃环境：追捕者为学习智能体，仅通过机载相机观测，逃逸者每回合从四种固定启发式行为中采样，状态含逃逸者类型；在无障碍开阔竞技场和带墙竞技场比较 memory-state、state-only、history-state 与 reactive critic。

### 三、结果（Result）
实验显示 memory-state critic 的最终回报与 history-state critic 匹配，但收敛更快，符合其省去第二个循环编码器的设计预期。相对于 state-only critic，它保持无偏，并在带墙竞技场中略有优势，因为该场景下 actor 的历史包含仅靠特权状态无法提供的信息。

### 四、结论（Conclusion）
结果表明，非对称 actor-critic 无需为 critic 再训练一个独立的历史循环表示；复用策略记忆并配合 stop-gradient 即可获得与 history-state critic 相同的无偏价值学习，同时降低训练计算和表示不一致风险。该方法在视觉追逃任务中有效，说明在训练时可获得真实状态时，memory-state critic 是更简洁且高效的替代方案。

### 五、方法论与关键技术细节
关键点包括：POMDP 中历史 h_t 与状态 s_t 的区分；记忆定义为确定性循环编码器 z_t=u(z_{t-1},a_{t-1},o_t) 的输出，策略为 π_θ(a|h)=g_θ(a|z^a)；无偏性依赖状态 s_t 与策略记忆 z_t^a 联合条件，缺少状态时 z_t^a 不是未来回报的充分统计量；stop-gradient 防止价值损失塑造策略编码器并避免 on-policy 训练失稳；环境使用两架四旋翼、机载相机、每回合从固定池采样的启发式逃逸者、开阔与带墙两类竞技场，并基于 IsaacLab 与 skrl 实现且公开代码；潜在局限是仍需训练期特权状态、依赖确定性循环编码器与 TD 价值近似。
