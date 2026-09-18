# LEAP: Learning Emergent Active Perception for Quadruped Navigation

- 区域：精读区
- 排名：7
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Ü. Bora Gökbakan, Stéphane Caron, Philippe Souères
- 机构：Inria, CNRS, Sorbonne University, PSL, University of Toulouse
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17628v1) · [PDF](https://arxiv.org/pdf/2609.17628v1)

## TLDR
LEAP learns emergent active perception for goal-oriented quadruped navigation without any hand-designed sensing reward by using a gaze-invariant egocentric belief map so that task pressure alone produces gaze control, achieving 92.7% success and transferring to simulated quadruped locomotion.

## Abstract
Active perception allows autonomous agents to select their viewpoints rather than passively process the viewpoints given to them, enabling them to target where to reduce uncertainty about their environment. Learned systems typically encourage this behavior with hand-designed proxy objectives, such as coverage or curiosity bonuses, that may conflict with the task. In this work, we propose a method to learn emergent active perception (LEAP) without augmentation of the task objective. We formulate the problem of goal-oriented navigation over hazardous terrains with goals that must be discovered visually. We then propose an architecture for navigation policies with active perception, and train them on a terrain curriculum where task pressure alone leads to the emergence of gaze control. Key to this emergence, LEAP works on a gaze-invariant representation that integrates depth images into egocentric belief maps. We validate its performance in held-out evaluation scenarios, where it achieves a 92.7% success rate, compared to 74.2% for scripted or 34.5% for passive perception, and comes within 4.6 points of a privileged oracle. We validate that LEAP navigation policies, unchanged, can be directly applied to steering quadrupedal locomotion policies in physics simulation.


## 精读解读（中文）
### 一、研究动机
主动感知允许智能体选择视角以降低环境不确定性，但已有学习系统常依赖覆盖率、好奇心等手工代理目标，这些目标可能与导航任务本身冲突。本文研究危险地形上目标必须通过视觉发现的目标导向导航，旨在不增加任务目标的前提下学习涌现式主动感知。

### 二、技术方案（Method）
将导航建模为POMDP：状态包含基座位姿、传感器构型、目标位置与地形；动作由平面机体twist和相机pan-tilt速度组成；观测为当前相机位姿下的深度图加目标二值通道，目标不直接提供；奖励只依赖机体位置与任务进展，不对感知动作给任何奖励。策略用固定相机几何把深度图反投影到以机器人为中心的鸟瞰信念图，该表示对注视方向不变，并充当记忆；用批量高度图射线投射器在on-policy训练规模渲染深度。训练采用自适应地形课程，课程通过代价到目标场phi的梯度下降从最难出生点反向生成出生点；phi由可通行性约束及坡度/间隙代价定义。单个策略联合输出机体与相机动作，用强化学习训练，任务压力单独驱动注视控制涌现。

### 三、结果（Result）
在留出评测场景中，LEAP达到92.7%成功率，高于脚本式感知的74.2%和被动感知的34.5%，仅比特权oracle低4.6个百分点。导航策略无需改动即可直接用于物理仿真中的四足运动策略，在留出地形上完成全身sim2sim迁移并操纵独立训练的运动策略。对比表明涌现的注视行为由任务驱动，而非由感知代理奖励驱动。

### 四、结论（Conclusion）
LEAP证明无需在任务目标外增加覆盖、好奇心或重建等感知代理项，仅靠导航任务压力即可涌现主动注视控制。其关键在于注视不变信念表示和地形课程，使相机控制不被表示校准误差惩罚，并能将导航策略迁移到四足运动。

### 五、方法论与关键技术细节
POMDP中传感动作无直接奖励；深度相机带pan-tilt，观测为深度图叠加目标二值通道；信念图由固定几何反投影生成且无学习编码器，因此新注视只改变哪些栅格被观测，而不改变观测如何编码。代价到目标phi的约束包括最大可通行高度变化0.4 m、机身宽度排除过窄通道，运行代价含坡度项w_h=0.5和间隙项w_c=10、间隙截止0.575 m；训练用批量高度图射线投射器渲染深度，地形课程基于phi梯度下降生成出生点。局限：导航层将机体抽象为平面twist，四足实现分离，验证限于物理仿真与留出场景，未给真实机器人实验；课程依赖已知地形高度场和代价到目标计算。
