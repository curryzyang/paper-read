# Learning-Based Measurement-Robust Control Barrier Functions for Obstacle Avoidance under State Estimation Error

- 区域：精读区
- 排名：1
- 匹配度：6.4/10
- 来源：arxiv
- 作者：Nicholas Rober, Yixuan Jia, Jonathan P. How
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20467v1) · [PDF](https://arxiv.org/pdf/2608.20467v1)

## TLDR
The paper proposes two control barrier function formulations—drift-measurement-robust (DMR-CBF) and a learned neural measurement-robust (NMR-CBF) variant—that enable safe, non-conservative obstacle avoidance under state estimation error, outperforming standard robust methods in simulation and on a real quadruped robot.

## Abstract
Safety filters are an effective tool for enforcing constraints in safety-critical systems, but most existing methods assume perfect state information, which is rarely available in practice. Recent work has begun to close this gap by developing filtering mechanisms that are robust to state estimation error, but these methods can still exhibit safety violations or overly conservative behavior as estimation error grows. Focusing on obstacle avoidance, we develop two new control barrier function (CBF) formulations: drift-measurement-robust (DMR)-CBFs and neural measurement-robust (NMR)-CBFs. The DMR-CBF augments the standard CBF condition with an inner optimization over the worst-case uncertainty in the drift dynamics, improving robustness to estimation error. This DMR-CBF then supervises a pretraining phase for the NMR-CBF, which replaces the inner optimization with a learned term. The NMR-CBF is subsequently finetuned through differentiable trajectory rollouts, yielding a filter that achieves empirical safety comparable to the DMR-CBF while reducing both conservativeness and computational cost. We provide theoretical analysis of the DMR-CBF along with numerical results on a planar double integrator and a 12D quadrotor, where both proposed approaches prevent collisions while other robust methods either fail or are overly conservative. Finally, we deployed the NMR-CBF on a Unitree Go2, enabling successful navigation of an obstacle field under odometry errors that caused a standard CBF to collide.


## 精读解读（中文）
### 一、研究动机
现有安全滤波器大多假设系统能够获得完美状态信息，但实际系统中状态估计误差不可避免；已有针对估计误差的鲁棒CBF方法在误差增大时仍会出现安全性违规或过于保守的问题，尤其在避障场景中，点式方法容易碰撞、集合式方法因绕障方向不明确而过度保守，难以兼顾安全性与任务性能。

### 二、技术方案（Method）
提出两种新的控制障碍函数：漂移测量鲁棒CBF（DMR-CBF）和神经测量鲁棒CBF（NMR-CBF）。DMR-CBF在标准CBF条件中引入一个针对漂移动力学最坏情况不确定性的内层优化，以处理状态估计误差并提供可证明的安全保障；随后该DMR-CBF作为监督信号对NMR-CBF进行预训练，NMR-CBF用学习得到的鲁棒项替代DMR-CBF中的内层优化，再通过可微轨迹展开进行微调。推理时，将学习到的CBF作为安全滤波器，在满足CBF约束的前提下最小化对名义控制输入的改变，输出安全控制量。

### 三、结果（Result）
在平面双积分器和12维四旋翼的数值实验中，DMR-CBF与NMR-CBF均能避免碰撞，而其他鲁棒方法要么发生碰撞要么过于保守；在Unitree Go2实物平台上，NMR-CBF在导致标准CBF碰撞的里程计误差下成功穿越障碍物区域，实现了与DMR-CBF相当的经验安全性，同时降低了保守性和计算成本。

### 四、结论（Conclusion）
基于学习的测量鲁棒CBF能够结合点式鲁棒方法的低保守性和集合式鲁棒方法的安全性，在状态估计误差下实现安全且不过度保守的避障；DMR-CBF提供可证明的鲁棒性，NMR-CBF通过监督预训练和可微轨迹微调降低计算负担，适合实时部署，为实际机器人系统中的安全滤波提供了有效方案。

### 五、方法论与关键技术细节
方法输入为状态估计及其有界误差集，并假设漂移动力学不确定性具有已知结构；DMR-CBF通过内层最坏情况优化构造后验安全条件，NMR-CBF用神经网络学习该鲁棒项，预训练阶段使用DMR-CBF生成的标签，微调阶段使用可微轨迹展开损失；实验覆盖2D和12D仿真以及Unitree Go2硬件平台；DMR-CBF的主要局限是内层优化带来较高计算复杂度，NMR-CBF的经验安全缺乏严格理论保证，且依赖估计误差有界和训练分布覆盖。
