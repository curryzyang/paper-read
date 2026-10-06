# MOSAIC-SV: Real-Time Adaptive Identification of Vessel Dynamics for the Control and Deployment of Aquatic Robots

- 区域：精读区
- 排名：3
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Wensen Liu, Jerry Peng, Shravani Vedagiri, Aaron M. Johnson
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03898v1) · [PDF](https://arxiv.org/pdf/2610.03898v1)

## TLDR
MOSAIC-SV is a real-time adaptive identification and control system that starts from a spec-sheet engineering prior, continuously re-estimates a vessel’s hydrodynamic, disturbance, and actuator parameters during closed-loop missions for model-predictive control, and achieves faster, lower-error transit on aquatic robots without dedicated identification trials.

## Abstract
Model-based control of an aquatic robotic platform depends on a hydrodynamic model that is costly to identify and specific to the hull, payload, and conditions it was measured in. Here, we present MOSAIC-SV, a deployable real-time adaptive dynamics identification and control system that identifies a control-sufficient dynamics model from a spec-sheet engineering prior, without dedicated identification trials, and re-estimates it at every control step of a closed-loop mission while the controller plans on it. A physically admissible unscented Kalman filter re-estimates hydrodynamic, disturbance, and actuator parameters at every control step of the closed-loop mission; while a command-dependent consider projection withholds corrections the current command cannot attribute between actuator effectiveness and external force; and a model predictive path integral controller plans on the current estimate. In simulation on a CyberShip II plant, MOSAIC-SV recovers the transit performance of the calibrated model under static mismatch and transient changes, and stays within 20% of its own transit time at the unscaled prior when its inertia or damping prior is wrong by an order of magnitude. In on-water field trials on the Blue Robotics BlueBoat, a twin-thruster catamaran, MOSAIC-SV transits at least 25% faster and predicts its own motion with at least 56% less error than its frozen engineering prior, including under an unmodeled payload. The same MOSAIC-SV system concept was also feasibly deployed on a 6.3-tonne dual outboard monohull.


## 精读解读（中文）
### 一、研究动机
水面机器人基于模型的控制依赖水动力模型，但此类模型辨识成本高且强依赖船体、载荷和工况，换船或加装载荷后需重新辨识。现有在线辨识多需要已知标称模型或专用机动试验，难以在闭环任务中从规格表先验直接部署。MOSAIC-SV 旨在无需专用辨识试验、从工程先验出发，在闭环控制每一步在线重估控制充分模型并让控制器即时使用。

### 二、技术方案（Method）
MOSAIC-SV 采用平面 Fossen 模型，状态包括 NED 位姿与体速度，待估参数为惯性/线性阻尼的 Cholesky 因子、二次阻尼系数、外力偏置和执行器增益/力臂偏差，共21维；先验均值由规格表质量、长度、梁、添加质量因子、参考速度与二次阻尼份额构造，先验协方差约20%。在线流程为每控制步先用 scaled UKF 将上一时刻参数经 Ornstein-Uhlenbeck 过程预测，外力偏置回归先验、其余随机游走；以相邻导航状态一步 RK4 预测作为测量模型做 UKF 更新，并用命令相关 consider projection 在 [F_ext, theta_a] 的弱瞬时敏感方向抑制增益，Joseph 协方差更新保证半正定。随后模型预测路径积分控制器在当前参数估计上规划控制，形成辨识-规划-执行闭环。

### 三、结果（Result）
在 CyberShip II 仿真中，MOSAIC-SV 在静态失配和瞬态变化下恢复标定模型的 transit 性能，且当惯性或阻尼先验错一个数量级时仍保持在其未缩放先验 transit time 的20%以内。BlueBoat 双推进器双体船现场试验中，相比冻结工程先验，MOSAIC-SV 的 transit 至少快25%、自身运动预测误差至少低56%，并能在未建模额外载荷（岩石）下工作。同一系统概念还在6.3吨双舷外单体船上完成可行性部署。

### 四、结论（Conclusion）
研究表明，水面机器人可从规格表工程先验启动，在闭环任务中实时重估物理动力学并直接供 MPPI 规划，无需专用辨识试验，且对数量级先验误差和未建模载荷具有鲁棒性。该框架在小型双体船和大型单体船上均具部署可行性，指向跨船型、跨载荷的即插即用自适应控制。

### 五、方法论与关键技术细节
关键实现包括：参数采用正定 Cholesky 表示并给对角线下限，二次阻尼用 c⊙c 保证非负；先验中双体船添加质量因子为(1.10,1.50,1.15)、单体船为(1.10,1.80,1.25)，二次阻尼份额分别为0.70和0.85，参考速度由设计速度、10°侧滑和3倍船长转弯半径定义；过程模型对外力偏置设0<lambda<1并令Q保持先验方差平稳，对水动力和执行器参数设lambda=0的随机游走；观测噪声R按状态估计器不确定度并膨胀以处理时间相关误差，S求逆前加机器精度级正则；consider projection只抑制当前命令无法区分执行器有效性与外力的修正。局限是依赖导航状态估计质量，执行器模型针对固定方向推进器，6.3吨结果仅为可行性验证，且未在字段中给出计算开销和所有海况的定量覆盖。
