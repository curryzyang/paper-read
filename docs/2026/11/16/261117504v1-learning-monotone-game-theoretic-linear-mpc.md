# Learning monotone game-theoretic linear MPC

- 区域：精读区
- 排名：2
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Alberto Bemporad, Tatiana Tatarenko
- 机构：Technische Universität Darmstadt, IMT School for Advanced Studies Lucca
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17504v1) · [PDF](https://arxiv.org/pdf/2611.17504v1)

## TLDR
The paper proposes a bilevel imitation-learning method that learns a strongly monotone game-theoretic linear MPC law from recorded multi-agent input/output data—without requiring agents’ objectives—while enforcing hard input constraints, soft output constraints, and closed-loop stability via a jointly learned quadratic Lyapunov penalty.

## Abstract
We propose a method to learn a game-theoretic model predictive control (GT-MPC) law by imitation from input and output data of a running multi-agent system. By interpreting the recorded inputs as the first moves of the equilibria of a game played by the agents, we learn the GT-MPC weights under hard input constraints and soft output constraints, without requiring the agents to reveal their objectives. We also impose that the resulting generalized Nash equilibrium (GNE) problem is strongly monotone, which ensures the existence and uniqueness of the equilibrium and, hence, that the learned GT-MPC law is well defined and can be evaluated efficiently online by variational GNE-seeking algorithms for linear-quadratic games. Moreover, strong monotonicity implies that the equilibrium is almost everywhere differentiable with respect to the references and the weights, which enables automatic differentiation for gradient-based optimization. In addition, we promote closed-loop stability of the unconstrained equilibrium feedback by incorporating a penalty that involves a jointly learned quadratic Lyapunov function. Learning a GT-MPC formulation enables us to explain the agents' objectives, reproduce their behavior in simulation in new scenarios, optimize their set-points, design mechanisms, and enforce additional constraints. A numerical example illustrates the approach.


## 精读解读（中文）
### 一、研究动机
多智能体系统中各智能体往往不愿公开自身目标，且实际运行可能由分散控制回路甚至人工操作完成，因此仅凭观测输入输出学习一个可复现其行为的博弈论MPC律很有价值。学习到的GT-MPC还能继承MPC处理输入/输出约束的能力，并用于闭环仿真、设定点优化、机制设计和附加约束实施。

### 二、技术方案（Method）
先从多次实验采集参考、输入和输出数据，用带ℓ2正则的输出误差辨识线性离散状态空间模型并估计初始状态，再用卡尔曼滤波得到状态估计。将记录输入解释为智能体博弈广义纳什均衡的第一步，构建含智能体特定跟踪权重、输入增量权重和共享输出约束松弛惩罚的参数化线性二次GT-MPC，并把参数设为状态估计、上一输入和参考。学习采用双层优化：内层对每个数据点求解变分GNE，外层拟合权重使均衡第一步逼近期望输入；同时通过对称部分正定约束按构造保证强单调性，利用均衡对参数几乎处处可微进行自动微分，并用L-BFGS-B优化，另加联合学习的二次Lyapunov函数惩罚促进无约束均衡反馈的闭环稳定性。

### 三、结果（Result）
该方法无需智能体公开目标即可学习GT-MPC权重，强单调性保证每个参数下变分GNE存在且唯一，使学习到的控制律定义良好并可用线性二次博弈的变分GNE算法高效在线求解。数值算例表明能够较精确地重建智能体背后的博弈，并可通过参考优化塑造闭环行为。

### 四、结论（Conclusion）
学习强单调的博弈论线性MPC可从输入输出数据中解释智能体目标、在新场景中复现其行为，并支持设定点优化、机制设计及附加约束实施；其核心是以唯一可微均衡为内层、以模仿第一步为外层进行可扩展的逆博弈学习。

### 五、方法论与关键技术细节
关键实现包括：以输出误差最小化加小ℓ2正则辨识(A,B,C)及各实验初始状态，卡尔曼滤波噪声协方差为调参量；GT-MPC含预测/控制/约束时域T、Tu、Tc，输入与增量约束为硬约束、共享输出约束通过各智能体松弛变量软约束；参数p=(ξ̂k,uk−1,rk)，决策含输入增量和松弛变量；强单调性条件为sym(Ā)⪰μI，μ>0；稳定性由联合学习的二次Lyapunov函数惩罚项促进；外层用L-BFGS-B和自动微分，且未知量规模不随样本数线性增长。局限包括线性时不变模型与线性二次成本假设、强单调性限制、仅观测均衡第一步、噪声与卡尔曼滤波调参影响，以及主要数值算例验证。
