# TriSAR: Task Coordination and Collision Avoidance for Aerial Robot Teams in Disaster Response

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Aditya Anil Kapile, Pedro Machado, Isibor Kennedy Ihianle
- 机构：Nottingham Trent University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01731v1) · [PDF](https://arxiv.org/pdf/2609.01731v1)

## TLDR
TriSAR uses a 2×2 factorial simulation of a five-UAV disaster-response system to show that reactive collision avoidance substantially improves safety under both task-allocation strategies, whereas a genetic-algorithm allocator improves mission efficiency over greedy allocation only when reactive repulsion is disabled.

## Abstract
Multi-Unmanned Aerial Vehicle (UAV) disaster-response systems require coordinated task assignment and local trajectory control, yet the individual and combined contributions of these coordination layers to mission efficiency and operational safety remain insufficiently characterised under controlled experimental conditions. TriSAR is evaluated as a five-UAV coordination system operating in a physics-based Gazebo simulation of an earthquake-damaged urban environment. A 2 x 2 factorial design compares two task-allocation strategies (Genetic Algorithm and greedy fitness-based allocation) with reactive collision avoidance enabled or disabled. Each of the four configurations was evaluated over 30 stochastic episodes in a common scenario of five UAVs and eight targets. Under greedy allocation, enabling repulsion eliminated recorded collision-threshold violations, confirmed by a Mann-Whitney test (U = 885, p = 4.03 x 10^-12, rank-biserial r = 0.97). Under GA allocation, the same protective effect was confirmed (U = 675, p = 1.26 x 10^-5, rank-biserial r = 0.50). For mission-efficiency metrics, GA-based allocation showed no statistically detectable advantage over greedy allocation when repulsion was enabled, but a significant advantage in steps, path length, and energy when repulsion was disabled (Welch's t-tests, |g| between 0.92 and 1.76). These results show that reactive repulsion provides a substantial, allocation-dependent safety benefit, while the additional computational complexity of GA-based task allocation yields a detectable mission-efficiency benefit only when repulsion is disabled.


## 精读解读（中文）
### 一、研究动机
多无人机灾害响应系统需要协同任务分配与局部轨迹控制，但现有研究通常只评估完整混合架构的整体性能，缺乏在受控实验条件下对任务分配与防碰撞这两个协调层各自贡献及交互作用的量化分析。文献中的分配研究常报告质量提升却不测计算代价或不进行消融，防碰撞研究未放入任务分配流水线评估，混合GA-PSO系统则将两层融合过紧难以独立测量。TriSAR旨在通过可控的2x2因子消融实验填补这一空白，回答GA分配是否比贪心分配更高效、反应式排斥是否降低碰撞违规、以及排斥的安全效果是否依赖分配策略这三个问题。

### 二、技术方案（Method）
TriSAR采用五架UAV在基于物理的Gazebo模拟地震损坏城市环境（500m×500m×120m，3架搜索救援代理+2架固定中继代理，8个目标含4屋顶4地面）中运行。系统包含GA任务分配器和PSO轨迹控制器，二者可独立开关以实现消融。任务分配中，染色体为目标索引的排列，解码时按最低分配成本将任务依次分给代理，成本函数含距离、电池、目标紧迫度及屋顶类型惩罚（屋顶1.25倍）；GA使用40种群、100代、3-way锦标赛选择、PMX交叉概率0.85、基因交换突变概率0.15、精英保留2个、15代无改进早停；贪心基线直接用同一成本函数分配。轨迹控制采用每代理速度空间的局部PSO：每控制步（10 Hz）维护10个候选速度向量，围绕当前目标朝向方向重新初始化，经5次内迭代更新（w=c1=c2=0.5），选最终成本最低的候选速度；反应式排斥作为独立调节项，对安全距离2.5m内的邻居或障碍施加与侵入深度成比例的排斥力（k_rep=3.0 m/s）。能量模型采用三次阻力模型（悬停功率0.28、阻力系数7e-5、质量系数0.05）。实验采用2x2因子设计（GA/贪心分配 × 排斥启用/禁用），四种配置各运行30次随机种子独立的情节，配置间地面目标坐标有±2m抖动。碰撞违规定义为代理间距离低于2.5m的步数。统计使用Mann-Whitney U检验和Welch's t检验。

### 三、结果（Result）
在贪心分配下，启用排斥使碰撞阈值违规从有变为零，Mann-Whitney检验确认显著（U=885，p=4.03e-12，秩双列r=0.97）；在GA分配下同样显著（U=675，p=1.26e-5，r=0.50），但效应量更小。对于任务效率指标（步数、路径长度、能量），GA分配相对于贪心分配在排斥启用时没有统计可检测优势，但在排斥禁用时表现出显著优势（Welch's t检验，|g|介于0.92到1.76）。研究还记录了GA分配相比贪心分配需要额外计算时间（原文Section VI-C报告了该缺失的测量）。

### 四、结论（Conclusion）
反应式排斥提供了实质性且依赖分配策略的安全效益：在贪心分配下的安全效果远大于在GA分配下的效果。GA分配增加的搜索复杂度仅在排斥禁用时带来可检测的任务效率收益；在排斥启用时，GA相对贪心没有效率优势。因此对于小规模机队，简单贪心分配加上反应式排斥可能是成本效益更高的方案，而复杂优化分配器的价值取决于防碰撞层是否激活。研究同时暴露了基于位置的排斥的局部极小值脆弱性。

### 五、方法论与关键技术细节
关键要点包括：使用n=30每种配置的一致性批次，所有统计对比在同一批次内完成；碰撞违规定义为距离低于2.5m的离散步数，持续违规计为多次步数，未被折叠为单次事件；无代理-障碍违规记录，安全分析主要针对代理间距离；GA和贪心使用相同成本函数以隔离分配搜索策略的影响；PSO是每代理速度空间的局部轨迹优化器而非全局标准PSO；排斥机制为人工势场，继承了局部极小值脆弱性；能量模型参数是模拟尺度代理指标而非物理校准值；GA分配的计算成本（运行时间）在结果中作为缺失测量被报告，但摘要与重点结论未给具体数值；目标是5UAV/8目标场景，结论针对该规模，不推广到更广泛方法族。实验局限包括只测试一种分配器和一种反应式防碰撞机制。
