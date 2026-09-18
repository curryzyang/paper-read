# Equivalent-Agent Guidance for Cooperative UAV Payload Transportation

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Saurabh Kumar, Shashi Ranjan Kumar, Abhinav Sinha
- 机构：Indian Institute of Technology Bombay, University of Cincinnati
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19312v1) · [PDF](https://arxiv.org/pdf/2609.19312v1)

## TLDR
This paper proposes an equivalent-agent guidance framework that models a rigidly coupled UAV–payload system as a virtual agent and uses robust fixed-time sliding mode guidance with link-orientation control allocation to cooperatively deliver the payload to stationary or maneuvering platforms with guaranteed bounded-time convergence, real-time feasibility, and improved tracking accuracy and energy efficiency.

## Abstract
This paper develops a guidance framework for cooperative transportation of a rigid payload by two uncrewed aerial vehicles (UAVs) to stationary and maneuvering landing platforms. A virtual equivalent-agent representation is first introduced to describe the translational motion of the rigidly coupled UAV-payload system, allowing the transportation problem to be formulated in terms of relative range and line-of-sight dynamics with respect to the landing platform. A geometric analysis establishes the terminal feasibility conditions for payload delivery. In particular, an arbitrary prescribed approach angle can be achieved for a stationary platform, whereas successful delivery to a maneuvering platform with zero relative velocity requires terminal velocity and heading angle synchronization and consequently a zero landing angle. Leveraging this framework, a robust fixed-time sliding mode guidance strategy is developed to regulate both relative range and line-of-sight dynamics. A separate link-orientation controller and control allocation scheme is presented to map virtual equivalent agent commands to the individual UAV's control inputs. The proposed strategy guarantees convergence to the desired landing configuration within a uniformly bounded time, independent of initial engagement geometries, while explicitly accommodating uncertainties arising from target maneuvers. Numerical simulations demonstrate accurate delivery under different terminal approach angles and platform maneuvers, while processor-in-the-loop implementation on a Raspberry Pi demonstrates that the guidance algorithm satisfies the real-time computational requirements. Nonetheless, a comparative analysis shows that the proposed framework achieves better tracking accuracy and faster sliding surface convergence while requiring significantly less control energy from each UAV.


## 精读解读（中文）
### 一、研究动机
单架无人机载荷能力受尺寸与动力限制，多机协同运输可提升模块化、冗余与成本效益，但刚性连接载荷会带来强耦合非线性、欠驱动与内力分配问题；现有研究多关注轨迹跟踪、编队和载荷稳定，未显式处理终端投放几何，尤其动平台。本文从制导视角把载荷投放建模为等效智能体与着陆平台的终端交会问题。

### 二、技术方案（Method）
考虑两架点质量非完整无人机在恒高平面上刚性连接长度L的载荷，并对其与静止或机动平台P的耦合平移运动引入虚拟等效智能体，将其约化为以相对距离和视线角为核心的状态方程，几何分析终端可达条件。基于该模型，对相对距离与视线动力学分别设计鲁棒固定时间滑模制导律，使收敛时间上界与初始交会几何无关并容忍有界平台机动；另设连杆方向控制器和控制分配，将等效智能体指令映射为两架无人机各自的控制输入。流程为：建立等效智能体和相对运动模型，分析终端可行域，设计固定时间滑模面与制导律，进行控制分配与连杆姿态控制，再通过数值仿真、蒙特卡洛和树莓派处理器在环验证实时性。无学习训练环节。

### 三、结果（Result）
几何分析表明：对静止平台可实现任意指定接近角；对机动平台若要求零相对速度成功投放，则终端速度与航向必须同步，导致着陆角为零。仿真显示不同终端接近角与平台机动下均能精确投放；树莓派处理器在环表明制导算法满足实时计算要求；对比分析中，所提框架跟踪精度更好、滑模面收敛更快，且每架无人机所需控制能量显著更少。

### 四、结论（Conclusion）
该工作提出等效智能体、固定时间滑模制导与控制分配的协同运输框架，把双机刚体载荷投放统一为相对距离和视线终端交会问题，并明确静止与机动平台的可达终端几何。它能保证在一致有界时间内收敛到期望着陆构型，且不依赖初始交会几何，并可显式处理目标机动不确定性。结果支持该框架用于实时机载协同载荷运输，但结论建立在平面恒高、点质量、刚性连接等简化假设上。

### 五、方法论与关键技术细节
关键细节包括：两架点质量非完整无人机、刚性长度L载荷、恒高平面运动、忽略垂直与姿态动力学；虚拟等效智能体用于降阶建模，状态量为相对距离与视线角；制导采用鲁棒固定时间滑模，需设定固定时间收敛参数和对目标机动的有界性假设；控制分配把虚拟加速度分解到各无人机并维持连杆方向。验证包括不同接近角与机动平台数值仿真、蒙特卡洛对比和Raspberry Pi处理器在环；摘要未给出具体质量、增益、时间常数等超参数，且局限在于二维平面、两机、刚性连接与理想点质量模型。
