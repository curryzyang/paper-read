# Cognitively-Grounded On-Device Runtime Learning for Ground Robots in Unknown Physical Environments

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Yihao Cai, Yanbing Mao, Christian Lebiere
- 机构：Wayne State University, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28677v1) · [PDF](https://arxiv.org/pdf/2608.28677v1)

## TLDR
CogRun is a cognitively-grounded framework that enables safety-critical ground robots to perform safe, efficient runtime learning entirely on edge-AI devices in unknown environments by combining reinforcement learning with instance-based learning, a rational safety agent, and a coordinator.

## Abstract
This paper presents \ul{CogRun}, a framework that enables safety-critical ground robots to perform cognitively-grounded runtime learning entirely on edge-AI devices in unknown physical environments, without prior maps or perceptual knowledge. CogRun consists of three components: a Learning-Agent, a Rational-Agent, and a Coordinator. The Learning-Agent is novel in cognitive-neural learning architecture, which featurs dedicated replay buffers, cognition-driven experience sampling, and a safety-aware action blending of actor-critic reinforcement learning (RL) with instance-based learning (IBL). The Rational-Agent is a non-learning module that complements the Learning-Agent by exclusively handling safety-critical functions, while the Coordinator manages interactions between the two agents to promote safe and efficient runtime learning. CogRun's full autonomy stack (i.e., perception, learning, and control) on edge-AI devices eliminates dependence on wireless communications, enabling broader applications in challenging environments with limited or no connectivity. Experiments on a quadruped robot in real-world wild forests and on an off-road autonomous vehicle in a simulated wild forest demonstrate that CogRun enables safe and efficient runtime learning, allowing robots to safely and continuously interact with the physical world for enhancing task performance in complex, unknown environments.


## 精读解读（中文）
### 一、研究动机
地面机器人在未知、非结构化的物理环境中部署时面临三大挑战：非平稳环境导致离线训练策略失效、通信受限环境下云边架构不可用、经验重放效率低且忽视与当前状态的相关性。现有运行时学习方法依赖云边通信或缺乏认知启发的记忆机制，难以在安全关键任务中实现高效自适应。

### 二、技术方案（Method）
CogRun框架在边缘AI设备上实现完整的感知-学习-控制栈。其由Learning-Agent、Rational-Agent和Coordinator三部分组成：Learning-Agent采用actor-critic RL与实例学习(IBL)融合的认知神经架构，配置专用重放缓冲区（学习缓冲区B_L和理性缓冲区B_R），通过结合相似性、频率和近因的认知驱动采样机制选取最相关的经验进行训练，并采用安全感知的RL-IBL动作混合；Rational-Agent是非学习安全模块，基于可验证的安全方法在状态超出安全集时接管控制并共享安全经验；Coordinator根据安全条件实时切换两个智能体的动作。系统在ROS2和NVIDIA Jetson AGX Orin上运行，通过CPU-GPU解耦执行（Rational-Agent和Coordinator在CPU，Learning-Agent在GPU）实现低延迟控制。

### 三、结果（Result）
在真实野外森林的四足机器人和模拟野外森林的越野自动驾驶车辆上进行的实验表明，CogRun能够使机器人安全、持续地与物理世界交互并提升任务性能。与基线方法相比，CogRun显著增强了安全保证、经验效率和任务完成质量，验证了其在复杂未知环境中进行安全高效运行时学习的有效性。

### 四、结论（Conclusion）
CogRun通过认知启发的记忆机制和理性安全代理的协同，在边缘设备上实现了无需无线通信的自主运行时学习，有效解决了非平稳环境适应、通信限制和经验效率三大挑战，为安全关键地面机器人在未知场景中的自主部署提供了可行方案。

### 五、方法论与关键技术细节
关键实现细节包括：专用重放缓冲区将安全经验与试错经验分离，并在每个mini-batch中混合采样以降低危险探索；认知驱动的排序分数由相似性（欧氏距离）、频率和近因（基于记忆衰退的指数衰减函数）共同构成；Rational-Agent采用保守但可证明安全的控制方法（如物理模型或Interactive-Far），其干预频率由安全集条件决定；系统在500Hz状态估计和100Hz视觉特征输入下，Learning-Agent以20Hz运行，Rational-Agent以200Hz运行，协调器实时管理切换；架构的局限性在于安全集需要预定义且依赖感知模型精度，以及边缘AI设备的算力约束。
