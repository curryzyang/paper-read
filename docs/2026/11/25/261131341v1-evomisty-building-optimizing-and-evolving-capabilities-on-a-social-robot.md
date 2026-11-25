# EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot

- 区域：精读区
- 排名：7
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Xiao Wang, Lu Dong, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31341v1) · [PDF](https://arxiv.org/pdf/2611.31341v1)

## TLDR
EvoMisty is a plugin-based framework that enables coding agents to autonomously build and verify robot capabilities from documentation, solve tasks by combining atomic capabilities and skills, optimize completed programs against user-specified metrics, and distill reusable skills for future tasks, demonstrated on a physical Misty II social robot with improved performance and cross-task reuse.

## Abstract
Social robots face diverse and changing tasks in companionship and education. LLM-based methods can generate task programs, but they still rely on manually developed control interfaces and predefined capabilities. They also lack a general mechanism to optimize completed tasks based on user-specified metrics and reuse performance improvements across tasks.We present EvoMisty, a plugin-based framework that enables coding agents to build and continually improve robot capabilities. EvoMisty builds a control program from official documentation and verifies candidate capabilities on a physical robot. Verified capabilities are stored in an atomic capability library and combined with existing skills to solve tasks. After task completion, EvoMisty can collect execution data, measure user-specified metrics, and iteratively improve task programs. It then distills reusable skills from final solutions into a skill library for future tasks.We evaluate EvoMisty on a physical Misty II robot using Claude Code and Codex. The two agents construct 109 and 107 verified atomic capabilities, respectively. Both complete all 28 AutoMisty benchmark tasks and seven additional tasks beyond AutoMisty's capabilities. Optimization improves all seven evaluated metrics across five tasks. For example, dialogue response latency decreases by 52% and 71%, respectively. Reusing skills from one optimized dialogue task reduces latency by 33% to 72% in three other dialogue tasks without further optimization. All code and experimental videos will be publicly released through the webpage: https://wangxiaoshawn.github.io/projects/evomisty/index.html


## 精读解读（中文）
### 一、研究动机
社交机器人在陪伴与教育中面临多样且变化的任务，现有基于LLM的方法虽能生成任务程序，但仍依赖人工开发的控制接口和预定义能力，且缺乏按用户指定指标优化已完成任务并将性能提升复用到新任务的通用机制。

### 二、技术方案（Method）
EvoMisty是插件式框架，分为Build、Solve、Optimize、Evolve四阶段：Build让编码代理阅读官方文档构建控制程序，设计输入、预期结果与通过条件并在真实机器人上验证，将通过验证的能力封装为原子能力库；Solve结合原子能力库与技能库生成任务程序，将成功标准拆成可验证条件并在物理机器人上测试；Optimize通过数据钩子记录原始音视频、程序输出和机器人反馈，通过测量钩子记录事件时间戳等客观证据，结合离线回放与物理机器人评估按用户指定指标迭代改进程序并保持原成功标准；Evolve从最终方案中蒸馏可复用技能存入技能库。

### 三、结果（Result）
在物理Misty II机器人上使用Claude Code和Codex评估，两者分别构建109和107个经验证的原子能力，均完成全部28个AutoMisty基准任务以及7个超出AutoMisty能力的附加任务；优化在5个任务上提升全部7项评估指标，例如对话响应延迟分别降低52%和71%；从一个已优化对话任务复用技能后，在另外三个对话任务中无需进一步优化即可将延迟降低33%至72%。

### 四、结论（Conclusion）
EvoMisty使编码代理能够自主构建、验证、优化并演化机器人能力，将设备级能力构建与任务级执行分离，并在真实社交机器人上展示了指标驱动的性能优化与跨任务复用效果。

### 五、方法论与关键技术细节
关键实现包括：能力必须在物理机器人上通过设备状态、执行日志等客观证据或人工反馈验证，失败候选会迭代修复并在固定尝试次数后丢弃；任务成功条件区分程序自动检查与人工观察/听觉检查，且先自动后人工；Solve优先复用技能库；Optimize以数据钩子和测量钩子采集证据，并用离线回放加物理评估优化，同时保持原成功标准；局限包括仅在Misty II单一平台和两种编码代理上验证、部分感知条件依赖人工、重试预算固定、评估指标与任务规模有限。
