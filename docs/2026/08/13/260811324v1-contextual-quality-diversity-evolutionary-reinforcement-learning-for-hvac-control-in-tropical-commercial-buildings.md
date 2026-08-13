# Contextual Quality-Diversity Evolutionary Reinforcement Learning for HVAC Control in Tropical Commercial Buildings

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Tran Le Vu
- 机构：Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11324v1) · [PDF](https://arxiv.org/pdf/2608.11324v1)

## TLDR
CQD-ERL is a contextual quality-diversity evolutionary reinforcement-learning controller for tropical HVAC systems that maintains an archive of regime-specialized policies via evolutionary and soft actor-critic operators with a safety shield, outperforming the ASHRAE Guideline 36 baseline in annual backtests.

## Abstract
This paper proposes a contextual quality-diversity evolutionary reinforcement-learning controller, CQD-ERL, for the supervisory control of a tropical, water-cooled chiller plant and its associated air side. Rather than converging to a single scalarised policy, the controller maintains a product archive of specialised policies indexed jointly by a data- driven operating context, a cluster of daily weather and load regime, and a context-invariant behaviour descriptor, filled by a gradient-free evolutionary operator and a soft-actor-critic policy-gradient operator that share one replay buffer. Every action is filtered through a deterministic safety shield before execution. The controller is trained on a two-tier reduced-order environment representing the latent load, cooling-tower approach and humidity constraints of a Singapore commercial building, and is evaluated over a full annual backtest against an ASHRAE Guideline 36 baseline.


## 精读解读（中文）
### 一、研究动机
热带商业建筑中空调能耗占建筑总能耗的50%-60%，湿球温度常年高且年变化小，冷却塔趋近成为冷凝水优化的主要约束，设计显热比约0.71使得除湿而非降温主导盘管尺寸。传统监督控制如ASHRAE Guideline 36基于分层启发式，难以灵活适应多变的天气和负荷工况，而模型预测控制需要频繁维护显式模型。强化学习虽能免除显式模型，但收敛到单一折中策略无法应对热带多变的运行条件，且缺乏安全保证。因此需要一种能够维护多个专业化策略并强制安全约束的控制框架。

### 二、技术方案（Method）
提出CQD-ERL，一种上下文质量-多样性进化强化学习控制器。输入为每日天气负荷特征（平均冷负荷、潜热负荷分数、峰值湿球温度、日太阳辐照），经PCA投影到前两主成分后划分18个上下文单元；每个上下文单元内按4维行为描述符（冷冻水设定点对室外温度斜率、冷却塔风机速度对湿度斜率、非占用期间植物开启比例在低于/高于29度漂移阈值的分数）分配12个行为niche，形成18×12共216个档案单元。每个训练回合从一周中当天热状态库中随机初始化，使用无梯度进化算子（各向同性+定向line变异）和SAC策略梯度算子共同生成后代，二者共享一个回放缓冲区，并每隔固定代数将当前actor插入档案。动作先通过确定性安全屏蔽（相对湿度/露点上限、执行器范围、斜坡限制、最小启停时间）投影再执行。环境为两层：降阶微分代数系统用于训练，高保真Modelica/EnergyPlus用于验证，最终在全年8760小时顺序回测中与ASHRAE Guideline 36基线对比。

### 三、结果（Result）
在全年顺序回测中，CQD-ERL相对ASHRAE Guideline 36基线在维持舒适度和湿度约束的同时降低了年能耗。所有被评估控制器的相对湿度上限违规率为零，证明安全屏蔽的硬投影机制有效。此外，上下文档案的覆盖率达到约99.5%，验证了产品档案能有效填充多样化专业策略。

### 四、结论（Conclusion）
CQD-ERL通过上下文感知的产品档案结构，将进化搜索的全局探索与SAC的样本效率结合，避免了单一折中策略，在热带建筑HVAC监督控制中优于G36基线。实验证实质量-多样性进化强化学习能够处理非平滑动力学、离散冷水机组分级和露点约束，为热带建筑提供了一种可行的、可复现的智能控制方案。

### 五、方法论与关键技术细节
关键细节包括：上下文特征PCA前两主成分联合解释77.1%方差；行为描述符基于固定探针电池，直接从策略参数计算，保证纯函数性并对上下文不变；适应度按同日Guideline 36回报归一化，消除上下文间回报方差；SAC使用裁剪双Q熵正则损失，温度自动调节；进化变异采用σ1各向同性噪声与σ2方向性变异组合；每个上下文单元12个行为niche，共216个；安全屏蔽为确定性投影而非奖励惩罚，保证湿度违规率为零；奖励由三项组成：整合能耗、占用加权PMV不舒适度、屏蔽依赖惩罚；训练环境为微秒级降阶模型，验证环境为高保真模型，满足ASHRAE Guideline 14精度标准；评估保留周末热质量效应；局限性在于依赖训练环境的保真度和大量环境步数。
