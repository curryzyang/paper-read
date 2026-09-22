# ASGARD: Action-Space Guard for UAV Resilience via Reinforcement Learning

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Mohsen Salehi, Karthik Pattabiraman
- 机构：The University of British Columbia
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20982v1) · [PDF](https://arxiv.org/pdf/2609.20982v1)

## TLDR
ASGARD is a two-phase teacher–student reinforcement learning pipeline that trains an attack-aware teacher with privileged action-attack information to supervise an onboard student encoder and monitor, enabling UAV controllers to correct corrupted action commands at runtime and remain resilient to unseen and stealthy action-space attacks.

## Abstract
Reinforcement learning (RL) controllers have been recently adopted for Unmanned Aerial Vehicles (UAV) navigation and control. However, they are susceptible to action-space attacks that overwrite the action commands after the policy generates them and before the actuators execute them. While most existing defenses target attacks on the policy's inputs, those addressing action-space attacks retrain the policy at training time and are not resilient to corrupted actions at runtime. We propose ASGARD, a two-phase teacher-student pipeline for making RL-based UAV control resilient to action-space attacks. In the teacher phase, an encoder combines the UAV's physical state with action-attack-related privileged information to produce an action-attack-aware latent that trains the RL control policy and a monitor that outputs corrected action commands to the actuators. In the student phase, both the encoder and the monitor are trained via supervised learning from their teacher counterparts to run on-board using only the UAV's physical state history. We evaluate ASGARD across attack scenarios targeting different action commands on UAV. We find that ASGARD is resilient to action-space attacks and completes the missions despite the attack. We further find that ASGARD generalizes to unseen attacks and remains resilient against stealthy attacks.


## 精读解读（中文）
### 一、研究动机
RL控制器已用于UAV导航与控制，但其动作空间存在关键漏洞：攻击者可在策略生成动作命令之后、执行器执行之前覆写动作命令，如修改roll、pitch、thrust或gain，从而使控制策略表面正常但无人机实际执行错误动作。现有防御多针对策略输入侧攻击，而针对动作空间攻击的方法主要在训练时重训策略，部署后对运行时已损坏动作缺乏韧性，因此需要一种能在运行时检测并纠正动作命令的防护机制。

### 二、技术方案（Method）
方法采用两阶段教师—学生流水线：教师阶段用VAE教师编码器将UAV物理状态与动作攻击特权信息（如目标动作、攻击持续时间）融合为攻击感知隐变量，训练RL控制策略及教师监控器；监控器是基于MLP的轻量模块，置于策略与执行器之间，以教师隐变量、策略动作和预期下一状态为输入，输出校正后的动作命令。训练在干净与受攻击轨迹混合数据上端到端进行，使监控器学会透传安全命令并修复被覆写命令。学生阶段用监督学习训练LSTM学生编码器和学生监控器，学生编码器仅以UAV物理状态历史为输入去匹配教师隐变量，学生监控器受教师监控器监督并接收学生隐变量、策略预期状态和动作命令；部署时学生编码器、沿用控制策略和学生监控器在板载每步运行，由监控器向执行器转发校正动作。

### 三、结果（Result）
论文在针对UAV不同动作通道的攻击场景上评估ASGARD，发现其能在攻击下保持韧性并完成任务；典型场景中ASGARD任务完成率为95%，而RL-only控制器和ARMOR仅40%；当四个动作命令同时被损坏时，两个基线全部任务失败，ASGARD仍完成67%。此外，ASGARD可泛化到训练未见过的攻击通道，并对隐秘攻击模式保持韧性。

### 四、结论（Conclusion）
结论是，仅在训练时对动作扰动鲁棒化或仅做攻击检测不足以应对策略输出后、执行器执行前的动作空间攻击；ASGARD通过运行时主动校正每个输出动作命令，在策略与执行器之间建立最后一道防护，使RL UAV控制器在多种动作空间攻击下继续安全执行任务。该机制不依赖部署时的特权信息，且对未见攻击和隐秘攻击具有泛化能力。

### 五、方法论与关键技术细节
关键细节包括：UAV动作命令为pitch、roll、thrust、gain四通道，任务成功要求全程跟踪误差不超过安全半径epsilon；攻击模型为攻击者将动作替换为a_t+b_t，可作用于一个或多个通道且可变严重度、模式、持续时间，并可用小偏差保持隐秘，物理/GPS欺骗及通信链路攻击不在范围内。实现上教师编码器为VAE，学生编码器为LSTM，监控器为轻量MLP，训练混合干净与受攻击轨迹并采用端到端与监督模仿；监控器主动修复而非检测后降落，且置于策略和执行器之间以缩短篡改窗口并形成信任边界。约束是编码器、策略和监控器部署后只读，动作命令可写，学生仅用物理状态历史运行以满足板载实时性；预览未给出具体超参，局限是未覆盖传感器物理攻击、地面站、任务计划和通信链路攻击。
