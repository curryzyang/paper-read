# Extending the Speed Limit of Quadrupedal Locomotion via Refined Actuator Modeling and Adaptive Command Scheduling

- 区域：精读区
- 排名：9
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Yucheng Tao, Shaowen Cheng, Guorong Lan, Yanyan Yuan, Yongbin Jin, Hongtao Wang
- 机构：ZJU-Hangzhou Global Scientific and Technological Innovation Center, MirrorMe Robotics Co., Ltd., Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13289v1) · [PDF](https://arxiv.org/pdf/2609.13289v1)

## TLDR
This paper presents a high-speed quadrupedal locomotion framework that combines refined actuator modeling of high-speed voltage coupling and magnetic saturation with a two-stage curriculum and adaptive command scheduling, enabling the 36.5 kg BlackPanther2 robot to achieve record sprinting speeds of 13.2 m/s on a treadmill and 11.65 m/s outdoors.

## Abstract
Achieving high-speed locomotion in quadrupedal robots remains highly challenging, as actuators operate near their physical limits and exhibit pronounced nonlinearities. However, many existing methods neglect actuator nonlinearities and physical constraints during training, leading to a significant sim-to-real gap under highly dynamic motions and limiting achievable performance. To address this issue, we propose a high-speed locomotion framework that reduces sim-to-real discrepancies and stabilizes learning over a wide command distribution. A refined actuator model explicitly captures high-speed voltage coupling and magnetic saturation, enabling a more accurate representation of the torque-speed envelope. In addition, a reinforcement learning framework incorporating a two-stage curriculum and adaptive command scheduling (ACS) ensures stable training. Experiments on the 36.5 kg quadruped BlackPanther2 (BP2) demonstrate speeds of up to 13.2 m/s on a treadmill and 11.65 m/s outdoors, establishing a new state-of-the-art and, to the best of our knowledge, a world record for quadrupedal robot locomotion. The results further highlight the importance of accurate actuator modeling in preventing non-physical policy exploitation, and show that ACS improves robustness without sacrificing performance.


## 精读解读（中文）
### 一、研究动机
高速四足运动时执行器接近物理极限并呈现强非线性，但现有训练常忽略执行器非线性与物理约束，导致高速动态下sim-to-real差距大且性能受限；同时从静止到10 m/s以上的宽指令分布使DRL训练不稳定、收敛差，难以兼顾性能与鲁棒性。

### 二、技术方案（Method）
方法上先建立精细执行器模型：在同步dq坐标系采用i_d=0，保留d轴与q轴电压，用电压椭圆约束v_d^2+v_q^2≤(γV_bus/√3)^2并解二次不等式得到临界转速ω_c，从而刻画受d轴电压耦合而收缩的力矩-速度包络，同时用τ_output=τ_c(1-α|τ_c|/τ_m)建模磁饱和；训练采用非对称actor-critic与VAE估计器，从历史观测推断16维隐变量z和8维结构化估计向量（线速度、基座高度、足端接触），actor输入45维本体感知，critic输入52维含仿真真值；课程为两阶段：Stage I从[-1,1]扩到[-2,6] m/s，Stage II扩到[-2,12] m/s并加入自适应权重正则，ACS根据机器人瞬时速度动态约束指令邻域而非固定加速度上限；仿真中动作映射为关节力矩并受执行器极限约束，硬件部署时低层电机控制器直接跟踪指令力矩。

### 三、结果（Result）
在36.5 kg四足机器人BlackPanther2上实现跑步机13.2 m/s、户外11.65 m/s的冲刺速度，作者称其刷新四足机器人运动速度的state-of-the-art与世界纪录；结果表明精确执行器建模能防止策略利用非物理仿真漏洞，ACS在不牺牲性能的前提下提高鲁棒性，并显著降低高速运动中的不稳定。

### 四、结论（Conclusion）
该工作说明，将高速执行器非线性与物理可行性边界显式纳入RL训练，并配合自适应指令调度，是把四足机器人推向物理速度极限的关键；精细力矩-速度包络可缩小高速sim-to-real差距，两阶段课程与ACS则在宽指令范围内稳定学习，为高动态电驱四足控制提供了可落地范式。

### 五、方法论与关键技术细节
关键实现包括：采用γ=0.95电压利用系数、i_d=0策略，电压约束保留v_d和v_q并求解ω_c二次方程，磁饱和修正中α由离线力矩-电流数据拟合；RL使用VAE推断z∈R^16和估计向量∈R^8，actor观测45维（角速度、重力、指令、关节位置/速度、上一动作），critic 52维含仿真真值；线速度指令范围[-2,12] m/s、角速度[-1,1] rad/s，Stage I为[-1,1]到[-2,6] m/s，Stage II到[-2,12] m/s，奖励含线/角速度跟踪、基座高度/姿态/关节功率/动作平滑/足滑/偏航率等多项分阶段权重；局限性在于执行器模型仍是低维结构化近似且依赖离线辨识参数，摘要与预览未报告复杂地形、负载变化和长期耐久性下的泛化。
