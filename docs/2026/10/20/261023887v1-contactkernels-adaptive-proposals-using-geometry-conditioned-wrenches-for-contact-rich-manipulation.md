# ContactKernels: Adaptive Proposals using Geometry-COnditioned Wrenches for Contact-Rich Manipulation

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Aditya Kamireddypalli, Matías Mattamala, João Moura, Sethu Vijayakumar, Steve Tonneau, Subramanian Ramamoorthy
- 机构：University of Edinburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23887v1) · [PDF](https://arxiv.org/pdf/2610.23887v1)

## TLDR
ContactKernels is a contact-adaptive proposal kernel for sampling-based MPC that uses geometry-conditioned wrench measurements to estimate contact location and local geometry, steering the sampling distribution toward corrective motions and substantially improving contact-rich insertion success and speed in simulation and on a real robot.

## Abstract
Contact-rich insertion requires precise geometric alignment despite uncertainty in perception, geometry, and con- trol. When this uncertainty causes unintended contact, the re- sulting contact provides local information that can guide correc- tive motion. Sampling-based Model Predictive Control (SMPC) is well suited to this setting because it optimizes through forward simulation without requiring gradients through contact dynamics. However, standard SMPC methods typically use generic proposal distributions that do not exploit observed contact to determine where to search next. We introduce ContactKernels, a contact-adaptive proposal kernel that uses geometry-conditioned wrench measurements to estimate contact location and local contact geometry. The estimated contact state directly adapts the proposal distribution: contact location biases the search toward corrective motions, while the contact normal shapes the sampling covariance. We evaluate ContactKernels with Predictive Sampling (PS) and Model Predictive Path Integral (MPPI) control across multiple insertion geometries in simulation and on a real robot. In simulation, ContactKernels improves mean insertion success by over 50 % points across both controllers. On the real robot, it increases insertion success from 53.3 % to 90.0 % and reduces mean time to insertion by 33 %. These results show that contact information can improve sampling-based control not only as feedback, but also by directly determining where the controller searches


## 精读解读（中文）
### 一、研究动机
接触丰富的插入任务在感知、几何和控制存在不确定性时容易产生非预期接触，而接触本身携带局部几何错配信息，可指导纠偏运动。采样型模型预测控制（SMPC）无需对接触动力学求梯度，适合此类任务，但标准方法通常使用通用提议分布，未利用已观测接触来决定下一步搜索方向，导致接触后的探索效率低。

### 二、技术方案（Method）
作者将销孔插入建模为SMPC问题：状态为销的SE(3)位姿，控制为末端六维速度旋量，在规划时域内用M个控制结点经三次插值表示控制序列，采样K条候选轨迹并通过接触动力学前向仿真评估；代价包含末端到孔口的平移对齐、SO(3)测地旋转对齐以及仅在平移对齐低于阈值后激活的插入进度项，分别用Predictive Sampling选最小代价序列或用MPPI进行代价加权更新，且只执行首控制并经Operational Space Control映射到关节指令后重规划。ContactKernels从几何条件化力/力矩测量中估计P个候选接触点、表面法向和归一化权重，以接触位置偏置提议分布朝纠偏运动搜索，以接触法向塑造采样协方差，并用接触置信度缩放适应强度，从而把接触状态直接注入提议核而非仅作为反馈。

### 三、结果（Result）
在多种插入几何的仿真中，ContactKernels使PS和MPPI两种控制器的平均插入成功率提升超过50个百分点；在真实机器人上，MPPI结合ContactKernels将插入成功率从53.3%提高到90.0%，并将平均插入时间缩短33%。这些对比表明，接触信息不仅可作为反馈，还能通过决定控制器搜索位置显著改善采样型控制。

### 四、结论（Conclusion）
ContactKernels通过接触自适应的提议核，将估计的接触位置和局部接触几何用于偏置搜索与塑形协方差，使SMPC在接触后更高效地探索纠偏动作。该方法在仿真和真实机器人上均验证有效，且无需学习接触到动作的映射或对接触动力学求导，为接触丰富操作提供了一种测试时自适应方案。

### 五、方法论与关键技术细节
方法假设夹持固定、孔位已知，接触估计器基于力/力矩测量输出候选接触点、法向与置信权重；关键实现包括接触位置偏置、法向协方差、置信度缩放，以及代价权重、插入激活阈值、规划时域、控制结点数、采样数和协方差等超参。其优势是零阶优化避免接触梯度且无需额外策略训练，但效果依赖接触估计精度与参数调节，当前验证集中在销孔插入和固定夹持设定。最终执行首控制并滚动重规划，真实机器人实验验证了实时闭环可行性。
