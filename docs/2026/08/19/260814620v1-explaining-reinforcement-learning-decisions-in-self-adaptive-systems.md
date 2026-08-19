# Explaining Reinforcement Learning Decisions in Self-adaptive Systems

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Jasmina Gajcin, Juan C. Rosero, Ivana Dusparic
- 机构：Trinity College Dublin
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14620v1) · [PDF](https://arxiv.org/pdf/2608.14620v1)

## TLDR
EARL is a Python library that generates counterfactual "what-if" explanations for reinforcement learning decisions in self-adaptive systems, demonstrated on a CitiBikes bike-sharing simulation to improve transparency and user trust.

## Abstract
Reinforcement Learning (RL) has been extensively used in autonomous and self-* systems, but RL policies, especially deep RL ones relying on neural networks, lack transparency and are difficult to understand. This can lead to diminished user trust, and makes for a more challenging verification of systems. To address this challenge, this paper introduces Explanations using Alternative Realities for Reinforcement Learning (EARL), a Python library to produce counterfactual explanations in RL settings. This library allows the user to produce explanations by exploring What-if scenarios to clarify agent behavior by comparing possible outcomes. Counterfactual explanations have been shown to be intuitive and user-friendly in psychology research, but have only recently been explored in RL, with existing implementations usually limited to toy examples and benchmarks. EARL supports counterfactual explanation generation in realistic RL-based self-adaptive systems. To demonstrate its applicability, we demonstrate its use in a simulation of CitiBikes, a self-adaptive bike-sharing system, and we provide evaluations showing how it performs in real applications.


## 精读解读（中文）
### 一、研究动机
深度强化学习策略在自适应系统中缺乏透明度，导致用户信任降低并增加系统验证难度；现有XRL方法多面向开发者，依赖低层可视化或全局近似，不便于非专家理解。反事实解释在心理学和监督学习中已被证明直观有效，但在RL中研究较少，且现有实现多局限于玩具环境，缺少支持真实RL自适应系统的统一开源工具。因此本文提出EARL库，用于在RL场景中生成反事实解释。

### 二、技术方案（Method）
EARL是一个模块化Python库，包含解释方法、模型包装器、评估接口以及DQN/PPO默认实现。解释方法模块集成了四种反事实生成算法：GANterfactual-RL（基于StarGAN的域转移，提供非图像版本）、RACCER-HTS（启发式树搜索）、RACCER-Advance（NSGA-II从当前状态搜索未来动作序列）和RACCER-Rewind（NSGA-II修改过去动作序列）。模型包装器为不同RL模型提供统一接口，使解释方法无需修改即可调用智能体动作和决策指标；评估接口计算覆盖率、生成时间、相似性、可行性和多样性。在CitiBikes案例中，环境包含5个站点、38维状态特征，动作为多离散的源站/目标站/转移车辆数；先训练PPO黑盒策略，再通过自定义generate_obs、set_nonstoch_state等环境修改实现任意中间状态重置，最后对100个高信息量状态生成反事实解释。

### 三、结果（Result）
在CitiBikes仿真环境中，EARL成功为RL智能体的重定位决策生成反事实解释，展示了策略会从车辆返还较多的站点S2/S5向高需求站点S3/S4调度车辆，其中S4接收车辆最多且主要来自S2。四种反事实生成方法均可在该真实规模任务上运行；通过覆盖率、生成时间、特征相似性、可行性和多样性等指标，能够对不同方法进行统一比较和评估，证明EARL适用于非玩具级别的RL自适应系统。

### 四、结论（Conclusion）
EARL填补了RL反事实解释缺少统一可扩展开源库的空白，通过统一接口、模型包装器和评估框架，将原本局限于简化环境的反事实方法扩展到真实自适应系统。CitiBikes案例表明该库能够生成直观、用户友好的反事实解释，有助于提升用户信任、支持系统验证，并为进一步研究提供了可复现的实验基础。

### 五、方法论与关键技术细节
关键细节包括：CitiBikes环境状态特征共38维，覆盖站点车辆数、容量、天气、日类型、履约率、短缺、失败归还和行程需求等；动作空间为MultiDiscrete([num_stations, num_stations, max_bike_transfer])。奖励函数为R=-100*bike_shortage-0.01*n，即强烈惩罚短缺且轻微惩罚车辆转移。GANterfactual-RL的生成器结构为[128,128,128]，判别器为[256,256]，生成器与判别器学习率均为1e-4，训练数据规模5e5，训练timesteps为1000；RACCER-HTS迭代300次；RACCER-Advance和RACCER-Rewind设置24代、种群大小100。RACCER系列优化三个目标：最小化原状态到反事实状态之间的动作步数、保证路径在解释策略下具有高概率、降低随机环境中的不确定性。可行性约束包括站点存储车辆不超过容量、站点不能借出超过容量的车、站点短缺量不超过容量。局限性方面，GANterfactual-RL仅基于转移数据集，不考虑环境时序和随机性；RACCER需要访问执行环境；目前评估基于有限状态集，且未做用户主观研究，后续可扩展更多方法和真实部署场景。
