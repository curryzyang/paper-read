# World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jie He, Wei Li, Junwen Tong, Rui Shao, Wei-Shi Zheng, Liqiang Nie
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02323v1) · [PDF](https://arxiv.org/pdf/2610.02323v1)

## TLDR
ProAct is a world-calibrated proposal-to-action flow framework for vision-language-action models that initializes generation from a motion- and scene-aware proposal calibrated by a predicted latent future, improving simulation and real-world task performance while halving denoising steps and reducing latency/increasing throughput compared with π₀.₅.

## Abstract
Flow-based Vision-Language-Action (VLA) policies generate action chunks by transporting samples from a task-agnostic isotropic Gaussian source. As this source is conditioned on neither recent execution nor predicted future evolution, (i) it discards the local continuity established by recently executed motion. (ii) Even when predictive world representations are introduced, they often only condition the transport dynamics rather than determine where generation starts, how far it may deviate, or along which action directions it may expand. Building on this observation, we introduce ProAct, a world-calibrated proposal-to-action framework that makes the generative source itself predictable. (i) To preserve motion continuity, a lightweight Proposal Expert converts recent actions into a scene-aware hypothesis via one motion-anchored endpoint flow-matching step, initializing generation near the demonstrated action manifold. (ii) To jointly capture intended scene evolution and proposal-future compatibility, a prospective World Expert treats the hypothesis as a soft motion prior while predicting the task-consistent latent future. (iii) From this compatibility, the model calibrates a proposal-centered anisotropic source, where a bounded per-step extent controls the allowed deviation and a trace-normalized low-rank geometry under a condition-number budget allocates refinement over coupled translation, rotation, and gripper directions. Compared with $π_{0.5}$, ProAct improves performance across simulation and real-world tasks while reducing denoising steps by 50%, inference latency by up to 25.8%, and increasing throughput by up to 34.8%.


## 精读解读（中文）
### 一、研究动机
基于流的VLA策略通常从任务无关的各向同性高斯源生成动作块，而该源既不条件于近期执行动作，也不条件于预测的未来演化，因此会丢弃近期运动建立的局部连续性；即使引入预测性世界表示，它们往往只调节传输动力学，而不决定生成从哪里开始、可偏离多远、沿哪些动作方向扩展。ProAct的动机是让生成源本身可预测，并由世界模型校准。

### 二、技术方案（Method）
输入包含视觉语言观测与近期执行动作序列，首先由轻量Proposal Expert将近期动作经一个运动锚定的端点流匹配步骤转换为场景感知假设，使生成初始化靠近示范动作流形；随后Prospective World Expert把该假设作为软运动先验，预测任务一致的潜在未来；再由提议与未来的兼容性校准以提议为中心的各向异性源，其中受限的每步范围控制允许偏差，迹归一化低秩几何在条件数预算下把细化能力分配到平移、旋转和夹爪耦合方向上，最后动作流从该校准源出发生成动作块。

### 三、结果（Result）
与π0.5相比，ProAct在仿真和真实世界任务上均提升性能，同时将去噪步数减少50%、推理延迟最多降低25.8%、吞吐量最多提升34.8%。这些结果说明，让生成源由近期动作与预测未来共同校准，可以在更少采样步数下获得更高任务表现和更高推理效率。

### 四、结论（Conclusion）
ProAct通过世界校准的提议到动作流，把生成源从任务无关高斯分布变为由近期动作和预测未来共同决定的各向异性提议中心分布，从而保留运动连续性并增强提议与未来的兼容性。该框架在VLA策略中同时改善了任务性能与推理效率，表明源分布校准是流式动作生成的重要设计维度。

### 五、方法论与关键技术细节
关键实现点包括：原始源为任务无关各向同性高斯；Proposal Expert轻量且仅用一步运动锚定端点流匹配；World Expert以软运动先验预测潜在未来；校准器使用有界每步范围、迹归一化低秩几何和条件数预算，并将细化分配到平移、旋转、夹爪耦合方向。效率收益来自去噪步数减少50%以及延迟和吞吐量改善。局限是摘要未给出具体数据规模、训练损失、超参数值与仿真/真实任务细节，且方法效果可能依赖近期动作质量与世界预测器精度。
