# Adversarial Calibration Attack on Autonomous Vehicles

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Liangkai Liu, Qingzhao Zhang, Kang G. Shin
- 机构：Texas Tech University, University of Arizona, University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28778v1) · [PDF](https://arxiv.org/pdf/2608.28778v1)

## TLDR
TLDR: This paper introduces the first physically realizable attack against online camera–LiDAR calibration in autonomous vehicles, using a single adversarial poster to both trigger unnecessary recalibration and corrupt the estimated extrinsic transform, causing severe calibration errors and downstream safety failures.

## Abstract
Autonomous vehicles (AVs) rely on accurate camera-LiDAR calibration for multimodal sensor fusion. In practice, calibration can drift due to vibration, temperature variation, or minor sensor displacement, motivating online calibration algorithms that detect and correct misalignment at runtime while allowing the vehicle to continue operating without a factory visit. Existing AV attacks largely assume correct calibration. We instead identify online sensor calibration as a new attack plane. A corrupted calibration update can persist across subsequent fusion operations, causing system-wide errors that propagate from perception to planning and control. We present Adversarial Calibration Attack (ACA), the first physical attack against camera-LiDAR online calibration. Using a single adversarial poster, ACA first spoofs the miscalibration detector to trigger the calibration process and then steers the calibration estimator toward an incorrect transformation. A unified optimization jointly designs the poster's geometry and texture for both objectives. We evaluate ACA across benchmark datasets, simulation, and physical experiments. On benchmark datasets such as KITTI and nuScenes, ACA induces up to 33.9 degrees mean rotational calibration error, thereby severely degrading object detection. In the CARLA simulator, the attack causes a collision when the corrupted calibration is accepted in vulnerable scenarios crafted by the attacker. On a real Husky robot, a printed adversarial poster successfully reproduces the calibration error. These results demonstrate that online calibration is a practical and safety-critical attack surface for AVs.


## 精读解读（中文）
### 一、研究动机
现有自动驾驶攻击大多假设传感器标定正确，而在线标定作为可运行时更新的系统状态，一旦被篡改会持续影响后续多模态融合、感知、规划与控制，构成被忽视的高风险攻击面。本文首次针对相机-激光雷达在线标定流程提出物理可实现攻击，利用单一对抗海报同时欺骗失准检测器触发标定并引导标定估计器输出错误外参。

### 二、技术方案（Method）
提出ACA攻击，目标为在线标定流水线中的失准检测器D和标定网络f_theta。攻击者部署一张同时被相机和LiDAR观察到的平面海报，通过统一优化同时设计海报的几何与纹理。Stage-1使用铰链损失，当检测器超过触发阈值后优化转向破坏标定；Stage-2通过完整迭代轨迹对标定网络求导，采用EOT和跨多帧通用训练增强鲁棒性。物理约束渲染器模拟不透明印刷表面、面积平均成像和LiDAR按角度栅格采样，保证相机外观与LiDAR点云对应同一物理物体。

### 三、结果（Result）
在KITTI和nuScenes数据集上，ACA可诱发最高33.9度的平均旋转标定误差，严重降低3D检测性能；PointPainting的Car 3D AP@R40从51.72降至0.36，而不用外参的PointPillars几乎不变。在CARLA仿真中，接受被污染标定可在攻击者设计的脆弱场景中导致碰撞；在真实Clearpath Husky A300上，打印的对抗板成功复现标定误差。

### 四、结论（Conclusion）
在线标定是自动驾驶实际且安全关键的攻击面。单个物理对抗物体能够同时破坏标定触发与估计，产生持久且系统级的跨模态错位，且该攻击对不验证外参状态的输入一致性防御具有盲区。

### 五、方法论与关键技术细节
攻击假设匹配替代灰盒：攻击者知道检测器和标定网络架构族、传感器配置及数据分布，可训练替代标定网络，但无需精确参数。关键模块为门控流水线：检测器D判断何时标定，标定网络f_theta迭代外参T。攻击需同时满足两个目标，Stage-1用铰链损失确保检测器触发，Stage-2通过完整迭代轨迹优化外参偏差。物理约束包括海报为不透明平面、面积平均成像、LiDAR按角度栅格采样，并通过EOT和跨帧通用训练增强对视角和场景变化的鲁棒性。局限性为仅需部署在攻击者选定的地点，无需泛化到任意道路；攻击依赖标定流水线未独立验证外参状态的盲区。
