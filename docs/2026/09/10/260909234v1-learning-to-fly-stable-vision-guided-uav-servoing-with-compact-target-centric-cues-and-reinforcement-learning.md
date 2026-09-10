# Learning to Fly: Stable Vision-Guided UAV Servoing with Compact Target-Centric Cues and Reinforcement Learning

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Saurbh Singh Jamwal, Nived Chebrolu
- 机构：Indian Institute of Technology Bombay
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09234v1) · [PDF](https://arxiv.org/pdf/2609.09234v1)

## TLDR
This paper demonstrates that using compact target-centric visual cues—image-space offsets and relative depth combined with proprioceptive measurements in a 12D observation—with PPO and curriculum learning enables stable, robust long-horizon vision-guided UAV visual servoing that outperforms classical visual-servo controllers under perturbations.

## Abstract
Vision-guided reinforcement learning for Unmanned Aerial Vehicles (UAVs) remains challenging due to unstable policy optimisation, aggressive exploration, and the cost of high-dimensional visual perception. In this work, we investigate long-horizon UAV visual servoing using compact target-centric cues combined with low-dimensional sensor measurements. Rather than learning directly from RGB images, lightweight target segmentation provides image-space offsets and relative depth, which are combined with quadrotor velocity and projected-gravity measurements into a compact 12D policy observation. We compare Direct PPO with three matched-budget curriculum strategies: a Visual curriculum that progressively expands target placement difficulty, a Dynamics curriculum that gradually relaxes action constraints and smoothing, and a Joint curriculum that combines both progressions. All strategies reach comparable nominal performance, with complementary advantages across tracking metrics. Observation ablations show that proprioceptive measurements are critical for stable flight and image-space cues for target alignment, while explicit depth is not necessary for strong performance in the evaluated setting. Against tuned classical visual-servo controllers, learned policies show greater robustness to strong control and visual perturbations, while the Visual curriculum exhibits the smallest degradation under unseen target motion. Overall, the results demonstrate that compact target-centric representations can support robust long-horizon aerial visual servoing and that visual curriculum training can improve robustness to dynamic distribution shifts despite limited gains in nominal performance.


## 精读解读（中文）
### 一、研究动机
视觉引导无人机强化学习面临策略优化不稳定、探索激进及高维视觉感知成本高等问题；论文旨在研究长时程无人机视觉伺服，避免直接学习RGB图像，转而使用紧凑目标中心线索与低维传感器测量，以提升稳定性、训练可行性和鲁棒性。

### 二、技术方案（Method）
框架先用轻量目标分割从RGB-D中提取归一化图像横向/纵向偏移和相对深度，并与四旋翼机体线速度、角速度、投影重力拼接成12维策略观测；PPO策略输出集体推力与机体滚转、俯仰、偏航力矩四维连续动作，在IsaacLab并行环境中闭环训练。奖励由目标居中、深度调节、可见性、角运动正则和高度稳定组成，且直接PPO与三种课程策略共享相同奖励、网络、PPO超参和优化预算，课程仅改变难度进度：视觉课程逐步扩大目标深度和横纵向位移，动力学课程逐步放宽动作限幅与力矩尺度并降低动作平滑，联合课程同时施加二者。

### 三、结果（Result）
等预算下，直接PPO与视觉、动力学、联合课程策略在名义性能上相当，但在跟踪指标上各有互补优势；观测消融显示本体感受测量对稳定飞行至关重要，图像空间线索用于目标对齐，而在所评估范围内显式深度并非强性能必需。与调参后的经典2D/3D视觉伺服控制器相比，学习策略在强控制扰动和视觉扰动下鲁棒性更强，视觉课程策略在未见目标运动下性能退化最小。

### 四、结论（Conclusion）
紧凑目标中心表示能够支撑稳健的长时程空中视觉伺服，视觉课程训练虽未显著提升名义性能，但可改善动态分布偏移下的鲁棒性；这表明将感知压缩为任务相关的几何接口并结合强化学习是无人机视觉伺服的有效路线。

### 五、方法论与关键技术细节
关键实现包括12维观测（机体线速度、角速度、投影重力、归一化图像偏移u/v与相对深度d）、归一化动作到推力/力矩的映射、IsaacLab仿真以及基于颜色的目标分割掩码质心偏移，深度作为标量可由RGB-D、立体、单目深度估计或学习深度模块替代。实验采用每配置200回合、5个随机种子，成功步要求目标可见且中心与深度误差低于阈值，鲁棒性测试在动作噪声、视觉噪声和视觉丢失率均为0.2下零样本评估且不重调控制器；局限在于分割器未作基准比较、深度来自仿真、主要在仿真中验证，课程调度和奖励权重向真实部署的迁移仍需检验。
