# Reinforcement Learning-Guided NSGA-II Enhanced with Gray Relational Coefficient for Multi-Objective Optimization: Application to NASDAQ Portfolio Optimization

- 区域：精读区
- 排名：7
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Zhiyuan Wang, Qinxu Ding, Ding Ding, Siying Zhu, Jing Ren, Yue Wang, Chong Hui Tan
- 机构：Singapore University of Social Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16194v1) · [PDF](https://arxiv.org/pdf/2607.16194v1)

## TLDR
The paper proposes a reinforcement learning-guided NSGA-II enhanced with gray relational coefficients (RL-NSGA-II-GRC) that adaptively adjusts evolutionary parameters and uses GRC-based selection to improve convergence and diversity, achieving superior Pareto fronts in both benchmark multi-objective problems and a NASDAQ portfolio optimization case study.

## Abstract
In modern financial markets, decision-makers increasingly rely on quantitative methods to navigate complex trade-offs among multiple, often conflicting objectives. This paper addresses constrained multi-objective optimization (MOO) with an application to portfolio optimization for minimizing risk and maximizing return. To address existing gaps, we propose a novel reinforcement learning (RL)-guided non-dominated sorting genetic algorithm II (NSGA-II) enhanced with gray relational coefficients (GRC), termed RL-NSGA-II-GRC, which combines an RL agent controller and GRC-based selection to improve convergence and diversity of Pareto fronts. The agent adapts evolutionary parameters online using metrics of hypervolume, feasibility, and diversity, while the GRC tournament operator ranks parents via a unified score considering dominance rank, crowding distance, and proximity to ideal reference. We evaluate the framework on the Kursawe and CONSTR benchmarks and a NASDAQ portfolio application. On the benchmarks, RL-NSGA-II-GRC achieves convergence improvements of about 5.8% and 4.4% over NSGA-II, while preserving well-distributed non-dominated solutions. In the portfolio application, it produces a smooth, densely populated efficient frontier supporting identification of the maximum Sharpe ratio portfolio (annualized Sharpe =1.92) and utility-optimal portfolios for different risk-aversion levels. The main contributions are three-fold: 1) we propose an RL-NSGA-II-GRC method integrating an RL agent into the evolutionary framework to adaptively control parameters via generational feedback; 2) we design a GRC-enhanced binary tournament operator providing a comprehensive indicator to guide the search toward the Pareto front; 3) we demonstrate, on benchmark MOO and a NASDAQ case study, that the method delivers improved convergence and well-populated frontiers supporting actionable insights.


## 精读解读（中文）
### 一、研究动机
现代金融市场中，决策者需在多个冲突目标（如风险和收益）间权衡，但标准NSGA-II在约束紧、可行域窄时收敛慢且多样性易丧失。本文提出RL-NSGA-II-GRC方法，通过强化学习在线调整演化参数并引入灰色关联系数增强选择，以提升多目标优化的收敛性和Pareto前沿多样性。

### 二、技术方案（Method）
方法将RL agent集成到NSGA-II框架中，输入包括决策变量和有约束的多目标函数（最小化风险与负收益）。关键模块：1）RL agent（基于Q-learning）以种群超体积、可行性比和多样性为状态，自适应控制四个参数（交叉概率、变异强度、约束容忍度、前沿采样分数）；2）GRC增强的二元锦标赛选择算子，综合支配等级、拥挤距离和与理想参考点的几何接近度生成统一分数进行父代选择；3）非支配排序和拥挤距离维持多样性。流程：初始化种群，每代计算状态，RL agent选择动作，应用约束容忍支配规则，GRC选择父代、执行SBX交叉和多项式变异生成子代，合并父代与子代后按分式前沿采样机制进行精英生存选择，迭代直至满足终止条件。

### 三、结果（Result）
在Kursawe和CONSTR基准问题上，RL-NSGA-II-GRC相比NSGA-II收敛指标分别提升约5.8%和4.4%，并保持良好分布的Pareto解集。在NASDAQ-100投资组合优化中，生成光滑密集的有效前沿，最大夏普比率组合年化夏普比率达1.92，且支持不同风险厌恶水平下的效用最优组合识别。

### 四、结论（Conclusion）
本文提出RL-NSGA-II-GRC方法，主要贡献包括：1）RL agent自适应控制进化参数以平衡探索与利用；2）GRC增强选择算子提供综合性能指标引导搜索；3）在基准和NASDAQ案例中验证了方法能改善收敛性并生成充分的有效前沿，为投资者提供可操作的决策支持。

### 五、方法论与关键技术细节
数据采用NASDAQ-100成分股历史数据，约束包括预算和投资比例等；RL使用Q-learning，状态和动作经离散化处理；GRC采用无先验权重的形式；超参数包括种群大小、代数等；时间复杂度为O(MN^2)与标准NSGA-II一致；局限性包括RL学习效率依赖离散化设计，且参数调整可能对问题敏感，需进一步验证泛化性。
