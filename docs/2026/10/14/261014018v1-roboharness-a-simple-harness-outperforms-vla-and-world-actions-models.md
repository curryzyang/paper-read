# RoboHarness: A Simple Harness Outperforms VLA and World Actions Models

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Bince Qu, Wei Chen, Bo Zhang
- 机构：Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14018v1) · [PDF](https://arxiv.org/pdf/2610.14018v1)

## TLDR
RoboHarness is a simple visual-geometric harness that lets LLM agents directly control robots without training, enabling Qwen3.8-Flash-Next to outperform state-of-the-art VLA and world-action models on BEHAVIOR Challenge 2025 tasks.

## Abstract
The rise of large language models (LLMs) has opened a path toward generalist embodied AI, raising the question of how LLMs can act in the physical world. One straightforward approach is training the model to generate actions: collect robot-action data and video demonstration, refine LLM architecture with an action head, and train a vision-language-action (VLA) model at scale. However, we argue that coding agents have the potential to realize generalist embodied manipulation. All they need is a simple yet effective robot harness. We present RoboHarness: a robotic harness that gives LLM agents a visual-geometric control panel so that they can directly understand and invoke embodied tasks. With RoboHarness, Qwen3.8-Flash-Next outperforms state-of-the-art VLA models on BEHAVIOR Challenge 2025 tasks. The implementation will be released as open source.


## 精读解读（中文）
### 一、研究动机
LLM已具备任务分解、规划、空间推理与工具使用能力，但其世界知识停留在文本空间，需要桥梁连接物理世界。VLA与世界动作模型依赖大规模机器人动作数据和后训练，数据难以覆盖真实世界的物体、场景与任务多样性；已有可调用函数接口又受预定义任务、物体和策略限制。作者因此主张瓶颈在动作接口而非LLM能力， coding agents 只需一个简单而完备的机器人harness即可实现通用具身操作。

### 二、技术方案（Method）
RoboHarness无需训练模型，为LLM智能体提供视觉-几何控制面板：先定义统一相机坐标系，x向前、y向左、z向上；track_object工具让LLM在头部相机图像选点，harness用光流跨帧持续跟踪，再经深度图反投影得到机器人相机系下的度量坐标。动作工具集分两层：关键点约束工具让LLM指定on-hand与off-hand点的空间关系，harness采样候选动作、剔除逆运动学不可行或不可达候选、规划轨迹并执行；常见关系封装为touch、linear、line-vertical-plane、plane-parallel、line-vertical-ground、face to、move to reach、grasp等quick requests。底层调整工具则直接增量控制左右末端位姿、底盘、高度和俯仰，用于精细修正和滑落等失败恢复，整个流程是跟踪-约束-执行-验证的闭环。

### 三、结果（Result）
在BEHAVIOR Challenge 2025任务上，Qwen3.8-Flash-Next搭载RoboHarness后超过当前最优VLA模型。该方法无需微调即可直接求解BEHAVIOR-1K中的长时程家庭任务，并在完全分布外泛化测试中显著优于VLA和世界动作模型基线。作者同时声明实现将开源发布。

### 四、结论（Conclusion）
论文提出一种新的具身智能范式：通用LLM配合正确工具harness，可在不训练动作生成模型的情况下完成复杂操作，并优于VLA与世界动作模型。其核心结论是，构建通用具身操作的关键不在于让LLM生成更多动作，而在于提供表达充分、可组合、LLM友好的最小原始动作接口，并以空间 grounding 把语言能力接到物理世界。

### 五、方法论与关键技术细节
关键细节包括：完备性证明使用夹爪三点F_L、F_R、G，任意抓取位姿(f_l,f_r,θ)与表面点(a1,a2,a3)在overlap[a1,F_L]、overlap[a2,F_R]、linear[c,a3,G]约束下构成解析双射，其中c=(a1+a2)/2；已抓取时假设夹爪与物体刚性连接，任意目标空间关系可用两组关键点约束表示，因此工具集既极小又完备。track_object不使用仿真先验，依赖头部RGB、深度和光流跟踪；执行管线为候选采样、IK可行性过滤、运动规划、轨迹执行。约束模式表包含touch、linear、line-vertical-plane、plane-parallel、line-vertical-ground、face to、move to reach、grasp等，并允许通用坐标约束；调整工具以增量方式控制EEF位姿、底盘、高度和pitch。局限与约束在于依赖深度质量、光流鲁棒性、VLM二维点定位精度、IK可达性与约束求解稳定性，且全文未报告训练超参，因为方法本身不训练模型；评估涉及BEHAVIOR-1K、BEHAVIOR Challenge 2025、R1 Pro与RoboDojo ARX X5等平台。
