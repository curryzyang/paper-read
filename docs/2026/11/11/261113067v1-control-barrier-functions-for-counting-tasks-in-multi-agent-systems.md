# Control Barrier Functions for Counting Tasks in Multi-Agent Systems

- 区域：精读区
- 排名：2
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Georgios Mitsos, Sofie Haesaert, Siyuan Liu
- 机构：Eindhoven University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13067v1) · [PDF](https://arxiv.org/pdf/2611.13067v1)

## TLDR
This paper proposes a control barrier function framework that uses recursion-based differentiable CBFs in quadratic programs to enforce counting invariance and counting convergence tasks in multi-agent systems—requiring at least \(m\) agents to satisfy a condition—without explicit agent assignment or combinatorial subteam enumeration.

## Abstract
Multi-agent systems increasingly operate in dynamic environments and execute complex tasks that require coordination, posing significant computational challenges. Counting tasks, which require a minimum number of agents to satisfy a given condition, arise naturally in such systems. Examples include surveillance tasks, where at least m drones must continuously monitor a critical area, and emergency-response tasks, where at least m robots must converge to an incident location. The identities of the agents assigned to these tasks may change dynamically depending on their states, input bounds, and individual objectives. In this work, we propose a control barrier function (CBF)-based framework for enforcing counting invariance and counting convergence tasks, without explicitly assigning agents or enumerating all possible subteams. We develop a recursion-based method for constructing differentiable CBFs for counting tasks. The resulting CBF constraints are incorporated into quadratic programs, enabling online controller synthesis. Numerical experiments demonstrate scalability to large multi-agent systems, while a multi-drone emergency-response case study illustrates the satisfaction of counting tasks.


## 精读解读（中文）
### 一、研究动机
多智能体系统在动态环境中常需完成计数任务，即至少 m 个智能体持续或最终满足某条件，且满足条件的智能体身份可随状态、输入能力和个体目标动态变化。预先分配智能体或枚举所有子队会造成分配低效、不可行或组合爆炸，而现有计数时序逻辑方法多依赖离散模型和离线综合，组合CBF方法虽避免枚举但需每个智能体一个约束，在大规模团队中带来计算与QP可行性挑战。

### 二、技术方案（Method）
针对每个智能体定义C1标量函数 h(x_i)，其非负当且仅当该智能体满足任务条件；计数任务等价于第 m 大值 h_(m)≥0。由于 h_(m) 通常不可微，方法用LogSumExp对前 k 大值之和 σ_k 构造C1近似，并以下界 ar h_(m)=hatσ_m-τln binom(M,m)-hatσ_(m-1) 作为候选CBF；通过前向递推高效评估该CBF值、后向递推计算梯度，避免显式任务分配和子队枚举。随后将计数不变与计数收敛对应的聚合CBF约束加入二次规划，在线求解各智能体在非线性输入仿射动力学下的控制输入。

### 三、结果（Result）
数值实验表明该方法可扩展到较大规模多智能体系统，多无人机应急响应案例验证了计数任务约束的满足。与每智能体一个CBF约束的组合式方法相比，该方法对每个计数任务仅使用一个聚合CBF约束，避免枚举组合数量子队并降低QP规模。

### 四、结论（Conclusion）
论文提出了统一的CBF框架，同时处理计数不变和计数收敛任务，允许满足条件的智能体身份动态变化，并通过在线QP实现无需显式分配的控制器综合。在标准可行性与正则假设下，还给出了QP控制器局部Lipschitz连续性的充分条件，适用于监视、应急响应等计数型多智能体任务。

### 五、方法论与关键技术细节
关键点包括：用 h_i 的非负性编码单智能体条件，用第 m 大值编码至少 m 个智能体满足条件；排序值不可微，因此构造可微下近似，保证 ar h_(m)≥0 可推出 h_(m)≥0，近似保守度由 τ 和 ln binom(M,m) 项控制；采用集中式CBF定义，控制器可依赖联合状态，需满足标准可行性与正则性以保证局部Lipschitz；主要局限是LogSumExp近似的保守性、τ选择影响紧度与数值行为，以及集中式计算和通信依赖。
