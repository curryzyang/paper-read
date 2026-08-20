# Terrain-Aware Local Path Planning with Global DEM Data Integration for Autonomous UGV Navigation

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Devender Singh, Issah Nazif Suleiman, Paul Mitten, Glenn Cutler, Vinicius Prado da Fonseca, Matthew Hamilton
- 机构：Memorial University of Newfoundland, Compusult Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17038v1) · [PDF](https://arxiv.org/pdf/2608.17038v1)

## TLDR
The paper proposes a hybrid UGV navigation framework that integrates low-resolution global DEM data with real-time LiDAR-based local path correction, achieving 95% obstacle avoidance and reduced terrain slope traversal in simulations.

## Abstract
Autonomous navigation in complex outdoor terrains presents critical challenges for unmanned ground vehicles (UGVs) due to the inherent disconnect between global mapping and real-time sensor feedback. This work proposes a hybrid framework that integrates low-resolution Digital Elevation Model (DEM) data with real-time LiDAR-based obstacle detection and terrain analysis for efficient path planning. A global path is initially computed using a preprocessed DEM-based A* algorithm. Subsequently, local sensor data drives adaptive path correction, enabling the UGV to negotiate sudden environmental changes while maintaining safety and efficiency. Simulation results in Gazebo demonstrate significant improvements over a baseline approach, achieving a 95\% obstacle avoidance rate and reducing the average encountered slope from $8^\circ$ to $2.7^\circ$ in custom terrain. This integration enhances path efficiency and terrain traversability and supports robust real-time adaptation, paving the way for more reliable autonomous navigation in dynamic outdoor environments.


## 精读解读（中文）
### 一、研究动机
户外复杂地形下无人地面车辆（UGV）的自主导航面临全局地图与实时传感器反馈脱节的挑战，现有系统难以实时适应突发环境变化，且安全与效率之间常存在权衡，缺乏将全局路径优化与局部地形分析统一起来的混合框架。

### 二、技术方案（Method）
提出混合导航框架：首先使用SRTM 1弧秒（30m分辨率）DEM数据，经裁剪、插值、归一化生成3D地表z(x,y)，计算坡度s(x,y)与代价函数C(x,y)=1.0*s+0.5*z，并对极端低海拔施加惩罚P=10，归一化后基于A*算法计算全局最优路径；随后在局部路径校正模块中，利用实时LiDAR点云，通过Ground Plane Fitting（GPF）结合迭代RANSAC进行地面分割（初始种子取最低250点，距离阈值0.1m，迭代3次），基于地面法向量与垂直轴计算当前坡度，并用滑动窗口（N=40）的坡度均值μ与标准差σ动态设定预警阈值τ_warn=μ+σ和临界阈值τ_crit=μ+3σ，实现分级响应（正常行驶、避障、紧急停车）；障碍物规避通过非地面点建模为高度分布，计算皮尔逊偏度系数S判断偏斜方向，或在对称分布时比较左右两侧中位高度h_L与h_R来决定左转或右转。

### 三、结果（Result）
在Gazebo自定义地形仿真中，相比基线方法，该框架实现了95%的障碍物规避率，并将平均遭遇坡度从8°降至2.7°，显著提升了路径效率和地形可通行性，同时支持实时动态路径调整，解决了UGV在动态环境中卡住的问题。

### 四、结论（Conclusion）
将低分辨率全球DEM数据与实时LiDAR感知融合的混合框架，能够有效弥补全局规划与局部执行之间的鸿沟，在保持全局路径最优性的同时实现实时地形自适应和障碍规避，为动态户外环境下的可靠自主导航提供了可行方案。

### 五、方法论与关键技术细节
关键细节：DEM采用SRTM 1弧秒约30m分辨率，区域为半径1000m的圆形，中心坐标（47.4870°N, -52.8629°W）；代价权重w_s=1.0, w_z=0.5，极端高程惩罚P=10；A*全局路径在归一化成本图上计算；局部处理使用LiDAR点云，地面分割阈值τ_seed=0.8m、τ_dist=0.1m、迭代3次；坡度滑动窗口N=40，动态阈值基于均值和标准差；障碍物偏度阈值τ=0.2；仿真环境为Gazebo，比较对象为未集成全局DEM的基线方法；局限性包括DEM分辨率低无法捕捉细粒度障碍（岩石、沟渠、坑洞），依赖经验阈值，且尚未在真实物理环境中验证。
