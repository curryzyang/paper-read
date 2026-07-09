# Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization

- 区域：精读区
- 排名：10
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Sounaq Das, Tanmay Sen, Raghu Nandan Sengupta, Aditya Gupta
- 机构：McKinsey and Company, Indian Statistical Institute Kolkata, Indian Institute of Technology Kanpur, Indian Institute of Management Amritsar
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06610v1) · [PDF](https://arxiv.org/pdf/2607.06610v1)

## TLDR
The paper proposes a deep reinforcement learning framework for bi-objective portfolio optimization that jointly optimizes expected return and downside risk using variance, CVaR, and EVaR under practical constraints, achieving reduced tail risk and scalability across market regimes.

## Abstract
Portfolio optimization under uncertainty is inherently a multi-objective decision problem involving complex interactions among return, risk, market dynamics, and practical investment constraints. Existing reliability based portfolio optimization approaches primarily rely on static optimization frameworks and often fail to capture sequential decision making, tail risk, and market frictions such as transaction costs. To address these limitations, we propose a deep reinforcement learning framework for multi-objective reliability based portfolio optimization (MORP-DRL). The proposed framework jointly optimizes expected return and downside risk using three complementary risk measures: variance, Conditional Value-at-Risk (CVaR), and Entropic Value-at-Risk (EVaR). To model uncertainty and heavy-tailed market behavior, asset returns are represented using GARCH(1,1), Extreme Value Theory, and a t-copula dependence structure, while realistic scenarios are generated through quasi-Monte Carlo simulation. A Proximal Policy Optimization (PPO) based strategy is developed under practical constraints including transaction costs and portfolio bounds, and is benchmarked against NSGA-II. Experiments on ten global equity indices across pre-COVID, COVID, and post-COVID market regimes demonstrate that MORP-DRL achieves competitive risk-return performance, reduced downside risk during periods of market stress, and scalability to high-dimensional portfolio settings.


## 精读解读（中文）
### 一、研究动机
现有基于可靠性的投资组合优化方法主要依赖静态优化框架，无法捕捉序列决策、尾部风险和交易成本等市场摩擦，难以适应动态市场环境。因此需要一种能同时优化预期收益与下行风险、处理不确定性和厚尾行为的动态方法。

### 二、技术方案（Method）
提出MORP-DRL框架，以10个全球股票指数的历史数据为输入，使用GARCH(1,1)、极值理论和t-copula对资产收益进行建模以捕捉不确定性和厚尾行为，并通过拟蒙特卡洛模拟生成情景。采用近端策略优化（PPO）作为强化学习策略，在包含交易成本和投资组合边界等实际约束下进行动态优化。同时构建三个模型分别使用方差、条件风险价值（CVaR）和熵风险价值（EVaR）作为风险度量，并与NSGA-II对比。

### 三、结果（Result）
在COVID前、中、后三个市场时期的实验表明，MORP-DRL实现了有竞争力的风险-收益性能，在市场压力期（如COVID期间）显著降低了下行风险，并扩展到FTSE100高维投资组合时仍保持有效性。相比等权重基准和NSGA-II，PPO策略在尾部风险控制方面表现更优。

### 四、结论（Conclusion）
提出的深度强化学习框架能够有效进行多目标可靠投资组合优化，通过整合尾部风险度量、可靠性约束和交易成本，实现了动态自适应性和可扩展性，为实际投资管理提供了稳健的决策支持。

### 五、方法论与关键技术细节
关键点包括：资产收益使用GARCH(1,1)和极值理论建模厚尾，依赖结构采用t-copula；情景生成通过拟蒙特卡洛模拟提高收敛性；PPO算法在连续动作空间下处理多目标；三种风险度量分别针对方差、CVaR和EVaR进行可靠性约束；交易成本为比例成本，投资组合权重有上下界；可靠性水平β1和β2设定为高置信度；实验涵盖三个极端市场时期；方法局限性在于依赖模拟环境且有参数敏感性。
