# Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs

- 区域：精读区
- 排名：3
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Jingjuan Huang, Zhiyao Zhang, Alvaro Velasquez, Nathaniel D. Bastian, Jia Liu
- 机构：Ohio State University, University of Colorado at Boulder, Johns Hopkins University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07069v1) · [PDF](https://arxiv.org/pdf/2611.07069v1)

## TLDR
This paper proves finite-time critic convergence and sublinear regret for neural reinforcement learning in POMDPs by approximating them with finite-memory superstate MDPs and combining neural TD learning with policy mirror descent.

## Abstract
Reinforcement learning (RL) in Partially Observable Markov Decision Processes (POMDPs) is computationally challenging due to the curse of long-range dependence on history. Fortunately, recent studies have shown that a range of POMDPs that satisfy the filter stability assumption can be well approximated by a superstate Markov Decision Process (MDP) based on a truncated history in a finite-memory window, with a value gap that decays with the window length. However, existing finite-time convergence analyses on such superstate MDP surrogates are either limited to over-simplified linear function approximation or rely on an i.i.d. sampling oracle that is violated by POMDP trajectories, both of which severely limit the applicability of these theoretical results in practice. This motivates us to bridge the gap by investigating RL in POMDPs with nonlinear neural value function approximation. Our main contributions are threefold: i) We first establish a new finite-state MDP point-wise approximation error bound, which lays the foundation for our RL algorithm design and analysis in POMDPs; ii) By applying Temporal-Difference (TD) learning to POMDP-generated superstate transitions and targeting the Bellman fixed point of the superstate MDP, we prove a finite-time critic error bound with nonlinear neural value function approximation; and iii) By combining the neural critic function approximation error bound with the policy mirror descent framework, we obtain a finite-time sublinear regret against the optimal POMDP value. To the best of our knowledge, such a finite-time sublinear regret based on neural function approximation is the first in the literature for finite-memory POMDPs. Our numerical experiments also verify our theoretical results.


## 精读解读（中文）
### 一、研究动机
POMDP 中策略依赖长历史导致计算困难，有限记忆窗口的超状态 MDP 可在滤波稳定性假设下近似原 POMDP，但已有有限时间分析要么局限于线性函数逼近，要么依赖与实际 POMDP 轨迹不符的独立同分布采样。作者因此研究带非线性神经网络值函数逼近的 POMDP 强化学习，以弥补超状态代理 MDP 在理论分析与实际 on-policy 轨迹采样之间的缺口。

### 二、技术方案（Method）
论文先将满足滤波稳定性假设的 POMDP 历史截断为有限记忆窗口并构造超状态 MDP，建立 POMDP 与超状态 MDP 之间的逐点值函数近似界，并说明奖励函数与转移核失配可由同一滤波稳定性误差控制。随后在由 POMDP 轨迹生成的超状态转移上使用时序差分学习训练非线性神经网络评论家，目标是逼近超状态 MDP 的 Bellman 不动点；通过新的 Lyapunov 下降分析分离轨迹采样误差、神经网络模型误差和部分可观测误差。最后将神经评论家误差界嵌入策略镜像下降框架进行策略迭代，并利用 concentrability 假设处理策略迭代间的非平稳分布偏移，推理流程为采样 POMDP 轨迹、构造超状态、TD 更新神经评论家、PMD 更新策略并累积遗憾。

### 三、结果（Result）
论文给出超状态 MDP 的逐点近似误差界，其值差距随有限记忆窗口长度呈 O((1-rho)^ell) 衰减；并证明在 POMDP 轨迹采样下神经评论家可在有限时间内以 epsilon_critic 量级的误差逼近超状态 MDP 的 Bellman 不动点。进一步结合 PMD 得到相对于最优 POMDP 值的有限时间次线性遗憾，且遗憾界显式分离神经评论家误差、有限记忆近似误差和策略优化误差；据作者所知，这是有限记忆 POMDP 中首个基于神经函数逼近的有限时间次线性遗憾结果，数值实验也验证了理论结论。

### 四、结论（Conclusion）
在滤波稳定性和 concentrability 等条件下，使用有限记忆超状态代理、神经 TD 评论家和 PMD 策略更新的 POMDP 强化学习算法能够获得有限时间收敛与次线性遗憾保证。该结果将超状态 MDP 近似、非独立同分布 POMDP 轨迹下的神经评论家分析和策略镜像下降统一起来，说明有限记忆窗口与神经网络逼近可在理论上有控地用于部分可观测强化学习。

### 五、方法论与关键技术细节
关键实现点包括：POMDP 具有有限状态、观测和动作空间，奖励有界且折扣因子在 0 到 1 之间；核心先验是滤波稳定性，记忆窗口长度 ell 控制 POMDP 到超状态 MDP 的近似误差；评论家使用非线性神经值函数而非线性模型，并在 POMDP 生成的超状态转移上做 TD 学习，不假设独立同分布采样；分析使用 Lyapunov 下降分解误差，并用 concentrability 假设连接不同策略访问分布；局限是理论依赖滤波稳定性、concentrability、有限状态空间和有限记忆设定，预印本摘要与正文预览未给出具体网络宽度深度、步长、样本复杂度常数和实验超参数。
