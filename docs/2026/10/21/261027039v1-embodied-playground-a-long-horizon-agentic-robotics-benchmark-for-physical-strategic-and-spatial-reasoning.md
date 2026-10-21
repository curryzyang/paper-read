# Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning

- 区域：精读区
- 排名：6
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Feng Chen, Pei Zhou, Lixuan He, Yunchao Yao, Li Sun, Shenghua Gao, Mingyu Ding, Kaifeng Zhang, Kaichen Zhou, Yi Ma
- 机构：Sharpa, Tsinghua University, University of North Carolina at Chapel Hill, Stanford University, MIT, HKU
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27039v1) · [PDF](https://arxiv.org/pdf/2610.27039v1)

## TLDR
The paper introduces Embodied Playground, a 410-environment robotics benchmark—with a representative 100-task EP-100 subset—for evaluating whether foundation-model agents can sustain physical, strategic, and spatial reasoning and revise plans from execution feedback across long-horizon tasks.

## Abstract
Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subsequent decisions. The playground comprises 410 task environments spanning basic manipulation, sequential puzzles, and multi-stage household activities, with variations in planning depth, geometric constraints, and physical execution demands. We curate EP-100, a representative selection of 100 tasks across five suites and 16 task types, together with the EP-Easy and EP-Hard difficulty splits and the compact EP-20 selection. A shared protocol specifies observation and tool access, resource budgets, repeated trials, and independent checks of goal completion, task-rule compliance, and physical validity. Embodied Playground provides a unified framework for studying whether foundation-model agents can sustain effective reasoning and action over extended task horizons. https://winniechen2002.github.io/Agent-bench-website/


## 精读解读（中文）
### 一、研究动机
基础模型在机器人任务中展现出视觉理解、空间与物理推理及策略制定潜力，但长时程任务要求智能体在相互依赖的阶段之间持续保持连贯推理与可靠物理执行，且早期动作会改变后续条件。现有机器人基准多聚焦控制策略的性能与泛化，缺少以基础模型智能体为中心、评估其跟踪进度、满足中间约束并依据执行反馈修订计划的能力。

### 二、技术方案（Method）
论文构建 Embodied Playground 模拟机器人基准，包含410个任务环境，覆盖基础操作、顺序谜题和多阶段家务活动，并从中选取100个任务形成EP-100，划分为五个套件和16种任务类型，同时提供EP-Easy、EP-Hard与紧凑版EP-20。所有环境共享describe、observe、step、finish接口，规定观测与工具访问级别、资源预算、重复试验，并由独立评估器检查目标完成、任务规则合规和物理有效性；智能体通过公共SDK编写并执行代码，利用相机、本体感觉和任务元数据及允许的感知或规划工具，根据执行反馈更新计划。环境后端使用MuJoCo、Isaac Lab和ManiSkill，涵盖双Panda、FR3-Sharpa、浮动Sharpa、ALOHA、Fetch、xArm7-Allegro、UR10e-Shadow等 embodiments。

### 三、结果（Result）
基准共包含410个任务-具身组合，EP-100覆盖Launch、Tower、Lock、Cube、Home五个套件和16种任务类型，并通过规划深度、几何约束、质量摩擦、动态交互与目标顺序等变化系统调节空间、物理和策略推理难度。预览图中的示例对比了GPT-6-Astra与Opus-5.5-extra在各套件上的Pass@2、条件结果和成功尝试平均时长，但给定摘要与预览未提供完整数值结果。

### 四、结论（Conclusion）
Embodied Playground 提供了一个统一框架，用于研究基础模型智能体能否在长时程任务中维持有效推理与行动，并支持跨推理需求和机器人具身的可解释比较。该基准强调进度跟踪、中间约束满足、执行反馈驱动重规划和物理有效性，有助于识别单一聚合分数掩盖的能力强弱与局限。

### 五、方法论与关键技术细节
任务包含Launcher、Hanoi、口袋魔方、Rubik魔方、孔明锁、书架及ManiSkill家务/几何/动力学任务，不同任务使用不同模拟器与具身；EP-100优先选择多数智能体可运行的任务，因此平行夹爪获得较多名额，灵巧手仅取较易原生配置的小样本，Launcher仅评估预装第一发弹丸的loaded模式并从80个已有完整成功记录的场景中抽取。协议规定累计访问级别、观测读取不推进物理时间、动作经声明控制器生效，并检查释放与稳定性等物理条件；种子和初始操作模式定义试验条件，部分案例标识跨具身复用以便比较平行夹爪与灵巧手。局限包括评测在仿真中完成、任务选择受可负担性影响而偏向平行夹爪，且给定预览未展示完整实验数值与统计结论。
