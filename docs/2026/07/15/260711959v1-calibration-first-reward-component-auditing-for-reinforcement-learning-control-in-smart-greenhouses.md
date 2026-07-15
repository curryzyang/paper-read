# Calibration-First Reward-Component Auditing for Reinforcement Learning Control in Smart Greenhouses

- 区域：精读区
- 排名：9
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Yuhui Bie, Guowei Xu, Yaojun Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11959v1) · [PDF](https://arxiv.org/pdf/2607.11959v1)

## TLDR
The paper proposes a reproducible calibration-first reward-component audit framework for greenhouse reinforcement learning that decomposes scalar rewards into interpretable named components (temperature, CO₂, humidity, screen, actuation) and validates their learnability, simulator calibration, and comparability across logged greenhouse data to make learned controller behavior inspectable before deployment.

## Abstract
Greenhouse reinforcement learning can test climate-control ideas at a speed and scale that is difficult to achieve with crop experiments alone. For smart-greenhouse control, however, a single simulator return is not enough: a grower or control engineer also needs to know when the policy heats, enriches CO2, vents, manages humidity, deploys screens, or uses lamps.We propose a reproducible calibration-first reward audit framework that keeps named greenhouse-control reward components comparable across simulator training, facility-adapted rollouts, logged Autonomous Greenhouse Challenge records, and actuator-rule distillation. In GreenLight-Gym, the framework decomposes the scalar reward into conditional temperature, CO2, humidity and vapor-pressure-deficit, screen, and actuation-proxy terms; adapts GreenLight to the second Autonomous Greenhouse Challenge logged climate traces; and scores the same components on logged greenhouse data.


## 精读解读（中文）
### 一、研究动机
温室强化学习中的单一模拟器回报难以解释，种植者或控制工程师需要知道策略如何获得回报，例如加热、CO2富集、通风、湿度管理、遮阳幕和补光等具体操作。现有研究缺乏一个可重复的奖励组件审计框架，无法确保奖励组件在模拟器训练、设施适应滚动、自主温室挑战日志和执行器规则蒸馏之间保持可比性。

### 二、技术方案（Method）
提出一个校准优先的奖励组件审计框架。首先，将GreenLight-Gym的标量奖励分解为七个命名组件：温度舒适、温度方向、CO2方向、湿度/饱和水汽压差、光照、遮阳幕和执行代理。其次，使用第二届自主温室挑战赛（AGC2）的47,809行天气数据和23,910行动/目标数据对GreenLight模拟器进行校准，通过阻挡验证改进状态预测准确性，搜索24个候选参数并以归一化RMSE之和为优化目标。然后，使用PPO训练策略，训练奖励为0.7原始GreenLight-Gym奖励与0.3诊断性物理先验奖励（七组件加权和）的混合，固定权重且不针对AGC结果调整。最后，在模拟器滚动、校准后模拟器滚动以及AGC1、AGC2、AGC4日志上计算相同组件，并通过深度为4的决策树蒸馏分析执行器行为的规则保真度。

### 三、结果（Result）
九个500k步PPO运行全部超过规则控制器基线。校准后模拟器在七个验证上下文中平均温度RMSE降低0.6°C、相对湿度RMSE降低4.3个百分点、CO2 RMSE降低563 ppm。奖励组件距离在时间步和日累计尺度上均减小，Wasserstein-1距离从0.01677降至0.01389（时间步）和1.19748降至0.97708（日累计）。物理先验奖励下，热屏、补光和遮光屏的浅层树规则保真度分别从0.652、0.631、0.592提高到0.835、0.838、0.750。AGC黄瓜产量排名与条件复合先验组件之间的Spearman相关系数为0.771（p=0.072，精确置换检验，六团队）。

### 四、结论（Conclusion）
该框架提供温室RL部署前的诊断层，能够报告策略如何获得奖励、模拟器校准如何改变结论、以及哪些作物或执行器通道需要检查。结果支持奖励组件审计作为部署前诊断工具，而非现场产量改进证据，强调在设施特定控制器试验前检查校准目标。

### 五、方法论与关键技术细节
关键点包括：使用PPO训练，超参遵循默认设置但未针对AGC优化；奖励混合比例0.7/0.3固定，组件权重均为1；校准使用AGC2数据，包含47,809天气行和23,910行动/目标行，搜索24个候选参数，验证目标为归一化RMSE（温度20°C、相对湿度20个百分点、CO2 500 ppm），且设置温度RMSE退化不超过0.5°C的守卫条件；局限性在于校准效果在个别通道上不均匀（62/112上下文改善），AGC产量相关性基于小样本团队（AGC1仅6团队），统计效力不足，且组件距离改善在行级别仅为55.4%。
