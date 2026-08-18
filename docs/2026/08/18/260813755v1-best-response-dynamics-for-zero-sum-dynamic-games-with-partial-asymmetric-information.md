# Best Response Dynamics for Zero-Sum Dynamic Games with Partial-Asymmetric Information

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Yuxiang Guan, Iman Shames, Tyler H. Summers
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13755v1) · [PDF](https://arxiv.org/pdf/2608.13755v1)

## TLDR
TLDR: This paper proposes a best response dynamics approach for zero-sum stochastic linear quadratic dynamic games with partial and asymmetric information, showing that although iterative best responses generate increasingly higher-order beliefs, the game's value converges after only a few iterations, indicating that higher-order beliefs offer vanishing benefit.

## Abstract
This work studies a class of zero-sum stochastic linear quadratic dynamic games (LQDGs) under partial and asymmetric information. Information asymmetry introduces fundamental challenges related to \textit{belief representation} and \textit{theory of mind}, where players must impute belief states and estimates of other players to inform their strategies. Existing work highlights the difficulty of applying dynamic programming-like decomposition approach to these problems. An alternative approach based on \textit{best response dynamics} is proposed, which provides insights into belief representation and theory of mind challenges. Explicit expressions for each player's best response within the class of pure linear dynamic output feedback control strategies are derived, where the internal state dimension of each control is an integer multiple of the system state dimension. As players iteratively update their best responses, they form increasingly higher-order belief states, leading to infinite-dimensional internal states. However, numerical results reveal that the game's value converges after only a few iterations, suggesting that higher-order belief states provide vanishing benefit. This work further conducts numerical experiments to analyze the impact of asymmetric beliefs, belief orders, relative controllability and observability, and direct feed-through on a linear quadratic pursuit-evasion game's value.


## 精读解读（中文）
### 一、研究动机
部分非对称信息下的零和随机线性二次动态博弈面临信念表示与心理理论挑战，玩家必须推测其他玩家的信念状态与估计来制定策略；现有基于动态规划分解的方法难以处理此类缺少共同信息结构的问题，因此本文提出基于最优反应动力学的替代求解途径。

### 二、技术方案（Method）
针对部分非对称信息零和随机LQ动态博弈，提出最优反应动力学求解框架。首先将某一玩家的策略初始化为零，另一玩家的最优反应即为标准LQG控制器，由LQR与Kalman滤波器组成，其内部状态维度等于系统状态维度；随后固定该策略，另一玩家的最优反应是增广LQG控制器，其Kalman滤波器不仅估计系统状态，还估计对方的状态估计，从而形成一阶信念状态。依次迭代更新双方策略，每轮都会引入更高阶信念，使内部控制状态维度逐步增加。文中推导了纯线性动态输出反馈控制策略类内每个玩家最优反应的显式表达式，其中控制内部状态维度为系统状态维度的整数倍。数值实验进一步分析了不对称信念、信念阶数、相对可控性与可观测性以及直接馈通对线性二次追击-逃避博弈值的影响。

### 三、结果（Result）
数值结果表明，博弈值在仅几次最优反应迭代后即收敛，说明高阶信念状态带来的收益随阶数增加而逐渐消失；研究还揭示了不对称信念、信念阶数、相对可控/可观性和直接馈通等因素对博弈值的影响。可复现的核心结论是：尽管理论上内部状态维数趋于无穷，实际中少数迭代即可达到近似收敛，高阶信念的边际价值可忽略。

### 四、结论（Conclusion）
最优反应动力学为缺乏共同信息结构的部分非对称信息动态博弈提供了一种可行的求解方法，其每次迭代只需求解标准LQG子问题，无需共同信息假设，且数值收敛迅速，适合用于分析此类博弈中的信念形成与策略交互。

### 五、方法论与关键技术细节
方法不依赖共同信息结构，直接适用于私有噪声测量设置；每次迭代通过求解标准LQG子问题获得最优反应；控制器内部状态维度为系统状态维度的整数倍，并随信念阶数增加而增大。理论上面临无限回归的高阶信念问题，但数值上数轮迭代即可收敛。局限性在于未与基于共同信息结构的序贯分解方法进行直接数值比较，因为现有方法在此类私有非对称信息设置下尚未定义。实验分析中重点考察了不对称信念、信念阶数、相对可控性和可观测性及直接馈通对博弈值的影响。
