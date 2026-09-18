# Dynamic-LIVO: A Dynamic-Aware LiDAR-Inertial-Visual Odometry System Using Spatio-Temporal Normals

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Zhixin Zhang, Samuel Ahiwe, Matthew Hale, Liang Zhao, Pawel Ladosz
- 机构：University of Edinburgh, University of Manchester
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19336v1) · [PDF](https://arxiv.org/pdf/2609.19336v1)

## TLDR
Dynamic-LIVO is a dynamic-aware LiDAR-inertial-visual odometry system that uses spatio-temporal normal analysis with time-delayed estimation to filter dynamic points and achieve robust state estimation and clean static colored mapping in dynamic environments.

## Abstract
This paper proposes Dynamic-LIVO, a dynamic-aware LiDAR-Inertial-Visual Odometry (LIVO) system for robust state estimation and static colored mapping in dynamic environments. Dynamic-LIVO employs Spatio-Temporal (S-T) normal analysis to identify dynamic LiDAR points and propagates the resulting classification to both LiDAR-inertial and visual-inertial updates, preventing dynamic LiDAR measurements and their associated visual observations from affecting state estimation and mapping. However, S-T normal estimation can be unreliable in newly observed and spatially sparse regions due to insufficient spatio-temporal observations. To address this issue, we introduce a time-delayed S-T normal estimation strategy that defers the classification of insufficiently constrained points and re-evaluates them as additional observations become available. This strategy improves dynamic classification reliability while preserving valid static points for map construction. Extensive experiments on public and self-collected datasets with diverse sensor configurations demonstrate that Dynamic-LIVO improves localization accuracy and produces cleaner static colored maps in challenging dynamic environments. The source code and self-collected dataset will be publicly released upon acceptance.


## 精读解读（中文）
### 一、研究动机
现有 LiDAR-Inertial-Visual Odometry 系统大多基于静态世界假设，动态物体会同时污染 LiDAR 几何约束、视觉深度关联和彩色建图，导致定位漂移与地图重影。已有 S-T normal 动态检测主要面向 LIO，且在新观测或空间稀疏区域因时空观测不足而不可靠，容易误删静态点或漏检动态点。

### 二、技术方案（Method）
Dynamic-LIVO 建立在 FAST-LIVO2 之上，输入 LiDAR 扫描、IMU 和图像，在 IESKF 中完成 LiDAR 处理、IMU 传播、视觉处理和静态彩色建图，并维护一个保留最近 1 秒 LiDAR 测量的短期稠密地图用于动态检测。对每个 3D 点在 4D 时空域中拟合局部切超平面，取协方差矩阵最小特征值对应特征向量作为 S-T normal，其时间分量非零则判为动态、为零则判为静态。为处理新观测或稀疏区域，采用时间延迟 S-T normal 估计：检索 K=20 个最近邻，若邻居不足、最远邻距离超阈值或时间分布不足至少 3 个时间箱且单一时间箱占比过高，则标记为 unknown 并延迟重评，最多重试 6 次后丢弃。随后进行空间一致性检查：将不稳定点上采样回原始稠密扫描，用 DBSCAN 去除孤立误检并与短期静态体素地图做重叠检查，拒绝与已观测静态区域重叠的候选簇。最终，动态 LiDAR 点从 LIO 点面残差中剔除，并通过 LiDAR-图像投影把动态分类传播到 VIO，使动态区域不参与视觉深度关联和状态更新；推理流程按扫描逐帧执行，无需学习或训练。

### 三、结果（Result）
在公开数据集和自采数据集、多种传感器配置下，Dynamic-LIVO 相比 FAST-LIVO2 提高了定位精度，并生成更干净的静态彩色地图。自采 PosterWall 序列中，运动行人等在 FAST-LIVO2 地图中的重影被有效去除，同时保留静态点用于建图。

### 四、结论（Conclusion）
该工作提出了一种无学习、动态感知的 LIVO 系统，通过 S-T normal 分析与时间延迟分类策略识别动态 LiDAR 点，并将动态信息同时传播到 LIO 和 VIO 更新中。实验表明，该方法能在挑战性动态环境中实现更鲁棒的状态估计和更干净的静态彩色建图。

### 五、方法论与关键技术细节
关键实现包括：使用 4D S-T normal 的时间分量作为动态判据；维护 1 秒滑动窗口的短期稠密地图以保证邻域密度；K=20 最近邻、至少 3 个时间箱、最多 6 次延迟重评等阈值/超参；DBSCAN 与短期静态体素地图重叠检查用于抑制误检。方法不依赖语义类别，泛化性较好，但性能受邻域阈值、DBSCAN 参数和重评次数影响，未知点在重试后仍不可靠会被丢弃，可能影响稀疏区域建图完整性。
