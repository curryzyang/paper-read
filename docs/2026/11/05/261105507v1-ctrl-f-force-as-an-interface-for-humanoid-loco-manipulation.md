# Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Mengjie Zhao, Yuxin Chen, Yiyang Shao, Chuye Hong, Jiakang Chen, Koushil Sreenath, Masayoshi Tomizuka
- 机构：University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05507v1) · [PDF](https://arxiv.org/pdf/2611.05507v1)

## TLDR
Ctrl-F is a hierarchical motion–force framework that augments humanoid motion tracking with explicit 3-D force commands at designated contact bodies, combining a low-level motion–force tracker with a high-level force planner to enable force-aware loco-manipulation and online load adaptation, demonstrated on hardware by dragging, pushing, lifting, and kicking objects up to 20 kg.

## Abstract
Humanoid motion tracking has scaled to general policies that reproduce diverse human motion, but the resulting behavior is in free-space: the tracker knows where the body should be, not how it should interact with the environment. Other work makes the object part of the objective, yet abstracts that interaction to contact or geometry, which leaves the demanding cases under-explored. We argue that force is a natural command channel between motion imitation and object interaction, one that specifies not just where to make contact but how hard. We present Ctrl-F, a hierarchical motion-force framework that augments motion tracking with an explicit force command, a 3-D force at each designated contact body such as a hand or a foot. The hierarchical framework comprises: (1) A unified motion-force controller tracks the reference motion while applying the commanded force to the world. (2) A high-level force planner that issues a force command online based on object state and proprioception observations. In simulation and on hardware, Ctrl-F completes loco-manipulation that demands large, sustained interaction force and adjusts its command online as the load changes, both out of reach of a force-blind tracker. On hardware, Ctrl-F demonstrates hand-based dragging, pushing, and lifting, as well as foot-based kicking, successfully manipulating boxes weighing up to 20kg in pushing and kicking tasks where the force-blind baseline fails, while adapting online to additional loads introduced mid-task.


## 精读解读（中文）
### 一、研究动机
现有的人形机器人运动跟踪已能复现多样人体动作，但行为仍停留在自由空间：跟踪器只知道身体该到哪里，不知道应如何与环境用力交互；已有物体交互工作多把交互抽象为接触或几何，未充分探索需要大力、持续力的困难场景。作者认为力是连接运动模仿与物体交互的自然命令通道，因为它不仅指定接触位置，还指定作用力度。

### 二、技术方案（Method）
Ctrl-F采用分层运动—力框架：低层统一运动—力控制器输入参考运动、每个指定接触身体（如手、脚）的三维力命令和本体感受，输出全身关节位置目标；训练时无物体，采用逆力训练，在负载掩码标记为可施力的身体上采样力命令并施加相反wrench，使策略为跟踪参考而学会产生等大反向力，并通过从零力到全范围的课程学习。高层力规划器冻结低层控制器，输入机器人及物体参考运动、物体期望接触点、物体测量状态和本体感受，输出力命令；其训练以分析力模型为教师，该模型用物体位姿/速度PD误差经牛顿—欧拉动力学、重力前馈和库仑摩擦补偿计算所需空间wrench，再经抓取矩阵闭式分配为接触力，并以DAgger式在线监督加退火模仿损失和PPO强化学习联合优化，奖励与成功定义在物体上，训练中随机化物体质量并在episode内改变负载。

### 三、结果（Result）
在仿真和硬件上，Ctrl-F完成了需要大且持续交互力的loco-manipulation，并能在负载变化时在线调整力命令，而无力感知的跟踪器无法做到。硬件在Unitree G1上展示了手部拖动、推动、举起以及脚部踢击，在推动和踢击任务中成功操作最重达20kg的箱子，力盲基线在这些任务中失败。实验中力盲跟踪器举起1.5–6kg箱子时因箱子从手掌滑落而零成功，Ctrl-F还能适应任务中途额外增加的负载。

### 四、结论（Conclusion）
论文表明力可作为通用且可命令的交互接口，将通用运动跟踪扩展到物体交互：低层无需物体即可学习力执行，高层基于物体状态和本体感受在线生成力命令。该框架在无需部署时力测量或物体质量的情况下，实现了仿真到硬件的多种全身操作任务和对负载变化的在线适应。

### 五、方法论与关键技术细节
低层训练使用每身体负载掩码，仅编码物理可行性而非任务语义，用以决定何时何地可采样力命令；每个接触身体有固定力范围，课程先零力后逐步放大。高层分析力模型虽使用特权物体状态和真实质量、不可直接部署，但只作粗引导，模仿损失权重退火使强化学习可偏离模型；任务以抓取矩阵、可行力集和负载三元组进入分配问题并闭式批量求解。部署时高层不需要力传感器或物体质量，闭环依赖物体状态与本体感受；实验涵盖举起、系绳箱、踢箱、推箱和拖箱，质量与摩擦设置见表，局限包括依赖参考运动与指定接触点、分析教师使用特权信息以及主要在特定任务集合上验证。
