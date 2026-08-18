# Multi-period Value-at-Risk Constrained Portfolio Optimization via DC Programming

- 区域：精读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Thi Thu Van Nguyen
- 机构：University of Economics Ho Chi Minh City
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13748v1) · [PDF](https://arxiv.org/pdf/2608.13748v1)

## TLDR
This paper formulates a multi-period portfolio optimization problem with finite-scenario Value-at-Risk constraints, transaction costs, and diversification regularization as a penalized difference-of-convex (DC) program, and proposes a projected inertial Boosted DC Algorithm (iBDCA) with convergence guarantees and numerical/backtest validation.

## Abstract
We study a multi-period portfolio optimization problem with finite-scenario Value-at-Risk (VaR) constraints, transaction costs, and diversification regularization. Using a finite-scenario VaR--CVaR identity, we derive a penalized difference-of-convex (DC) formulation over the underlying convex portfolio set. To solve the resulting nonsmooth and nonconvex problem, we propose a projected inertial Boosted Difference-of-Convex Functions Algorithm (iBDCA) that combines inertial extrapolation, an objective safeguard, and a boosted line search. We prove that the method is well defined, generates a monotonically decreasing objective sequence, and has only critical accumulation points for the penalized DC problem. Under a local no-ties condition at an accumulation point, we further establish whole sequence convergence with a local \(R\)-linear rate. Numerical experiments compare iBDCA with DCA and standard BDCA on matched problem instances. Out-of-sample backtests additionally include equal-weight and buy-and-hold benchmarks to illustrate the trade-offs among realized return, risk, transaction costs, and empirical VaR control.


## 精读解读（中文）
### 一、研究动机
多期投资组合优化在风险约束下具有重要应用，但Value-at-Risk（VaR）作为分位数风险度量在有限情景下是连续分段仿射且非凸非光滑，导致传统凸优化方法难以直接处理。现有研究多为单期静态模型或凸多期模型，缺乏统一处理多期VaR约束、交易成本和分散化正则的框架。本文旨在建立多期VaR约束投资组合问题的DC规划模型，并设计高效算法求解。

### 二、技术方案（Method）
本文考虑每个规划期具有预算与非负约束、VaR限制、交易成本耦合相邻期配置，以及二次分散化正则的多期投资组合问题。利用有限情景VaR-CVaR恒等式将VaR约束表示为两个CVaR函数的差，从而将原问题转化为带罚函数的DC规划问题，定义在凸投资组合集上。求解采用投影惯性增强DCA（iBDCA），其核心步骤包括：惯性外推生成外推点，投影到凸可行集；构造强凸DC子问题并求解；结合Armijo型增强线搜索和目标函数safeguard保证充分下降与单调性；迭代更新直到收敛。算法在每一步利用DC分解中凸函数的次梯度或梯度，实现非凸非光滑目标的有效优化。

### 三、结果（Result）
数值实验在两组多资产数据集上进行。匹配求解器实验比较了iBDCA与经典DCA和标准BDCA，在相同问题实例下评估惩罚目标值、胜率、迭代次数和求解时间；样本外回测额外加入等权重和买入持有基准，报告最终财富、夏普比率、最大回撤和经验VaR。结果表明iBDCA在目标值下降和计算效率上优于对比算法，且能有效控制VaR，同时展示收益、风险、交易成本和VaR控制之间的权衡。

### 四、结论（Conclusion）
提出的iBDCA算法理论性质完备：良定义、产生单调递减目标序列、所有累积点均为惩罚DC问题的临界点；在局部无并列条件下建立全序列收敛及局部R-线性收敛速率。实验验证了算法有效性和实用性，为多期VaR约束投资组合优化提供了可靠的DC规划求解方案。

### 五、方法论与关键技术细节
关键实现细节包括：有限情景VaR-CVaR恒等式需要选择参数γ满足0<γ<ε̄，其中ε̄由情景概率子集和的最大间隙确定；惩罚DC公式通过罚参数平衡原VaR约束和惩罚项，并给出与原始问题具有相同全局最优解的充分条件；DC分解中凸函数G和H均为连续分段仿射函数；求解子问题采用强凸化确保唯一解；增强线搜索使用Armijo条件并配合目标safeguard；收敛性分析依赖扩展值目标函数满足Kurdyka-Łojasiewicz不等式且指数为1/2；局部R-线性收敛需要累积点处的局部无并列条件。算法复杂度受情景数S和资产数n及期数T影响，实际中需适当选择γ和罚参数。局限包括有限情景近似误差、局部收敛性质依赖条件。
