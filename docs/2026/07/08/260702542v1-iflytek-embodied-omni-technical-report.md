# iFLYTEK-Embodied-Omni Technical Report

- 区域：精读区
- 排名：3
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Yuan Zhang, Jingfei Ni, Guanchen Lu, Shiqi Zhang, Qingshan Xu, Chi Liu, Xin Nie, Wenjie Xu, Lin Gao, Zhiyuan Cheng, Mingxin Zhou, Jiajia Wu, Diyuan Liu, Jia Pan, Chao Ji
- 机构：LindenBot, iFLYTEK, University of Science and Technology of China
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02542v1) · [PDF](https://arxiv.org/pdf/2607.02542v1)

## TLDR
iFLYTEK-Embodied-Omni is a unified multimodal foundation model that jointly models vision, language, and action through a brain-cerebellum architecture (VLM and VGM as brain, AGM as cerebellum) with shared multimodal self-attention, trained via a four-stage strategy on a comprehensive dataset, achieving an average success rate of 89.6% on zero-shot embodied tasks.

## Abstract
General-purpose embodied agents must understand multimodal instructions, anticipate how their environment will evolve, and produce precise control actions over extended horizons. Existing approaches typically specialize in visual-language reasoning, video-based world modeling, or action generation, while cascaded pipelines that first synthesize future observations and then infer actions can introduce interface bottlenecks and compound prediction errors. We present iFLYTEK-Embodied-Omni, a unified multimodal foundation model that jointly models vision(videos and images), language, and action within a single Omni framework. Its modality-specific visual-language, video-generation, and action-generation components communicate through shared multimodal self-attention. This design establishes brain-cerebellum collaboration: the vision-language modeland video generation model form a high-level brain for instruction understanding, task planning, progress tracking, and future visual-state prediction, whereas the action generation modelserves as a low-level cerebellum that directly converts planned subgoals and shared multimodal context into executable action chunks. To develop these capabilities, we combine action-annotated and action-free embodied videos from human demonstrations and robot interactions with embodied reasoning, embodied perception, and general-purpose image-text data to construct a comprehensive dataset. We further adopt a four-stage strategy that progressively trains the VLM, VGM, and AGM before jointly fine-tuning the complete model.


## 精读解读（中文）
### 一、研究动机
通用具身智能体需要同时理解多模态指令、预测环境演化并产生长时程精确控制，但现有方法或专精于视觉-语言-动作（VLA）或世界-动作模型（WAM），其级联管道引入接口瓶颈和复合预测误差。为解决这些挑战，本文提出一个统一的具身全模态基础模型，将视觉（图像与视频）、语言和动作在一个全模态框架内联合建模。

### 二、技术方案（Method）
模型包含三个模态专用组件：视觉语言模型（VLM）、视频生成模型（VGM）和动作生成模型（AGM），它们通过共享多模态自注意力层进行跨模态对齐和信息交换，形成“脑-小脑”协作架构（VLM+VGM为高层脑，AGM为低层小脑）。训练数据混合了动作标注和无动作的具身视频、具身推理/感知数据及通用图文数据。采用四阶段策略：阶段I微调VLM建立具身视觉-语言理解；阶段II训练VGM进行未来视频预测；阶段III冻结VLM和VGM、仅训练AGM在动作轨迹上生成动作块；阶段IV联合微调所有组件。推理时使用DiT速度缓存和V2A调度（先联合去噪N步后冻结视频潜变量，仅更新动作），实现3Hz推理和30Hz机器人控制频率。

### 三、结果（Result）
在零样本LIBERO-Plus基准上，iFLYTEK-Embodied-Omni的平均成功率达到89.6%，显著优于现有级联方法，证明了统一架构在长时程具身控制任务中的有效性。

### 四、结论（Conclusion）
通过脑-小脑协作架构和渐进联合训练策略，该模型成功统一了多模态语义理解、视觉世界建模和动作生成，为构建通用具身智能体提供了一种有效的统一框架，并在零样本迁移中展现了高成功率。

### 五、方法论与关键技术细节
关键细节包括：跨模态注意力掩码支持不同预测模式（如VLM、VLA、WM、VGM等）的正确信息流；多视图输入通过RoPE编码空间位置和可学习的视图嵌入区分相机视角；训练数据融合多源具身和通用数据以弥合语义与动作鸿沟；DiT速度缓存利用连续去噪步间的余弦一致性跳过冗余评估（阈值γ控制加速）；V2A调度在前N步联合更新后仅更新动作潜变量，减少计算量；模型在单RTX 4090上实现3Hz推理，但未报告其他硬件或长时程任务的泛化局限性。
