# Optimal Adaptive Market Making: A Theoretical Framework for High-Yield Liquidity Provision in Perpetual Futures Markets

- 区域：精读区
- 排名：7
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Minmin Zeng, Yi Liu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11888v1) · [PDF](https://arxiv.org/pdf/2607.11888v1)

## TLDR
This paper develops a rigorous theoretical framework for optimal market making in zero-fee perpetual futures markets, deriving closed-form conditions and strategies for achieving high annualized returns through adaptive spread, inventory, and hedging controls.

## Abstract
We develop a rigorous theoretical framework for optimal market making in perpetual futures markets with zero maker fees. We model the market maker's problem as a stochastic optimal control problem on a filtered probability space, where the controls are adaptive bid-ask spreads and inventory hedging decisions across two exchanges. Our contributions include: (i) a PnL decomposition theorem separating revenue into spread income, adverse selection loss, inventory carrying cost, hedging friction, and funding rate exposure; (ii) the Hamilton-Jacobi-Bellman equation for the joint spread-inventory-hedging control problem under CARA utility with a verification theorem; (iii) High-APY Regime Theorems characterizing profitable regions via five dimensionless parameters, culminating in a Master APY Formula; (iv) analysis of zero-fee economics on decentralized perpetual exchanges with optimal entry-exit thresholds; (v) optimal cross-exchange hedging policies with funding rate dynamics and a hedge regime trichotomy; (vi) a robustness margin quantifying parameter uncertainty tolerance; (vii) exponential drawdown probability bounds and a universal APY-VaR identity; (viii) ergodic inventory distribution under optimal control with Bayesian adaptive estimation; (ix) Kelly-optimal leverage with ruin boundaries; and (x) multi-pair portfolio allocation with diversification saturation results. Numerical analysis with twenty-three figures reveals phase transitions between profitable and unprofitable regimes. Our framework unifies and extends the Avellaneda-Stoikov, Gueant-Lehalle-Fernandez-Tapia, and Glosten-Milgrom paradigms for modern decentralized venue microstructure.


## 精读解读（中文）
### 一、研究动机
去中心化永续合约市场采用零做市商费用机制，这创造了与传统中心化交易所截然不同的经济环境。核心问题是：在零费用条件下，做市商能否实现年化50%至200%的持续高收益，以及相应的最优自适应策略是什么。

### 二、技术方案（Method）
将做市商问题建模为滤波概率空间上的随机最优控制问题，状态变量包括库存、现金、参考价格和DEX-CEX溢价，控制变量为自适应买卖价差和跨交易所对冲决策。采用CARA效用函数，通过动态规划推导HJB方程，并证明验证定理确保最优性。进一步导出PnL分解定理（分离价差收益、逆向选择损失、库存持有成本、对冲摩擦和资金费率暴露）、高APY区域定理（五个无量纲参数刻画盈利边界）、主APY公式、最优跨交易所对冲策略（包含资金费率动态和三分法对冲区间）、贝叶斯自适应估计知情交易比例、以及多品种组合的Kelly最优杠杆与多元化饱和结果。数值分析通过22张图表展示相变。

### 三、结果（Result）
提出主APY公式，统一所有成本渠道为单个闭式表达式，并给出年化夏普比率超过给定阈值所需满足的五参数条件。证明零费用机制扩展了盈利参数空间，构成经济护城河。推导出最优库存分布为高斯分布，并得到APY-VaR乘积为与策略无关的通用常数。数值分析揭示了盈利与非盈利区域之间的尖锐相变边界，其由逆向选择与价差捕获的比率主导。

### 四、结论（Conclusion）
该框架统一并拓展了Avellaneda-Stoikov、Gueant-Lehalle-Fernandez-Tapia和Glosten-Milgrom经典范式，为现代去中心化交易所的做市商提供了完整的理论指导，包括高收益区的充要条件、自适应策略、对冲决策和风险管理工具。

### 五、方法论与关键技术细节
关键假设包括：参考价格为零漂移算术布朗运动、DEX-CEX溢价服从Ornstein-Uhlenbeck过程、资金费率也遵循OU过程且与溢价独立（实际存在相关性）、成交到达为泊松过程且强度随价差指数衰减、知情交易比例固定（但通过贝叶斯在线估计）。重要参数包括知情交易概率、取消延迟、套利强度、五个无量纲参数。损失函数采用CARA效用，控制约束包括库存上下限。推导中运用了伊藤引理、鞅方法、贝叶斯后验集中率。局限性包括模型假设可能与真实微观结构存在偏离，但引入了鲁棒性边际量化参数不确定性的容忍度，以及指数回撤概率界和APY-VaR恒等式作为风险度量。
