# VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models

- 区域：精读区
- 排名：4
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Chenyu Su, Zhaolong Shen, Yuan Qian, Chen Qian, Rui Zhang, Feng Yan, Weixing Chen, Fei Zhang, Jiamin Wang, Shuang Cong, Weiwei Shang
- 机构：Beihang University, University of Science and Technology of China, State Key Laboratory of Precision and Intelligent Chemistry, Zhongguancun Academy, Hefei SpinX Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04355v1) · [PDF](https://arxiv.org/pdf/2609.04355v1)

## TLDR
VLA-Precision introduces an efficient real-world online RL framework for vision-language-action models, combining the Asymmetric Co-Bootstrapping (ACoB) algorithm to prevent policy drift and the ACoB-Stream architecture to improve throughput, achieving 98.3% mean success across high-precision tasks with up to 10.9× efficiency gains.

## Abstract
Pretrained vision-language-action (VLA) models enable broad manipulation but remain unreliable in tasks demanding precision and repeatability. Applying real-world online reinforcement learning (RL) to VLA post-training enables autonomous trial-and-error improvement beyond demonstrations alone, but exposes two bottlenecks: 1) unreliable value signals can induce policy drift; 2) large-VLA overhead constrains throughput and sample efficiency. To address these challenges, we present VLA-Precision, an efficient real-world online RL framework featuring the Asymmetric Co-Bootstrapping (ACoB) algorithm and the ACoB-Stream architecture. Specifically, ACoB establishes asymmetric co-bootstrapping across timescales: early intervention-guided behavioral learning rapidly improves policy performance while enhancing online experience quality. As autonomous experience accumulates, global return propagation and local preference ranking progressively calibrate value estimates, yielding relative action advantages for reference-regularized policy improvement while suppressing drift. To enable ACoB on large VLAs, we develop ACoB-Stream, a closed-loop experience--policy architecture that establishes invariant-state decoupling and on-demand streaming as design principles, delivering up to 10.9$\times$ improvements in throughput and computational efficiency. Extensive evaluations on nine high-precision chemistry tasks across four categories and four robot embodiments show that VLA-Precision achieves 98.3\% mean success rate in 45.8 min/task, with 27.6 s episodes running at 1.2$\times$ and 1.8$\times$ the speeds of VLA and RL baselines. Resources are available at https://vla-precision.github.io.


## 精读解读（中文）
### 一、研究动机
预训练的视觉-语言-动作（VLA）模型虽具备广泛操作能力，但在高精度高重复性任务中仍不可靠。将真实世界在线强化学习（RL）用于VLA后训练可实现超越演示的自主试错改进，但面临两个瓶颈：价值信号不可靠导致策略漂移，且大型VLA计算开销制约吞吐率与样本效率。

### 二、技术方案（Method）
VLA-Precision采用两阶段后训练：第一阶段在演示数据上对预训练VLA进行全参数模仿学习，获得任务特定策略先验Theta_IL；第二阶段以该先验初始化真实世界在线RL（异步演员-学习者闭环流程），仅优化动作专家中的LoRA参数，保持多模态前缀与动作专家主体冻结。算法层面提出异步协同引导（ACoB），在较快时间尺度上通过干预引导的行为学习快速改善策略与在线经验质量，在经验积累后通过全局回报传播与局部偏好排序逐步校准价值估计，得到相对动作优势，用于参考正则化的策略改进以抑制漂移。系统层面提出ACoB-Stream，依据不变状态解耦与按需流式原则管理经验上下文与策略状态生命周期，包括上下文形成（冻结VLM上下文跨更新复用）、持久化（去重与滑窗采样）、访问（目标对齐检索）和策略状态同步（可训练子空间分发）。整个流程在任务指令、视觉观测与机器人状态下生成H步动作块，经真实环境交互不断迭代，完成闭环在线RL后训练。

### 三、结果（Result）
在九个高精度化学任务（四类任务、四种机器人本体）上，VLA-Precision取得98.3%的平均成功率，平均每任务仅需45.8分钟训练；单集时长为27.6秒，运行速度分别达到VLA与RL基线的1.2倍和1.8倍。ACoB-Stream带来最高10.9倍的吞吐率与计算效率提升，表明该方法在真实世界高精度任务上兼具性能与效率优势。

### 四、结论（Conclusion）
VLA-Precision通过异步协同引导（ACoB）与闭环经验-策略流架构（ACoB-Stream）解决了真实世界大型VLA在线RL的价值漂移与系统开销两大瓶颈，可在演示基础上持续提升精确操作能力同时不丢失既有技能。实验证明其能高效完成多类高精度任务，为VLA机器人的真实世界后训练提供了可实际部署的范式。

### 五、方法论与关键技术细节
关键设置：策略基于预训练VLA的基于流的动作专家，第一阶段全参数模仿学习建立任务先验，第二阶段仅优化LoRA参数，兼容大规模参数下的在线更新。价值校准同时利用全局折扣回报传播和局部偏好排序，学习相对动作优势并通过参考正则化限制策略偏移；多时间尺度协同（快速行为学习+渐进价值校准）构成ACoB核心。ACoB-Stream通过不变状态解耦、上下文去重与滑窗采样降低存储和重复计算，采用目标对齐检索和可训练子空间传播减少访问与同步开销，从而支撑真实世界的持续交互。该工作评估集中在化学高精度任务，未覆盖更广泛的非结构化操作场景；文中也未给出具体的奖励函数公式或在异构复杂任务上的理论收敛保证，是尚需探讨的局限性。
