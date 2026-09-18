# ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Zejie Tian, Ruibing Hou, Bingpeng Ma, Börje F. Karlsson, Shiguang Shan
- 机构：Beijing Academy of Artificial Intelligence, University of Chinese Academy of Sciences, Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19340v1) · [PDF](https://arxiv.org/pdf/2609.19340v1)

## TLDR
ViLoMan is a scalable teacher–student framework that turns human-object interaction demonstrations into physically executable humanoid trajectories and learns a unified visual-proprioceptive whole-body policy, enabling a Unitree G1 to autonomously perform door-closing loco-manipulation from onboard depth and proprioception without motion references or intermediate commands.

## Abstract
Humanoid loco-manipulation requires adaptive whole-body coordination to seamlessly integrate locomotion and physical interaction. Despite recent advances, learning autonomous loco-manipulation remains challenging due to the scarcity of diverse, physically executable robot-object interaction data and the difficulty of learning unified whole-body control directly from onboard observations. We present ViLoMan, a scalable framework for autonomous humanoid loco-manipulation. ViLoMan first transforms partial kinematic demonstrations of human-object interactions into complete, physically executable robot trajectories. It then leverages these trajectories within a teacher-student distillation framework to learn a unified policy that maps egocentric depth observations and proprioceptive measurements directly to joint-level whole-body actions. During deployment, the policy requires neither reference motions nor intermediate commands. We evaluate ViLoMan on door-closing tasks across diverse door configurations and robot initial conditions in both simulation and the real world. Experimental results demonstrate that a single policy enables a Unitree G1 humanoid to complete the full task using only onboard depth sensing and proprioception, while generalizing robustly across task variations and transferring effectively from simulation to reality. Project page: viloman-anonymous.pages.dev.


## 精读解读（中文）
### 一、研究动机
人形机器人移动操作需要自适应全身协调，将行走、平衡与物理交互统一起来；但自主学习的难点在于缺乏多样且物理可执行的机器人—物体交互数据，以及难以直接从机载观测学习统一全身控制。现有方法常依赖运动参考、中间指令或解耦的移动与操作控制器，限制了泛化与部署自主性。ViLoMan旨在以可扩展方式利用人类—物体交互数据，学习无需参考运动与中间命令的视觉—本体感觉全身移动操作策略。

### 二、技术方案（Method）
ViLoMan控制29自由度Unitree G1（50 Hz）；部署时学生策略输入为808维本体感觉历史（角速度、投影重力、关节位置/速度、上一动作）与连续4帧4×36×64第一视角深度图，输出29维关节位置动作。方法分三阶段：先用TRUMANS的SMPL-X人—门交互经OmniRetarget做保持交互的机器人重定向，再用Kimodo为71个交互片段各生成10条从不同初始位姿到交互就绪位姿的接近轨迹，拼接成710条完整轨迹，并用DoorGym参数化门（把手类型、铰链侧、初始开角、尺寸）增强；随后为每条参考轨迹在仿真中训练联合跟踪人形与门的专用策略，经物理约束修正与过滤得到409条训练、106条测试轨迹（按TRUMANS源片段划分）。教师阶段以GentleHumanoid预训练通用运动跟踪策略为冻结先验，训练仅输出残差修正的特权交互策略；残差以任务阶段、门状态、接触目标、参考铰链运动为交互上下文，用PPO和分阶段奖励优化，并按运动聚类训练多个专家。学生阶段用在线DAgger将特权教师蒸馏为参考无关视觉运动策略：残差CNN将深度编码为32维特征并与本体感觉融合，动作按维度归一化后做监督损失；训练小批量三分之二来自当前学生rollout批次、三分之一来自回放缓冲区，深度图加入高斯模糊随机化。部署时学生仅用机载深度与本体感觉直接闭环输出全身关节动作，不需要参考运动、中间命令或特权物体状态。

### 三、结果（Result）
在仿真与真实Unitree G1上的door-closing任务中，单个ViLoMan策略可完成完整移动操作流程，覆盖接近、稳定接触与关门，并在多样门配置和机器人初始条件下保持泛化，且有效从仿真迁移到现实。对比表显示，ViLoMan是所比较方法中同时具备机载视觉、多运动策略、统一全身控制、无需参考运动且无需中间命令的方案。可见文本未给出具体成功率或误差数值，但报告了闭环执行、任务变化泛化与sim-to-real迁移结果。

### 四、结论（Conclusion）
ViLoMan提出了一条可扩展路径：把丰富但部分或运动学的人类—物体交互演示转化为物理可执行的人形机器人移动操作轨迹，再通过特权教师—学生蒸馏得到仅依赖机载深度与本体感觉的闭环全身策略。该方法缓解了人形移动操作中交互数据稀缺与统一全身控制困难的问题，并在真实人形机器人关门任务上验证了自主执行与泛化能力。其意义在于减少对运动参考和中间控制结构的依赖，推动更自主的接触丰富全身移动操作。

### 五、方法论与关键技术细节
数据与先验：源数据为TRUMANS的SMPL-X人—门交互；OmniRetarget保持人—物几何；Kimodo生成接近运动；DoorGym提供六类参数化门配置；710条增强轨迹经物理修正和过滤后保留409训练/106测试，按源片段划分防泄漏。教师：GentleHumanoid通用运动跟踪策略冻结，残差策略用PPO训练，交互上下文含任务阶段、门状态、接触目标和参考铰链运动；采用分阶段奖励及动力学、接触、地面、门动力学和外部扰动域随机化；按运动聚类训练专家。学生：在线DAgger缓解协变量偏移；观测为808维本体历史加4帧4×36×64深度，CNN特征32维；深度高斯模糊随机化；小批量2/3当前批次、1/3回放；动作按维归一化后最小化与教师动作的差异；输出29维关节位置、50 Hz闭环。局限与约束：当前评估集中在门交互任务，依赖仿真深度相机标定并与真机视角匹配；训练教师需特权物体状态和参考运动，人类数据经重定向、生成、物理修正可能引入可行性偏差；可见文本未报告具体成功率数值。
