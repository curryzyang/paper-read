# A 3DGS-Driven Dynamic Viewpoint and Vibrotactile Framework for Subsea Teleoperation Validated via fNIRS

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Fang Xu, Tianyu Zhou, Ruitong Tian, Md Jahidul Islam, Jing Du
- 机构：University of Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13067v1) · [PDF](https://arxiv.org/pdf/2607.13067v1)

## TLDR
A multimodal teleoperation framework combining a 3D Gaussian Splatting–driven dynamic exocentric viewpoint and torso-mounted vibrotactile cues significantly improves operator performance and sustains prefrontal executive control under severe communication latency, as validated by fNIRS in a human-subject study.

## Abstract
Teleoperating remotely operated vehicles (ROVs) in flooded, cluttered infrastructure is fundamentally limited by narrow 2D egocentric views and subsea communication latency. We present a multimodal teleoperation architecture built on a ROS-Unity framework that decouples proactive spatial planning from reactive boundary avoidance. The system replaces static camera feeds with a Dynamic Adaptive Viewpoint System (DAVS), which uses continuous optimization and real-time 3D Gaussian Splatting (3DGS) to synthesize an occlusion-free exocentric viewpoint from onboard state estimation. To further reduce sensory workload, a torso-mounted vibrotactile suit maps local obstacle clearance to intuitive haptic proximity cues. The architecture was evaluated in a controlled human-subject study (N = 30) using a BlueROV2 navigating a complex simulated underwater facility. A 3 x 4 repeated-measures design compared three interaction modalities (Egocentric, Haptic, Exocentric) under four communication delays (0.0-1.0 s). Performance was quantified using behavioral measures and functional near-infrared spectroscopy (fNIRS) to assess task-evoked prefrontal activation. Results show that reactive haptic feedback improves path adherence under minimal delay, whereas the 3DGS-driven exocentric visualization provides superior resilience under severe latency (0.5-1.0 s), significantly outperforming the other modalities. fNIRS further revealed a cognitive disengagement effect: increasing latency during conventional egocentric teleoperation overloaded working memory and reduced prefrontal activation, whereas the proactive spatial context provided by DAVS sustained executive control. These findings demonstrate that spatially grounded, multimodal assistance can substantially improve operator performance and cognitive endurance during latency-degraded underwater teleoperation.


## 精读解读（中文）
### 一、研究动机
水下遥操作受限于狭窄的2D自我中心视图和通信延迟，导致操作者需持续进行空间推断，增加认知负荷。为解决此感知瓶颈，提出一种多模态框架，将主动空间规划与反应性边界避免解耦。

### 二、技术方案（Method）
该架构基于ROS-Unity框架，包含实时MonoGS SLAM和动态自适应视角系统(DAVS)。MonoGS通过单目RGB图像以10Hz进行6-DOF位姿估计和3D高斯泼溅地图构建。DAVS在包围ROV的球面上候选视角中优化，通过最小化遮挡成本、最大化深度熵并施加平滑性约束，合成无遮挡的外部视角。同时，躯干固定的振动触觉背心将局部障碍清除映射为反应性触觉提示，通过非线性函数将距离转换为强度。实验采用3×4重复测量设计，30名参与者分别使用自我中心、触觉和外部视角三种模态，在0.0至1.0秒四种通信延迟下导航BlueROV2在模拟水下设施中。

### 三、结果（Result）
行为结果显示，触觉反馈在最小延迟下改善路径遵循，而3DGS驱动的外部视角在严重延迟(0.5-1.0秒)下显著优于其他模态，具有更好的延迟韧性。fNIRS神经生理学测量揭示了认知脱离效应：传统自我中心遥操作在延迟下导致前额叶激活崩溃，表明工作记忆过载；而外部视角维持了前额叶执行控制，证明空间基础辅助能保持操作者的认知耐力。

### 四、结论（Conclusion）
空间基础的多模态辅助（特别是3DGS驱动的外部视角）能显著提升操作者在水下遥操作中的性能，并在高延迟下维持认知功能。该框架通过解耦主动规划与反应性避免，有效减轻了操作者的感知和认知负荷。

### 五、方法论与关键技术细节
关键细节包括：MonoGS使用单目RGB和单目深度估计约束无纹理环境中的几何；DAVS优化权重α=1.0, β=0.3, γ=0.8, δ=0.5，平滑滤波系数0.3；触觉映射使用指数γ>1的强度函数和门控函数；视觉-触觉延迟严格低于20毫秒；实验排除联合外部+触觉条件以避免跨通道干扰；局限性包括模拟环境、未验证真实水下场景、样本量有限等。
