# Endogenous Exploration in Reinforcement Learning with Intrinsic Curiosity

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Armando Vieira
- 机构：University of Tartu
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05650v1) · [PDF](https://arxiv.org/pdf/2609.05650v1)

## TLDR
This paper proposes a reinforcement learning framework where exploration emerges endogenously from intrinsic curiosity via coherence regulation between reach and yield fields on a Liquid State Machine substrate, showing competitive performance on LunarLander-v2 and BipedalWalker-v3 and identifying a "curiosity window" at intermediate incoherence levels that is absent in Active Inference agents.

## Abstract
We propose a reinforcement learning framework in which exploration is driven by intrinsic curiosity, designed for scenarios where environments are non-stationary and rewards are sparse, delayed, uninformative, or absent. In our model, action selection is guided by a combination of external rewards and an epistemic motivation mechanism that biases the agent toward structured exploratory directions. The central hypothesis is that effective exploration emerges at intermediate levels of incoherence, while performance degrades under both overly rigid and overly disordered dynamics. To test this idea, we implement the framework on top of a Liquid State Machine (LSM) substrate and evaluate it on two standard benchmarks: the discrete-action LunarLanderv2 and the continuous-control BipedalWalkerv3. The proposed method achieves competitive performance on both tasks relative to established deep RL algorithms, including Proximal Policy Optimization (PPO) and Intrinsic Curiosity Module (ICM). We further show that the curiosity window is not recovered in Active Inference agents under the same analysis, suggesting that the proposed dynamics capture a distinct exploration regime


## 精读解读（中文）
### 一、研究动机
现有强化学习中的探索机制大多依赖外部设计的噪声、熵正则或预测误差等辅助目标，缺乏对探索何时应增加或减少的原理性解释，在奖励稀疏、非平稳或无奖励环境中容易过早收敛或陷入无序随机行为。本文提出探索应内生涌现于系统自身的相干性调节动力学，并预测有效探索发生在中间程度的不连贯区间，即好奇窗口。

### 二、技术方案（Method）
提出一个基于液体状态机（LSM）与相干性场调控的两层强化学习框架。LSM作为高维时间表征基底，状态x(t)按tanh(Wx+W_in o+ξ)更新，并加入慢速痕迹h构成增广状态z=[x,h]。相干性层在离散化场单元上定义三个概率场：可达π_t、约束y_t、记忆m_t，按耦合方程更新，其中π受y约束并加噪声，y由环境与π调节，m为π的慢速滑动平均。探索不依赖外部信号，而是内生调节噪声σ_π(t)=ψ(I(t))·G(t)，其中ψ(I)=A I e^{-I/I0}在中等I处取峰值；同时通过沉降学习π0更新，并引入空间耦合核维持整体集成。动作选择由外部奖励与内在好奇机制共同引导，在LunarLander-v2和BipedalWalker-v3上进行评测。

### 三、结果（Result）
该方法在LunarLander-v2与BipedalWalker-v3上取得了与PPO和ICM等深度RL算法相当的性能。核心发现是愉悦好奇功能C2=全局重叠G×相干盆地数B×盆地间转换率T在中等噪声水平出现单峰，峰值两侧下降超过1.5倍，验证了好奇窗口的存在；而Active Inference代理在相同分析下没有出现类似的峰值，表明该动力学捕获了独特的探索机制。

### 四、结论（Conclusion）
探索可以通过系统内部的相干性调节内生产生，而不需要外生噪声或辅助好奇心目标。在中间不连贯状态下，系统既能保持整体整合又能结构化访问多个相干盆地，从而出现最优探索。该框架提供了探索何时发生以及如何自适应调节的原理性描述，并区别于现有RL和Active Inference方法。

### 五、方法论与关键技术细节
C2函数定义为全局重叠（Bhattacharyya系数）乘以相干盆地数乘以盆地间转换速率，其乘积形式由表示定理唯一确定。场内通过软最大将增广状态映射到离散概率场，π更新依赖逐点乘指数负y再加噪声，噪声尺度由I的Unimodal函数调节；沉降学习以α为速率按历史不连贯的指数衰减更新基线π0。实验场为40单元空间中的五个高斯盆地；LSM稀疏循环权重谱半径ρ<1。局限包括理论证明在附录中依赖计算引入的函数形式，且仅验证了两个基准任务，尚未在更多非平稳领域测试。
