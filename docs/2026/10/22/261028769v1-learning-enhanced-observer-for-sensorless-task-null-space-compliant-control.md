# Learning-Enhanced Observer for Sensorless Task-Null-Space Compliant Control

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Nuo Chen, Ya-Jun Pan, Onur Toker
- 机构：Florida Polytechnic University, Dalhousie University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28769v1) · [PDF](https://arxiv.org/pdf/2610.28769v1)

## TLDR
The paper proposes a neural-network-enhanced momentum observer with task-null-space decomposition and a hybrid pose/force controller to enable robust, sensorless wrench estimation and compliant pose/force tracking for physical human–robot interaction without force/torque sensors.

## Abstract
This paper presents a novel framework integrating a robust wrench observer with a hybrid pose and force controller for physical Human-Robot Interaction (pHRI). In pHRI tasks, robots are expected to perform task-space motions robustly while remaining compliance with human disturbance, which proposes distinct control objectives. Most existing approaches focus mainly on either robustness or compliance and rely on force sensors for real-time tracking. To address these limitations, we propose a novel framework with the following key contributions. Firstly, a neural network (NN) is trained to improve the observer performance by compensating for system friction and unmodeled dynamics. Secondly, a task-null-space decomposition is applied to separate the joint velocity and reduce the effect of the human disturbance on the observer. Finally, a hybrid pose and force controller is introduced to achieve the end-effector pose and force tracking. Experimental results demonstrate that the proposed framework provides robust and accurate wrench estimation while maintaining reliable pose and force tracking performance. The proposed approach offers an effective solution and framework for pHRI without the need of force/torque sensor measurements which can be applied to many robotic manipulator platforms which do not have force/torque sensors.


## 精读解读（中文）
### 一、研究动机
物理人机交互要求机器人同时具备任务执行鲁棒性与对人扰动的柔顺性，但现有方法多偏重鲁棒或柔顺之一，且常依赖力/力矩传感器进行实时跟踪。无传感器力估计又受关节摩擦、未建模动态以及冗余机械臂零空间人扰动污染任务空间估计的影响，因此需要一种无需力/力矩传感器、能区分任务空间与零空间交互并同时实现位姿与力跟踪的统一框架。

### 二、技术方案（Method）
论文面向7自由度Franka Emika Panda机械臂，先基于广义动量观测器从关节运动与指令力矩估计外部wrench，避免使用噪声较大的加速度和惯性矩阵求逆；再训练神经网络对观测器进行补偿，以减小关节摩擦和未建模动态造成的sim-to-real误差。随后引入任务-零空间分解，将关节速度分离为任务空间速度与零空间速度，其中任务空间速度输入神经网络以降低人扰动对力估计的影响，零空间速度用于零空间柔顺控制。控制器侧构建混合位姿与力控制器，融合笛卡尔位置与姿态跟踪、力调节、任务空间导纳控制以及零空间柔顺控制，输出指令力矩，实现3D曲面上的位置、姿态和力同时跟踪。

### 三、结果（Result）
实验在配置3 kg负载、1 kHz关节力矩控制接口的7自由度Franka Emika Panda上进行，并使用三轴光学力传感器采集数据与验证观测器输出。结果表明，所提框架能够提供鲁棒且准确的外部wrench估计，同时保持可靠的位姿与力跟踪性能；在不同轨迹和交互场景下，力估计性能得到改善，位姿与力跟踪准确，并在零空间产生有效的柔顺响应。该框架无需力/力矩传感器测量即可完成任务执行与交互，避免了依赖模式切换的鲁棒/柔顺控制可能带来的不稳定问题。

### 四、结论（Conclusion）
论文提出并实验验证了一种学习增强观测器与混合位姿力控制相结合的无传感器物理人机交互框架，能够在冗余机械臂上同时实现任务空间鲁棒跟踪、外部力估计和零空间柔顺响应。其核心价值在于将神经网络补偿、任务-零空间分解与位姿力混合控制统一起来，为未安装力/力矩传感器的机械臂平台，包括水下机械臂等难以在末端安装传感器的场景，提供了可行方案。

### 五、方法论与关键技术细节
关键实现包括：采用广义动量观测器，观测器增益取kO=10，残差经J^{-T}映射为末端wrench；神经网络用于补偿关节摩擦和未建模动态，任务空间速度作为其输入以减少零空间人扰动对任务力估计的污染；控制器综合位置、姿态、力跟踪、任务空间导纳与零空间柔顺控制，末端沿法向有0.09 m固定偏移，实验用OptoForce OMD-20-FG-100N仅用于数据采集和验证。局限与约束在于全文预览未给出神经网络结构、训练损失、数据集规模及量化误差指标，方法依赖机器人动力学模型、雅可比与任务-零空间分解质量，实际性能可能受摩擦建模误差和神经网络泛化能力影响。
