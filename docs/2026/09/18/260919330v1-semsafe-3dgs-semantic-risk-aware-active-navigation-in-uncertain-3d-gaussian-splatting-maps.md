# SemSafe-3DGS: Semantic Risk-Aware Active Navigation in Uncertain 3D Gaussian Splatting Maps

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee
- 机构：Lehigh University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19330v1) · [PDF](https://arxiv.org/pdf/2609.19330v1)

## TLDR
SemSafe-3DGS introduces a semantic risk-aware active navigation framework that uses class-dependent risk weights to modulate Average Value-at-Risk collision clearances in a unified CBF-QP, jointly enforcing semantically informed safety and trajectory-relevant active perception for robots navigating uncertain 3D Gaussian Splatting maps.

## Abstract
Autonomous robots operating in partially observed environments must navigate safely while acquiring observations that improve future planning. Existing safety formulations generally reason primarily about geometry. Consequently, geometrically similar scene elements may induce comparable control responses despite having different semantic consequences. We present a semantic risk aware safe-active perception framework for navigation in attributed 3D Gaussian maps. Semantic attributes modulate an Average Value-at-Risk collision clearance model through class dependent risk weights, allowing safety-critical Gaussian primitives to receive greater influence in the composite barrier. The resulting weighted clearances are aggregated into a control barrier function, while a trajectory-relevant active perception barrier promotes observations that reduce geometric map uncertainty along the robot's anticipated motion. Both objectives are integrated in a unified CBF-QP that enforces semantic risk-aware collision avoidance as a hard constraint while relaxing information acquisition when it conflicts with safety or task progress. Experiments demonstrate efficient safety constraint, improved navigation through active perception, semantic dependent trajectory adaptation, and real-robot execution under Ackermann dynamics.


## 精读解读（中文）
### 一、研究动机
现有3D高斯溅射导航的安全约束主要围绕几何距离展开，几何构型相似但语义后果不同的物体可能触发相近控制响应，导致语义危险物未被优先规避。部分观测环境下机器人还必须主动观测以降低未来规划相关区域的不确定性，而信息获取常与安全、任务进度冲突，因此需要语义风险感知的安全-主动感知统一框架。

### 二、技术方案（Method）
方法以带属性3D高斯地图为环境表示，每个高斯包含位置、旋转、尺度、不透明度、颜色和语义属性，机器人通过在线RGB-D观测持续更新地图。对每个高斯计算机器人到其距离分布的下尾AV@R净空，并用类别与置信度映射的正语义风险权重kappa进行调制，得到语义风险净空rho=kappa(AV@R-r_rob)，再以soft-min复合控制屏障h_s平滑聚合全部高斯并施加CBF硬安全约束。主动感知部分以参考轨迹为中心生成随语义风险变化的局部掩膜，仅在轨迹相关高斯上计算Fisher信息效用I=tr(H H_prior^{-1})，构造感知屏障h_p=I-I_c；最终在统一CBF-QP中最小化对参考控制与感知松弛delta的偏差，安全约束不可松弛，感知约束通过delta在冲突时软化。

### 三、结果（Result）
在四个3DGS场景的安全屏障对比中，所提方法安全率约98%至100%，与SAFER-Splat相近，但计算时间由30.9至186毫秒降至约1.5至2.8毫秒，最小距离与控制器偏差呈现可调权衡。在InteriorGS闭环导航中，所提方法74秒到达目标，优于CAAP的82秒和无主动感知的103秒，路径长度相近约16.4至16.9米，平均速度0.212米每秒，平均安全屏障0.724，平均感知屏障0.005，而CAAP为-0.275。真实Ackermann机器人室内3DGS实验中安全屏障h_s全程为正，感知屏障h_p、松弛delta和自适应权重显示安全-感知在线交互，验证了语义依赖轨迹调整与实机可行性。

### 四、结论（Conclusion）
该工作将语义风险权重嵌入AV@R净空与复合控制屏障，并把轨迹相关主动感知作为可松弛软约束，统一在一个CBF-QP中实现安全优先的信息获取。实验表明该方法能在保持安全硬约束的同时提高导航效率、减少保守行为，并支持语义相关避障和真实Ackermann平台部署。

### 五、方法论与关键技术细节
关键细节包括：使用Splatfacto训练的100K至500K高斯地图与在线RGB-D更新，安全对比采用双积分器动力学，感知对比采用unicycle动力学，实车为Ackermann转向机器人；语义风险权重kappa越小表示风险越高，soft-min温度beta_s引入约log M_k/beta_s的保守下界，感知掩膜半径r_tau=r_min+beta1 exp(-beta2 min rho)，信息效用基于高斯参数Fisher信息与先验H_prior的逆的迹，阈值I_c控制感知屏障。统一QP中安全CBF约束永不松弛，感知CBF以delta和lambda_delta软约束，并受控制限幅；复杂度主要随高斯数量M_k线性增长，soft-min注意力每步计算毫秒级，但语义权重、AV@R分位数、beta_s、I_c与lambda_delta需标定，性能依赖地图质量、语义置信度和Fisher近似及部分观测条件。
