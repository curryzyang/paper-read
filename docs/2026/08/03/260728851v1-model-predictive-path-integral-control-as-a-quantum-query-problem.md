# Model Predictive Path Integral Control as a Quantum Query Problem

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Goutam Das, Takashi Tanaka
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28851v1) · [PDF](https://arxiv.org/pdf/2607.28851v1)

## TLDR
This paper reformulates model predictive path integral (MPPI) control as a quantum query problem, showing that quantum amplitude estimation can quadratically improve the query complexity of the control update over classical Monte Carlo sampling.

## Abstract
Model predictive path integral control computes its update from cost-weighted trajectory samples and may require many classical rollouts in rare-event or high-accuracy regimes. We reformulate each component of the finite-ensemble MPPI update as a ratio of bounded path expectations and construct reversible rollout oracles encoding them as success probabilities, making the update directly estimable by quantum amplitude estimation. This gives a quadratic improvement in the query dependence on accuracy and rare-event desirability over classical Monte Carlo sampling, matching known lower bounds for the underlying scalar problem below the exhaustive-evaluation threshold, while our coordinatewise construction incurs a linear dependence on the number of control inputs. For a fixed ensemble, the low-temperature weights concentrate on the minimum-cost trajectories, connecting the limiting control to quantum minimum finding when the minimizer is unique. A fully enumerable guidance example validates the predicted estimator scalings, and an illustrative operation-count model with a crossover condition separates query advantage from modeled implementation advantage.


## 精读解读（中文）
### 一、研究动机
模型预测路径积分控制（MPPI）通过成本加权轨迹样本来计算更新，在罕见事件或高精度场景下可能需要大量经典轨迹模拟，其计算瓶颈本质上是期望估计问题。本文旨在将MPPI更新重新表述为量子查询问题，利用量子振幅估计实现查询复杂度的二次加速，并探讨其与已知下界的匹配关系。

### 二、技术方案（Method）
将有限集MPPI更新表示为两个有界路径期望的比率（a和b_i），并构造可逆的rollout代价预言机，通过受控旋转将路径成本编码为成功概率，从而直接用量子振幅估计估计a和b_i，得到控制更新。具体地，用Rademacher变量将噪声序列编码为比特串，形成D=2^{Nm}个码字的有限集成；由Hadamard门制备均匀叠加，代价预言机通过可逆算术计算轨迹成本S(z)，再经受控旋转编码g(z)=e^{-S(z)/λ}。对每个控制输入坐标分别估计b_i，得到坐标式构造，查询复杂度线性依赖于控制输入数m。另外，在低温极限下权重集中于最小成本轨迹，可采用量子最小搜寻恢复极限控制。

### 三、结果（Result）
证明了量子方法在查询复杂度上对精度ε和罕见事件需求获得二次改进（相比经典蒙特卡洛），并匹配已知标量估计问题的下界；但坐标式构造带来对控制输入数的线性依赖。在固定集成下，当温度趋于零且最小值唯一时，权重集中于最小成本轨迹，量子最小搜寻以二次减少的预言机评估次数恢复极限控制。一个可完全枚举的引导示例验证了预测的估计量缩放，操作计数模型给出了查询优势与实现优势的分离及交叉条件。

### 四、结论（Conclusion）
该工作将MPPI控制更新转化为量子查询问题，证明了量子振幅估计可显著降低期望估计的查询复杂度，为随机最优控制中的量子加速提供了理论基础，并指出了可逆实现成本与查询优势之间的权衡。

### 五、方法论与关键技术细节
关键细节包括：使用Rademacher分布代替高斯噪声，编码为Nm比特串，形成有限码本；成本函数S(z)=φ(x_N)+Σq(x_k)Δt，权重g(z)=e^{-S(z)/λ}；状态制备无需QRAM，均匀叠加由Hadamard门实现；量子振幅估计要求固定点可逆算术和多项式近似旋转角；假设弱逼近误差为O(Δt)（Assumption 3），以及算术精度ηa（Assumption 4）。方法的主要局限是坐标式构造导致查询次数线性依赖控制输入数m，且可逆电路的实际门开销可能抵消查询优势，需通过交叉条件判断；此外，低温极限分析限于固定集成，未断言有限码本更新对连续最优反馈的收敛性。
