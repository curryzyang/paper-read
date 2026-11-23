# Latent Space Planning with Sequential Monte Carlo

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Hrishikesh Viswanath, Anindita Ghosh, Uttaran Bhattacharya, Aniket Bera
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26706v1) · [PDF](https://arxiv.org/pdf/2611.26706v1)

## TLDR
The paper proposes an SMC-guided latent-space planner that evolves a population of action sequences alongside gradient-based plan updates and uses a PDE-derived cost-to-go over the latent state space, outperforming gradient-based, sampling-based, and MPPI planners on visual and proprioceptive navigation and manipulation tasks.

## Abstract
Planning with learned world models amounts to finding action sequences whose predicted rollouts reach a goal. Sampling-based planners often struggle at longer horizons, while gradient-based methods can become trapped in local minima. Meanwhile, model predictive path integral control (MPPI), a complementary approach, alternates between estimating an expectation under a cost-weighted distribution from samples and updating the plan from this estimate. Its samples, however, are drawn afresh at every iteration from a Gaussian proposal and reach the target distribution only through importance weights. Moreover, a target distribution favoring goal-reaching trajectories can be difficult to define directly, motivating a sequence of intermediate distributions. Sequential Monte Carlo (SMC) provides a natural mechanism for evolving such a sequence through importance weighting and resampling. Motivated by this, we formulate latent-space planning as optimization guided by SMC, which moves a population of action sequences while a gradient-based optimizer updates the plan. Inspired by classical planning, we further introduce a PDE-derived cost-to-go that guides the evolution of the sample distribution using the structure of the latent state space. On navigation and manipulation tasks with visual and proprioceptive world models, our formulation outperforms gradient-based planners by $29$ and $50$, sampling-based planners by $35$ and MPPI by $7$ percentage points in average success rate, while succeeding in fewer iterations than gradient-based planners and within 4\% of MPPI.


## 精读解读（中文）
### 一、研究动机
基于学习世界模型的规划本质是搜索能使预测轨迹到达目标的操作序列。采样规划器在较长时域上容易失效，梯度方法则可能陷入局部极小；MPPI虽交替进行代价加权期望估计与规划更新，但每轮从高斯提议重新采样，仅靠重要性权重逼近目标分布，且直接定义偏好目标到达的目标分布较困难，因此需要一串中间分布。

### 二、技术方案（Method）
本文将潜空间规划表述为由序贯蒙特卡洛（SMC）引导的优化：维护一组操作序列种群，通过重要性加权与重采样沿中间分布序列演化，同时用基于梯度的优化器更新规划。受经典规划启发，引入由PDE推导的cost-to-go，利用潜状态空间结构引导样本分布演化。在带视觉与本体检知世界模型的导航和操作任务上，将所提方法与梯度规划器、采样规划器和MPPI进行对比。

### 三、结果（Result）
在导航与操作任务上，所提方法平均成功率相较梯度规划器高29和50个百分点、相较采样规划器高35个百分点、相较MPPI高7个百分点；同时达到成功所需迭代次数少于梯度规划器，并与MPPI的迭代次数相差在4%以内。

### 四、结论（Conclusion）
将SMC的种群演化与梯度规划更新结合，并利用潜空间结构构造PDE导出的cost-to-go，可显著提升世界模型潜空间规划的成功率与迭代效率，说明序贯中间分布和结构化代价引导是改善长时域目标到达规划的有效途径。

### 五、方法论与关键技术细节
关键实现包括：以操作序列种群为SMC样本，通过重要性权重和重采样实现中间分布序列演化；以梯度优化器持续更新规划；用PDE导出的cost-to-go依据潜状态空间结构引导样本分布。实验覆盖视觉与本体检知世界模型下的导航和操作任务，比较梯度规划、采样规划和MPPI，指标为平均成功率与迭代次数。局限在于方法依赖学习到的潜世界模型及cost-to-go构造，SMC种群、重采样和PDE代价会带来计算/内存开销与超参调节需求；摘要未给出具体网络架构、损失、种群规模、分布调度和精确迭代数。
