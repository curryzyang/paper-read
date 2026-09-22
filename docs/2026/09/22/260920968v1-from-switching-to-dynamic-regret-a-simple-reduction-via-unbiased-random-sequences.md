# From Switching to Dynamic Regret: A Simple Reduction via Unbiased Random Sequences

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Yibo Wang, Wenhao Yang, Sifan Yang, Yuanyu Wan, Lijun Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20968v1) · [PDF](https://arxiv.org/pdf/2609.20968v1)

## TLDR
This paper presents a simple reduction from dynamic regret minimization to switching regret minimization via unbiased random auxiliary sequences, recovering minimax-optimal dynamic regret bounds for strongly convex, exp-concave, and general convex losses.

## Abstract
In non-stationary online learning, dynamic regret has attracted increasing attention as a measure of how well an online learner performs against a time-varying comparator sequence. Despite considerable advances, attaining optimal bounds for strongly convex and exp-concave losses often involves intricate analysis. In this paper, we present a \textit{simple} framework that reduces dynamic regret minimization to switching regret minimization. As a result, we can derive dynamic regret bounds by using off-the-shelf algorithms with switching regret guarantees. The key idea of our reduction is to construct, for \textit{any} comparator sequence, an auxiliary random sequence that is unbiased at each round, with the controlled variance and a manageable number of switches. Combining this construction with suitable surrogate losses, we can decompose dynamic regret into the expected switching regret against the random sequence and its controlled variance. Theoretically, for strongly convex and exp-concave losses, we establish the $\widetilde{O}(T^{1/3}P_T^{2/3})$ dynamic regret bounds, where $T$ denotes the time horizon and $P_T$ denotes the path-length of the comparator sequence. Moreover, for general convex losses, the same reduction also recovers the $O(\sqrt{T(1+P_T)})$ dynamic regret bound. Notably, all our findings match the minimax optimal results for these three types of losses, highlighting the versatility of our proposed framework.


## 精读解读（中文）
### 一、研究动机
在非平稳在线学习中，动态遗憾衡量在线学习器相对于随时间变化比较器序列的性能，近年来受到广泛关注。然而，针对强凸损失和指数凹损失取得最优界通常需要复杂分析。本文希望提供简单框架，把动态遗憾最小化归约到切换遗憾最小化，从而复用已有切换遗憾算法。

### 二、技术方案（Method）
给定在线学习序列、损失类型以及任意比较器序列，构造一个每轮无偏的辅助随机序列，并控制其方差和切换次数。结合合适的代理损失，将动态遗憾分解为对该随机序列的期望切换遗憾与受控方差项。随后直接调用具有切换遗憾保证的现成算法，即可推导动态遗憾界，无需为不同损失类型重新进行复杂分析。

### 三、结果（Result）
对强凸损失和指数凹损失，该框架得到 \widetilde{O}(T^{1/3}P_T^{2/3}) 的动态遗憾界，其中 T 为时间 horizon，P_T 为比较器序列的路径长度。对一般凸损失，同一归约恢复 O(\sqrt{T(1+P_T)}) 的动态遗憾界。这些结果分别匹配三类损失的极小极大最优保证。

### 四、结论（Conclusion）
本文提出了一种从切换遗憾到动态遗憾的简单归约，核心是无偏随机序列构造与代理损失分解。该归约能够借助现成算法统一获得强凸、指数凹和一般凸损失下的最优动态遗憾界。这突出了所提框架的通用性和简洁性。

### 五、方法论与关键技术细节
关键细节包括：构造的辅助随机序列必须每轮无偏，且其方差与切换次数可控；通过代理损失把动态遗憾拆解为期望切换遗憾加方差项；最终调用现成切换遗憾算法得到理论界。理论上覆盖强凸、指数凹和一般凸损失，并达到极小极大最优。局限方面，摘要未涉及实验验证，贡献主要是理论归约，其应用依赖于随机序列构造和相应凸性假设。
