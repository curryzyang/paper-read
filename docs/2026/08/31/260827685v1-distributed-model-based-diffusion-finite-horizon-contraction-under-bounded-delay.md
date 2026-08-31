# Distributed Model-Based Diffusion: Finite Horizon Contraction under Bounded Delay

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Seth Golembeski, Keith L. Gibson, Alexander Gross, Shreyas Kousik, Anirban Mazumdar
- 机构：Sandia National Laboratories, Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27685v1) · [PDF](https://arxiv.org/pdf/2608.27685v1)

## TLDR
TLDR: This paper proves finite-horizon contraction and latency robustness for Distributed Model-Based Diffusion, a distributed sampling-based MPC method for nonlinear, nonconvex multi-agent systems, and demonstrates that it outperforms centralized Model-Based Diffusion on tasks like circleswap and aerial combat despite communication delay.

## Abstract
Simultaneously optimizing the trajectories of multiple agents is a challenging problem plagued by nonlinearity, nonconvexity, and the curse of dimensionality. A collection of interacting aerial vehicles or self-driving cars in an intersection are examples of complex multi-agent systems that remain difficult to solve without many simplifying assumptions. The presence of communication latency between agents further increases the difficulty. In this paper, we analyze Distributed Model-Based Diffusion: a sampling-based Model-Predictive Control method suitable for highly nonlinear, nonconvex, nonsmooth, multi-agent systems. We prove contraction and robustness to latency for multi-agent, nonconvex problems, showing applicability to real-world constraints. We test the algorithm on a circleswap task, a cooperative medium-fidelity driving task, and in an aerial combat scenario. Despite the addition of latency, our algorithm improves circleswap makespan by 31% and increases aerial combat win rate by 25% compared to centralized Model-Based Diffusion.


## 精读解读（中文）
### 一、研究动机
多智能体轨迹同时优化面临非线性、非凸、高维度以及智能体间通信延迟等挑战，现有方法常需线性、凸性或可微等强假设，难以应对真实世界约束。本文旨在分析分布式模型基扩散（DMBD）方法，证明其在有界延迟下对多智能体非凸问题的收缩性与鲁棒性，从而支持其在实际网络退化场景中的部署。

### 二、技术方案（Method）
DMBD将标准MBD扩展到M个智能体：每个智能体m维护自身扩散状态x_m并估计其他智能体状态x_hat_m，按反向SDE索引从N到1迭代。每步中，智能体从自身状态为中心的高斯分布Y_{j,j}~N(x_{j,j}, sigma^2)采样自身动作，结合异步消息队列中收到的其他智能体最新时间戳状态（丢弃旧信息），构成完整联合样本Y；在固定其他智能体动作下，用指数权重计算加权均值Y_bar^(0)，估计梯度∇G_m，再按梯度上升公式x_{j,j}^{i-1} = x_{j,j}^i + eta * gradient更新自身状态，并向其他智能体广播新状态。整个过程并行运行，可使用再ceding horizon方式；实验中设置最大延迟50ms。

### 三、结果（Result）
DMBD在有通信延迟下仍然收敛。与集中式MBD相比，加入延迟后DMBD在circleswap任务中makespan改进31%，在空战场景中胜率提高25%。在circleswap、多智能体赛车和空战三类递增复杂度任务中，仿真结果验证了理论分析的有效性。

### 四、结论（Conclusion）
本文首次为DMBD提供了全局有限时域收缩证明，并分析了有界延迟下的鲁棒性，表明该方法适用于高度非线性、非凸、非光滑的多智能体系统，且能在真实网络延迟下保持收敛，优于集中式MBD。

### 五、方法论与关键技术细节
理论假设包括：目标函数具有光滑凸核与次高斯尾部、弱耦合成本结构（耦合度量C控制最佳响应偏差）、有界延迟（估计状态至多滞后tau_max步）、初始点位于最大凸球内，且步长需满足上下界（几何噪声调度下下界为1-gamma/a_m）。证明过程基于扩散诱导的块状平滑目标G，利用最优间隙引理、逐级收缩引理和RMS误差递归界，最终得到有限时域误差界（定理3.6）。实现细节：消息带时间戳以避免重复或乱序，每智能体仅采样自身动作而保持其他智能体估计值不变，使用几何sigma调度，温度lambda较小。局限性包括：需要验证步长范围非空，且证明依赖于弱耦合等假设；实验延迟50ms为保守设定。
