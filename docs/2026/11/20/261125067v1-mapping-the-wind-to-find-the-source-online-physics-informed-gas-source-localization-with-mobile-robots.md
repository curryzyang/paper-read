# Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Wanting Jin, Thomas Wiedemann, Han Fan, Achim Lilienthal, Alcherio Martinoli
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25067v1) · [PDF](https://arxiv.org/pdf/2611.25067v1)

## TLDR
The paper presents a lightweight physics-informed probabilistic framework that reconstructs indoor airflow online from sparse robot measurements and uses an advection–diffusion forward model with wind-support-aware Bayesian inference and informative path planning to efficiently localize gas sources, validated through high-fidelity simulations and physical experiments.

## Abstract
Gas Source Localization (GSL) with mobile robots is challenging because wind and gas measurements are spatially sparse, noisy, and potentially affected by robot motion. Indoor airflow can vary substantially across space, while detailed environmental layouts, boundary conditions, or precomputed airflow fields are often unavailable. Moreover, hazardous sources must be localized as quickly as possible, making exhaustive exploration impractical. This paper presents a lightweight physics-informed probabilistic framework for efficient GSL under spatially varying indoor airflow. As the robot navigates, it continuously collects wind and gas measurements and reconstructs the spatially varying airflow field online. The estimated wind field drives a forward dispersion model that predicts the gas pattern for each candidate source location. These predictions are compared with the measured gas pattern to update a probabilistic belief over the source location. As the wind field is reconstructed incrementally, the framework also accounts for the spatially non-uniform reliability of wind field estimation and its influence on the source estimation. The resulting belief map is then used for informative path planning to guide the robot toward informative regions. High-fidelity simulations provide a comprehensive evaluation of the individual components and their integrations within the complete system, while physical indoor experiments assess the system performance under realistic sensing, motion, and airflow conditions. The results demonstrate that incorporating lightweight physical knowledge significantly improves localization robustness under spatially complex airflow and enables more efficient exploration.


## 精读解读（中文）
### 一、研究动机
室内气体源定位中风与气体测量稀疏、含噪且受机器人运动影响，气流随空间显著变化，而详细布局、边界条件或预计算风场通常不可得；危险源又要求尽快定位，穷举探索不现实。现有模型法常依赖均匀气流或先验环境信息，在线重建风场时又常忽略其空间非均匀可靠性，可能导致过度自信的后验和低效探索。

### 二、技术方案（Method）
机器人连续采集气体浓度、平面风矢量和位置，在线用核方法增量重建细预测网格上的空间变化风场；对粗估计网格中的每个候选源，以重建风场驱动二维ADE前向扩散模型预测气体分布，并与实测气体模式比较构造贝叶斯似然以更新源位置信念图。框架引入风支持感知不确定性，根据风图局部测量支持程度调节各候选源预测对似然的影响，再用信念图进行信息增益路径规划，并依据置信终止准则输出MAP源估计。整个过程无需入口/出口、边界条件或预计算风场，障碍几何可未知并可选用在线地图信息。

### 三、结果（Result）
高保真仿真对扩散模型、在线风估计、风支持感知推断及其与IPP的集成进行了消融，物理室内实验在真实传感、运动和气流条件下评估系统；结果表明引入轻量物理知识可显著提升空间复杂气流下的定位鲁棒性并实现更高效探索。可见摘要未给出具体定位误差或成功率数值，定量对比需参考原文实验表格。

### 四、结论（Conclusion）
该工作提出一种轻量、物理信息驱动的在线概率GSL框架，将增量风场重建、ADE前向扩散预测、风支持感知贝叶斯更新和信息路径规划结合，在缺乏详细环境先验的室内场景中实现高效源定位。结果支持任务导向的轻量物理模型足以改善复杂气流下的鲁棒性与探索效率，但方法仍受二维、单源和准稳态气流假设约束。

### 五、方法论与关键技术细节
关键实现包括双网格设计：较细预测网格表示风场和源条件气体分布，较粗估计网格表示候选源并排除障碍及边界附近单元；风场采用核方法局部增量更新以支持在线计算，ADE在预测网格上数值求解以在保真度和成本间折中，风支持感知似然用风图局部测量支持度修正预测可靠性。方法假设二维、单一静止源、时间平均气流和气体分布近似稳态且任务期间缓慢变化，不显式建模垂直变化；可见文本未给出具体损失函数或超参数，且核重建的局部支持、ADE简化与稀疏噪声测量会带来模型失配和不确定性，是主要局限。
