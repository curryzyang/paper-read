# Scalable Self-Supervised Learning for Multiphase AC-OPF in Distribution Systems with Topology Reconfiguration

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Hoang T. Nguyen, Shaohui Liu, Reetam Sen Biswas, Varsha Pendyala, Nurali Virani, Deepjyoti Deka, Priya L. Donti
- 机构：Massachusetts Institute of Technology, GE Vernova
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.25095v1) · [PDF](https://arxiv.org/pdf/2608.25095v1)

## TLDR
Penalty+SLFS is a self-supervised learning framework for multiphase distribution AC-OPF that trains directly from the optimization objective and constraints via a differentiable power-flow solver, efficiently handles switch-induced topology changes using Sherman-Morrison-Woodbury updates, and achieves near-optimal, feasible solutions with up to three orders of magnitude speedups over IPOPT on feeders up to 8,500 nodes.

## Abstract
The proliferation of distributed energy resources (DERs) in distribution grids enables the active coordination of these assets to reduce costs and enable cleaner operations. Realizing this potential requires solving multiphase AC optimal power flow (AC-OPF) quickly across varying loads, DER availabilities, and topology reconfigurations, at much greater speed and scale than conventional nonlinear solvers. Learning-based surrogates can offer millisecond inference, yet existing methods target largely balanced transmission systems and do not scale to the multiphase, unbalanced, and reconfigurable nature of distribution feeders at utility scale. We present the Penalty + Sequential Linearized Feasibility Seeking (SLFS) algorithm, a self-supervised learning framework for multiphase distribution AC-OPF under switch-induced topology changes. Penalty+SLFS requires no labeled optimal solutions and trains directly from the AC-OPF objective and constraints through a differentiable fixed-point power flow solver, avoiding expensive label generation and admitting robust training procedures. Topology changes are handled efficiently using Sherman-Morrison-Woodbury updates of the admittance-matrix inverse, while an M-step Jacobian approximation accelerates differentiation through the power flow solver. At inference, SLFS repairs any infeasible predictions, providing feasibility guarantees with low computational overhead. On IEEE feeders ranging from 13 to 8,500 nodes, Penalty+SLFS achieves negligible optimality gaps and near-zero constraint violations, delivers up to three orders of magnitude speedups over IPOPT, and remains robust under large distributional shifts, demonstrating a viable path toward real-time, topology-aware AC-OPF for large-scale distribution grids.


## 精读解读（中文）
### 一、研究动机
配电网中分布式能源的普及要求快速求解多相交流最优潮流（AC-OPF），以适应负荷、DER可用性和拓扑重构的变化。传统非线性求解器速度慢，而现有基于学习的替代方法主要针对平衡输电网，无法扩展至多相、不平衡且可重构的配电网馈线，且监督学习需要昂贵的标签生成。

### 二、技术方案（Method）
提出Penalty+SLFS自监督学习框架。该方法无需最优解标签，直接以AC-OPF目标函数和约束作为损失，通过可微不动点潮流求解器训练神经网络，输入为负荷、DER可用性和开关状态，输出DER有功/无功设定值。训练时采用惩罚损失处理约束，利用Sherman-Morrison-Woodbury公式高效更新拓扑变化下的导纳矩阵逆，并用M步雅可比近似加速对潮流求解器的微分。推理阶段使用序列线性化可行性搜索（SLFS）迭代修正不可行预测，通过逐次线性化和矩阵-向量操作实现GPU友好的可行性修复。

### 三、结果（Result）
在13至8500节点的IEEE馈线上，Penalty+SLFS实现了可忽略的最优性差距和接近零的约束违规，相对IPOPT提速高达两到三个数量级，并在较大分布偏移下保持鲁棒性。

### 四、结论（Conclusion）
Penalty+SLFS为大规模配电网提供了一条实时、拓扑感知的AC-OPF可行路径，能够同时处理多相不平衡、开关重构和数千节点规模，兼具高精度、强可行性保证和显著加速。

### 五、方法论与关键技术细节
关键点包括：训练数据无需可行解标签，可同时使用可行和不可行样本，增强泛化；利用SMW更新导纳矩阵逆，应对开关拓扑变化，对病态情况采用迭代细化；M步雅可比近似提高训练速度和内存效率，并给出误差界；SLFS在标准假设下保证约束违规单调递减；方法为GPU友好，仅用矩阵-向量操作；局限性可能在于需要可微潮流求解器及对大型系统的计算资源要求。
