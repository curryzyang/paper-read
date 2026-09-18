# Optimal Resource Extraction under Distribution Learning and Infinite-Horizon Stochastic Hamilton--Jacobi Equations

- 区域：精读区
- 排名：4
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Ulrich Horst, Jinniao Qiu, Yang Yang
- 机构：Humboldt-Universität zu Berlin, University of Calgary
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17717v1) · [PDF](https://arxiv.org/pdf/2609.17717v1)

## TLDR
TLDR: This paper shows that an optimal exhaustible-resource extraction problem with unknown reserves and combined endogenous and exogenous learning admits an equivalent time-consistent formulation characterized by the unique viscosity solution of an infinite-horizon stochastic Hamilton–Jacobi equation, with the long-run optimal extraction rate determined by the asymptotic hazard rate of the limiting reserve distribution.

## Abstract
We study an infinite-horizon stochastic control problem for the optimal exploitation of an exhaustible resource with unknown total reserves. Information is generated both endogenously through continued extraction without depletion and exogenously through an external information flow. This interaction makes the natural problem non-Markovian and time-inconsistent. We show that it nevertheless admits an equivalent time-consistent formulation with the same optimal controls. The associated value function is characterized as the unique viscosity solution of a stochastic Hamilton--Jacobi equation with random coefficients. We prove comparison on the infinite horizon through a Snell-envelope-based strict-contact argument and establish uniqueness by an independent Brownian regularization and a BSDE correction, avoiding piecewise Markovian approximations. Finally, we identify the deterministic benchmark and show that, under persistent reserve uncertainty, the rescaled stochastic value function converges to a pathwise deterministic control problem, with the long-run optimal extraction rate determined by the asymptotic hazard rate of the limiting reserve distribution.


## 精读解读（中文）
### 一、研究动机
可耗竭资源的最优开采自Hotelling以来就是核心问题，但总储量未知时，开采不仅消耗资源还会通过“未耗竭”产生内生学习，同时地质调查等外生信息流又持续更新储量信念。两种学习交织使问题天然非马尔可夫且时间不一致，经典确定性动态规划与Hamilton-Jacobi方法无法直接适用。

### 二、技术方案（Method）
在由Wiener过程生成的过滤下，建立单生产者模型，控制变量为开采率、过程在资源耗尽时终止；总储量X_bar非负、无原子、无界支撑，用条件生存函数F_hat(t,x)=P(X_bar>x|F_t)刻画路径依赖的学习。将条件归一化导致的时间不一致目标重构为等价时间一致问题并保持相同最优控制。值函数被刻画为带随机系数的无限时域随机Hamilton-Jacobi方程的粘性解；比较原理通过Snell包络构造严格接触停止时，唯一性通过独立布朗正则化、空间平移和线性BSDE修正构造上下障碍并做挤压论证。

### 三、结果（Result）
论文证明等价时间一致形式与原问题具有相同最优控制，且值函数是相应无限时域随机Hamilton-Jacobi方程的唯一粘性解；该证明避免分段马尔可夫近似。长期分析表明，在持续储量不确定性下，重标度随机值函数收敛到路径确定性的控制问题，长期最优开采率由极限储量分布的尾部危险率显式决定；确定性基准情形下值函数可分解为贴现因子和满足一阶边值问题的平稳分量。

### 四、结论（Conclusion）
该工作为未知总储量、内生与外生学习并存的资源开采提供了严格的无限时域随机控制与随机粘性解理论，并揭示残余尾部不确定性直接控制长期最优开采行为。其结果连接时间不一致控制、随机HJ方程和资源经济学，可作为信息流下长期开采政策的理论基准，但一般方程仍难以显式求解。

### 五、方法论与关键技术细节
关键细节包括：信息由布朗过滤生成，但条件生存函数依赖整段历史，因此系数可随机且路径依赖；假设总储量有限期望、无原子、无界支撑，且生存函数几乎处处为正并对状态Lipschitz。比较原理需处理随机测试函数的鞅项，相切通过条件期望与最优停止定义，并用Snell包络和鞅修正获得有限停止时；无限时域需一侧渐近条件排除排序违反逃逸至时空无穷。唯一性依赖独立布朗扰动使辅助方程一致超抛物，再做空间平移和线性BSDE修正；渐近收敛还需条件生存概率一致收敛、额外正则性及大储量极限危险率存在。
