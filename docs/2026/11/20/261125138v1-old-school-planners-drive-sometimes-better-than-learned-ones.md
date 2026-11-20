# Old-School Planners Drive (Sometimes) Better Than Learned Ones

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Andreas Look
- 机构：Coburg University of Applied Sciences and Arts
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25138v1) · [PDF](https://arxiv.org/pdf/2611.25138v1)

## TLDR
Sixteen textbook hand-written planners can match or outperform learned end-to-end planners such as UniAD across nuScenes, nuPlan, and HUGSIM when using the same frozen perception—with hybrid A* plus nonlinear trajectory optimization improving HUGSIM driving score from 32.0 to 41.8—showing that many crashes stem from planning rather than perception.

## Abstract
End-to-end driving models learn to plan from data, and hand-written planners are widely treated as a thing of the past. We test whether this is justified: we implement sixteen textbook planners, each combining a path source (reference line, A*, hybrid A*, RRT*) with a trajectory method (Frenet lattice, nonlinear optimization, $s$--$t$ search, dynamic window), and evaluate them on three benchmarks: open loop on nuScenes, closed loop on nuPlan with ground-truth perception, and photorealistic closed loop on HUGSIM. On HUGSIM, they replace only the planner of the end-to-end model UniAD and read its frozen perception, without an HD map or other privileged information. On nuScenes and nuPlan, the best textbook planners are competitive (L2 error of 0.735\,m against 0.947\,m for UniAD's planner; a nuPlan score of 79.3 against 76.1 for the rule-based PDM-Closed on Test14-hard with reactive agents). On HUGSIM, nine of the sixteen score above UniAD's learned planner on the same perception,. The best, a hybrid A* path followed by nonlinear trajectory optimization, raises HUGSIM's driving score (HD-Score) from 32.0 to 41.8. The gain is largest with standing and oncoming cars; against cars that steer at the ego, there is none. In 31 of the 182 runs in which UniAD's planner hits a car, the best textbook planner completes the route on the same perception: these crashes are due to the planner, not the perception.


## 精读解读（中文）
### 一、研究动机
端到端驾驶模型从数据中学习规划，而人工编写的教科书式规划器常被视为过时；作者要检验这一判断是否成立，并厘清 UniAD 在真实感闭环模拟器中的碰撞究竟源于感知还是规划。

### 二、技术方案（Method）
作者实现 16 个教科书式规划器，由 4 种路径源（参考线、A*、hybrid A*、RRT*）与 4 种轨迹方法（Frenet lattice、非线性优化、s-t 搜索、动态窗口 DWA）组合而成。规划器读取 UniAD 的跟踪智能体与 6 秒运动预测、占据预测、BEV 可行驶区域掩码、自车速度/加速度/横摆角速度及导航指令，输出与 UniAD 相同格式的 6 个 0.5 秒间隔路点，并在 HUGSIM 中只替换冻结 UniAD 的规划器、保留其感知和同一控制器，不使用 HD 地图或其他特权信息。参考线由可行驶掩码生成，目标点为 3 秒可达范围之外且最多前方 50 米处，静态智能体作为路径源障碍物，动态智能体交由轨迹方法按预测位置逐步碰撞检查。评估覆盖 nuScenes 开环、nuPlan 带真值感知的闭环以及 HUGSIM 照片级闭环；代价权重和间隙通过随机搜索在 nuScenes 与 nuPlan 训练集上调参，HUGSIM 不调参并直接沿用 nuScenes 配置。

### 三、结果（Result）
在 nuScenes 上，参考线加 Frenet lattice 的 L2 误差为 0.735 米，优于 UniAD 规划器的 0.947 米；在 nuPlan 上 Val14 得分为 90.0，比 PDM-Closed 低 2.8 分，而在含反应式智能体的 Test14-hard 上得分为 79.3，高于 PDM-Closed 的 76.1。HUGSIM 上 16 个规划器中有 9 个在相同感知下超过 UniAD 学习规划器，最佳组合 hybrid A* 路径加非线性轨迹优化将 HD-Score 从 32.0 提升到 41.8。增益主要来自静止车辆和迎面车辆场景，对朝自车转向的车辆没有增益；在 UniAD 规划器撞车的 182 次运行中，有 31 次最佳教科书规划器在相同感知下完成路线，说明这些碰撞应归因于规划器而非感知。

### 四、结论（Conclusion）
最佳教科书式规划器在开环和闭环基准上具有竞争力，并能在 UniAD 的噪声感知下有时显著优于学习规划器，表明手工规划器不应被简单视为过时基线。结果同时显示这种优势并非普遍存在：组合方式与场景类型决定成败，尤其对朝自车转向的车辆没有改善，因此端到端系统的失败不能一概归因于感知。

### 五、方法论与关键技术细节
HUGSIM 使用官方 UniAD v2.0 检查点并冻结感知，仅替换最终规划输出，HD-Score 按源数据集和难度层级等权平均，增益以逐场景差值均值±标准误报告。nuScenes 同时采用 UniAD 的粗碰撞框指标和 Li 等的更严格指标，两者不可直接比较；开环 L2 会奖励从实测速度/加速度起步的规划器。nuPlan 使用真值目标、恒速预测和 HD 地图路线中心线，因此与 HUGSIM 的无地图设置不同；HUGSIM 未调参，存在配置迁移限制。方法局限还包括 s-t 搜索平均仅 29.4、加速不足，且没有单一规划器处处最优，例如 hybrid A* 加优化在 nuScenes 为 0.871 米、Val14 为 81.6。
