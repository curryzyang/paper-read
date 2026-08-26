# ODG-NoMaD: Overhead-Camera Direction-Guided NoMaD

- 区域：精读区
- 排名：4
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Blossom Treesa Bastian, Keerthi S. Shetty, Manish Kolachalam, Rani Malhotra, Ashish Dutta
- 机构：IIT Kanpur, Infosys Center for Emerging Technologies
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21395v1) · [PDF](https://arxiv.org/pdf/2608.21395v1)

## TLDR
ODG-NoMaD steers NoMaD's goal-masked diffusion exploration in unseen environments by injecting the gradient of a direction cost—derived from an overhead-camera-built occupancy map and global path, refined by onboard traversability—into the denoising process, dramatically improving goal-reaching and collision avoidance without retraining.

## Abstract
NoMaD [31] is a learned vision-navigation policy that unifies goal-conditioned navigation and exploration in a single goal-masked diffusion policy. In an unseen environment, however - where neither a goal image nor a topological map is available - it can only explore undirectedly, wandering without global awareness. We present ODG-NoMaD, which gives NoMaD's exploration mode a global sense of where to proceed, without retraining the policy. An overhead depth camera is used once on deployment to build an occupancy map and plan a global path, which is segmented to yield a desired heading; a per-frame traversability map from the robot's onboard depth then refines this into a collision-free direction. The gradient of a cosine direction cost is injected into the final denoising steps, rotating sampled trajectories toward this direction while preserving the multimodality of exploration. In simulated office environments with and without random obstacles, ODG-NoMaD reduces the residual distance to the target by up to an order of magnitude over unguided exploration, outperforms the point-goal cost guidance of NaviDiffusor [37], and is the only configuration that remains collision-free on every trial.


## 精读解读（中文）
### 一、研究动机
NoMaD是一种将目标条件导航与探索统一于单一掩码扩散策略的视觉导航模型，但在未见环境中既无目标图像也无拓扑地图时，其探索模式只能盲目游走，缺乏全局感知，容易重复访问已覆盖区域并困于局部环境。为此，ODG-NoMaD在不重训策略的前提下，将经典规划的全局引导与NoMaD探索模式的反应性、泛化性结合，使探索具有明确的前进方向。

### 二、技术方案（Method）
ODG-NoMaD的流程是：部署时用顶部深度相机拍摄一次深度图像，经外参标定将有效像素（0.3–8 m）反投影为点云并旋转到世界系，按高度阈值（-0.05、0.08、2.5 m）分类为自由/占用/未知，以0.05 m分辨率栅格化并做形态学开闭运算得到占用地图；在该地图上用全局规划器规划从机器人当前位置到目标的路径。随后用Ramer–Douglas–Peucker算法将稠密路径简化为若干近似直线段，用atan2计算当前所在段的期望航向角。机器人每帧使用机载深度图构建BEV可通行图，通过两层选择器将全局航向与局部可通行方向融合为无碰撞的引导方向；在NoMaD的动作扩散模型去噪过程中，将余弦方向代价的梯度注入最终去噪步，使采样轨迹朝该方向旋转，同时保留探索的多模态性。整个过程不需要重新训练NoMaD策略。

### 三、结果（Result）
在模拟办公环境（含随机障碍物与不含随机障碍物）中，ODG-NoMaD相较无引导探索将到目标的平均残差距离降低约7倍，最高可降低一个数量级；其性能优于NaviDiffusor基于点目标代价的引导方式，并且是唯一在所有试验中都保持无碰撞的配置。当地图构建后引入新障碍物时，ODG-NoMaD仍能在沿全局路径走向目标的同时绕开新障碍物，保持无碰撞。

### 四、结论（Conclusion）
ODG-NoMaD表明，通过推理期方向引导将顶部相机提供的全局路径信息注入NoMaD的探索模式，可以显著提升未见环境中的定向探索效率，同时保持学习策略的碰撞感知与多模态探索能力；方向引导比点目标代价引导更适合用于扩散导航策略的全局路径注入，且结合可通行图可增强对新障碍的鲁棒性。

### 五、方法论与关键技术细节
关键实现细节包括：占用地图构建采用高度阈值分类（地板带-0.05至0.08 m，天花板截止2.5 m）和3×3椭圆结构元素的开闭运算去噪；全局路径用RDP算法按垂直距离容差ε简化为段，每段方向由atan2计算；方向代价采用余弦形式，梯度只注入最终去噪步骤以保留探索多模态性；NoMaD为预训练模型，掩码目标token后进入探索模式，动作表示为归一化位移序列；引导方向由全局路径航向与机载深度可通行图融合得到，以规避训练分布外的障碍物。该方法的局限性在于顶部地图只在部署时构建一次，若环境发生全局结构性变化，需重新建图或依赖局部可通行图进行补偿。
