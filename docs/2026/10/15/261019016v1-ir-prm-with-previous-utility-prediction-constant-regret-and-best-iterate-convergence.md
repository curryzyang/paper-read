# IR-PRM+ with Previous-Utility Prediction: Constant Regret and Best-Iterate Convergence

- 区域：精读区
- 排名：7
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Michael Sullins, Ian A. Kash
- 机构：University of Illinois Chicago
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19016v1) · [PDF](https://arxiv.org/pdf/2610.19016v1)

## TLDR
The paper proves that IR-PRM+ with previous-utility prediction, for both simultaneous and alternating updates, retains constant regret, \(O(T^{-1})\) average duality gap, \(O(T^{-1/2})\) best-iterate convergence, and Nash convergence in two-player zero-sum games, with an extension to CFR for extensive-form games.

## Abstract
Regret matching (and its variants) and counterfactual regret minimization are central algorithms in practice for normal-form and extensive-form game solving. Yet these have historically lacked the stronger theoretical convergence guarantees available to optimistic and extra-gradient methods. Recent work introduced IREG-PRM+, a regret matching variant which does have strong theoretical convergence guarantees. However, it relies on a simultaneous, extra-gradient update. IREG-PRM+ is an instance of the more general IR-PRM framework, where empirically optimistic and alternating updates often have better performance. However, the prior extra-gradient analysis does not extend to these cases. We introduce a new approach that covers both settings. For simultaneous and alternating IR-PRM+ in finite two-player zero-sum matrix games, previous-utility prediction recovers the constant-regret and convergence-rate guarantees previously obtained with extra-gradient prediction: external regret bounded independently of T, an O(T^{-1}) average duality gap, and an O(T^{-1/2}) best-current-iterate gap. Moreover, the current duality gap vanishes and the current profile converges to the Nash equilibrium set. The key step bounds the component of consecutive strategy movement not controlled by the existing IR-PRM+ regret inequality using the relative growth of the nondecreasing regret-vector norm rho_t. Coupling this bound across the two players yields recurrences whose effective coefficient scales as 1/(rho_t^X rho_t^Y), preventing unbounded norm growth. We extend the analysis to finitely many simplex learners under a weighted Minty condition and, through the corresponding CFR variant IR-PCFR+, recover analogous guarantees for finite two-player zero-sum perfect-recall extensive-form games under the same full-reach condition as prior work.


## 精读解读（中文）
### 一、研究动机
后悔匹配、CFR及其变体是正规式和扩展式博弈求解的常用实用算法，但历史上缺乏乐观/外梯度方法所具备的更强收敛保证；近期IREG-PRM+虽有强保证，却依赖同时外梯度预测，无法覆盖实践中常更优的上一轮效用乐观预测与交替更新。Zhang等人明确将这两类设置留作开放理论问题，因此本文要为IR-PRM+框架补齐这些实用更新下的常数后悔与快速收敛理论。

### 二、技术方案（Method）
在有限二人零和矩阵博弈中，对IR-PRM+采用上一轮效用预测：首轮预测为零，t>=2时行玩家用A y_{t-1}、列玩家用-A^T x_{t-1}；每轮由非负累积后悔向量归一化得中间策略，加入预测后经唯一标量平移保持正部L2范数，得到实际策略并仅在所玩策略处评估博弈，再以中心化预测误差更新后悔向量。证明从RVU中间不等式出发，把预测误差中未被控制的从x_{t-1}到tilde x_t的事后位移，用非减后悔向量范数rho_t的相对增长rho_t-rho_{t-1}来界定；将两名玩家的界耦合得到系数约1/(rho_t^X rho_t^Y)的递推，从而抑制范数无界增长。对交替更新则使用第一名玩家更新后的中间剖面处理错时预测误差，并把分析推广到加权Minty条件下的有限多个单纯形学习器及IR-PCFR+。

### 三、结果（Result）
证明在同时和交替IR-PRM+中，上一轮效用预测无需外梯度即可恢复IREG-PRM+的保证：外部后悔被与T无关的常数界住，平均对偶间隙为O(T^{-1})，最佳当前迭代间隙为O(T^{-1/2})。当前对偶间隙趋于零，且当前策略剖面向纳什均衡集收敛。对IR-PCFR+在相同full-reach条件下，得到有限二人零和完美回忆扩展式博弈的类似序列形式保证。

### 四、结论（Conclusion）
本文表明后悔向量范数增长本身可作为一种自阻尼机制，控制上一轮效用预测和交替更新带来的额外策略移动，从而弥合了实用后悔匹配变体与一阶方法强收敛理论之间的差距。该分析将常数后悔与最优平均率扩展到更实用的IR-PRM+/IR-PCFR+更新方式，并给出了额外的双位移RVU界。

### 五、方法论与关键技术细节
关键细节包括：算法参数自由、尺度不变，除首轮外每轮仅一次博弈评估；初始化采用对称单位向量以避免除零，零初始化在附录F处理；每步通过选择唯一gamma_t使正部后悔向量L2范数保持为rho_t，预测误差g_t=(u_t-m_t)-<u_t-m_t,x_t>1，更新为正部。理论针对有限二人零和矩阵博弈和有限二人零和完美回忆扩展式博弈，依赖加权Minty条件与full-reach假设；收敛常数与T无关但依赖动作维度、Minty权重、初始化和博弈，属于当前迭代/最佳迭代保证而非一般最后迭代收敛率，且扩展式结果继承先前工作的full-reach限制。
