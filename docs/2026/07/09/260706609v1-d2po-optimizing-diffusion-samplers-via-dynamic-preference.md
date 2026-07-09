# D2PO: Optimizing Diffusion Samplers via Dynamic Preference

- 区域：精读区
- 排名：3
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Jinkyu Kim, Jinyoung Choi, Bohyung Han
- 机构：Ulsan National Institute of Science and Technology, Seoul National University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06609v1) · [PDF](https://arxiv.org/pdf/2607.06609v1)

## TLDR
D2PO optimizes diffusion samplers by reformulating the sampling policy as a preference-based alignment problem via an energy-based model and dynamic self-improving preferences, overcoming the perceptual quality limitations of static student-teacher regression under low-NFE constraints.

## Abstract
We propose D2PO (Dynamic Direct Preference Optimization), a principled framework for optimizing diffusion sampling policies with respect to timestep schedules and classifier-free guidance (CFG) weights. Our work is motivated by a fundamental limitation of existing student-teacher regression frameworks; low-NFE student samplers are trained to mimic high-NFEteachers, often sacrificing high-frequency texture fidelity while preserving coarse global structures, thereby misaligning the sampler with perceptual quality. D2PO addresses this challenge by reformulating sampler optimization as a preference-based alignment problem, leveraging the Direct Preference Optimization (DPO) framework. To make DPO applicable to diffusion samplers, we model the sampling policy as an energy-based model (EBM), transforming preference comparisons into tractable energy differences. We further introduce a novel energy formulation derived directly from the pretrained score network, enabling preference evaluation in perturbed spaces that jointly capture structural consistency and fine-grained details. Moreover, we introduce dynamic preferences, where the preferred samples used for alignment progressively improve as the sampling policies are learned. This self-improving mechanism replaces rigid static teacher supervision with an iterative, preference-guided refinement process, providing progressively stronger alignment signals. Extensive experiments demonstrate that D2PO aligns diffusion samplers with perceptual quality more faithfully, unlocking the full potential of high-quality teachers and consistently outperforming conventional regression-based schedulers under low-NFE constraints.


## 精读解读（中文）
### 一、研究动机
现有的学生-教师回归框架在低NFE学生模仿高NFE教师时，优先保持粗粒度结构而牺牲高频纹理保真度，导致采样器与感知质量对齐不足，尤其在教师-学生NFE差距大时退化严重。

### 二、技术方案（Method）
D2PO将采样策略优化重新表述为基于偏好的对齐问题，利用DPO框架。首先将确定性采样策略建模为能量基模型（EBM），使偏好比较转化为可处理的能量差异。从预训练得分网络导出新的能量公式，在多个噪声水平上计算得分差异，同时捕获结构一致性和细粒度细节。引入动态偏好机制：每步训练中，用当前策略的密集时间步生成胜者样本，用稀疏时间步生成败者样本，代替静态教师监督；通过最大化胜者相对败者的能量差并保持接近参考策略的KL约束来更新策略。

### 三、结果（Result）
大量实验表明D2PO更忠实地对齐扩散采样器与感知质量，在低NFE约束下始终优于LD3等传统回归式调度器，充分释放高质量教师的潜力，生成的图像在纹理和结构上均更优。

### 四、结论（Conclusion）
D2PO通过动态偏好对齐而非静态回归，消除了固定教师误差限制，使采样器能自我改进并有效探索高质量路径，为极低NFE下的高性能扩散采样提供了可行框架。

### 五、方法论与关键技术细节
关键细节包括：基于得分的能量度量从预训练噪声预测网络导出，在多个噪声水平权衡结构一致性与高频细节；动态偏好对由同一策略的不同计算量生成，实现自改进；仅优化低维采样参数（时间步和CFG权重），不修改骨干网络；训练中交替生成偏好对并优化DPO损失，无需额外奖励模型；在较大教师-学生NFE差距下优势更明显，但对极端低步数可能仍有挑战。
