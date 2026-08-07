# VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jihoon Oh, Kento Kawaharazuka, Kei Okada
- 机构：University of Tokyo
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05215v1) · [PDF](https://arxiv.org/pdf/2608.05215v1)

## TLDR
VLAff introduces a unified vision-language-affordance foundation model trained on the large-scale EgoAffordance dataset extracted from egocentric human videos, jointly predicting visual, grasp, and trajectory affordances to enable state-of-the-art visual affordance prediction and effective real-robot manipulation.

## Abstract
Learning manipulation skills from human videos is promising for scalable robot learning. However, the embodiment mismatch between humans and robots makes this challenging. One promising solution is to learn object-centric actionable affordances that are embodiment-agnostic. In this work, we propose a framework that leverages egocentric human videos with state-of-the-art 3D Structure-from-Motion and hand mesh reconstruction to extract actionable affordances such as visual, grasp, and trajectory affordances that explicitly encode where to interact, how to grasp, and how to move. We construct EgoAffordance, a large-scale dataset comprising 204K episodes with 5.6M visual affordances and 11.6M grasp and trajectory affordances. Building on this, we introduce VLAff, a large vision-language model-based unified foundation model that learns cross-modal correlations across all actionable affordances. Given a visual observation and instruction, VLAff generates visual affordance heatmaps, grasp poses, and trajectories, which are then converted into directly executable actions by utilizing 3D scene information. Through extensive experiments, we demonstrate that VLAff not only achieves state-of-the-art performance on visual affordance prediction, but can also be effectively applied to real robot applications such as zero-shot manipulation and affordance-guided robot learning.


## 精读解读（中文）
### 一、研究动机
从人类视频学习操作技能具有规模化潜力，但人与机器人之间存在具身差异，直接迁移困难。现有affordance工作多只建模单一模态（如仅视觉热图、仅手部姿态或仅轨迹），且常限于2D图像空间或静态实验室数据，缺乏统一的可操作affordance框架。本文旨在从第一人称人类视频中提取与具身无关的、以物体为中心的可操作affordance（视觉、抓取、轨迹），并构建统一基础模型以支持跨具身机器人操作。

### 二、技术方案（Method）
数据构建上，对大规模第一人称视频，先用预训练大VLM提取接触关键帧、动作标签、物体类别与交互手部信息；再用H2O检测器、SAM2分割、ViTPose关键点与CoTracker3跟踪获取接触区域；用WiLoR重建MANO手部参数，并用EgoHOS分割+ProPainter修补去除自我视角偏差；最后用MoGe2估计单目深度、COLMAP估计相机内参、DROID估计相机位姿并滤除动态区域，用TAPIR-3D跟踪3D手部轨迹，构建EgoAffordance数据集（204K片段、5.6M视觉affordance、11.6M抓取与轨迹affordance）。模型上，VLAff以预训练VLM为骨干，额外引入DINOv2视觉编码器以增强细粒度空间特征，并新增三类专用token：<SEG>经分割解码器生成像素级视觉热图，<GRASP>解码为96维MANO参数（全局手腕旋转+15个局部关节旋转，采用6D旋转表示），轨迹token通过对6D位姿空间进行空间分箱量化后自回归生成。训练采用Soft Dice损失监督视觉热图（s=1.0, p=1.5）、Smooth L1损失监督抓取参数、轨迹使用token级交叉熵。推理时输入图像与语言指令，输出热图、抓取姿态和轨迹，将热图峰值交互点经相机内参与深度反投影为3D锚点，对抓取和轨迹做物体中心化空间变换，最终结合3D场景信息转换为可直接执行的动作。

### 三、结果（Result）
在视觉affordance预测任务上，VLAff达到当前最优（SOTA）性能。在真实机器人上，该模型可有效应用于零样本操作和affordance引导的机器人学习。EgoAffordance数据集提供了目前最全面的可操作affordance标注（5.6M帧、1.7K实例/动作、16.4K物体类别），同时包含接触区域、手部姿态和相机轨迹，规模显著超过UMD、AGD20K、HOVA-500K等现有数据集。

### 四、结论（Conclusion）
统一建模视觉、抓取与轨迹三种可操作affordance能够捕捉它们之间的跨模态关联，是从人类视频向机器人操作进行跨具身迁移的有效中间表示。以物体中心的affordance表示配合大视觉语言模型架构，可在一模型中规模化学习多模态操作知识，并直接支持零样本操作与下游策略学习等真实机器人应用。

### 五、方法论与关键技术细节
关键细节包括：物体中心化空间变换（将热图峰值点经深度与内参投影为3D锚点，再变换抓取与轨迹到该锚点坐标系）是实现跨具身迁移的核心；Soft Dice损失中平滑因子s=1.0、幂参数p=1.5用于处理热图前景背景不平衡；轨迹采用RT系列的空间分箱量化，将6D位姿空间离散化为token序列，推理时自回归生成并按bin解码回连续位姿；额外DINOv2编码器弥补VLM细粒度空间定位不足；用分割+修补去除自我身体区域以减少第一人称视角偏差，并在SfM中过滤动态区域以提高相机位姿估计鲁棒性。局限方面，方法依赖单目深度和SfM的精度，深度估计误差会传导至3D锚点与轨迹；轨迹量化分辨率受分箱数量限制，可能损失细粒度运动信息。
