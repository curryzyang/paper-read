# D2PO: Optimizing Diffusion Samplers via Dynamic Preference

- 区域：精读区
- 排名：8
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Jinkyu Kim, Jinyoung Choi, Bohyung Han
- 机构：Seoul National University, Ulsan National Institute of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06609v1) · [PDF](https://arxiv.org/pdf/2607.06609v1)

## TLDR
D2PO introduces a preference-based alignment framework for diffusion sampling that replaces static teacher-student regression with dynamic, self-improving preference optimization using an energy-based surrogate derived from the score network, consistently surpassing conventional schedulers under low-NFE constraints.

## Abstract
We propose D2PO (Dynamic Direct Preference Optimization), a principled framework for optimizing diffusion sampling policies with respect to timestep schedules and classifier-free guidance (CFG) weights. Our work is motivated by a fundamental limitation of existing student-teacher regression frameworks; low-NFE student samplers are trained to mimic high-NFEteachers, often sacrificing high-frequency texture fidelity while preserving coarse global structures, thereby misaligning the sampler with perceptual quality. D2PO addresses this challenge by reformulating sampler optimization as a preference-based alignment problem, leveraging the Direct Preference Optimization (DPO) framework. To make DPO applicable to diffusion samplers, we model the sampling policy as an energy-based model (EBM), transforming preference comparisons into tractable energy differences. We further introduce a novel energy formulation derived directly from the pretrained score network, enabling preference evaluation in perturbed spaces that jointly capture structural consistency and fine-grained details. Moreover, we introduce dynamic preferences, where the preferred samples used for alignment progressively improve as the sampling policies are learned. This self-improving mechanism replaces rigid static teacher supervision with an iterative, preference-guided refinement process, providing progressively stronger alignment signals. Extensive experiments demonstrate that D2PO aligns diffusion samplers with perceptual quality more faithfully, unlocking the full potential of high-quality teachers and consistently outperforming conventional regression-based schedulers under low-NFE constraints.


## 精读解读（中文）
### 一、研究动机
现有学生-教师回归框架中，低NFE学生采样器被迫模仿高NFE教师，在保留全局结构的同时牺牲高频纹理细节，导致采样器与人类感知质量不对齐。这种结构刚性阻碍了从强教师中充分获益，尤其是在需要激进加速时。

### 二、技术方案（Method）
D2PO将采样策略优化重新表述为偏好对齐问题。首先将确定性采样策略建模为能量模型（EBM），从而将DPO的偏好比较转化为可计算的能量差。能量函数直接利用预训练分数网络在不同噪声水平下的输出差异，以同时捕捉结构一致性和高频细节。在训练中，每个步骤使用当前策略构建偏好对：失败样本来自稀疏时间步调度（低成本），获胜样本来自同一策略的密集调度（高质量）。然后优化DPO损失，使策略倾向于自身的高质量近似版本，实现动态自我改进，取代静态教师蒸馏。

### 三、结果（Result）
实验表明，D2PO在低NFE约束下能够更忠实地对齐扩散采样器与感知质量，生成图像保留更好的纹理和结构细节。与LD3等基于回归的调度器相比，D2PO持续取得更优性能，充分发挥了高NFE教师的潜力，而不会像静态蒸馏那样在教师NFE增益时出现质量退化。

### 四、结论（Conclusion）
D2PO通过动态偏好对齐有效优化了扩散采样策略，消除了静态蒸馏的误差下限，为加速扩散采样提供了轻量且高效的新方案。

### 五、方法论与关键技术细节
该方法将采样策略分布建模为能量模型（EBM），使得偏好损失可计算；能量函数基于预训练分数网络的预测差异，在多个噪声水平上度量多尺度感知差异；动态偏好机制利用当前策略在稀疏和密集调度下的输出构建偏好对，实现自我改进；训练期间固定生成网络权重，仅优化低维采样参数（时间步和CFG权重），计算开销极小；超参数β控制KL正则化强度；局限性是依赖预训练分数网络的质量，且密集调度可能增加训练计算成本。
