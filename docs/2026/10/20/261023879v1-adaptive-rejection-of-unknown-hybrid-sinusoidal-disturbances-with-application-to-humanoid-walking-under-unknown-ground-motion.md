# Adaptive Rejection of Unknown Hybrid Sinusoidal Disturbances with Application to Humanoid Walking under Unknown Ground Motion

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：I-Chia Chang, Jacob Stewart, Petros A. Ioannou, Yan Gu
- 机构：University of Southern California, Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23879v1) · [PDF](https://arxiv.org/pdf/2610.23879v1)

## TLDR
This paper develops an adaptive output-feedback controller that rejects unknown hybrid sinusoidal disturbances in hybrid linear systems and demonstrates its effectiveness for bipedal walking under unknown ground motion, substantially improving body-position tracking accuracy in simulation and real-world experiments.

## Abstract
Legged robot control is not yet practical in non-inertial environments, where the ground and surroundings accelerate in the inertial Earth frame, mainly because of the unknown, time-varying, persistent perturbations caused by environmental motion, compounded by the associated hybrid robotic dynamics. We formulate the problem of robot walking control as unknown-disturbance rejection for hybrid linear systems subject to hybrid sinusoidal disturbances (i.e., a linear combination of sinusoidal components with instantaneous phase jumps at discrete events). First, necessary and sufficient conditions for solvability of the disturbance rejection problem are derived and used to characterize the control input that rejects the disturbances. Second, with the Youla-Kucera parametrization, an output feedback controller capable of rejecting the disturbance is introduced. Third, an adaptive law is proposed to estimate the controller parameters that reject the disturbance in the practical case where the disturbance and its parameters are unknown. Experiments on bipedal walking during ground motion demonstrate substantially improved body-position tracking accuracy, with an average improvement of over 60% in simulations and up to 47% in real-world experiments.


## 精读解读（中文）
### 一、研究动机
非惯性环境中地面与周围环境在惯性系中加速，会给双腿机器人带来未知、时变且持续的扰动，并与支撑脚切换等混合动力学耦合，使现有数据驱动方法缺乏理论保证、反馈/预测控制又常假设地面运动已知或将扰动简化为有界输入。本文因此直接把机器人行走控制建模为受混合正弦扰动作用的混合线性系统未知扰动抑制问题，以面向未知地面运动下的双足行走。

### 二、技术方案（Method）
论文将系统写成含连续相位微分动力学和离散事件跳变的混合线性系统，并把扰动建模为若干正弦分量叠加且在每个离散事件处发生瞬时相位跳变；先推导混合调节器方程，给出扰动抑制可解的充要条件及理想部分状态反馈控制输入，再基于Youla-Kucera参数化构造输出反馈控制器，并通过混合结构抵消跳变带来的时变过渡效应；在扰动状态和参数未知时，提出自适应律并借助混合交换引理得到线性参数估计方程，在线估计补偿器参数。最后将该混合自适应控制器嵌入双足机器人分层控制框架，用于未知多方向运动平台上的行走。

### 三、结果（Result）
理论结果给出了混合线性系统抑制混合正弦扰动的充要可解条件，并证明所设计的自适应输出反馈控制器可在扰动及参数未知时实现输出收敛。实验在MuJoCo高保真仿真和Digit机器人真实平台行走中验证，未知多方向地面运动下质心位置跟踪误差平均降低超过60%（仿真），真实实验最高降低47%，表明无需完整地面运动知识也能显著改善跟踪精度。

### 四、结论（Conclusion）
该工作将非惯性环境双足行走控制提升为混合线性系统的未知混合正弦扰动抑制问题，提供了从可解性条件、输出反馈控制器到自适应参数估计的完整框架，并在仿真与硬件上验证了有效性。结果表明混合自适应输出反馈控制可在未知、时变、持续地面扰动下提升双足机器人质心跟踪，为混合动力学机器人在非惯性环境中的控制提供了有理论保证的路径。

### 五、方法论与关键技术细节
关键假设包括离散事件周期T恒定、无扰动系统稳定、连续扰动谱与系统谱不相交，理论分析阶段已知系统与扰动矩阵，实际控制仅用测量输出且不依赖扰动状态和特征；扰动先验为有限个正弦分量叠加并在离散事件处相位跳变，控制器参数在线自适应且Youla-Kucera结构用于维持闭环稳定性，混合交换引理把参数估计转化为线性方程。局限在于采用降阶混合线性模型和正弦扰动先验，可能难以覆盖强非线性、非平稳或复杂碰撞主导的地面运动，验证场景也局限于特定双足平台与实验条件。
