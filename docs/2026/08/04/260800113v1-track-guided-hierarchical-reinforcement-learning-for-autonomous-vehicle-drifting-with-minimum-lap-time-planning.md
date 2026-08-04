# Track-Guided Hierarchical Reinforcement Learning for Autonomous Vehicle Drifting with Minimum-Lap-Time Planning

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Sheng Zhao, Bolin Zhao, Xiaodong Wu, Chen Lv
- 机构：Shanghai Jiao Tong University, Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00113v1) · [PDF](https://arxiv.org/pdf/2608.00113v1)

## TLDR
The paper proposes a track-guided hierarchical reinforcement learning framework with minimum-lap-time optimal-control-based drift planning that progressively trains a drift controller to stabilize highly nonlinear drift dynamics and minimize lap time on low-friction tracks.

## Abstract
In Formula 1, drivers optimize racing lines within tire grip limits to minimize lap times; however, in rally racing, drivers intentionally break traction to drift on loose surfaces. This maneuver rapidly aligns the vehicle for corner exits, ultimately reducing lap time. Autonomously executing such maneuvers formulates a complex dual-objective control problem: stabilizing highly nonlinear drift dynamics while strictly minimizing lap time. Addressing this challenge motivates the development of advanced Minimum-Lap-Time (MLT) drift control architectures. This paper proposes a planning-control framework specifically designed for MLT drifting scenario. First, we formulate an optimal control problem to generate a MLT drift planning trajectory, which is used as prior data to train a deep reinforcement learning drift controller. Given that drifting involves extremely large sideslip angles and is therefore challenging to learn directly, a Track-guided Reinforcement Learning (TgRL) drift control method is proposed to enable progressive training in a step-by-step manner, from drift control policy, to drift corner policy, and finally to a comprehensive drift race policy. The reward function incorporates both an instant reward term and an end reward term derived from the Minimum-Lap-Time objective. Simulation results demonstrate that the proposed framework enables the agent to learn a drift racing policy that not only ensures vehicle motion control performance but also effectively reduces lap time.


## 精读解读（中文）
### 一、研究动机
在拉力赛中，车手通过漂移故意突破轮胎抓地力极限，以快速调整车身姿态并缩短过弯时间，但这一过程同时涉及高度非线性的漂移动力学稳定与最小单圈时间优化双重目标。现有基于强化学习的漂移控制方法大多依赖昂贵且车辆专用的专家示范数据，且缺乏对早期训练的结构化引导，导致策略收敛缓慢且泛化性差。为此，本文提出一种面向最小单圈时间（MLT）漂移场景的规划-控制分层框架。

### 二、技术方案（Method）
该方法首先基于3自由度自行车模型和Magic Formula联合滑移轮胎模型，在Frenet坐标系下构建以状态（车速v、质心侧偏角β、横摆角速度r、横向偏移l、横摆角误差Δψ）和控制量（前轮转角δ_f、后轮滑移率λ_r）为变量的最优控制问题，通过求解MLT漂移规划（MLTDP）生成包含位置、姿态和速度信息的动态可行参考轨迹，作为先验数据。然后提出轨道引导强化学习（TgRL）方法，采用课程学习思想分三阶段渐进训练：先从基础漂移控制策略学起，再过渡到漂移过弯策略，最后综合为完整漂移比赛策略。奖励函数由即时跟踪项和源自最小单圈时间目标的终端奖励项组成，控制器以规划轨迹为参考进行深度强化学习训练。

### 三、结果（Result）
仿真结果表明，所提框架能够使智能体学习到一种漂移比赛策略，既保证了车辆运动控制性能（如稳定跟踪大质心侧偏角状态），又有效减少了单圈时间。对比不采用分层课程引导或缺少MLT先验轨迹的基线方法，TgRL显著提升了训练稳定性与最终圈速表现，验证了从规划到控制的分层架构在极限漂移场景中的有效性。

### 四、结论（Conclusion）
本文通过将最优控制生成的MLT漂移规划轨迹与轨道引导的分层强化学习控制器相结合，解决了漂移稳定控制与最小化单圈时间的双重难题。三阶段渐进训练策略使得智能体能够从基础漂移控制逐步掌握完整比赛策略，同时无需高成本专家示范数据。该框架为极限工况下自动驾驶赛车提供了可行的规划-控制解决方案，并为未来向实车迁移奠定了基础。

### 五、方法论与关键技术细节
关键实现细节包括：采用低附着路面μ=0.6模拟光滑赛道，车辆参数为质量1300kg、轴距前后各1.4m、横摆惯量1750kg·m^2；MLTDP以单圈时间最小化为目标，在OCP中施加道路边界、状态和输入约束，生成用于RL训练的参考轨迹；TgRL的课程式训练分为基础漂移控制、漂移过弯和完整比赛策略三个阶段，奖励由即时轨迹跟踪误差项与MLT终端奖励组成。该方法的局限性在于目前仅在仿真环境验证，且对规划参考轨迹质量与车辆模型精度有一定依赖，未来需进一步研究sim-to-real迁移及更复杂多变路况下的泛化能力。
