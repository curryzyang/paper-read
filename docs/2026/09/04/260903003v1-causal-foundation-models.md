# Causal Foundation Models

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Christopher Stith, Hossein Rahmani, Jesse C. Cresswell
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03003v1) · [PDF](https://arxiv.org/pdf/2609.03003v1)

## TLDR
This paper introduces causal foundation models (CFMs)—pretrained neural networks that estimate causal effects on new datasets via in-context learning without fine-tuning—and offers a practical introduction to the area with example code.

## Abstract
Causal inference is the practice of estimating the effect of a treatment or intervention from data. It traditionally requires a bespoke pipeline for every new problem: first proposing a causal mechanism, selecting a compatible estimator, and finally training it. Meanwhile, across diverse settings and modalities, much of machine learning has shifted to the paradigm of foundation models: networks pretrained once at scale and applied to new tasks without fine-tuning. Causal foundation models (CFMs) bring this paradigm to causal inference. CFMs are pretrained neural networks that estimate causal quantities, such as the average treatment effect, on entirely new datasets using in-context learning without requiring model updates. This work provides a practical introduction to this emerging area. We summarize the necessary background in causal inference and machine learning before discussing CFMs. Throughout, we include example code and Jupyter notebooks.


## 精读解读（中文）
### 一、研究动机
传统因果推断对每个新问题都需要定制化流程：先提出因果机制、选择兼容的估计器，再训练模型，过程繁琐且难以跨任务泛化。与此同时，机器学习领域普遍转向基础模型范式：一次性大规模预训练，然后无需微调即可用于新任务。该工作旨在将基础模型范式引入因果推断，提出因果基础模型（CFM），以在全新数据集上直接估计因果量。

### 二、技术方案（Method）
CFM是预训练神经网络，其核心方案是让模型在大规模因果估计任务上预训练，以观测数据集为输入，通过上下文学习直接输出平均处理效应等因果量，推理时不需要任何模型更新或重新训练。文章采用实用导向的编排方式，先介绍因果推断与机器学习所需背景，再系统说明CFM的构建思路与应用方式，并配套给出示例代码和Jupyter notebooks来演示实际操作流程。

### 三、结果（Result）
该文是面向这一新兴方向的实用介绍性工作，没有报告新的基准实验或数值型指标。其可复现的产出主要体现为对CFM范式的完整背景介绍、示例代码与Jupyter notebooks，可帮助研究者在实际数据上快速体验和评估因果基础模型。

### 四、结论（Conclusion）
因果基础模型将基础模型的零样本泛化能力与因果推断相结合，有望简化因果估计的流程、增强跨数据集的可迁移性。本文为该方向提供了务实入门指南，并通过实践示例说明CFM如何在不更新参数的情况下估计因果量。

### 五、方法论与关键技术细节
关键要点包括：CFM以观测数据作为上下文输入，估计的对象通常是ATE等因果量；其推理机制依赖上下文学习而无需微调。方法形式以预训练后的序列/数据集到估计量的映射为基础，避免了传统的逐任务建模与估计器选择。由于该文定位为导论性综述，未深入给出具体网络架构、超参数或损失函数等实现细节；在因果推断本身的可识别性假设和估计偏差方面也仍需后续研究与系统评估。
