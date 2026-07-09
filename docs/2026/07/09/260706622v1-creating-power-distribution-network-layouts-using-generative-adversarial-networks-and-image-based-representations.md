# Creating Power Distribution Network Layouts Using Generative Adversarial Networks and Image-Based Representations

- 区域：精读区
- 排名：7
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Juan Manuel Garcia-Perez, Carlos Mateo
- 机构：Comillas Pontifical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06622v1) · [PDF](https://arxiv.org/pdf/2607.06622v1)

## TLDR
This paper proposes a generative framework using GANs and image-based representations to create power distribution network layouts, learning from rasterized GIS data to produce realistic topologies that can incorporate geographical context, though it faces challenges in training stability, resolution artefacts, and lack of explicit electrical constraints.

## Abstract
Utilities increasingly rely on planning and operational tools to cope with the increased penetrations of distributed energy resources, yet the lack of realistic, openly available datasets remains a major barrier for benchmarking and comparison. Traditional test feeders, and recently proposed large-scale synthetic networks alleviate this issue but are typically based on heuristic rules and do not learn directly from data. This paper proposes a generative framework based on Generative Adversarial Networks (GANs) to create power distribution network layouts using image-based representations. The model is trained on rasterised views of distribution systems and can operate in two modes: an unconditional configuration that learns layout patterns from the training dataset, and conditional configurations that incorporate geographical context such as street maps and the spatial distribution of consumers. The methodology includes dataset preparation from Geographic Information System (GIS) sources, GAN architecture design, and the analysis of training stability and image resolution. Results from three representative cases show that the proposed approach can reproduce the topologies of low (LV), medium (MV) and high voltage (HV) feeders and align generated layouts with underlying geographical structures. At the same time, the study reveals limitations related to training stability, resolution-dependent artefacts and limits, and the absence of explicit electrical constraints. The proposed framework constitutes a data-driven complement to existing synthetic network generation methods, and could be applied to propose distribution network layouts for the electrification of new areas. This would require future extensions towards power flow, electrically validated models.


## 精读解读（中文）
### 一、研究动机
现有配电网络数据集因保密性难以获取，传统测试馈线和合成网络依赖启发式规则，无法直接从数据中学习布局模式，限制了工具验证与对比。本文旨在提出一种基于生成对抗网络（GAN）的数据驱动方法，利用图像表示直接学习配电网络拓扑布局。

### 二、技术方案（Method）
方法基于GAN，使用栅格化图像表示配电系统（来自GIS数据）。模型分两种配置：无条件GAN仅从潜在噪声生成通用布局；条件GAN输入地理上下文（街道图、用户分布或低压网络）生成对齐布局。架构包括卷积生成器（含上采样层）和卷积判别器，对抗训练采用标准损失和稳定技巧（梯度惩罚、批归一化）。数据预处理包括从GIS生成图像、裁剪无关区域、调整线宽和分辨率统一。训练迭代交替更新生成器和判别器。

### 三、结果（Result）
三个案例验证：案例1（无条件）生成具有径向分支的馈线布局；案例2（低压条件）生成的网络与街道和用户分布对齐，分支密度匹配；案例3（中/高压条件于低压）产生与输入低压网络空间对齐的上游结构。定性结果表明GAN能复制低、中、高压馈线拓扑并整合地理上下文，但存在训练不稳定、分辨率依赖伪影和无电气约束等限制。

### 四、结论（Conclusion）
本文提出基于GAN的图像化配电网络布局生成框架，从数据中学习拓扑模式，可无条件或条件生成布局。结果证明其能生成符合空间特征的拓扑，但需进一步扩展到电气验证模型（如潮流分析）以用于实际规划。

### 五、方法论与关键技术细节
关键细节：1）训练数据来自公开合成网络GIS栅格化图像；2）条件GAN使用街道图和用户分布作为输入先验；3）训练稳定性敏感，需调整生成器/判别器更新频率；4）分辨率选择影响生成质量与计算成本；5）生成布局无显式电气约束（如径向性、连通性）；6）依赖训练数据集分布，稀疏区域易产生伪影；7）没有给出量化指标，仅基于视觉评估。
