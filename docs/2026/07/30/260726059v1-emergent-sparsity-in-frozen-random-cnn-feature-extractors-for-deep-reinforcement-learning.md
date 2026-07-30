# Emergent Sparsity in Frozen Random CNN Feature Extractors for Deep Reinforcement Learning

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Scott M. Norton
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26059v1) · [PDF](https://arxiv.org/pdf/2607.26059v1)

## TLDR
Deep reinforcement learning agents with frozen, randomly initialized CNN feature extractors spontaneously develop extremely sparse fully-connected representations whose active neuron count scales with task complexity, without any sparsity-inducing objective.

## Abstract
We report a striking phenomenon: deep reinforcement learning agents trained with frozen, randomly initialized CNN feature extractors spontaneously develop extremely sparse fully-connected representations, without any sparsity-inducing objective. In the first fully-connected layer (FC1, $3{,}136 \to 64$), agents compress task-relevant information through as few as 1-3 neurons out of 64 for deterministic Pong (5-11 for stochastic Pong), while trainable CNNs activate 55-64 neurons under matched conditions. We establish four principal findings. First, FC1 sparsity scales with task complexity: 1-11 for Pong, 19-26 for Breakout, and $\sim$42 for Space Invaders. Width-scaling confirms this reflects task structure rather than a fixed capacity fraction. Second, within-game scaling emerges: three identical Pong seeds produce 5, 7, and 11 active neurons. The 5-neuron seed plateaus at $+14$ reward, while the others reach expert performance ($+18.4$, $+18.7$), suggesting the random projection's usable dimensionality bounds achievable performance. Third, ablation confirms necessity: removing these active neurons crashes performance across two PPO implementations and four games. Fourth, the information bottleneck commits early: a sweep shows the active set locks by 15-30M steps, while reward turns positive 35-105M steps later. A complementary finding in Breakout shows frozen and trainable CNNs reach competitive rewards via structurally different bottlenecks: frozen agents use 17-25 active neurons (participation ratio $\sim$10-14), while trainable agents use 51 (participation ratio $\sim$3.6). Finally, wherever input dimensionality dwarfs intrinsic task dimensionality, gradient descent on a frozen random projection may reveal the effective rank of the underlying problem without explicit sparsity machinery.


## 精读解读（中文）
### 一、研究动机
深度强化学习中，标准端到端训练使用密集的分布式神经网络处理高维像素输入，虽然有效但掩盖了任务的内在结构。现有稀疏性方法需要显式诱导（如剪枝、正则化），而本文发现在冻结随机CNN特征提取器的条件下，稀疏性可以从学习动态中自然涌现，无需任何稀疏性目标。这一现象揭示了任务复杂性与表示维度的内在关系。

### 二、技术方案（Method）
采用Nature-DQN CNN架构：三个卷积层（32个8x8步长4、64个4x4步长2、64个3x3步长1）输出3136维特征，接两个全连接层FC1（3136→64）和FC2（64→64）使用ReLU激活。冻结CNN条件下，CNN权重用Kaiming均匀初始化并固定，仅训练FC层和策略/价值头（72.5k参数）。使用PPO算法在两个独立实现（Stable-Baselines3同步PPO和Sample Factory异步PPO）中训练，超参数包括学习率2.5e-4线性衰减、剪裁范围0.1、熵系数0.01。环境为四个Atari游戏（Pong、Breakout、Space Invaders、Freeway），使用84×84灰度4帧堆叠预处理。激活分析定义神经元在1000个样本中平均后ReLU激活>0.01为活跃，并通过保留/移除活跃神经元的消融测试验证瓶颈必要性。

### 三、结果（Result）
核心发现：冻结随机CNN的FC1层激活神经元数量远少于可训练CNN，且与任务复杂性成比例。Pong（确定性）仅1-3个活跃，Pong（随机粘滞）5-11个，Breakout 19-26个，Space Invaders约42个，而可训练CNN激活55-64个。消融实验证实移除活跃神经元导致性能崩溃至随机水平（两个PPO实现、四个游戏）。信息瓶颈在训练早期锁定（15-30M步），而奖励正向变化滞后35-105M步。在Breakout中，冻结CNN使用17-25个活跃（参与率10-14），可训练CNN使用51个（参与率3.6），两者达到竞争性奖励但瓶颈结构不同。

### 四、结论（Conclusion）
研究表明，当输入维度远大于任务内在维度时，对冻结随机投影进行梯度下降可以自然揭示问题的有效秩，无需显式稀疏机制。稀疏性从学习动态中涌现，活跃神经元数量追踪任务复杂性，为理解表示学习、泛化和模型简化提供了新视角。这一发现挑战了稀疏性必须被工程化诱导的普遍观点，并可能推广到其他高维输入场景。

### 五、方法论与关键技术细节
关键细节包括：CNN权重初始化使用Kaiming均匀分布并固定；活跃神经元阈值设为平均后ReLU激活>0.01；消融协议评估五种掩码条件；跨两个PPO实现（SB3和SF）和不同硬件（Mac和Ubuntu/RTX5090）结果一致；宽度缩放实验（32/64/128）确认活跃绝对数量稳定而非容量比例；训练随机性通过粘滞动作（p=0.25）和渐进课程控制；信息瓶颈锁定时间约15-30M步；局限性包括Freeway部分种子产生残存非功能性瓶颈，以及n=3的样本量使得缩放模式为提示性而非正式定律。
