# Localization in Spatiotemporal Fields via Environmental PDEs

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Jose Fuentes, Abdullah Al Redwan Newaz, Ana Cavalcanti, Leonardo Bobadilla
- 机构：Florida International University, University of New Orleans
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00272v1) · [PDF](https://arxiv.org/pdf/2608.00272v1)

## TLDR
A localization framework uses PDE-governed spatiotemporal environmental fields (shallow water and advection-diffusion) as signatures, with a Rao-Blackwellized particle filter fusing multimodal measurements to outperform standard filtering in GPS-denied vehicle localization, as validated in simulations and field experiments.

## Abstract
This paper proposes a localization framework that uses spatiotemporal fields governed by partial differential equations (PDEs) as localization signatures. Two PDE classes are considered: the shallow water equations, which describe free-surface flows in coastal and riverine environments, and the advection-diffusion equation, which models the transport and mixing of scalar quantities such as temperature, salinity, and dissolved oxygen. A numerical PDE solver provides predicted fields over the domain, and multiple field channels are fused as multimodal measurements to improve localization accuracy. We formulate the problem within a Rao-Blackwellized particle filter (RBPF) that partitions the vehicle state into a nonlinear component sampled by particles and a linear sensor bias component tracked analytically via per-particle Kalman filters. This factorization reduces the required number of particles compared to a standard particle filter while accounting for realistic sensor drift. Simulation studies on both PDE scenarios show that the RBPF consistently outperforms a standard particle filter in terms of final position error and Root Mean Square Error (RMSE) across varying particle counts. Field experiments with an autonomous surface vehicle measuring salinity, temperature, and dissolved oxygen validate that PDE-governed environmental fields provide sufficient spatial variability for practical localization. Related experimental videos are available at https://localization-environmental-pdes.github.io/.


## 精读解读（中文）
### 一、研究动机
GPS拒止环境下的自主车辆定位是水下、室内及电磁对抗场景中的基础挑战。现有替代定位方法多依赖静态空间场或稳态流场，难以处理海洋调查、污染追踪等实际场景中物理场随时间的显著动态变化。浅水方程与对流扩散方程等环境PDE能够刻画水体的复杂时空演化，但尚未被系统用于车辆自身的定位反问题。为此，本文提出利用PDE控制的时空场作为定位签名，并构建能融合多通道环境测量、同时处理传感器漂移的滤波框架，以提升GPS拒止条件下的定位精度与鲁棒性。

### 二、技术方案（Method）
本文提出一种基于环境PDE时空场的定位框架。建模方面，考虑两类PDE：浅水方程（SWE）描述近岸与河流自由表面流，提供水位η和流速(u,v)三个通道；对流扩散方程描述温度、盐度、溶解氧、叶绿素等标量输运混合，通过耦合流速场生成多通道标量场。数值PDE求解器在域上提供预测场，车辆配备M个传感器同步测量对应通道，观测模型为φ(位置,t)+零均值高斯噪声。状态估计采用Rao-Blackwellized粒子滤波（RBPF）：将车辆状态划分为非线性部分（位置/航向）由粒子采样，线性传感器偏置部分用每个粒子附带的卡尔曼滤波器解析更新，从而在考虑传感器漂移的同时大幅减少所需粒子数。输入为控制序列和PDE预测的多通道场值，每个粒子依据运动模型传播，用多模态测量似然加权重采样，卡尔曼滤波器在线更新偏置项。仿真中设定测量噪声协方差diag(0.2^2,0.2^2,0.1^2)，运动噪声diag(0.5^2,0.087^2)，线性过程噪声diag(10^-8,...)，粒子数在实验中变化以对比。

### 三、结果（Result）
在两类PDE仿真场景中，RBPF在最终位置误差和RMSE上均一致优于标准粒子滤波（PF）。SWE场景下，500粒子时RBPF的RMSE为0.80±0.03 m，PF为1.07±0.04 m，精度提升约25%；对流扩散场景中，500粒子时RBPF的RMSE为1.23±0.35 m，相比PF的约2.3-2.4 m降低近47%，标准PF在所有粒子数下误差稳定在约2.3-2.4 m，显示出精度上限。特征消融实验显示，SWE模型融合全部三个特征时RMSE为0.82±0.06 m，仅用单一特征时升至1.59±0.55 m；对流扩散模型从全特征1.51±0.79 m退化至单特征2.63±1.63 m，方差显著增大，证实多通道融合显著提升精度。实船实验采用自主水面艇测量盐度、温度、溶解氧，验证了PDE场具有足够空间变异性用于实际定位。

### 四、结论（Conclusion）
基于环境PDE的时空场可作为GPS拒止环境下有效的定位签名，且RBPF通过将线性传感器偏置解析化能显著优于标准粒子滤波，在较少粒子数下获得更高精度。浅水方程与对流扩散方程分别适用于水动力场景和水质监测场景，多通道测量融合是提升定位鲁棒性的关键。实验结果支持该框架在水下及近岸自主定位中的实用潜力。

### 五、方法论与关键技术细节
关键细节包括：1）SWE源项包含由GEBCO数据估计的 bathymetry 和实测风速（约12 m/s）构建的风应力项；2）对流扩散方程的扩散系数设置在0.01-1 m²/s之间，流速平均约1.0 m/s，初始场由实测数据拟合；3）RBPF的线性偏置状态采用卡尔曼滤波器，线性过程噪声设为diag(10^-8,10^-8,10^-8)以保证数值稳定；4）性能度量使用最终误差（末时刻位置误差）与RMSE（全程平均跟踪误差）互补，避免单点或均值偏差；5）特征消融中，随机选择测量通道并相应降低卡尔曼维度，重复5次独立运行以覆盖随机性；6）仿真步长1 s，总时长500 s，粒子数从数百到500变化；7）局限性包括：PDE场需先验数值求解，对复杂环境网格计算成本较高；对流扩散场梯度较弱时定位精度存在基础上限，且RBPF在高粒子数（如400）时方差较大，稳定性受场特征影响。
