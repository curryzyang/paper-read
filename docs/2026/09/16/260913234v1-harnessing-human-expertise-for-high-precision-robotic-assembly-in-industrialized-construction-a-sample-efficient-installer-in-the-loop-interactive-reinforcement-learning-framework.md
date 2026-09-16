# Harnessing human expertise for high-precision robotic assembly in industrialized construction: A sample-efficient installer-in-the-loop interactive reinforcement learning framework

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Zekai Jin, Huiguang Wang, Xiaoning Sun, Yi Shao
- 机构：McGill University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13234v1) · [PDF](https://arxiv.org/pdf/2609.13234v1)

## TLDR
The paper presents an installer-in-the-loop interactive reinforcement learning framework that combines offline teleoperated demonstrations, sparse event-driven human takeovers, and acceptance-aligned terminal rewards with a temporally abstract Q-chunking/Flow Q-Learning policy to achieve sample-efficient, high-precision robotic assembly in industrialized construction, reaching 100% autonomous seating under 2 mm clearance with only 12–15 minutes of human supervision.

## Abstract
Industrialized construction imposes stringent precision requirements on robotic assembly of modular components such as prefabricated window units. In tolerance-critical operations, the central bottleneck is not only mechanical clearance but also converting tacit installer expertise into data-efficient autonomy under sparse acceptance feedback, contact variability, and millimeter-scale constraints. We present an installer-in-the-loop interactive reinforcement learning framework that acquires expertise through offline teleoperated demonstrations, sparse event-driven binary takeovers at contact-failure boundaries, and acceptance-aligned terminal rewards, logged under a unified schema for traceable offline-to-online adaptation. A temporally abstract action-sequence policy built on Q-chunking with Flow Q-Learning captures multimodal recovery maneuvers under sparse terminal rewards, while a non-updating warm-start phase stabilizes the offline-to-online transition. The framework is evaluated in MuJoCo across the workflow from suction acquisition through clearance-limited seating, under structured staging and end-to-end randomized placement. Within a defined stress-test regime with 2 mm per-side clearance, bounded pose perturbations, and friction randomization, the pipeline attains 100\% autonomous seating with 12--15 min of cumulative installer supervision over 3.0 h of online training, and reaches the 95\% success milestone in approximately 0.5 h and 1.5 h in the two experiments. We also report wall-clock adaptation time, cumulative takeover minutes, intervention-rate decay, and stage-wise failure attribution to inform supervision budgeting. Ablations isolate the complementary contributions of temporal abstraction, installer intervention, and warm-start value calibration.


## 精读解读（中文）
### 一、研究动机
工业化建造中预制窗单元等模块化构件的机器人装配对毫米级公差极为敏感，终端插入与就座阶段受接触多变、间隙狭小和验收反馈稀疏制约，核心瓶颈不只是机械间隙，而是如何把安装工人的隐性纠错经验转化为数据高效的自主策略。现有建筑机器人自动化多在自由空间搬运和粗定位表现良好，一旦进入持续多面接触与绑定、楔紧、卡死等失效边界，脚本控制和常规RL都难以发现并稳定执行退让、偏转、再插入等多步恢复动作。

### 二、技术方案（Method）
该研究提出安装工在环的交互式强化学习框架，统一采集三类经验：离线遥操作演示、在线训练中接触失败边界处的事件驱动二值接管、以及与验收语义对齐的终端稀疏奖励，并按统一日志模式存入离线与在线回放缓冲。学习核心采用基于Q-chunking with Flow Q-Learning的时间抽象动作序列策略，在固定长度动作块空间做块级Q学习，用基于流的教师行为模型提供多模态序列先验并蒸馏到噪声条件学生演员，由评论家评估已执行动作块；训练分三阶段：离线行为初始化、非更新warm-start价值校准、在线微调并允许安装工二值接管覆盖高层动作接口。系统在MuJoCo中覆盖从吸盘获取、搬运、对齐到间隙受限插入与就座的完整工作流，在结构化分段和端到端随机放置两种设置下评估，高层控制接口为10 Hz，观测包括双视角RGB和本体感觉，动作块由统一低层跟踪控制器展开执行。

### 三、结果（Result）
在每侧2 mm间隙、有界位姿扰动和摩擦随机化的定义压力测试场景中，该流程实现100%自主就座；实验A和B分别仅需约12分钟和15分钟累计安装工监督，对应3.0小时在线训练，并在约0.5小时和1.5小时达到95%成功里程碑。论文还报告了真实时钟适应时间、累计接管分钟数、干预率衰减和分阶段失败归因，用于监督预算与故障诊断；消融实验表明时间抽象、安装工干预和warm-start价值校准各自具有互补贡献，其中时间抽象与多模态序列建模在压力测试区间内均属必要。

### 四、结论（Conclusion）
该框架把公差关键建筑装配中的隐性安装技能分解为结构化演示、事件触发恢复干预和验收对齐评估，证明安装工在环交互强化学习可以在稀疏终端奖励和毫米级约束下显著提升样本效率与自主就座成功率。其方法贡献不在于提出通用RL新算法，而在于面向预制幕墙装配的领域工程信息化实例化，为细粒度机器人建造技能提供了可追溯、可核算监督成本的训练模板。当前证据来自MuJoCo压力测试，为仿真部署导向指标而非现场保证，后续需验证从仿真到物理环境的迁移边界。

### 五、方法论与关键技术细节
关键实现包括：有限时域MDP建模，观测为双视角RGB加本体感觉，动作块在10 Hz高层接口上决策并由统一低层控制器执行；奖励采用验收对齐的终端二值成功信号，避免密集塑形错位；二值接管仅发生在接触失败边界，兼具安全包络约束和将回放数据偏向高价值恢复片段的作用；非更新warm-start阶段在梯度更新前校准评论家以适应在线分布，缓解离线到在线分布漂移；QC-FQL中流教师提供多模态动作序列先验，学生演员为噪声条件、常数时间推理，评论家进行块级价值学习，从而支持退让-偏转-再插入等恢复模式；评估固定2 mm每侧间隙、有界位姿扰动和摩擦随机化，并统计干预率衰减、接管分钟和阶段失败归因；局限在于全部结果来自仿真，未给出真实工地泛化保证。
