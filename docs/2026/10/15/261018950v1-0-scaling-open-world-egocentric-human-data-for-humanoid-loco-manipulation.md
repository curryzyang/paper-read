# $λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Lambda-humanoid Team
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18950v1) · [PDF](https://arxiv.org/pdf/2610.18950v1)

## TLDR
The paper introduces HumanVerse, a 500-hour open-world egocentric human loco-manipulation dataset and human-to-humanoid alignment/refinement pipeline, and uses it to train λ₀, a humanoid foundation model that achieves 90.0% success on SIMPLE and 62.5% on real-world loco-manipulation tasks via zero-shot transfer to Unitree G1 without target-task robot demonstrations.

## Abstract
Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector execution. We introduce HumanVerse, a 500-hour dataset of open-world human loco-manipulation pairing egocentric video with synchronized body and hand motion. Our human-to-humanoid pipeline aligns camera viewpoints and arm appearance, and refines motion references and controller inputs offline to reduce end-effector errors while preserving whole-body coordination. We validate the pipeline through zero-shot transfer to Unitree G1 on representative whole-body manipulation and long-range loco-manipulation tasks, without target-task robot demonstrations. Building on this pipeline, we develop $λ_0$, a humanoid foundation model for whole-body loco-manipulation, with robot-aligned human demonstrations providing supervision for mid-training. Increasing whole-body human data consistently improves downstream task progress. $λ_0$ achieves 90.0% success on SIMPLE and 62.5% across real-world loco-manipulation tasks. We expect this study to guide scalable whole-body human data collection toward humanoid foundation models for richer interaction with the physical world. Homepage: https://lambdahumanoid.github.io/


## 精读解读（中文）
### 一、研究动机
人形机器人全身移动操作需要与物理世界协调交互，但大规模采集真实机器人演示成本高昂。人类第一视角演示是可扩展替代方案，但现有自视角人类监督常缺失移动与姿态信息，且具身差异与控制器动力学阻碍末端执行器精确执行。为此，本文提出HumanVerse数据集与人类到人形流水线，并构建人形全身移动操作基础模型λ0。

### 二、技术方案（Method）
本文构建500小时开放世界人类移动操作数据集HumanVerse，配对第一视角视频与同步身体和手部运动。人类到人形流水线先对齐相机视角与手臂外观，再离线精修运动参考和控制器输入，以降低末端执行器误差并保留全身协调。基于该流水线，作者在Unitree G1上验证零样本迁移，无需目标机器人任务演示；进而开发λ0人形全身移动操作基础模型，以机器人对齐的人类演示进行中期训练监督。

### 三、结果（Result）
零样本迁移到Unitree G1在代表性全身操作和长距离移动操作任务上得到验证，无需目标机器人任务演示。增加全身人类数据可持续提升下游任务进展。λ0在SIMPLE基准上达到90.0%成功率，在真实世界移动操作任务中平均成功率为62.5%。

### 四、结论（Conclusion）
研究表明，可扩展的全身人类数据采集能够为人类到人形迁移提供有效监督，并显著减少对真实机器人演示的依赖。HumanVerse与λ0为面向开放世界物理交互的人形基础模型提供了可复现的数据与训练路径。

### 五、方法论与关键技术细节
关键细节包括：500小时开放世界第一视角人类移动操作数据，含同步身体与手部运动；核心先验是全身协调与机器人对齐的人类演示；方法模块为视角对齐、手臂外观对齐、离线运动参考与控制器输入精修；λ0在中期训练阶段使用机器人对齐人类演示监督；评估为零样本迁移至Unitree G1，SIMPLE成功率90.0%，真实任务成功率62.5%。局限在于具身差异和控制器动力学仍需精修，真实世界成功率低于仿真，开放世界覆盖与规模化效果仍待进一步验证。
