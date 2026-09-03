# Designing Versatile Samples for Learned Trajectory Scoring

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Yaguang Li, Jiaru Zhang, Chuheng Wei, Can Cui, Ziran Wang
- 机构：Purdue University, Bosch Artificial Intelligence Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01799v1) · [PDF](https://arxiv.org/pdf/2609.01799v1)

## TLDR
By training a lightweight transformer-based trajectory scorer on synthetically perturbed samples along lateral and longitudinal decision boundaries instead of only the frozen planner's safe proposal pool, the paper improves EPDMS scores on NAVSIM for DiffusionDrive and MeanFuser (90.1 and 90.4, respectively).

## Abstract
Many current end-to-end driving policies emit a pool of candidate trajectories and select one, which makes selection a separable component: a scorer can be retrained while the planner, its backbone, and its trajectory generator all stay frozen. However, many strong planners concentrate their proposals around safe mode, providing limited supervision near decision boundaries. In this work, we design a training dataset that provides more informative supervision for the scorer. In particular, we construct two generators that perturb the logged human trajectory along the two axes a vehicle can be displaced: laterally toward the drivable boundary and longitudinally toward a leading vehicle. The designed dataset produces more informative positive and negative samples than the base planner's proposal pool. We attach a transformer-based scorer to two frozen generative planners, DiffusionDrive and MeanFuser, and train it on the NAVSIM navtrain dataset. The results of the experiments show that we achieve 90.1 EPDMS on DiffusionDrive and 90.4 EPDMS on MeanFuser when using ResNet-34, with 0.4 and 0.3 EPDMS respectively, from the designed training dataset.


## 精读解读（中文）
### 一、研究动机
当前许多生成式规划器的候选轨迹高度集中在安全区域，导致决策边界附近缺少可用于学习的有效监督样本，而驾驶指标的级联二元结构又使微小轨迹偏差可能获得完全相反的分数，这让学习型评分器难以准确排序。本文由此出发，通过构造具有信息量的扰动轨迹数据集来弥补边界区域的监督，在保持规划器冻结的前提下提升打分与选择的质量。

### 二、技术方案（Method）
方法以录制的驾驶员轨迹为锚点构造训练数据：横向生成器将轨迹逐点推向可行驶边界，纵向生成器使自车沿本车弧线前行并逼近引导车；两类位移用10米弧长的光滑步进斜坡加权到八个航路点，并通过模拟器在环内求解各分级目标margin，得到跨越决策边界的近碰撞与违规样本。评分器是一个轻量Transformer模块，将候选轨迹展平并升维为查询，在冻结规划器输出的小型上下文特征token上进行三层解码器交叉注意力，再用九个相互独立的解码头分别预测EPDMS的四个规则项与五个质量项；损失中二元项采用聚焦交叉熵且gamma等于2，连续进度项采用均方误差，NAVSIM中未定义标签的分量不参与对应损失。推理时按EPDMS公式合成总分并选取argmax轨迹，同时只使用基础规划器自身的候选池，因此在线开销不变。

### 三、结果（Result）
在NAVSIM navtrain数据集上以ResNet-34进行实验，将所提评分器加至DiffusionDrive后EPDMS达到90.1，加至MeanFuser后达到90.4，相比仅用基础规划器自身提议池训练分别带来0.4和0.3的提升。两个规划器拥有不同传感器配置、骨干网络与候选池规模，因此增益具有跨规划器的可复现性；分量分解表明增益主要集中于乘法的规则安全项上。

### 四、结论（Conclusion）
本文说明评分器的训练数据可以作为一种主动设计变量：与其扩大固定或超密集的轨迹词汇，不如从人类轨迹出发，沿驾驶中最影响安全判断的两个自由度生成接近决策边界的正负样本。与冻结的生成式规划器联用时，该方法以很低训练成本显著改善最终选出的轨迹，且对不同形态的规划器具有普适性。

### 五、方法论与关键技术细节
关键点包括：EPDMS由四个乘积规则项与五个加权质量项构成，单个违规会清零整分，故评分器须按组件独立建模而非直接回归总分；九个组件网络不共享权重，并且所有损失权重lambda都设为1。在数据生成中，横向margin使用车辆四角到可行驶区域边界的有符号距离，纵向margin取前保险杠到引导车的最小间隙，扰动沿10米弧长的平滑斜坡逐渐增强，且生成轨迹长度被限制在冻结规划器最大提议长度以内，避免出现不可行的长轨迹。训练使用真实模拟器标签，时间在单GPU上少于1小时；推理不评估合成样本，因此原始评分延迟不变。
