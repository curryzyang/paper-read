# Optimality of Threshold Policies for Heat Storage Optimization and a Policy Gradient Algorithm

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Nicole Bäuerle, Florian Döttling
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37853v1) · [PDF](https://arxiv.org/pdf/2610.37853v1)

## TLDR
The paper proves that optimal heat-storage control for a prosumer trading with a district heating network follows a two-parameter threshold policy and develops a projected stochastic policy-gradient algorithm with finite-sample convergence guarantees by optimizing time-dependent thresholds.

## Abstract
We study the optimal control of a stylized finite-horizon heat-storage system operated by a prosumer who can buy heat from and sell heat to a district heating network. Heat production and consumption are uncertain, and charging and discharging decisions have to be taken before the subsequent heat balance is observed. The resulting problem is formulated as a Markov decision process with continuous state and action spaces. We first establish a structural characterization of the optimal policy as a two-parameter threshold policy. Under additional regularity assumptions, we prove differentiability and Lipschitz properties of the value functions.
  Exploiting the threshold structure, we parameterize the policy by the time-dependent lower and upper thresholds and derive a pathwise stochastic-gradient estimator. We then propose a projected stochastic policy-gradient algorithm, establish a constrained Kurdyka-Łojasiewicz inequality and derive global finite-sample bounds for both the objective optimality gap and the distance to the optimal threshold vector. Finally, numerical experiments for a non-stationary heat-balance process illustrate the evolution of the threshold parameters.


## 精读解读（中文）
### 一、研究动机
分布式可再生能源与产消者场景下，热储能需要在随机热生产与需求、以及充放电决策相对热平衡观测存在时滞的条件下运行，错误决策会导致储能不足并以更高紧急价格补热。论文旨在为这类有限时域热储能系统建立结构清晰、可解释且可数值求解的最优控制方法，并将策略优化从一般连续动作策略降维到少量阈值参数。

### 二、技术方案（Method）
论文将小时级有限时域热储能控制建模为连续状态与连续动作的马尔可夫决策过程，状态为当前储能水平，热生产减消费的随机热平衡由独立但时间非齐次的随机变量序列刻画，目标为最大化有限时域期望收益。首先证明最优策略具有两参数时变阈值结构：储能低于下阈值时从区域供热网购热，高于上阈值时向网络售热，并在附加正则假设下证明值函数的可微性与Lipschitz性质。随后利用该结构将策略参数化为每个时刻的下阈值和上阈值，共2T个参数，推导路径wise随机梯度估计器，并设计带投影的随机策略梯度算法，训练/推理流程为采样热平衡轨迹、沿轨迹计算阈值策略动作与收益、构造梯度估计并按投影更新阈值向量。

### 三、结果（Result）
论文给出最优策略为时变双阈值策略的结构性结论，并在正则条件下建立值函数可微和Lipschitz性质；基于阈值参数化得到投影随机策略梯度算法，建立受约束的Kurdyka-Łojasiewicz不等式，并给出目标最优性间隙与到最优阈值向量距离的全局有限样本界。数值实验针对非平稳热平衡过程，展示了阈值参数随时间的演化，说明算法可用于24小时日周期示例中的阈值学习与策略解释。

### 四、结论（Conclusion）
该工作表明，在文中的简化热储能模型下，复杂连续控制可等价或近似归结为时变上下阈值的低维策略优化，从而兼顾理论可解释性与数值可计算性。作者提出的投影随机策略梯度算法具有有限样本理论保证，可作为更复杂产消者储能系统的基准策略或传感器受限场景下的易实现方案。

### 五、方法论与关键技术细节
关键假设包括线性充放电动态且充放电量无约束、储热无损耗、无老化与维护、购售价格固定且成比例、热平衡随机变量相互独立；这些简化使阈值结构成立，但也构成主要局限。算法关键点在于将策略压缩为2T个时变阈值参数，使用路径wise随机梯度估计和投影更新，并借助受约束Kurdyka-Łojasiewicz条件推导全局有限样本界；理论分析允许时间非齐次扰动，数值实验采用小时级24小时日周期非平稳热平衡过程。
