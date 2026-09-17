# AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Fouad Bahrpeyma, David Heik, Dirk Reichelt
- 机构：Hochschule für Technik und Wirtschaft Dresden -- University of Applied Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16075v1) · [PDF](https://arxiv.org/pdf/2609.16075v1)

## TLDR
AssemblyGrid v1 is a reproducible benchmark for multi-robot production that integrates process progression, decentralized local observations, material routing, temporary robot coalitions, concurrency, and geometry-dependent feasibility across Flow, Coalition, and Concurrency workloads to evaluate centralized, decentralized, and MARL controllers.

## Abstract
Flexible robotic production requires joint decisions on process progression, material routing, resource assignment, temporary cooperation, and simultaneous execution, since each decision can affect the feasibility of the others. The challenge is greater under decentralized control, where each robot acts from bounded local information while system progress depends on collective decisions, shared resources, material state, and workspace compatibility. These properties closely match cooperative multi-agent decision making under partial observability and resource contention. This paper introduces AssemblyGrid v1, a reproducible benchmark for repeated multi-robot production that combines explicit process progression, decentralized observations, material transfer, temporary multi-robot coalitions, productive concurrency, and geometry-dependent feasibility within one task-level formulation. The benchmark includes Flow, Coalition, and Concurrency workload families, each with three scenario levels. Task success and evaluation measures are defined independently of learning reward and solution method, allowing learning-based and non-learning methods to address the same production problem. AssemblyGrid v1 is evaluated through executable conformance checks, mechanism studies, and algorithmic experiments using a privileged centralized reference, structured decentralized controllers, and MARL methods including IPPO, MAPPO, and QMIX. Results demonstrate productive execution under centralized and decentralized control. The MARL experiments further show that decentralized policies can learn effective production behavior from local observations and actions, supporting AssemblyGrid as a controlled benchmark for studying cooperative decision making in flexible robotic production.


## 精读解读（中文）
### 一、研究动机
柔性机器人生产需要联合决定工序推进、物料路由、资源分配、临时协作与并发执行，这些决策相互耦合，且几何可行性会反过来限制任务与资源选择。去中心化控制下各机器人仅有有限局部信息，系统进度却依赖共享资源、物料状态与集体决策，这与部分可观测、资源竞争下的合作多智能体决策高度相似。现有基准通常把重复物料转化、临时联盟、局部执行和几何约束分散在不同问题设定中，缺少统一且可复现的任务级生产基准。

### 二、技术方案（Method）
论文提出AssemblyGrid v1，以任务级生产单元建模：固定基座机械臂位于规则栅格，原料从左进入、按显式配方工序加工、成品从右离开，重叠工作空间决定交互、临时联盟与并发冲突。环境向每个机器人提供局部观测，要求控制器选择工序、物料转移、资源分配、临时多机器人联盟及并发动作，并以几何可行性约束动作是否可执行；任务成功与评估指标独立于学习奖励和方法。评测流程包括可执行一致性检查、机制研究与算法实验，对比集中式特权参考、结构化去中心化控制器以及IPPO、MAPPO、QMIX等MARL方法；MARL采用集中训练与去中心化执行范式，从局部观测与动作学习生产策略。

### 三、结果（Result）
实验确认基准可执行且机制检查有效，集中式与去中心化控制均能实现生产性执行。MARL实验表明，去中心化策略能够仅凭局部观测和动作学习到有效的生产行为，说明AssemblyGrid可作为研究柔性机器人生产中合作决策的受控基准。评测覆盖Flow、Coalition、Concurrency三类负载族，每族含三个场景级别，用于系统变化过程、联盟和并发需求。

### 四、结论（Conclusion）
AssemblyGrid v1的主要贡献是把显式过程推进、临时操作级联盟、去中心化局部执行、生产并发与几何相关可行性整合到一个与控制器无关的基准中，使学习、规划、调度、优化和启发式方法可在同一生产问题上比较。该基准填补了相邻基准族之间机制分散的空白，并为工业多机器人生产中的MARL研究提供可复现实验平台。其当前形态是任务级抽象代理，几何与物理细节被简化，结果主要支持机制验证而非高保真装配性能结论。

### 五、方法论与关键技术细节
关键细节包括六项设计原则：部分工序需要多机器人合作；产品按配方显式推进；所需机器人组是临时且工序特定的；信息局部性与操作局部性分开表示；几何可行性约束任务和资源选择；基准结果独立于控制器目标。评测以任务级成功和生产率类指标为准，独立于学习奖励，包含可执行一致性检查、机制研究与IPPO、MAPPO、QMIX等参考实验。局限是几何仅为抽象代理，未覆盖完整任务与运动规划、接触动力学和真实硬件约束，摘要也未报告具体数值超参、损失函数或可复现指标数值。
