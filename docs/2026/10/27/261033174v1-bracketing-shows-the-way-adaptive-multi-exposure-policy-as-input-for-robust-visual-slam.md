# Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos, Jean-Michel Fortin, François Pomerleau, Philippe Giguère
- 机构：Université Laval
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33174v1) · [PDF](https://arxiv.org/pdf/2610.33174v1)

## TLDR
The paper proposes B-Adapt, an adaptive multi-exposure bracketing policy, and BVSLAM, a factor-graph visual SLAM estimator that directly uses bracketed images without HDR merging, improving robustness to rapid illumination changes and reducing tunnel-exit state-estimation error by 78% versus auto-exposure.

## Abstract
Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photometric overlap, and BVSLAM directly uses the multi-exposure sequence as constraints in a factor graph state estimator without relying on High Dynamic Range (HDR) merging. We evaluate both methods against state-of-the-art approaches in nominal environments and during a repeated tunnel-exit transition at an emulated vehicle speed of 32 m s-1. In the tunnel, combining our B-Adapt with BVSLAM reduces the state estimation error by 78 % compared with AE images. These results suggest that bracketing efficiently improves visual pose estimation robustness to rapid illumination disturbances while retaining low error under nominal conditions. Our code is available at https://github.com/norlab-ulaval/bracketing-shows-the-way.


## 精读解读（中文）
### 一、研究动机
快速光照变化（如高速隧道出口）会让自动曝光策略来不及适应，图像饱和并丢失视觉对应，导致视觉SLAM跟踪失败。论文希望在图像采集端和状态估计端同时缓解这一扰动，而不是依赖单曝光或HDR融合。

### 二、技术方案（Method）
提出B-Adapt自适应包围曝光策略：用EV域标量统一控制曝光时间与增益，分别用Low和High两个独立控制环，通过单侧百分位尾部目标使亮区仅少量像素接近饱和、暗区仅少量像素过暗，并用EMA更新曝光值；当n≥3时在上下界之间按EV等间隔插入中间曝光，施加最小间隔约束，并按Low、Mid、High、Mid…的顺序采集以保持相邻帧光度重叠。提出BVSLAM：用SuperPoint和LightGlue在已知包围曝光周期内匹配特征，仅关联曝光步差不超过1且位于回看窗口W内的图像，将立体与时序对应作为因子图约束，联合优化SE(3)位姿和路标，使用零运动先验避免弱视觉区域传播轨迹，先滑动窗口增量求解再做全局BA，不进行HDR合并。

### 三、结果（Result）
在名义环境和以32 m/s模拟车速重复通过的隧道出口过渡中进行评估；在隧道场景中，B-Adapt与BVSLAM组合相比自动曝光图像将状态估计误差降低78%，同时在名义条件下仍保持较低误差。

### 四、结论（Conclusion）
结果表明，自适应多曝光包围能有效提升视觉位姿估计对快速光照扰动的鲁棒性，并且直接将多曝光序列作为因子图约束使用，无需HDR重建即可保留跨曝光视觉信息，兼顾名义环境精度。

### 五、方法论与关键技术细节
关键实现包括：标准相机硬件、8位图像动态范围有限而隧道出口场景动态范围可达约120 dB、Low/High尾部目标由α和β参数化、EMA系数λ控制响应速度、最小曝光间隔Δ_min、中间曝光按EV线性分配、回看窗口W取包围周期倍数；BVSLAM刻意采用零运动先验而非运动学模型以隔离采集策略影响；当前实现面向离线处理、非实时，且不依赖HDR融合，主要验证包围曝光对视觉约束和位姿估计的影响。
