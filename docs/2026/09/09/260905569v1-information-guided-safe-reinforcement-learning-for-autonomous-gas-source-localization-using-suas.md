# Information-Guided Safe Reinforcement Learning for Autonomous Gas Source Localization using sUAS

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Sachin Giri, Thomas Zhao, Matthew Huynh, YangQuan Chen
- 机构：University of California, Merced
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05569v1) · [PDF](https://arxiv.org/pdf/2609.05569v1)

## TLDR
A paper introduces an Information-Guided Safe Reinforcement Learning framework that combines a classical empirical observability Gramian planner with learned Soft Actor-Critic exploration—managed by a KL-divergence meta-supervisor and safeguarded by a Robust Control Barrier Function—to break the Gramian bias in airborne gas source localization, achieving ~80% localization success in GPU-accelerated turbulent simulations versus ~30% for classical baselines with zero safety violations.

## Abstract
The autonomous localization of fugitive gas emissions using small Unmanned Aircraft Systems (sUAS) constitutes a fundamentally ill-posed inverse problem. In turbulent atmospheric boundary layers, highly intermittent scalar concentration fields violate the assumptions of classical gradient-based navigation, causing data-driven estimators to suffer from severe noise and spurious local minima. To address these challenges, we introduce an Information-Guided Safe Reinforcement Learning framework evaluated within a custom, GPU-accelerated 3D simulation environment coupling an Eulerian wind solver with a Lagrangian puff dispersion model. We identify a critical vulnerability in deterministic information-seeking planners - a Gramian bias where agents act greedily upon flawed early estimates, starving the estimator of spatial diversity. To systematically break this degeneracy, our architecture integrates a classical empirical observability Gramian (EMGR) planner with a learned Soft Actor-Critic (SAC) exploratory policy. A deterministic meta-supervisor actively monitors estimator reliability via Kullback-Leibler (KL) divergence, dynamically blending deterministic exploitation with learned exploration to steer the sUAS into high-information zones. Trained via a progressive curriculum and safeguarded by a strictly enforced Robust Control Barrier Function (RCBF), our RL framework achieves nearly 80% localization success on complex, mobile sources - drastically outperforming classical baselines (~30%) - while ensuring zero safety violations.


## 精读解读（中文）
### 一、研究动机
自主定位 fugitive gas emissions 是一个病态逆问题，在湍流大气边界层中高度间歇的标量浓度场使传统梯度导航失效，数据驱动估计器易受严重噪声和虚假局部最小值干扰。确定性信息搜索规划器存在 Gramian 偏差，即代理对早期错误估计的贪婪利用会耗尽估计器的空间多样性，从而陷入停滞。需要一种安全且信息引导的强化学习框架来平衡确定性开发与探索，主动正则化该病态逆问题，并保证实际部署的安全性。

### 二、技术方案（Method）
提出 Information-Guided Safe RL 框架，在 GPU 加速 3D 仿真环境中训练，该环境耦合欧拉风场求解器（Stable Fluids、红黑 SOR、Ornstein-Uhlenbeck 过程）与拉格朗日高斯 puff 扩散模型以还原间歇性羽流结构。架构上，将经典经验可观测性 Gramian（EMGR）规划器与学习型 Soft Actor-Critic（SAC）探索策略相结合，由确定性元监督器通过在线 KL 散度监测估计器可靠性，动态混合确定性 EMGR 速度与 SAC 探索动作，引导无人机进入高信息区。估计器采用 MLE（投影相关加 Grünwald-Letnikov 分数阶滤波）和粒子滤波器保持假设多样性。训练采用渐进课程，并用鲁棒控制障碍函数（RCBF）求解 QP 将混合策略映射到严格安全动作空间，考虑最坏情形扰动；输入为浓度测量、位置和风场数据，输出为安全导航速度。

### 三、结果（Result）
在复杂移动源场景中，所提框架达到近 80% 的定位成功率，而经典 EMGR 基线仅约 30%，同时实现零安全违规。对比实验表明，纯确定性信息规划存在 Gramian 偏差，而加入 SAC 探索与 RCBF 安全约束的混合策略能显著提升成功率并保证安全，展示了学习型探索对打破估计退化的有效性。

### 四、结论（Conclusion）
信息引导的安全 RL 框架能够有效解决湍流环境下气体源定位的病态逆问题，通过元监督器动态平衡 EMGR 开发与 SAC 探索，并用 RCBF 严格保障安全，显著优于经典基线。GPU 加速仿真平台结合真实感流动模型缩小了 sim-to-real 差距，为实际 sUAS 甲烷泄漏定位提供了可行方案。

### 五、方法论与关键技术细节
关键实现细节：仿真环境使用 NVIDIA Warp，Eulerian 风场采用 Stable Fluids 算子分裂、Helmholtz-Hodge 投影和红黑 SOR 求解 Poisson 方程，地面边界为无穿透并施加局部阻力，障碍物内部速度清零；Lagrangian puff 模型使用 RK2 积分和 Langevin 噪声，pasquill-Gifford 稳定度类决定扩散系数，甲烷浮力加速度约 4.55 m/s²，地面采用镜像法满足无通量条件。观测量为传感器浓度，噪声为高斯；MLE 采用滑动窗口投影相关目标，并用阶次 α∈[-0.9,0] 的分数阶滤波处理风历史；粒子滤波在 ESS 过低时进行系统重采样。KL 散度监测使用缓冲长度 N_b，用于切换开发与探索。RCBF 安全层通过 QP 求解，假设最坏情况扰动，每个时间步执行。训练采用渐进课程提高任务难度。局限性：结果基于仿真，真实硬件验证尚未报告；方法依赖环境模型精度，且需更多真实风场验证约 30% 的经典基线对比条件。
