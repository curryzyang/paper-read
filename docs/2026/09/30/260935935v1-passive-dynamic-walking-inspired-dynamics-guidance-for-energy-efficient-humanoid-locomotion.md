# Passive-Dynamic-Walking-Inspired Dynamics Guidance for Energy-Efficient Humanoid Locomotion

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Hyeonjin Choi, Joongheon Kim, Daekyum Kim
- 机构：Korea University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35935v1) · [PDF](https://arxiv.org/pdf/2609.35935v1)

## TLDR
The paper proposes a passive-dynamic-walking-inspired reinforcement learning framework that temporarily uses tilted-gravity, slope-equivalent guidance during early training and then removes it, enabling a 29-DoF Unitree G1 humanoid to achieve 6.8–15.2% lower mechanical cost of transport while preserving velocity tracking.

## Abstract
Learning energy-efficient humanoid locomotion requires discovering mechanically economical gait coordination, not merely reducing actuator effort. Reinforcement learning promotes efficiency through effort-related reward penalties, which guide the step-to-step mechanics of walking only indirectly. This article proposes a framework inspired by passive dynamic walking (PDW) that temporarily creates slope-equivalent conditions favorable to economical gait discovery and removes all PDW-specific guidance before nominal-dynamics optimization. During early training, a tilted-gravity field assists sagittal progression on flat collision geometry, complemented by curriculum-coupled reward terms. The core framework requires no reference trajectories, gait phases, or contact schedules. In a five-seed forward-locomotion study on a 29-DoF Unitree G1, the framework reduces mechanical cost of transport by 6.8-15.2% over commanded speeds of 0.5-2.0m/s without degrading velocity tracking. Mechanical-work decomposition attributes the reduction to positive actuator work, and reward-matched comparisons separate the guided regime's faster gait acquisition from the tilt's additional benefit to converged economy. The framework extends to unassisted omnidirectional locomotion, where its benefit persists once a walking-specific motion prior supplies kinematic coordination, the combination reducing speed-matched cost of transport by 18.7%. On hardware, forward cost of transport falls by 16.3% with the motion prior and by 4.5% without it, the latter within the trial-to-trial spread.


## 精读解读（中文）
### 一、研究动机
学习节能人形机器人步态的关键不只是降低执行器出力，而是要发现机械上经济的步态协调；现有强化学习多通过出力/平滑惩罚间接影响步态力学，而运动模仿先验又在运动学空间评分，难以直接对应机器人执行器功。受被动动态行走启发，本文希望在早期策略搜索中临时创造有利于经济步态发现的等效下坡条件，并在名义动力学优化前移除全部PDW特定引导，从而偏置最终无辅助策略。

### 二、技术方案（Method）
该框架在平坦碰撞几何上，通过命令条件化的虚拟倾斜重力场在早期训练中提供等效下坡的矢状面推进助力；训练分三阶段：Phase 1全倾斜、PDW奖励激活且命令以矢状为主，Phase 2倾斜线性衰减、PDW奖励按同一课程因子σ(k)缩放并扩展到全向命令，Phase 3移除所有PDW特定引导并在名义平地动力学和基线目标下优化。核心框架无需参考轨迹、步态相位或接触时序；基线目标仍包含速度跟踪、稳定性/姿态/关节运动/动作平滑/不良接触/执行器出力的正则。方向依赖倾斜角由θ(k)=θ_init σ(k)与前后倾比ρ=sinθ_back/sinθ_init给出，默认θ_init=5°，K_w=150、K_t=200；AMP作为独立因子可全程启用。仿真在29-DoF Unitree G1上进行5种子前向实验、2×2课程×AMP全向实验和硬件验证。

### 三、结果（Result）
在29-DoF Unitree G1五种子前向仿真中，该方法在0.5–2.0 m/s指令速度范围内将机械运输成本降低6.8–15.2%，且不损害速度跟踪；机械功分解显示收益主要来自正执行器功减少。奖励匹配对照将引导期更快的步态获得与倾斜对收敛后经济性的额外收益区分开。扩展到无辅助全向运动时，若加入步态专用运动先验提供运动学协调，组合条件将速度匹配运输成本降低18.7%。硬件上前向运输成本在含运动先验时下降16.3%，不含时下降4.5%，后者处于试次间波动范围内。

### 四、结论（Conclusion）
结论是，临时施加PDW启发的动力学引导可以偏置最终无辅助策略，使其收敛到更经济的步态，而不仅是加速技能获得；该方法与AMP式运动先验互补，且核心框架不需要参考轨迹、步态相位或接触时间表。其意义在于通过改变早期策略搜索所经历的动力学条件，为节能人形运动学习提供一条独立于奖励塑形和运动学模仿的机制。

### 五、方法论与关键技术细节
关键实现点包括：训练在平坦碰撞几何上使用命令条件化虚拟倾斜重力场，仅沿偏航对齐的矢状轴提供前向助力，横向运动靠命令课程而非旋转下坡方向；PDW奖励与倾斜按σ(k)同步退火，三阶段结束后全部移除。输入为平面速度/偏航率命令与29-DoF机器人状态，输出为关节动作，使用PPO类策略优化，基线奖励含执行器出力正则；核心方法不依赖参考轨迹、步态相位或接触时序。可调超参包括初始/后向倾斜角θ_init、θ_back、K_w、K_t及奖励权重，论文默认θ_init=5°、K_t=200、全向K_w=150，并做了初始角敏感性分析。主要局限是倾斜仅提供矢状面协助且碰撞几何保持水平，硬件上无运动先验的4.5%收益落在试次波动内，运动先验的加入对全向和硬件效果重要，设计参数和sim-to-real仍需调参。
