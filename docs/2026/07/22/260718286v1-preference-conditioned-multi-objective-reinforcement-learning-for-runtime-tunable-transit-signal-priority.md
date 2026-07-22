# Preference-Conditioned Multi-Objective Reinforcement Learning for Runtime-Tunable Transit Signal Priority

- 区域：精读区
- 排名：1
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Philip-Roman Adam, Stefanie Schmidtner
- 机构：Technische Hochschule Ingolstadt
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18286v1) · [PDF](https://arxiv.org/pdf/2607.18286v1)

## TLDR
This paper proposes a preference-conditioned multi-objective reinforcement learning approach for transit signal priority that enables runtime tuning of the bus-priority vs. overall traffic delay trade-off via a single preference parameter without retraining, and demonstrates superior performance over fixed-time and rule-based baselines while respecting operational constraints.

## Abstract
Transit signal priority (TSP) requires balancing competing objectives: reducing bus delay while limiting adverse impacts on non-bus traffic and avoiding extreme waits for a subset of vehicles. Existing reinforcement-learning (RL) approaches to TSP typically encode transit-aware features (e.g., occupancy and schedule deviation) but optimize a fixed reward or fixed scalarization, which limits operational flexibility when agency priorities change across time-of-day or disruption conditions. We present a preference-conditioned TSP controller, $π(a \mid s,w)$, that selects the next signal phase under minimum/maximum green and transition-feasibility constraints and can be tuned at runtime via a preference parameter $w$ to trade off bus-priority emphasis against overall traffic delay without retraining. We implement this on top of IntersectionZoo by introducing a constrained signal-control/TSP wrapper, and we extend scenario generation with bus-prevalence augmentation and timetable-based bus insertion to address sparse transit-priority events during training. Experiments against fixed-time control, a rule-based TSP overlay, and fixed-weight PPO specialists show that a single learned conditioned policy spans a smooth empirical trade-off frontier across runtime preferences, outperforms fixed-time and rule-based baselines, and maintains constraint feasibility, while tail-delay diagnostics reveal that non-bus externalities remain limited for moderate preference settings but can increase substantially under high bus-priority weights. The source code of this work is available at https://github.com/urbanAIthi/morl-tsp.


## 精读解读（中文）
### 一、研究动机
现有基于强化学习的公交信号优先方法通常优化固定奖励或固定标量化，缺乏运行时调整能力；当机构优先级因时段或中断条件变化时，需要重新训练，操作灵活性有限。为此，本文提出一种偏好条件控制器，支持运行时通过偏好参数连续调节公交优先级与整体交通延迟的权衡。

### 二、技术方案（Method）
在IntersectionZoo平台上实现约束信号控制/TSP包装器，构建标准化基准测试环境。输入包括信号状态、交通特征（车道密度、队列、延迟）和公交特征（固定尺寸的公交槽编码，含最近两辆公交距离），以及运行时偏好参数w（公交优先权重）。控制器π(a|s,w)使用Envelope Q-Learning训练，学习偏好条件动作价值函数Q(s,a,w)，通过最大化w^T Q选择下一相位，并在最小绿灯20s、最大绿灯50s和转换可行性约束下执行。训练时采用偏好课程（初始w~U(0.1,0.9)，后扩展至[0,1]），奖励向量包含公交延迟和全车辆延迟，并加入非公交尾部延迟CVaR惩罚（α=0.1，阈值120s，权重0.25）。推理时仅需改变w即可调整权衡。

### 三、结果（Result）
在三个交叉口案例（NYC10802, LA2114, CHI2412）上，偏好条件策略在11点偏好扫描中覆盖平滑的经验权衡前沿，超体积指标优于固定时间和基于规则的TSP基线，且与固定权重PPO专家相比，单个策略即可实现连续权衡而无需重新训练。尾部延迟诊断显示，适中偏好（w=0.5）下非公交外部性有限，高公交权重（w=0.7）下非公交车辆尾部延迟显著增加。

### 四、结论（Conclusion）
偏好条件多目标强化学习方法实现了运行时可调的公交信号优先控制，单个策略在连续偏好空间内提供平滑权衡，避免了重新训练，且性能优于传统基线和固定权重专家策略。该方法在保持约束可行的同时，能有效管理非公交交通的负外部性，适用于机构优先级动态变化的场景。

### 五、方法论与关键技术细节
关键细节包括：使用Envelope Q-Learning训练偏好条件Q函数，Q网络为4层MLP（256单元）；采用最小绿灯20s、最大绿灯50s、黄灯转换3s，决策间隔4s，动作不可行时施加120.0惩罚；输入观测含每车道2个公交槽的距离编码（0-250m归一化）；训练时偏好课程和3次梯度更新/环境步；局限为仅评估单交叉口、未使用车辆占用/时刻偏差特征、仿真假设可能限制实际部署。
