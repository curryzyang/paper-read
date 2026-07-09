# Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization

- 区域：精读区
- 排名：4
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Sounaq Das, Tanmay Sen, Raghu Nandan Sengupta, Aditya Gupta
- 机构：Indian Institute of Technology Kanpur, McKinsey and Company, Indian Institute of Management Amritsar, Indian Statistical Institute Kolkata
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06610v1) · [PDF](https://arxiv.org/pdf/2607.06610v1)

## TLDR
The paper proposes a deep reinforcement learning framework (MORP-DRL) that jointly optimizes expected return and downside risk using variance, CVaR, and EVaR under transaction costs and reliability constraints, demonstrating competitive risk-return performance and reduced tail risk across market regimes.

## Abstract
Portfolio optimization under uncertainty is inherently a multi-objective decision problem involving complex interactions among return, risk, market dynamics, and practical investment constraints. Existing reliability based portfolio optimization approaches primarily rely on static optimization frameworks and often fail to capture sequential decision making, tail risk, and market frictions such as transaction costs. To address these limitations, we propose a deep reinforcement learning framework for multi-objective reliability based portfolio optimization (MORP-DRL). The proposed framework jointly optimizes expected return and downside risk using three complementary risk measures: variance, Conditional Value-at-Risk (CVaR), and Entropic Value-at-Risk (EVaR). To model uncertainty and heavy-tailed market behavior, asset returns are represented using GARCH(1,1), Extreme Value Theory, and a t-copula dependence structure, while realistic scenarios are generated through quasi-Monte Carlo simulation. A Proximal Policy Optimization (PPO) based strategy is developed under practical constraints including transaction costs and portfolio bounds, and is benchmarked against NSGA-II. Experiments on ten global equity indices across pre-COVID, COVID, and post-COVID market regimes demonstrate that MORP-DRL achieves competitive risk-return performance, reduced downside risk during periods of market stress, and scalability to high-dimensional portfolio settings.


## 精读解读（中文）
### 一、研究动机
现有基于可靠性的投资组合优化方法主要依赖静态优化框架，无法捕捉序列决策过程、尾部风险以及交易成本等市场摩擦，导致在动态市场环境中的表现不佳。为了克服这些局限性，本文提出一种深度强化学习框架，用于多目标可靠性投资组合优化。

### 二、技术方案（Method）
使用十个全球股票指数在COVID前、中、后三个市场时期的数据，首先通过GARCH(1,1)、极值理论和t-copula依赖结构对资产收益的不确定性和重尾行为进行建模，然后利用拟蒙特卡洛模拟生成现实场景。构建三个基于不同风险度量（方差、条件风险价值CVaR和熵风险价值EVaR）的可靠性约束双目标优化模型，并引入比例交易成本。采用近端策略优化（PPO）算法作为深度强化学习策略，在交易成本和投资组合边界等实际约束下学习动态资产配置策略，并与经典多目标进化算法NSGA-II进行对比。训练和推理流程包括定义状态（历史收益、当前权重等）、动作（权重调整）、奖励（考虑风险和交易成本后的净收益）以及PPO的迭代更新。

### 三、结果（Result）
在三个市场时期（COVID前、中、后）的实验中，MORP-DRL框架相对于等权重基准和NSGA-II方法实现了具有竞争力的风险-收益表现，尤其在市场压力时期显著降低了下行风险。此外，该框架在FTSE100指数的高维投资组合设置中展现出良好的可扩展性，PPO和NSGA-II均能有效处理高维问题，但资产配置特征存在差异。

### 四、结论（Conclusion）
本文提出的基于深度强化学习的多目标可靠性投资组合优化框架（MORP-DRL）成功地将可靠性约束、交易成本和多种尾部风险度量整合到统一的序列决策框架中，在动态市场条件下比传统静态优化方法和现有DRL方法表现更优，为实际投资管理提供了有效的工具。

### 五、方法论与关键技术细节
关键细节包括：(1) 使用GARCH(1,1)、极值理论和t-copula联合建模来准确刻画收益的波动聚集和尾部依赖；(2) 采用拟蒙特卡洛模拟生成高维低差异场景，提高可靠性估计效率；(3) PPO算法使用截断的替代目标函数稳定训练，并处理连续动作空间；(4) 在奖励函数中显式纳入比例交易成本，通过权重的绝对变化计算；(5) 设定两个可靠性水平（β1和β2）分别约束收益和风险，置信度通常取0.95；(6) 实验覆盖三个不同市场制度，验证模型对不同波动环境的适应性；(7) 与NSGA-II的对比显示PPO在尾部风险控制上的优势，但NSGA-II在帕累托前沿多样性上可能更好；(8) 局限性：依赖历史数据训练，可能对快速结构变化敏感；未考虑流动性约束和非线性交易成本。
