# Enforcing Opacity in Discrete Event Systems via Delayed Observations

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jiwei Wang, Simone Baldi, Wenwu Yu, Xiang Yin
- 机构：Linyi University, Shanghai Jiao Tong University, Southeast University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06489v1) · [PDF](https://arxiv.org/pdf/2608.06489v1)

## TLDR
This paper introduces K-delayed opacity for discrete event systems with artificially delayed observations, and develops methods to verify this opacity and synthesize optimal sensor activation policies that guarantee it.

## Abstract
Artificially introducing a delay in the observations of a system can be an effective mechanism to mask the system itself, with the goal to increase its opacity and thus its security. This work investigates opacity in discrete event systems with delayed observations. We focus on two questions: how to verify opacity under delayed observations, and how to synthesize sensor activation policies that guarantee opacity under such delayed conditions. To address these questions, we first introduce the definition of opacity under delayed observation and develop a corresponding verification method. We then extend such analysis tool into a synthesis tool by proposing an optimization approach for designing sensor activation policies guaranteeing opacity under delayed observations. An example is used to illustrate the analysis and synthesis procedures.


## 精读解读（中文）
### 一、研究动机
现有离散事件系统（DES）的 opacity 研究主要关注静态观测，未利用人为引入观测延迟来增强系统安全性。本文旨在填补这一空白，从防御者角度考虑通过人为延迟观测来遮蔽秘密状态，防止窃听者推断系统状态。

### 二、技术方案（Method）
方法分为分析和合成两部分。分析部分首先提出 K-delayed opacity 定义，引入延迟观测下的 delay observer 结构，用于验证系统在延迟观测下是否满足 opacity。具体地，利用有限自动机 G=(X,E,α,X0) 建模，传感器激活策略由 Ω=(R,Θ) 表示，定义投影算子 P_Ω 和延迟操作 ζ^K_Ω(s)，构造延迟观察器 O_Ω^K(G) 并递归计算状态估计与延迟计数，验证所有到达秘密状态的事件串是否存在同延迟观测的非秘密串。合成部分提出一个针对延迟观测的容器结构，涵盖所有能保证 K-delayed opacity 的传感器激活策略，并依据特定准则（如最优性）从中选择最优策略，以实现动态传感器激活下的 opacity 保证。

### 三、结果（Result）
通过示例验证了分析和综合方法的有效性。结果表明，人为引入观测延迟可以显著增强系统的 opacity；且延迟越大，系统满足 K-delayed opacity 的可能性越高，即 K' 延迟 opacity 蕴含 K 延迟 opacity（K ≥ K'）。

### 四、结论（Conclusion）
本文系统研究了离散事件系统中延迟观测下的 opacity 分析与综合问题。提出了 K-delayed opacity 的定义、基于 delay observer 的验证方法，以及基于容器结构的传感器激活策略合成方法，为通过人为延迟增强系统安全性提供了系统化工具。

### 五、方法论与关键技术细节
关键细节包括：系统模型为有限自动机，秘密状态集 X_S 需保护；传感器激活策略 Ω=(R,Θ) 需满足可行性条件（不可观测事件不触发传感状态转移）；延迟操作 ζ^K 收集与延迟后观测一致的前缀；delay observer 构造时考虑了多个延迟事件的记录（区别于仅记录单个延迟的已有方法）；算法中延迟计数 u 初始为无穷，若初始状态估计全在秘密状态则置为 K，不可观测事件使 u 减一（直至 0），可观测事件根据目标状态估计是否仍属秘密状态决定是否记录；合成方法扩展了动态掩码合成和最许可观测器框架，需在 K-delayed opacity 约束下优化传感器激活策略。
