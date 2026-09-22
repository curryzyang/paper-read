# Continuous Delayed-Memory Stochastic Gradient Descent and Continuous-Time Reinforcement Learning from History of Astrophysical Time Series Studies

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Debartha Paul, Juncheng Yi
- 机构：Iowa State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20906v1) · [PDF](https://arxiv.org/pdf/2609.20906v1)

## TLDR
This paper introduces a Continuous-Delayed-Memory Stochastic Gradient Descent that uses past iteration states to improve exploration and convergence over vanilla SGD, and proposes a continuous-time policy-gradient reinforcement learning method that avoids solving the HJB PDE while recovering the Gibbs policy, motivated by neural-SDE modeling of astrophysical quasar light curves.

## Abstract
Quasars are luminous objects in the universe that exhibit stochastic brightness variations encoding information about the supermassive black holes powering them, and modeling these variations from ground-based survey data time series, known as light curves, is a statistical challenge. This paper reviews how stochastic differential equations (SDEs) have been adapted with neural network parameterizations to overcome this challenge in history. We create the Continuous-Delayed-Memory Stochastic Gradient Descent which depend on the past state of the discrete iteration process. We performed the simulation on some 2-dimensional landscape and observed some wider-exploration and more precise convergent behavior compared to Vanilla SGD by adjusting hyperparameters. Besides, we proposed a reinforcement learning structure with continuous time policy gradients for exploratory policies without solving HJB PDE, and we show that its optimality conditions recover the Gibbs policy of previous works.


## 精读解读（中文）
### 一、研究动机
类星体光变曲线具有不规则采样、随机性和潜在延迟记忆特征，传统OU/DRW模型线性、单波段且高频PSD斜率不匹配，难以支撑LSST时代大规模多波段时序建模；同时，随机梯度下降和连续时间强化学习也需要能利用历史状态的探索-收敛机制。本文因此回顾天体物理时序中SDE到神经SDE/SDDE的发展，并提出带延迟记忆的连续时间SGD与无HJB方程的连续时间策略梯度框架。

### 二、技术方案（Method）
作者先综述OU/DRW、CARMA、Neural ODE、Latent SDE及Neural SDDE在类星体光变建模中的路线，重点引入以z(t)和z(t-τ)为漂移输入的神经随机延迟微分方程及其函数空间马尔可夫性、重构性质和延迟感知伴随反向传播。随后构造Continuous-Delayed-Memory SGD：将离散迭代过程写成依赖当前与过去状态的连续时间延迟记忆随机动力系统，在二维损失曲面上用Euler-Maruyama类离散化进行模拟并调节超参数。连续时间强化学习部分则用策略梯度结构直接优化探索策略，避免求解HJB偏微分方程，并通过最优性条件与Gibbs策略建立联系。

### 三、结果（Result）
二维景观模拟显示，调参后的Continuous-Delayed-Memory SGD相比Vanilla SGD具有更宽的探索范围和更精确的收敛行为，表明历史状态记忆可改善探索-利用权衡。强化学习部分的最优性条件可恢复已有工作的Gibbs策略，说明所提连续时间策略梯度框架在理论上与经典探索策略一致。综述还表明，神经SDE/SDDE在类星体多波段光变重建、季节空隙插值和黑洞质量等参数推断上优于逐对象高斯过程基线，并能利用延迟结构建模X射线到光学波段的再处理时延。

### 四、结论（Conclusion）
本文把天体物理时序建模中的随机微分方程、延迟记忆优化和连续时间强化学习统一到同一类带漂移与噪声的动力系统视角，提出Continuous-Delayed-Memory SGD作为利用历史状态的连续时间优化器，并给出无需解HJB方程的连续时间探索策略梯度框架。其核心结论是延迟记忆可带来更优探索与收敛，且连续时间最优性条件自然导向Gibbs策略。该工作为LSST时代类星体光变建模和更广泛的延迟随机系统优化提供了理论线索，但新优化器仍主要停留在二维合成实验层面。

### 五、方法论与关键技术细节
关键实现包括：Neural SDDE漂移γ(X(t),X(t-τ);θγ)和扩散σ(t,X(t),X(t-τ);θσ)中的延迟τ为固定超参数，初始条件需在[-τ,0]上给定历史函数φ；反向传播采用延迟感知伴随方法，将时间区间按≤τ分段并处理未来t+τ的伴随贡献，同时借助重构性质实现内存高效梯度。天体物理综述涉及10年LSST、6波段u,g,r,i,z,y、不规则采样和约6个月季节空隙，训练数据为10^5条模拟光变曲线，并比较ELAsTiCC/PLAsTiCC；模型损失含NLL、上下文MSE、路径KL和参数NLL，KL权重循环退火。局限性在于CDM-SGD主要用二维合成景观验证、延迟τ固定、未在大规模真实类星体数据上端到端检验，且随机梯度估计方差与伴随分段计算复杂度仍需评估。
