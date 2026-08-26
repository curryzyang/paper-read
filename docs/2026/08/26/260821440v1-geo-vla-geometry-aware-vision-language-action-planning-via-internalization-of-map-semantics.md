# Geo-VLA: Geometry-Aware Vision-Language-Action Planning via Internalization of Map Semantics

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ran Chen, Jiaxing Ren, Zhikun Zhang, Yunhao Hou, Junbao Zhuo, Bochao Zou
- 机构：University of Science and Technology Beijing
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21440v1) · [PDF](https://arxiv.org/pdf/2608.21440v1)

## TLDR
Geo-VLA is a plug-and-play framework that improves vision-language-action planners for autonomous driving by internalizing geometric map semantics into visual representations during training via a new Geo-QA dataset, achieving state-of-the-art performance on NAVSIM without requiring HD maps at inference.

## Abstract
Vision-language-action (VLA) models have advanced end-to-end autonomous driving by leveraging foundation models for semantic reasoning and long-tail generalization. However, their planning performance remains limited in complex driving environments because image-only representations inadequately capture planning-relevant road geometry and topology. In this paper, we propose Geo-VLA, a plug-and-play framework that enhances VLA models by learning geometry-aware visual representations. During training, Geo-VLA internalizes geometric map semantics to strengthen road-structure representations, while requiring no HD maps or additional lane information during inference. To support this approach, we introduce Geo-QA, a geometry-focused question-answering dataset that injects road geometry into vision-language representations through contrastive learning and instruction tuning. Experiments on NAVSIM v1 demonstrate that Geo-VLA consistently improves VLA planners with distinct action-generation architectures, achieving 92.1 PDMS and establishing a new state-of-the-art among single-camera VLA planners.


## 精读解读（中文）
### 一、研究动机
现有视觉-语言-动作（VLA）模型在端到端自动驾驶中依赖纯图像表示，难以充分捕捉规划所需的道路几何与拓扑信息，导致在转弯、交叉口等复杂场景中轨迹预测偏离专家轨迹和真实道路结构。直接引入高精地图作为推理输入虽能提供结构信息，但带来数据维护、定位、地图编码等额外开销，且未改善视觉-语言骨干本身的结构表示能力。因此，本文提出将地图语义作为训练监督，使VLA模型在不改变推理输入（无需高精地图）的前提下内化道路几何与拓扑知识。

### 二、技术方案（Method）
Geo-VLA是一个即插即用的两阶段训练框架。首先进行几何感知预训练：利用Geo-QA数据集（3000个样本，覆盖车道结构、道路方向/曲率、交叉口结构、可行驶区域边界、道路拓扑五类）构造图像-文本对和问答对，其中问答由GPT-5.4结合前视图像与离线地图标注生成，答案同时作为对比学习中的文本描述。预训练采用对比学习（对齐图像与地图语义描述）和指令微调（问答生成）联合优化，使用LoRA适配器更新视觉编码器和LLM骨干中的参数子集，辅助投影头在预训练后丢弃。随后进行规划微调：固定预训练后的骨干，仅用专家轨迹监督优化各基线VLA模型的原始动作解码器。推理时仅需前视图像、自车历史、自车状态与导航命令，无需高精地图、地图文本或额外地图编码器。

### 三、结果（Result）
在NAVSIM v1 navtest基准上，Geo-VLA一致提升了两种不同动作生成架构的VLA基线：DynVLA + Geo-VLA取得92.1 PDMS，ReCogDrive + Geo-VLA取得91.2 PDMS，均超过各自基线（DynVLA 91.0，ReCogDrive 90.8），并创下单相机VLA规划器的新SOTA。消融实验表明，静态道路结构监督（如车道、边界、拓扑）比动态目标监督带来更大的规划收益；与显式HD map编码器相比，Geo-VLA在零推理开销下取得了接近的性能（ReCogDrive变体：Geo-VLA 91.2 vs HD map encoder 91.9）。

### 四、结论（Conclusion）
Geo-VLA通过训练时将地图语义内化为视觉-语言骨干的几何感知表示，在保持原始推理接口、无需高精地图的前提下显著提升了VLA规划性能，验证了“地图语义作为监督而非推理输入”的有效性，为端到端自动驾驶规划提供了一种轻量、可迁移的增强方案。

### 五、方法论与关键技术细节
关键细节包括：Geo-QA数据集通过GPT-5.4基于前视图像和离线地图标注自动生成问答，类别均衡（各400/600样本？原文未具体分配，但总共3000份）且仅用于训练；对比学习使用图像-文本对（答案作为描述），指令微调使用问答对，两者联合优化骨干中的LoRA适配器；预训练时辅助投影头（g_v, g_t）仅用于目标计算，之后丢弃；规划微调冻结骨干，只更新解码器，保留基线原始训练协议；实验采用标准单轨迹协议，排除Best-of-N和候选选择方法；与显式几何输入（HD map encoder、车道检测）对比，Geo-VLA无额外推理开销，但性能略低于HD map encoder（可能因后者直接提供结构化特征）；潜在局限性包括依赖离线地图标注生成监督数据、仅在单相机设置下验证，以及未测试更大规模数据或更多种VLA架构。
