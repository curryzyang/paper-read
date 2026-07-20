# Co-Design of Aeroelastic Systems with Deep Reinforcement Learning

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Yao Cheng Li, Urban Fasel
- 机构：Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15329v1) · [PDF](https://arxiv.org/pdf/2607.15329v1)

## TLDR
This paper presents a model-free nested co-design framework using deep reinforcement learning to jointly optimize aeroelastic system design and control, demonstrating improved performance across three case studies, including a flexible glider performing thermal soaring under uncertainty.

## Abstract
Control co-design considers the physical system and its controller together, enabling the strong coupling between system design and control to be uncovered and exploited. This is especially relevant in aeroelastic flight systems, where structural, aerodynamic, and control design choices jointly determine manoeuvrability and efficiency. This paper presents a model-free nested co-design framework for aeroelastic systems using deep reinforcement learning, in which a design-conditioned control policy is trained with proximal policy optimisation while an outer loop updates a distribution over candidate design parameters. The approach is evaluated on three case studies of increasing complexity: a spring-mass-damper system, a pitch-plunge-flap aerofoil, and a highly flexible high-aspect-ratio glider performing a thermal-soaring mission in a stochastic environment. Across these case studies, the framework is shown to progressively concentrate the design search towards high-performing regions and to outperform policies trained on randomly sampled designs. The results also show that reward shaping plays an important role in enabling stable learning in partially observed and stochastic environments. In the final glider case, the method jointly addresses wing design, flight control, and mission-level behaviour in the presence of aeroelastic coupling and atmospheric uncertainty. These results highlight the potential of model-free co-design for complex aeroelastic systems in which design, control, and mission objectives are tightly coupled.


## 精读解读（中文）
### 一、研究动机
气动弹性飞行系统中结构、气动与控制设计强耦合，共同决定机动性与效率，但传统方法常将系统设计与控制分开优化，无法充分发掘耦合潜力。本研究旨在利用深度强化学习开发一种模型自由的嵌套协同设计框架，用于联合优化高展弦比柔性滑翔机的气动弹性设计、飞行控制与任务行为，特别是在热力翱翔这一高不确定性与部分观测环境中。

### 二、技术方案（Method）
方法采用嵌套协同设计框架：外层循环维护一个多元高斯分布作为候选设计参数的先验，每次迭代从分布中采样设计参数并分配给多个并行环境；内层循环使用近端策略优化算法训练一个以设计参数为条件的控制策略，该策略在给定状态和设计参数下输出动作，并在每个环境中收集轨迹。内层循环进行N_inner次PPO更新（不训练至收敛以降低计算成本），然后外层根据累计奖励更新设计参数分布（通过性能加权或剪枝机制将搜索聚焦于高性能区域）。框架在三个复杂度递增的案例上评估：弹簧-质量-阻尼器、俯仰-沉浮-襟翼翼型以及一个在随机热力场中执行热力翱翔任务的高柔性高展弦比滑翔机。其中滑翔机模型使用Mujoco实现低保真度但完全参数化的气动弹性动力学仿真。

### 三、结果（Result）
在三个案例中，所提框架均能逐步将设计搜索集中在高性能区域，且训练出的设计条件策略显著优于基于随机采样设计训练的策略。在滑翔机案例中，框架成功联合优化了机翼设计（如展弦比、刚度）、飞行控制策略与任务级热力搜索行为，展示了在气动弹性耦合与大气不确定性下的稳健性能。实验还表明，奖励塑造对于在部分观测和随机环境中实现稳定学习至关重要，缺失中间导向奖励时策略容易陷入局部最优。

### 四、结论（Conclusion）
本研究证明模型自由的嵌套协同设计框架能够有效解决气动弹性系统中的强耦合优化问题，将系统设计、控制与任务目标统一优化。该方法在热力翱翔场景中取得了优于分离设计的效果，为高柔性飞行器的敏捷与高效设计提供了新途径。未来工作可扩展至更高保真度模型、多任务场景以及与其他优化范式（如贝叶斯优化）的结合。

### 五、方法论与关键技术细节
关键细节包括：设计参数维度随案例增加，滑翔机案例中涉及机翼展弦比、弯曲刚度、扭转刚度等连续参数；初始设计分布为多元高斯，外层更新采用基于性能的加权最大似然估计（类似期望最大化），每次外环迭代剪枝低性能分布以加速收敛；PPO超参数如裁剪因子ε=0.2、学习率3e-4、步长N_step=2048、内环迭代N_inner=80、并行环境数N_env=8；奖励塑造在滑翔机案例中引入高度改变惩罚和热力接近奖励以引导探索；局限性包括模型依赖低保真度仿真（忽略高阶气动弹性效应）、模型自由方法的高样本复杂度、以及奖励函数设计需要领域知识。计算复杂度方面，内环不训练至收敛显著降低了总训练步数，但总交互样本量仍达到千万量级。
