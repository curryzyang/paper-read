# SPARROW: Survival-POMCP for Adaptive Robot Routing, Observation, and Waiting

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Hshmat Sahak, Aoran Jiao, Nicholas Rhinehart, Timothy D. Barfoot
- 机构：University of Toronto
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.21008v1) · [PDF](https://arxiv.org/pdf/2609.21008v1)

## TLDR
TLDR: SPARROW is a belief-space POMCP planner for robot navigation among temporary obstacles that decides whether to traverse, wait, observe, or reroute while learning class-conditioned survival models online from censored data and estimating the value of collecting labeled observations, reducing mean time-to-goal by 12–26% in simulation and 20.5% on a physical robot compared with OSCAR.

## Abstract
Temporary obstacles that may block a robot's planned route create a sequential navigation problem: a robot must decide whether to wait for a blockage to clear, reroute, or acquire more information about the obstacle before acting. We formulate graph navigation among temporary obstacles as a partially observable semi-Markov decision process and introduce SPARROW, a belief-space planner built on Partially Observable Monte Carlo Planning (POMCP). SPARROW searches over traversal, observation, and finite-duration waiting actions while maintaining a particle belief over latent obstacle classes and clearance times. Class-conditioned survival models are learned online from both clearance observations and right-censored encounters where the robot reroutes before clearance is observed. A generative model simulates obstacle arrivals and clearances as each action unfolds, so the planner can account for blockages that may occur along alternative routes. We further introduce a value-of-learning criterion that trades the immediate cost of collecting labelled survival data against its expected reduction in future navigation regret. Across two simulation graphs and multiple obstacle-class settings, SPARROW reduces mean time-to-goal by 12-26% relative to OSCAR, a recent survival-based method for the same problem. On a physical mobile robot, SPARROW reduces mean time-to-goal by 20.5% relative to OSCAR while selectively observing, waiting, and rerouting as environment conditions change.


## 精读解读（中文）
### 一、研究动机
在结构化环境中，移动机器人常受限于固定图路径，而临时障碍会阻塞计划路线，机器人必须顺序决定等待障碍清除、绕行或先观察获取信息。现有 OSCAR 只围绕当前阻塞选择耐心阈值，并假设下游阻塞也被等待，因而高估绕行成本且不显式规划未来遭遇，这促使作者把该问题建模为部分可观察半马尔可夫决策过程并显式搜索未来决策。

### 二、技术方案（Method）
SPARROW 将图导航形式化为 POSMDP，状态包含机器人顶点与潜在障碍配置，动作包括 Traverse、MaxWait(e,W) 和 Observe(e)，成本为实际耗时并以无折扣随机最短路径目标最小化多回合到达目标时间。它用粒子信念表示潜在障碍类别与剩余寿命，并在线为每类障碍拟合 Kaplan-Meier 生存模型，样本同时来自观测到清除的未删失数据和机器人提前绕行造成的右删失数据；生成模型按事件顺序模拟障碍到达与清除，支持 POMCP 在 Traverse、Observe 和有限等待动作上做成本最小 UCT 搜索。叶节点用时间依赖期望成本最短路径 A* 近似未展开价值，已知障碍按年龄条件残存生存积分计算延迟，未知障碍用平稳期望延迟，KM 阶梯积分闭式缓存；外层的知识梯度式价值学习近似决定是否值得为获取标记生存样本而承担当前绕行成本。

### 三、结果（Result）
在两个仿真图和多种障碍类别设置中，SPARROW 相对 OSCAR 将平均到达目标时间降低 12% 到 26%；在物理移动机器人上，相对 OSCAR 将平均到达目标时间降低 20.5%。实验还表明它能随环境条件变化选择观察、等待或绕行，并与标准始终等待、始终绕行及 oracle 模型规划器等基线进行了比较。

### 四、结论（Conclusion）
结果表明，在临时障碍图导航中，显式对下游障碍遭遇和未来决策进行信念空间多步规划，比仅优化当前阻塞的生存阈值方法更有效。SPARROW 通过在线生存学习、右删失数据利用和时间依赖叶评估，实现了自适应观察、等待与绕行，并在仿真和真实机器人上验证了收益。

### 五、方法论与关键技术细节
关键实现细节包括 POSMDP 无折扣 gamma=1、动作成本等于经过时间、Traverse 仅在无阻塞时完成、Observe 固定耗时并假设分类器完美但实验用现成分类器验证、MaxWait 的等待时长从有限集合 W 选取。生存数据每类初始为空且无合成预热，只有 Observe 得到的标记遭遇进入对应类，提前离开产生右删失样本；粒子信念需与局部自由/阻塞观测及语义标签一致，必要时重采样增强。搜索中持续时间仅按 Δ 量化用于树索引，精确 τ 用于成本、障碍老化和信念更新；叶评估不暴露未观测边的粒子隐藏状态，TDSP 的延迟非负且满足 FIFO，积分按 KM 事件时间以 O(|D_k|) 闭式求和并缓存。主要约束或局限是依赖离散图和动作选择、分类器准确性、障碍过程平稳性假设以及仿真到真实部署的近似，价值学习采用可计算的知识梯度代理而非完整贝叶斯自适应 POMDP。
