# WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Maeve Zhang, Rain Sun, Xiang Wang, Cyril Zhang, Shalfun Li, Meng Cao, Howard Lu, Ethan Chen, Harry Jhou, KZ Zheng, Lights Shi, Regis Cheng, Lorenzin, Robert Wang, Victor Yao, Gody Li, Elise Mon, Yohann Tang, Ryan Yu, PS Zhang, Vincent Chen, Hang Su, Roy Gan, Hao Wang, Qian Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26239v1) · [PDF](https://arxiv.org/pdf/2608.26239v1)

## TLDR
WALL-SS introduces a next-scale autoregressive world model that generates action-controllable, long-horizon robotic visual futures via coarse-to-fine prediction with scale-aligned action conditioning, scale-compressed memory, and on-policy alignment, enabling coherent streaming rollouts and calibrated closed-loop policy evaluation.

## Abstract
Generative world models provide robots with predictive models of how the world evolves under interaction, with growing potential for simulation, planning, policy evaluation, and robot learning. Beyond clip-level future prediction, a unified generative formulation should relate actions to consequences, support flexible horizons and continuous interaction, and enable reward-driven optimization. We introduce WALL-SS, a world model that generates visual futures through Scale-wise autoregressive Scaling, enabling action-controllable and long-horizon robotic simulation. WALL-SS represents embodied trajectories as causal sequences of temporally interleaved observations and actions, making action-dependent state transitions explicit while naturally supporting variable-length generation, streaming extension through reusable causal states, and direct optimization through sequence probabilities. To make this formulation effective over long horizons, we generate each future observation in a coarse-to-fine manner and develop three complementary components within the same hierarchy. Action-conditioned next-scale prediction injects scale-aligned action representations to improve action-future coupling and model both successful and failed behaviors. Scale-compressed long-horizon memory retains recent interactions at fine resolution while compressing distant observations and actions, with scale-wise dream forcing enhancing robustness to self-generated context. Finally, on-policy alignment optimizes autoregressive visual dynamics with action-following and long-term consistency rewards while preserving the pretrained visual distribution. Experiments show that WALL-SS improves action following and trajectory accuracy, supports coherent minute-long streaming rollout under bounded memory, and consistently benefits from on-policy alignment in reducing action drift and long-horizon inconsistency.


## 精读解读（中文）
### 一、研究动机
现有视频世界模型大多以片段级未来预测为主，未将动作与后果在统一因果序列中显式关联，难以支持灵活时长、流式交互和奖励优化；自回归式世界建模又面临误差累积和长期记忆不一致的挑战。为此提出WALL-SS，利用next-scale自回归生成可控、长程的机器人视觉未来。

### 二、技术方案（Method）
WALL-SS将具身轨迹表示为时间上交叉的观测与动作的因果序列，以粗到细的next-scale自回归逐尺度生成每个未来观测。输入为初始多视角观测、任务指令和时序对齐的动作序列；使用确定性渲染器将动作投影到各相机时间线，经共享因果编码器提取逐尺度动作条件，并以尺度对齐的因果掩码将动作token作为Transformer前缀注入，只在同一视觉尺度的对应动作上条件化。采用尺度压缩长时记忆：近期交互保持细粒度，历史观测与动作按尺度层级压缩为粗粒度摘要，在有限记忆预算下传播；通过尺度级dream forcing在自生成/损坏历史上训练以增强鲁棒性。最后将next-scale视觉token生成视为随机策略，在固定动作条件下用动作跟随和长时一致性奖励优化新采样轨迹，同时用自回归回放和参考模型正则化保持预训练视觉分布。

### 三、结果（Result）
实验表明WALL-SS在动作跟随和轨迹准确性上优于基线；在有限记忆下支持连贯的分钟级流式展开；on-policy对齐持续降低动作漂移和长程不一致。将同一外部机器人策略在WALL-SS和物理世界中闭环部署，得到校准的任务结果和一致的策略检查点排名，说明学到的世界模型保留了下游策略评估所需的动作相关动态。

### 四、结论（Conclusion）
WALL-SS提出了基于next-scale自回归的动作可控、长时程、可奖励对齐的机器人世界模型，以统一的因果公式连接感知、动作、记忆与优化。其三项互补设计（动作条件next-scale预测、尺度压缩记忆、on-policy对齐）共同提升了长时程一致性和动作保真度，为生成式世界模型用于机器人仿真、策略评估与学习提供了有效方案。

### 五、方法论与关键技术细节
关键实现细节：模型基于InfinityStar初始化，使用多尺度残差量化编码视觉token；动作条件通过确定性渲染器投影到相机时间线，共享因果编码器输出特征，按动作尺度集合S_A投影，查询在尺度ℓ时选择满足κ(ℓ)≤ℓ的最细动作尺度，动作图采用块对角掩码，禁止其他视角、相邻片段和未来动作的注意力。长时记忆将近期观测保留为细尺度、历史观测/动作逐步压缩为粗尺度，在有限记忆预算下进行流式传播；scale-wise dream forcing对自生成或损坏的历史上下文训练以缓解曝光偏差。on-policy对齐将next-scale生成视为随机策略，使用动作跟随奖励和长时一致性奖励，并通过自回归回放和参考模型正则化维持预训练视觉分布。数据来自异构机器人和UMI演示，初始为多视角观测。局限：自回归误差累积仍是核心挑战，且多尺度层级和流式记忆带来实现复杂度。
