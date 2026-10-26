# End-to-End Differentiable Diffusion Conditioning for Physics-Informed Optimization

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Ricardo Luna Gutierrez, Vineet Gundecha, Rahman Ejaz, Varchas Gopalaswamy, Riccardo Betti, Sahand Ghorbanpour, Aarne Lees, Soumyendu Sarkar
- 机构：Hewlett Packard Enterprise, University of Rochester
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31721v1) · [PDF](https://arxiv.org/pdf/2610.31721v1)

## TLDR
The paper proposes D2C, which converts a frozen conditional diffusion model into an end-to-end gradient-based optimizer for offline physics-informed design by backpropagating surrogate and physics-penalty gradients through deterministic denoising to optimize the conditioning signal at test time, achieving strong results on real-world laser pulse optimization and data-center workload scheduling as well as Design-Bench tasks.

## Abstract
Optimizing high-dimensional physical systems under expensive evaluations and complex constraints is a central challenge in science and engineering. In offline model-based optimization (MBO), methods must improve designs using only a fixed dataset and no test-time access to the true objective. However, existing methods typically suffer from conservatism, unconstrained surrogate exploitation, or function as static inference-time samplers that cannot refine candidates against precise physical objectives. In this paper, we propose Differentiable Diffusion Conditioning (D2C) for offline MBO, which leverages the fact that deterministic sampling makes the reverse denoising chain differentiable with respect to the conditioning signal. D2C turns a frozen conditional diffusion model into an end-to-end gradient-based optimizer by directly optimizing conditioning variables at test time via gradients from frozen surrogate objectives and physics-informed penalties backpropagated through the reverse chain. We implement this idea in a composed proposer-evaluator framework and evaluate it on laser pulse optimization for inertial confinement fusion, sustainable data-center workload scheduling, and four Design-Bench tasks. Our method achieves the strongest results on the two real-world tasks and the best average rank across four Design-Bench tasks.


## 精读解读（中文）
### 一、研究动机
高维物理系统在评估昂贵、约束复杂且需离线学习的场景下优化困难；现有离线模型优化方法存在过度保守、无约束代理利用或仅在推理时静态采样而无法按精确物理目标精修候选的问题。需要建立从物理目标到生成过程的可微路径，并在严格可行性约束下搜索高性能设计。

### 二、技术方案（Method）
D2C将冻结的条件扩散模型作为提议器、冻结的代理模型作为评估器；训练提议器时联合去噪损失、重构损失、物理保真损失和代理一致性损失，并采用空嵌入丢弃与EMA。推理时使用零随机项的确定性DDIM，使反向去噪链对条件可微，将条件拆为固定c_fix和可优化c_opt，仅通过复合物理损失经冻结扩散链反传更新c_opt；结合CFG、多次噪声采样、Dirichlet随机多目标权重和有效性优先筛选形成候选池并选最佳可行设计。

### 三、结果（Result）
D2C在惯性约束聚变激光脉冲优化和数据中心可持续负载调度两个真实任务上取得最强结果，并在四个Design-Bench任务上取得最佳平均排名；消融表明优化条件信号优于优化潜在噪声。核心比较结论是冻结提议器-评估器加端到端条件优化能在多个任务上同时提升性能与可行性。

### 四、结论（Conclusion）
将冻结扩散提议器与冻结代理评估器组合，并在确定性反向链上端到端优化条件变量，可在保持数据分布先验的同时由代理目标和物理惩罚引导出可行高性能设计，缓解保守性与无约束代理利用。该框架为安全关键物理设计提供了一种可微、可约束的离线模型优化途径。

### 五、方法论与关键技术细节
关键实现是仅更新c_opt且所有损失只依赖实际生成设计x_0，不直接依赖c_opt，从而避免目标标签漂移；梯度经完整T步DDIM与CFG反传，条件在每个时间步注入形成梯度捷径，引导尺度w影响梯度幅度和优化稳定性。推理需对N_z个噪声样本分别进行J步条件优化，计算和显存随T、J、N_z增长；物理约束包括积分守恒、幅值界和谱正则等，非光滑max/min用自动微分次梯度处理；损失项需按任务设计并保持可比尺度，存在任务依赖、固定噪声条件优化及多次采样成本等局限。
