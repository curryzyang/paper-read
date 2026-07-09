# The Approximation Ratio for the Risk of Myopic Bayesian Active Learning for Linear Regression

- 区域：精读区
- 排名：6
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Stephen Mussmann
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06642v1) · [PDF](https://arxiv.org/pdf/2607.06642v1)

## TLDR
This paper proves the first tight approximation ratio (up to an absolute constant) for the risk of the greedy algorithm in myopic Bayesian active learning for linear regression, showing it is linear in the maximum initial leverage score.

## Abstract
Active learning studies the fundamental question: what data should we choose to observe? The greedy algorithm in optimal experiment design is a common heuristic and also equivalent to myopic Bayesian active learning for linear regression, the common framework where long-term planning is replaced with the one-step optimal choice. In this work, we prove a first-of-its-kind approximation ratio for the greedy algorithm's risk that is tight up to an absolute constant. The approximation ratio is linear in the maximum initial leverage score (MILS), a newly identified quantity fundamental to the greedy algorithm's performance. Finally, we illustrate the results with simple numerical simulations.


## 精读解读（中文）
### 一、研究动机
主动学习研究如何选择最优数据，贪婪算法是常用启发式但缺乏理论分析。本文针对线性回归中短视贝叶斯主动学习等价于最优实验设计中的贪婪算法，首次给出其风险的近似比，填补理论空白。

### 二、技术方案（Method）
本文通过理论分析定义了一个关键量——最大初始杠杆分数（MILS），并利用该量导出贪婪算法风险的上界。具体地，证明了贪婪算法所选择数据导致的预测风险与最优风险的比值不超过MILS的线性函数，且此界紧至一个绝对常数。数值模拟在简单场景下验证了理论结果。

### 三、结果（Result）
核心发现：贪婪算法的风险近似比与最大初始杠杆分数线性相关，且该比值在绝对常数意义下是紧的。数值模拟显示，当MILS较小时，贪婪算法接近最优；当MILS较大时，性能退化在意料之中。

### 四、结论（Conclusion）
本文首次为短视贝叶斯主动学习（线性回归）的贪婪算法提供了理论保证，揭示了最大初始杠杆分数是控制其性能的关键指标。该结果有助于理解贪婪策略的适用条件，并对实际主动学习算法设计有指导意义。

### 五、方法论与关键技术细节
关键方法细节：定义了最大初始杠杆分数h_max = max_i x_i^T (X_0^T X_0 + λI)^{-1} x_i，其中X_0为初始数据，λ为正则化参数。近似比定理表明风险之比≤ C * h_max，C为绝对常数。局限性：结论限于线性模型和平方损失，且要求初始设计点可逆；理论紧性依赖于常数但未给出具体值。
