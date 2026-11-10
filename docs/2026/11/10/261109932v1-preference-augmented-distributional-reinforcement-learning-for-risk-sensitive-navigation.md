# Preference-Augmented Distributional Reinforcement Learning for Risk-Sensitive Navigation

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Zhaofan Zhang, Yue Chang, Rufeng Chen, Hechang Chen, Sihong Xie, Hui Xiong
- 机构：The Hong Kong University of Science and Technology (Guangzhou), The Hong Kong University of Science and Technology, Jilin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.09932v1) · [PDF](https://arxiv.org/pdf/2611.09932v1)

## TLDR
The paper proposes PAIQN, a preference-augmented distributional reinforcement learning method that represents risk preferences as quantile-weight distributions, trains with diverse preference-guided exploration, and deploys a distributionally robust conservative policy to improve risk-sensitive navigation by reducing collisions and increasing task success.

## Abstract
Ensuring safe and reliable navigation under diverse sources of uncertainty remains a central challenge for autonomous systems. Within distributional reinforcement learning (DistRL), Implicit Quantile Networks (IQN) have attracted interest for navigation under uncertainty because they enable risk adaptation through flexible quantile sampling. Existing approaches, however, typically use a fixed or randomly sampled Conditional Value-at-Risk (CVaR) level during training and adjust the risk level during deployment using hand-tuned hyperparameters or external sensor signals. This scalar-CVaR formulation confines learning to a narrow family of tail-risk preferences, creating a mismatch between training-time preference exposure and deployment-time risk adjustment. We instead represent variations in risk preference as shifts in quantile-weight distributions and expose the agent to diverse preferences through preference-guided exploration. At deployment, we optimize against the worst-case preference distribution to derive a conservative policy that accounts for multiple risk profiles. This reduces hyperparameter tuning and reliance on limited sensor signals under partial observability. Experiments across simulated environments and vehicle platforms show that our method reduces collisions while improving task success.


## 精读解读（中文）
### 一、研究动机
现有基于分布强化学习与IQN的风险敏感导航方法通常在训练时使用固定或随机采样的标量CVaR水平，并在部署时依靠手工超参数或外部传感器信号调整风险水平，导致训练期偏好暴露与部署期风险适应不匹配。标量CVaR还把学习限制在狭窄的尾部风险偏好族内，难以在部分可观测和潜在环境不确定性下可靠推断合适的保守程度。

### 二、技术方案（Method）
本文将风险偏好表示为分位数权重分布而非单一CVaR参数：训练时从Dirichlet分布采样权重，并通过随全局交互步退火的偏差项构造非均匀分位数权重，将其用于偏好贪婪动作选择，并与epsilon随机探索结合；在构造Bellman目标时也独立采样偏好权重以选择目标动作，但目标回报分位数与IQN分位Huber损失保持不变。部署时将分位数权重分布视为不确定量，在偏好分布模糊集上做分布鲁棒优化，以最坏偏好分布评估动作并得到保守策略。

### 三、结果（Result）
在多个模拟导航环境和不同车辆平台上的实验表明，PAIQN相较IQN在含障碍与阴影涡流等不确定场景中降低碰撞率并提高任务成功率，且在多数评估风险偏好设置下能够成功导航。理论分析给出偏好加权引入的Bellman误差上界随退火参数趋于零而消失，说明训练期偏好扰动不会造成持续的方向性偏差。

### 四、结论（Conclusion）
PAIQN通过分位数权重分布统一了训练期的多样风险偏好暴露与部署期的鲁棒保守决策，减少了对固定CVaR映射和有限传感器信号的依赖，从而提升部分可观测环境下风险敏感导航的安全性与任务成功率。

### 五、方法论与关键技术细节
实现上使用K个固定中点分位数，Dirichlet浓度b控制偏好形状，退火偏差采用Delta_t=Delta_0 max(t,1)^-(1+eta)，epsilon按线性调度退火；偏好权重在同一状态的所有候选动作间共享，目标动作使用独立采样的偏好权重但不对目标回报重新加权。理论界为||Q_{t+1}-Q*||<=gamma||Q_t-Q*||+gamma D/K+2gamma D Delta_t，其中D=(r_max-r_min)/(1-gamma)，需Delta_t<=1且依赖理想化同步Bellman更新等假设；实验细节与真实部署限制在可见文本中未完全展开。
