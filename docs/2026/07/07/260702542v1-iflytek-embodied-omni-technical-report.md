# iFLYTEK-Embodied-Omni Technical Report

- 区域：精读区
- 排名：3
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Yuan Zhang, Jingfei Ni, Guanchen Lu, Shiqi Zhang, Qingshan Xu, Chi Liu, Xin Nie, Wenjie Xu, Lin Gao, Zhiyuan Cheng, Mingxin Zhou, Jiajia Wu, Diyuan Liu, Jia Pan, Chao Ji
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02542v1) · [PDF](https://arxiv.org/pdf/2607.02542v1)

## TLDR
iFLYTEK-Embodied-Omni is a unified multimodal foundation model that jointly models vision, language, and action with a brain-cerebellum architecture, achieving an average success rate of 89.6% on zero-shot embodied tasks.

## Abstract
General-purpose embodied agents must understand multimodal instructions, anticipate how their environment will evolve, and produce precise control actions over extended horizons. Existing approaches typically specialize in visual-language reasoning, video-based world modeling, or action generation, while cascaded pipelines that first synthesize future observations and then infer actions can introduce interface bottlenecks and compound prediction errors. We present iFLYTEK-Embodied-Omni, a unified multimodal foundation model that jointly models vision(videos and images), language, and action within a single Omni framework. Its modality-specific visual-language, video-generation, and action-generation components communicate through shared multimodal self-attention. This design establishes brain-cerebellum collaboration: the vision-language modeland video generation model form a high-level brain for instruction understanding, task planning, progress tracking, and future visual-state prediction, whereas the action generation modelserves as a low-level cerebellum that directly converts planned subgoals and shared multimodal context into executable action chunks. To develop these capabilities, we combine action-annotated and action-free embodied videos from human demonstrations and robot interactions with embodied reasoning, embodied perception, and general-purpose image-text data to construct a comprehensive dataset. We further adopt a four-stage strategy that progressively trains the VLM, VGM, and AGM before jointly fine-tuning the complete model.

## 精读解读（中文）

### 一、研究动机
通用具身代理需要理解多模态指令、预测环境演化并产生精确控制动作。现有方法分别专注于视觉语言推理、视频世界模型或动作生成，而级联管道先合成未来观测再推断动作会引入接口瓶颈和复合预测错误。本文旨在通过统一的多模态基础模型联合建模视觉、语言和动作，实现脑-小脑协作，克服上述局限性。

### 二、技术方案（Method）
提出iFLYTEK-Embodied-Omni，一个统一的Omni框架，包含三个模态专用组件：视觉语言模型（VLM）、视频生成模型（VGM）和动作生成模型（AGM）。VLM和VGM构成高级“脑”，负责指令理解、任务规划、进度追踪和未来视觉状态预测；AGM作为低级“小脑”，直接将规划的子目标和共享多模态上下文转化为可执行的动作块。模型通过共享的多模态自注意力层实现跨模态对齐。训练采用四阶段策略：先微调VLM，再训练VGM，然后冻结前两者训练AGM，最后联合微调所有组件。

### 三、结果（Result）
在零样本LIBERO-Plus基准测试上，iFLYTEK-Embodied-Omni实现了89.6%的平均成功率，显著优于现有级联方法。

### 四、结论（Conclusion）
本文提出的统一多模态基础模型通过脑-小脑协作架构和渐进式训练策略，有效融合了视觉语言推理、世界建模和动作生成，在长期任务执行中实现了闭环具身控制，且推理效率高（单卡RTX 4090上3Hz推理频率，30Hz控制频率）。

### 五、方法论与关键技术细节
数据方面：使用多源混合数据，包括动作标注的机器人轨迹（OXE、AgiBot、Droid等）、无动作的演示视频、具身推理与感知数据以及通用图文数据。先验与损失：VGM继承预训练视频扩散模型，AGM从VGM权重初始化；训练采用扩散损失和自回归损失。超参与复杂度：四阶段训练中，前三阶段分别优化各组件，联合微调阶段协调所有模块；推理时引入DiT速度缓存（基于余弦一致性跳过冗余去噪步骤）和V2A式分段去噪（冻结视频分支，仅更新动作潜在），减少计算量。局限性：依赖大规模多源数据收集和计算资源，且当前仅在仿真和部分真实场景验证，泛化至极端环境的能力尚待探索。

