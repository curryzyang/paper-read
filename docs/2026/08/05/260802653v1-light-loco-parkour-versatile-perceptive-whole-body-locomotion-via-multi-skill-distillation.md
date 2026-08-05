# Light-Loco-Parkour: Versatile Perceptive Whole-Body Locomotion via Multi-Skill Distillation

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Hongming Chen, Zhuoran Li, Hongxi Wang, Jiangpeng Hu, Ziliang Li, Peize Liu, QingRui Zhao, Xuhao Liu, Liang Pan, Ximin Lyu, Yuntao Ma, Tingxiang Fan
- 机构：Light Origins
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02653v1) · [PDF](https://arxiv.org/pdf/2608.02653v1)

## TLDR
Light-Loco-Parkour presents a single deployable, perception-driven humanoid policy that learns versatile whole-body locomotion and parkour skills from sparse seed motions, autonomously transitions between them from onboard depth and velocity commands, and transfers zero-shot to real-world indoor and outdoor terrains.

## Abstract
Existing humanoid whole-body control systems still fall short of the way humans move through cluttered terrain: they either track expressive whole-body references without terrain generalization, or react to terrain online while leaving the arms, torso, and knees largely unused. We present \texttt{Light-Loco-Parkour} (LLP), an end-to-end perceptive whole-body locomotion system that closes this gap with a single deployable policy. Conditioned only on onboard depth and a velocity command, the policy decides when to walk, balance, climb, step down, or vault, with no reference input, skill label, hand-coded gate, or runtime motion graph. Compared with prior humanoid systems, LLP makes three contributions. First, it introduces a whole-body perceptive-control pipeline that extends an RL-trained, velocity-tracking locomotion policy with parkour skills learned from object-interacting motions, so the same policy tracks velocity in open terrain, executes whole-body traversal at obstacles, and resumes locomotion afterward. Second, it acquires terrain-conditioned skills from sparse seeds by expanding a single motion into dynamically feasible, terrain-paired references across obstacle geometry, rather than relying on a large motion corpus. Third, it learns autonomous skill transitions from reward, letting the policy decide when and which whole-body skill to invoke from depth and command alone, with no one-hot skill label, hand-coded state machine, or runtime motion generator. Simulation and real-world experiments show high success across both benchmarked terrains and unseen obstacle variations, and the same policy transfers zero-shot to indoor and outdoor hardware experiments. These results demonstrate autonomous perceptive whole-body locomotion on a humanoid in outdoor settings, using only onboard sensing and a single deployable policy.


## 精读解读（中文）
### 一、研究动机
现有仿人全身控制系统要么跟踪表达性全身参考运动但无法泛化到复杂地形，要么在线反应地形却主要依赖腿部而忽视手臂、躯干和膝盖；缺乏一个单一策略能够感知环境并协调全身穿越杂乱地形。

### 二、技术方案（Method）
提出Light-Loco-Parkour，一个端到端感知全身运动系统。首先用强化学习训练一个速度跟踪的感知运动教师策略，输入包含速度命令、本体感觉和局部高度扫描（特权信息）；其次，针对每种技能，从单个种子运动通过数据增强生成动态可行且地形配对的参考运动，训练各技能的教师策略；然后采用多专家DAgger将运动教师和技能教师蒸馏到一个统一的高度扫描学生策略，并设计仅由奖励驱动的转换阶段，使策略自主决定何时调用哪个技能；最后通过深度蒸馏将高度扫描策略转换为循环深度策略，仅使用机载深度、本体感觉和速度命令部署，以50Hz运行。

### 三、结果（Result）
在仿真和真实实验中，该方法在基准地形和未见障碍变体上均获得高成功率，并零样本迁移到室内外硬件实验，实现了户外环境下仅依靠机载感知和单一可部署策略的仿人自主感知全身运动。

### 四、结论（Conclusion）
证明了单一策略无需参考输入、技能标签、手写门控或运行时运动图，仅凭机载深度和速度命令即可在杂乱地形中自主选择并执行走、平衡、攀爬、下阶、跨跃等全身技能，完成长时程任务。

### 五、方法论与关键技术细节
采用教师-学生架构，教师使用特权信息（高度扫描）训练，学生通过多专家DAgger蒸馏；数据增强将单个种子运动扩展到连续障碍几何（如爬升高度从45cm到75cm），保证动态可行；转换阶段完全由RL奖励驱动，无专家、参考或技能标签，AMP先验用于在触发位置从运动切换到技能；深度蒸馏采用教师动作监督和辅助高度扫描重建；策略在机载以50Hz运行，所有训练在IsaacLab中进行。
