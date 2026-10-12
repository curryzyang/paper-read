# PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Xiaomeng Xu, Han Zhang, Zhian Ruan, Xiaofeng Guo, Jinkun Cao, Ruihan Yang, Carmelo Sferrazza, Shuran Song, Guanya Shi
- 机构：Stanford University, Amazon FAR, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12558v1) · [PDF](https://arxiv.org/pdf/2610.12558v1)

## TLDR
PanTact teaches humanoid whole-body dexterity from robot-free human demonstrations by using wearable contact patches to capture body-contact information, a visuomotor policy to predict contact goals, and contact-aware whole-body control to let a Unitree G1 manipulate with any suitable body surface.

## Abstract
Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body surface, directly from robot-free human demonstrations. Our key idea is to use contact as manipulation-centric information that transfers across embodiments. Contact locations and timing specify the interactions needed to accomplish a task, while the robot chooses how to coordinate its body to realize them within its own physical constraints. Specifically, PanTact captures, learns, and executes whole-body contact via: 1) a wearable, robot-free data collection interface that augments egocentric vision and bimanual UMI grippers with whole-body modular contact patches to record body contact locations and states; 2) a visuomotor policy that mitigates the egocentric observation gap and predicts whole-body contact goals; and 3) contact-aware whole-body control formulations that realize active contact goals using suitable robot surfaces. We deploy PanTact on a Unitree G1 humanoid without additional body contact sensors, demonstrating whole-body dexterity involving body support, pushing, sweeping, and load-sharing. Website: https://pantact.github.io


## 精读解读（中文）
### 一、研究动机
现有人形机器人loco-manipulation研究大多把手部以外的身体仅用于行走与平衡，并主动回避身体其他部位与环境的接触，因而浪费了人形本体大量自由度与潜在接触面。要从人类演示中学习这种全身灵巧性，必须同时解决三个环环相扣的问题：如何采集演示者的身体接触、如何在人到机的策略迁移中保留接触信息、以及如何用全身控制器在满足平衡与物理约束下真正实现接触。作者的核心洞察是：接触位置与时序属于以操作为中心、可跨本体迁移的任务级信息，而用哪块身体表面和什么关节构型去实现接触则应由机器人自身决定。

### 二、技术方案（Method）
PanTact由采集、策略、控制三部分组成。数据端使用无机器人的可穿戴接口：头戴ZED X Mini立体相机与双腕ZED X One S鱼眼相机以60Hz采集视觉，头与双腕的HTC Vive追踪器以250Hz采集位姿，夹爪宽度以1kHz采集，并在前臂与膝盖等处贴附可重构的模块化接触贴片，每个44×44mm模块含一枚FSR，通过磁吸连接件拼成任意形状，经菊花链RS-485总线或USB由定制PCB以1kHz、16通道、12位ADC加8倍过采样读出，最终以同步的N×4接触数组记录每个传感器的二值接触状态与三维位置。策略端是一个10Hz扩散策略，输入为经体部几何掩膜处理的3D自我中心点云（对夹爪与接触贴片定义的朝向身体半空间取交集后在视觉编码器注意力层遮蔽）、双腕图像和本体感知，预测H=16步动作块，每步包含头部3D注视点、双末端位姿与夹爪宽度，以及N个接触目标（二值接触状态加接触位置），所有量都表达在最新观测到的左夹爪坐标系下。控制端把接触位置当作可选跟踪目标：仅当接触状态为激活时才请求机器人接触该点，并用候选机器人身体集合上的软最小距离（T=0.02m）构造任意表面接触目标，同时采用虚拟接触目标——把设定点推到接触点内侧，使残余跟踪误差转化为按压力，论文给出上半身接触感知IK、全身IK加密集跟踪器、以及直接稀疏接触跟踪三种实现。

### 三、结果（Result）
系统部署在Unitree G1人形机器人上，且未额外加装任何身体接触传感器，成功展示了涉及身体支撑、推动、扫掠和负载分担的全身灵巧技能。具体包括同时用抓取与躯干支撑搬运不同尺寸物体、用前臂表面扫掠多个物体、用手被占用时的腿部做非抓握操作并与移动同步进行，以及按顺序在不同身体部位间切换接触。消融与量化指标在预览文本中未完整给出，作者将结果视频置于项目主页 https://pantact.github.io 供查看。

### 四、结论（Conclusion）
PanTact表明接触可以作为一种跨本体的、以操作为中心的接口：人类演示只需提供接触发生的位置与时序，机器人便可在自身形状与运动学约束下自行选择用哪块身体表面和何种构型去实现接触并保持平衡。由此把手部之外的身体表面纳入操作范畴，实现了从无机器人的人类演示直接学习人形机器人全身灵巧性，为超越手部操作的loco-manipulation提供了完整可行的系统范式。

### 五、方法论与关键技术细节
关键实现细节包括：FSR会随温度和安装压力漂移，因此接触判定采用逐通道自适应基线的相对二值化而非绝对阈值；每个贴片配一个追踪器，通过刚体变换把传感器中心映射到跟踪世界系；点云、本体位姿、末端位姿与接触位置统一表达在最新左夹爪坐标系中以降低人机运动学差异敏感性；体部掩膜由夹爪与接触贴片的半空间交集近似得到，不依赖任何一方的外观模型，可扩展到任意数量贴片；虚拟接触目标通过在物体内侧偏移设定点把跟踪误差转成接触力；非激活接触不被跟踪，避免对自由空间身体运动过约束，控制器可自由分配剩余自由度以维持平衡。局限方面，评测主要限于Unitree G1与若干演示任务，人机身高与视角差异仍需靠掩膜与坐标系设计缓解，虚拟目标与软最小温度等超参需要调节，预览文本未给出完整的定量对比与失败案例分析。
