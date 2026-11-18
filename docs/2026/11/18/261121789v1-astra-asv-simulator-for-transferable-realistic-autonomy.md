# ASTRA: ASV Simulator for Transferable Realistic Autonomy

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Tsimafei Lazouski, Cody Sheltraw, Alan Papalia, Maani Ghaffari
- 机构：University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21789v1) · [PDF](https://arxiv.org/pdf/2611.21789v1)

## TLDR
ASTRA is an open-source NVIDIA Isaac Sim framework that combines Fossen-style 6-DOF marine dynamics, geometry-based buoyancy, spectral wave disturbances, photorealistic sensing, and ROS 2 interfaces matched to a physical BlueBoat to enable transferable autonomous surface vehicle development and sim-to-real testing.

## Abstract
Autonomy development for marine autonomous surface vehicles (ASVs) remains challenging because field testing is costly and difficult to reproduce. Existing marine simulation tools provide mature capabilities in vessel dynamics, robotics integration, and visual rendering, but these strengths are emphasized differently across platforms. This paper presents ASTRA, an ASV simulation framework built in NVIDIA Isaac Sim that combines marine vehicle dynamics, photorealistic perception, and Robot Operating System (ROS 2) autonomy interfaces within a common environment. ASTRA incorporates a Fossen-style marine dynamics model together with geometry-based buoyancy and programmable spectral wave disturbances, enabling non-planar hydrostatic and wave-induced motion. The simulator reproduces the sensor configuration of a physical BlueBoat testbed, including GPS, IMU, LiDAR, and RGB-D sensing exposed through ROS 2. This allows localization, perception, planning, and control software to be developed against interfaces consistent with the physical platform. The BlueBoat's existing ROS 2 localization and perception modules were ported directly into ASTRA, while targeted zero-propulsion experiments were used to verify the implemented wave-body coupling. The simulated roll response was consistent with the expected non-oscillatory hydrostatic behavior, and heave remained highly coherent with the generated wave field, with approximately unity gain at the dominant wave frequency in the tested sea states. ASTRA is intended as an open-source testbed for marine autonomy development, simulation-based benchmarking, and sim-to-real experimentation.


## 精读解读（中文）
### 一、研究动机
海洋自主水面艇（ASV）的自主性开发受制于现场试验成本高、可重复性差且测试场景有限；现有海洋仿真器虽分别覆盖船舶动力学、机器人集成或视觉渲染，但缺少在Isaac Sim中同时支持水面艇动力学、波浪—船体耦合、照片级感知与ROS 2自主栈的开源环境。ASTRA旨在填补这一空白，为全栈自主性开发、基准测试和sim-to-real实验提供可迁移的真实感仿真平台。

### 二、技术方案（Method）
ASTRA以NVIDIA Isaac Sim 5.1.0为底座，将Fossen风格6自由度水面艇动力学、基于几何体的实时浮力求解器和可编程波浪谱扰动耦合到同一物理步回调中；浮力由BlueBoat浮筒代理网格的瞬时浸没体积及浸没顶点加权质心计算，波浪采用JONSWAP谱经TMA有限水深修正后在GPU上合成，并用1000个频率分量和128个传播方向生成时空水面高程，进而驱动升沉、横摇和纵摇。仿真器复现实体BlueBoat的GPS、IMU、LiDAR和RGB-D配置并通过ROS 2暴露，同时用29个现场测试bag中的零推力自由衰减段辨识平面阻尼，其中7段纵荡和7段艏摇分别拟合二次阻尼系数。

### 三、结果（Result）
系统辨识得到纵荡中位R²=0.94、艏摇中位R²=0.96，参数为X_u=0、X_uu=7.77、N_r=2.46、N_rr=9.01；线性纵荡阻尼收敛到非负下界，表明测试速度范围内以二次阻尼为主。零推进验证中，仿真的横摇响应符合预期的非振荡静水恢复行为，升沉与生成波场高度相干，在测试海况的主波频处增益约为1，说明波浪—船体耦合在升沉方向上得到较好复现。实体BlueBoat已有的ROS 2定位与感知模块可直接移植到ASTRA中运行。

### 四、结论（Conclusion）
ASTRA可作为开源ASV仿真测试平台，用于海洋自主性开发、基于仿真的基准评测和sim-to-real实验；其价值在于在同一Isaac Sim环境中联合迭代动力学、感知、规划与控制，并保持与实体BlueBoat一致的ROS 2接口。

### 五、方法论与关键技术细节
实现上采用仅含刚体惯性且无附加质量矩阵、阻尼矩阵对角化的低航速简化，除纵荡和艏摇外的阻尼系数为人工选取；浮力使用降采样代理网格和分段线性浸没体积映射，兼顾实时性与静水恢复及波浪诱导运动。波浪谱的总体幅值由用户尺度参数独立控制，尚未由风速和风程直接推断有效波高Hs，且虽采用TMA深度修正能量谱，色散关系仍用深水形式ω²=gk，有限水深色散留待后续；这些近似和局限是评估其波浪—船体保真度与sim-to-real适用边界时的关键。
