# Conflict Resolution under Degraded Surveillance in Air Corridors Using Multi-Agent Reinforcement Learning

- 区域：精读区
- 排名：1
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Esrat Farhana Dulia, Syed Arbab Mohd Shihab, Caleb Adams, Ruben Del Rosario
- 机构：Kent State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20547v1) · [PDF](https://arxiv.org/pdf/2607.20547v1)

## TLDR
This paper develops a Deep Q-Network-based Multi-Agent Reinforcement Learning framework for decentralized conflict resolution among heterogeneous small UAVs and eVTOL aircraft under degraded surveillance conditions in structured three-dimensional corridors.

## Abstract
Safe Advanced Air Mobility operations require aircraft to maintain separation when surveillance information is noisy, delayed, incomplete, or temporarily unavailable. This study develops a Deep Q-Network-based Multi-Agent Reinforcement Learning framework for decentralized conflict resolution among heterogeneous small unmanned aerial vehicles and electric vertical takeoff and landing aircraft operating within a structured three-dimensional corridor. Separate policies are trained for the two aircraft categories using local observations and a 14-action space that includes maintaining course, turning, vertical maneuvering, landing, and speed control. The simulation incorporates aircraft-specific dynamics, energy use, corridor constraints, observation noise, communication delay, information dropout, wind disturbance, actuator uncertainty, and model uncertainty. The trained policies are evaluated across 90 combinations of traffic density and minimum separation thresholds. Loss-of-separation frequency and duration generally increase with traffic density and separation requirements, although most events are resolved within 1s. Under safe conditions, agents maintain their motion approximately 79% of the time. During conflicts, turning accounts for 33% of actions, followed by maintaining motion at 29%, speed control at 25%, and vertical maneuvers at 13%. Six Pareto-optimal configurations reveal trade-offs between safety and corridor capacity. The framework supports the simulation-based evaluation of safer AAM conflict-resolution strategies under degraded surveillance conditions.


## 精读解读（中文）
### 一、研究动机
安全先进空中机动（AAM）操作要求飞行器在监视信息噪声、延迟、不完整或暂时不可用时保持间隔。现有方法在降级监视条件下处理异构飞行器冲突解决存在不足，尤其是小型无人机和电动垂直起降飞行器在结构化三维走廊中的协调问题。

### 二、技术方案（Method）
基于深度Q网络的多智能体强化学习框架，为异构小型无人机和电动垂直起降飞行器分别训练分散式冲突解决策略。仿真环境包含结构化三维走廊（具有独立高度层、定向交通流、巡航车道和超车道），引入观测噪声、通信延迟、信息丢失、风干扰、执行器不确定性和模型不确定性来模拟降级监视。状态空间包括自机状态和邻近飞行器观测信息，动作空间包含14种离散动作（保持航向、转弯、垂直机动、着陆和速度控制）。采用DQN算法，通过经验回放和目标网络训练策略，奖励函数综合考虑安全间隔、走廊保持、方向遵守和能量消耗。

### 三、结果（Result）
在90种交通密度与最小间隔阈值组合下评估，间隔丢失频率和持续时间随交通密度和间隔要求增加，但大多数事件在1秒内解决。安全条件下智能体约79%时间保持运动；冲突期间转弯占33%、保持运动29%、速度控制25%、垂直机动13%。识别出六种帕累托最优配置，揭示安全性与走廊容量之间的权衡。

### 四、结论（Conclusion）
该基于DQN的多智能体强化学习框架能够在降级监视条件下实现异构飞行器的分散式冲突解决，并支持对更安全AAM冲突解决策略进行仿真评估。

### 五、方法论与关键技术细节
关键点包括：14动作空间涵盖保持、转弯、垂直机动、着陆和速度控制；为UAV和eVTOL分别训练独立策略；仿真中集成了观测噪声、通信延迟（最大τ_max）、信息丢失（概率P_drop）、风干扰、执行器不确定性、模型不确定性以及基于功率模型的能量消耗；走廊约束包括边界和方向规则；训练使用DQN，经验回放和目标网络；评估涵盖90种交通密度与间隔阈值组合；局限性包括固定动作空间、未考虑连续机动以及eVTOL和UAV类别内的异构性。
