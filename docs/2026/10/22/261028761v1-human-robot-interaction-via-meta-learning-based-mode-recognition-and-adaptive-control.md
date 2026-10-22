# Human-Robot Interaction via Meta-Learning Based Mode Recognition and Adaptive Control

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Nuo Chen, Ya-Jun Pan
- 机构：Dalhousie University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28761v1) · [PDF](https://arxiv.org/pdf/2610.28761v1)

## TLDR
The paper proposes a meta-learning-based framework that recognizes human intention without predefined thresholds by incorporating force-dependent controller parameters, and combines it with an adaptive meta-learning controller trained on multiple trajectories for robust, safe, and adaptive physical human-robot interaction.

## Abstract
In human-robot interaction (HRI) tasks, humans may interact with the robot in either an active guiding or passive following state, resulting in distinct control objectives for each interaction mode. Most existing approaches rely on predefined switching thresholds to distinguish interaction modes, but their performance can be sensitive to measurement noise. To address this limitation, we propose a novel framework with the following key contributions. First, a neural network (NN) trained via meta-learning is developed to recognize human intention without manually defined thresholds. By successfully incorporating force-dependent parameters from the controller, the recognition rates are improved from 90.1\% to 99.1\% for the passive mode and from 79.8\% to 97.1\% for the active mode. Second, an adaptive meta-learning controller is introduced to compensate for human disturbances and enable online adaptation to varying interaction forces. Third, a multiple-trajectory meta-learning algorithm is designed to jointly learn an environment-basis representation and force-dependent parameters, allowing the controller to deal with unmodeled dynamics efficiently. Experimental results demonstrate that the proposed framework achieves robust and accurate control performance, while providing reliable mode recognition for safe and adaptive physical HRI.


## 精读解读（中文）
### 一、研究动机
在人机交互任务中，人类可能处于主动引导或被动跟随两种状态，二者对应不同的控制目标，因此机器人需要可靠识别交互模式并采取相应控制策略。现有方法多依赖预定义切换阈值或外力传感器区分模式，对测量噪声敏感，且纯数据驱动方法缺乏稳定性保证、基于模型的控制适应能力有限。力相关交互数据采集困难且噪声大，促使作者提出一个统一框架，将无阈值模式识别与自适应学习控制结合，以兼顾适应性、稳定性和安全性。

### 二、技术方案（Method）
作者以7自由度Franka机械臂为平台，在关节空间建立动力学模型，并将外部扰动近似为共享神经网络phi(q,qdot)与力相关线性参数a的乘积，其中phi刻画未建模动态，a对应人类外力并支持在线自适应。模式识别网络N以估计外部力矩和控制器估计的力相关参数为输入，采用模型无关元学习MAML训练，通过任务内适应集梯度更新与任务间元损失更新学习初始化，从而无需人工阈值地区分主动与被动模式。控制端设计自适应元学习控制器，其反馈项受非奇异终端滑模NTSM启发，并通过自适应律在线调节力相关参数以补偿未知外部扰动；当识别为被动模式时执行补偿控制，识别为主动模式时切换为跟随控制。为训练phi，作者提出多轨迹元学习MTML算法：采样多轨迹任务并划分适应集与训练集，先用最小二乘解出各轨迹参数，再按同一力条件计算均值参数，以rho1和rho2平衡单轨迹拟合与类内一致性并做范数约束，随后用重构损失减去辅助网络对抗损失更新phi，同时用交叉熵训练辅助网络t预测轨迹索引，以抑制phi中的轨迹特定信息并提升对未见过轨迹的泛化。

### 三、结果（Result）
摘要报告的核心指标是：将控制器中的力相关参数引入模式识别网络后，被动模式识别率由90.1%提升到99.1%，主动模式识别率由79.8%提升到97.1%。实验在仿真和真实机器人上验证了该框架能够提供可靠模式识别，并在人机物理交互中实现稳健、准确的跟踪控制。文中还声称，与仅使用单轨迹训练及相关基线控制器相比，所提自适应元学习控制器在未见过轨迹上具有更准确的跟踪性能，但预览文本未给出完整控制误差数值。

### 四、结论（Conclusion）
该工作表明，将元学习模式识别与自适应元学习控制耦合，可以在不依赖人工切换阈值的情况下识别人类主动引导或被动跟随意图，并提升对测量噪声和变化交互力的适应能力。所提方法把数据驱动的未建模动态学习与基于模型的控制和Lyapunov收敛分析结合，在仿真与真实机械臂实验中实现了可靠模式识别和稳健跟踪，为安全、自适应的人机物理交互提供了一种可验证框架。

### 五、方法论与关键技术细节
关键实现细节包括：对象为7自由度Franka机械臂，关节力矩接口信号频率1 kHz；动力学模型含惯性、科氏/离心和重力项，外部扰动采用phi(q,qdot)a线性参数化，并假设最优参数a*有界且一阶可微；模式识别采用MAML式内循环/外循环元训练，MTML在多轨迹任务上联合学习环境基网络phi和力相关参数a，使用最小二乘解、同类力条件均值约束、rho1与rho2更新、参数范数上界bar_a以及对抗辅助网络t的交叉熵损失和权重delta；控制器采用NTSM启发反馈加自适应律，并依据模式识别结果切换控制目标；局限性在于轨迹与力的解耦仅通过正则化和对抗训练鼓励而非严格保证，力传感器数据稀缺且噪声较大，元学习与网络训练依赖离线数据质量，在线适应主要局限于低维力相关参数。
