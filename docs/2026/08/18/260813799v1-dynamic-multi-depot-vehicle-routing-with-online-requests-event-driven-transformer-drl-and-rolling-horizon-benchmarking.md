# Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Faezeh Ardali, Gerald M. Knapp
- 机构：Louisiana State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13799v1) · [PDF](https://arxiv.org/pdf/2608.13799v1)

## TLDR
An event-driven learning and benchmarking framework for dynamic multi-depot vehicle routing shows that masked MLP/Transformer policies trained with behavior cloning and PPO provide fast, transferable decisions, but the nearest-feasible heuristic achieves the best overall routing quality, stability, and runtime, with rolling-horizon optimization best for service responsiveness at much higher computational cost.

## Abstract
This paper presents an event-driven learning and benchmarking framework for the Dynamic Multi-Depot Vehicle Routing Problem with progressively revealed requests and evolving vehicle states. Masked MLP and Transformer policies are trained through behavior cloning and proximal policy optimization. Deterministic feasibility masking prevents invalid vehicle--request assignments, while fixed-prefix/flexible-suffix route commitments protect completed, active, and near-term decisions and separately measure vehicle reassignment and resequencing. The learned policies are compared with dynamic insertion heuristics and time-limited rolling-horizon optimization. In a 20-scenario policy benchmark, all methods completed every request without invalid actions, but nearest feasible achieved the lowest mean objective and outperformed the learned policies in routing quality, waiting time, stability, makespan, and runtime. Across five independent training runs, PPO had little average effect on the MLP and improved the Transformer on average, although with greater seed variability. Under the common protocol, nearest feasible achieved the lowest combined objective and route disruption, whereas rolling horizon achieved the lowest waiting times and makespan at substantially higher computational cost. The learned policies retained millisecond-level decisions and transferred to instances with up to 80 requests without retraining, but did not outperform the strongest heuristic. No single method was best across routing efficiency, service responsiveness, stability, and online computation.


## 精读解读（中文）
### 一、研究动机
动态多车场车辆路径问题（D-MDVRP）在真实场景中面临请求逐步到达和车辆状态持续演化，传统静态路由方法难以应对在线决策。现有方法多将局部插入、滚动时域优化和学习式调度分开研究，缺乏在统一稳定性感知协议下对可行性和计划变动的系统比较。本文旨在构建一个事件驱动的学习与基准框架，在相同环境下评估启发式、学习策略和滚动时域优化，并显式处理可行性掩码、路线承诺和扰动度量，以平衡路由效率、响应性、稳定性与在线计算成本。

### 二、技术方案（Method）
本文提出事件驱动的D-MDVRP学习与基准框架。环境建模为有限时域MDP，状态包含请求、车辆、车场和全局特征，请求特征为10维归一化向量，车辆为9维，车场为6维。每个事件（请求到达、车辆到达、服务开始/完成）触发重规划，路线分为固定前缀和柔性后缀，仅柔性部分可重分配或重排序。策略采用掩码MLP和Transformer：MLP用30→64→32→1共享ReLU网络对每对车辆-请求打分，Transformer用单层四头注意力编码30个请求、4个车辆、2个车场token，维度32，结合5维边特征经101→64→1打分。训练分两步：先由专家行为克隆（MLP专家为等待感知插入，Transformer专家为混合评分选择），再用PPO微调，PPO奖励由增量距离、预测等待时间和变更指示符组成，并保证无折扣回合奖励与评估目标一致。确定性掩码排除无效动作，固定前缀/灵活后缀承诺保护已完成、激活和近期决策，并分别统计车辆重分配和前驱变更。测试中与最近可行、最便宜追加、动态插入启发式以及时间限制的滚动时域优化在20场景下比较。

### 三、结果（Result）
在20场景策略基准中，所有方法均无无效动作且完成全部请求，但最近可行启发式取得最低平均目标值，在路由质量、等待时间、稳定性、完工时间和运行时间上均优于学习策略。跨五次独立训练，PPO对MLP平均效果很小，对Transformer平均有提升但种子变异性更大。在统一协议下，最近可行获得最低组合目标和最小路线扰动，滚动时域获得最低等待时间和完工时间但计算成本显著更高。学习策略保持毫秒级决策，且无需重训练即可迁移到最多80个请求的实例，但未超越最强启发式。没有单一方法在路由效率、服务响应性、稳定性和在线计算上全面最优。

### 四、结论（Conclusion）
研究表明，事件驱动的Transformer-DRL框架能够有效处理动态多车场路由的在线请求和状态演化，确定性掩码与固定前缀/灵活后缀承诺保证了动作可行性和计划稳定性。然而在现有实验规模下，简单启发式（最近可行）在综合目标和多数指标上仍优于学习策略，滚动时域优化虽质量高但计算代价大。本文的贡献在于提供了统一的稳定性感知比较协议，并指出学习策略的优势在于毫秒级推理和实例迁移能力，但尚不足以替代强启发式；未来需改进策略训练或结合在线优化以提升竞争力。

### 五、方法论与关键技术细节
关键细节包括：请求特征含位置、需求、服务时长、优先级、到达时间、等待时间、状态码、分配车辆和待处理标志；车辆特征含位置、剩余/已用容量、状态、当前请求、柔性路线长度、归属车场和累计距离。MLP的BC训练集4525样本、验证1528，Transformer为4266/1372，专家不同（等待感知插入 vs 混合评分），BC后PPO微调（MLP-PPO迭代8/3/3，Trans-PPO 6/2/2）。评估目标J_eval=D+0.10W+2.00N_chg，稳定性目标J_stab=D+0.10W+2.00N_asg+1.00N_seq。PPO奖励采用-0.01*(增量距离+0.10预测等待+2.00变更指示)，并有终端修正使回合奖励等于-0.01J_eval。Transformer位置编码和token类型嵌入加入全局向量，未揭示请求被零化并通过padding mask排除。所有比较共享相同场景种子和可行性协议。局限性：仅测试4车30请求的基例和最多80请求迁移；启发式在质量上占优；PPO种子变异性大；滚动时域计算成本高；学习策略未超越最强启发式。
