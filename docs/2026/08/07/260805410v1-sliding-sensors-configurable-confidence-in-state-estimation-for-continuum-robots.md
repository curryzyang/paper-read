# Sliding Sensors: Configurable Confidence in State Estimation for Continuum Robots

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ella Walsh, Spencer Teetaert, Eric Diller, Timothy D. Barfoot, Jessica Burgner-Kahrs
- 机构：University of Toronto
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05410v1) · [PDF](https://arxiv.org/pdf/2608.05410v1)

## TLDR
Mechanically reconfigurable sliding sensors along a continuum robot enable spatial shaping of state-estimation confidence, improving full-body shape estimation accuracy compared to a fixed tip sensor.

## Abstract
Continuum robots often operate in uncertain environments, where accurate state estimation is essential for safe interactions. Estimate uncertainty is inherently spatially non-uniform: confidence varies depending on where measurements are available. Global estimation accuracy is not always the top priority, but rather achieving sufficient confidence at task-relevant locations along the robot. This extended abstract introduces mechanically reconfigurable sensing enabling uncertainty-shaping in state estimation for continuum robots. We present a concept hardware design demonstrating the feasibility of longitudinal translation of a sensor within a continuum robot. We demonstrate that state estimation confidence can be reconfigured by varying the sensor location, and show a reduction of full-body shape estimation errors when sliding the sensor back and forth over time, compared to a single fixed tip sensor.


## 精读解读（中文）
### 一、研究动机
连续体机器人常在不确定环境下作业，状态估计不确定性在空间上非均匀，固定传感器布置会在远离测量点的区域造成低置信度，而实际任务往往需要在变化的任务相关位置维持足够置信度。因此本文提出机械可重构传感，使传感器能沿机器人骨干纵向移动，以主动整形状态估计的置信度分布。

### 二、技术方案（Method）
系统硬件上，将直径0.5mm、长8mm的5-DOF电磁线圈位置传感器（Aurora v3）安装于内管中，由丝杆-伺服电机（Dynamixel XL430-W250）线性驱动，使其在外管内沿连续体机器人（70cm长、nitinol内外管）纵向滑动，行程60mm、速度24mm/s。实验中在静态机器人位姿下让传感器往复振荡三个周期，Vicon光学跟踪器提供真值。状态估计采用因子图优化，使用连续弧长-时间表示（参考Teetaert等），估计状态包括位姿、应变与速度；5-DOF测量误差由SE(3)距离度量定义，并投影掉偏航分量，以高斯噪声模型构建测量因子。推理时根据传感器当前弧长位置添加时变测量因子，求解因子图获得全身形状估计。

### 三、结果（Result）
实验表明，改变传感器位置可将高置信度区域重新配置到相应的弧长位置；在真实C形和S形机器人上，滑动传感器相比固定尖端传感器降低了全身形状估计误差，位置RMSE最高改进8.4%，方向RMSE也有下降，证明滑动感知可提升整体形状估计精度。

### 四、结论（Conclusion）
本文首次展示了将传感器纵向滑动作为主动自由度用于连续体机器人状态估计，验证了不确定性整形的可行性。该方法为动态环境下主动感知和信念感知规划奠定了基础，未来工作将扩展至动态机器人及传感器动力学。

### 五、方法论与关键技术细节
关键实现细节包括：传感器尺寸须足够小以装入中心骨干；使用5-DOF电磁测量并去除偏航分量，利用小角度近似；估计框架采用连续弧长-时间表示；真实实验的滑动行程为60mm，传感器在尖端与内部6cm之间滑动，而全长滑动仅在仿真中展示；实验限于静态/准静态结构，未考虑传感器滑动频率等动力学效应。局限性包括对传感器尺寸的严格限制以及当前仅在静态/准静态条件下验证。
