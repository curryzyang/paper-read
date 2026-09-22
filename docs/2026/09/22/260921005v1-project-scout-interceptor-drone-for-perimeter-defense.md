# Project SCOUT: Interceptor Drone for Perimeter Defense

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Azmain Yousuf, Siwei Cai, Knut Peterson, Lifeng Zhou, David Han
- 机构：Drexel University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.21005v1) · [PDF](https://arxiv.org/pdf/2609.21005v1)

## TLDR
SCOUT is an onboard ROS-integrated perception-and-control framework that combines TensorRT-accelerated drone detection, ByteTrack association, and robust track filtering to enable real-time closed-loop interceptor-UAV perimeter defense, achieving valid target detections in 92.2% of frames during real-world “goalkeeping” flights.

## Abstract
The rapid proliferation of unauthorized unmanned aerial vehicles (UAVs) has created a growing need for robust, jamming-resistant counter-UAV systems for perimeter defense. This paper presents \textbf{SCOUT} (Spatial Computation for Optimized UAV Tracking), a ROS-integrated onboard perception and control framework for real-time aerial defense against incoming UAVs. SCOUT performs visual detection, target association, track filtering, and control command generation directly onboard the defender UAV, without relying on external sensing infrastructure or ground-station computation. To provide stable control inputs, the perception pipeline combines TensorRT-accelerated drone detection with ByteTrack-based association and a lightweight track-retention state machine. The state machine rejects abrupt target jumps and maintains short-term target continuity during temporary detection degradation, reducing unstable control responses caused by false detections or target switching. We evaluate the proposed architecture through an integrated hardware deployment executing a planar ``goalkeeping'' interception strategy. In this setting, the defender UAV tracks the incoming target and adjusts its motion to maintain a blocking configuration near the protected boundary. Real-world flight results show that SCOUT maintains valid target detections for 92.2\% of frames while operating at real-time onboard detection rates, demonstrating the feasibility of visual tracking and closed-loop control for UAV perimeter defense. A video demonstration of the end-to-end perimeter defense operation is available online. https://figshare.com/s/497befc033091fc0b84f


## 精读解读（中文）
### 一、研究动机
未经授权无人机快速扩散，关键基础设施与限制空域面临新威胁，传统电子干扰、欺骗、弹丸或导弹拦截对线导与低成本无人机日益无效。防御无人机拦截成本有效，但要求机载感知与控制在严格实时、尺寸、重量和功耗约束下可靠运行，并在快速相对运动、尺度变化和视觉退化下输出稳定控制输入。现有系统多依赖外部雷达/射频或地面站计算，或机载推理速度与跟踪鲁棒性不足，因此需要统一的完全机载边缘感知到控制流水线。

### 二、技术方案（Method）
SCOUT 采用感知到控制的顺序方案：先训练 YOLO26n 检测器，用 DroneHunter、Det-Fly、DUT Anti-UAV、LRDDv3 共 184.4k 图像预训练 50 epoch（AdamW，lr 1e-3，batch 48），再在自采 3,931 张 DJI Neo 图像上微调 10 epoch；随后部署于 ROS 集成流水线，包括异步单元素队列丢帧取最新帧、TensorRT FP16/ONNX 编译与层融合加速推理、ByteTrack 双池关联（高置信≥0.50，低置信≥0.06）、顺序几何滤波状态机（归一化框中心，拒斥 d_t>2D_{t-1} 且置信不高于 K=10 帧历史最大值的候选，T_stale=0.5s 清除丢失轨迹）。最后将滤波后的归一化目标中心误差 e_u=c_x-0.5、e_v=c_y-0.5 输入饱和 PD 控制律，生成仅横向 v_y 与垂直 v_z 的速度命令，v_x=0、ω_z=0，经死区和高度钳位后通过 MAVROS 在 OFFBOARD 模式发送给飞控。

### 三、结果（Result）
真实硬件飞行中，SCOUT 执行平面“守门员”拦截策略，防御无人机跟踪来袭目标并调整运动以在保护边界附近维持阻挡配置。系统在实时机载检测率下对 92.2% 的帧保持有效目标检测，且 TensorRT 编译引擎相比初始 PyTorch 实现将完整流水线性能提升约 114%。这些结果验证了视觉跟踪与闭环控制用于 UAV 周界防御的可行性。

### 四、结论（Conclusion）
SCOUT 表明，完全机载、边缘加速的检测-关联-滤波-控制流水线可在嵌入式无人机上实现实时周界防御，并减少误检或目标切换导致的不稳定控制响应。其核心贡献是面向闭环节点的临时一致目标中心估计，而非孤立帧级检测，从而支撑防御无人机的自主拦截机动。该工作为后续更复杂三维拦截与多目标防御提供了可部署的系统基线。

### 五、方法论与关键技术细节
数据与训练：四数据集预训练共 184.4k 图像（DroneHunter 58.6k、Det-Fly 13.3k、DUT Anti-UAV 10k、LRDDv3 102.5k），自采 DJI Neo 3,494 训练/437 验证，YOLO26n 预训练 50 epoch、微调 10 epoch，AdamW lr=1e-3、batch=48，RTX 3090 与 Threadripper 3960X。部署：Jetson Orin NX 16GB 最大性能模式，720p 流、检测输入 736、batch=1，TensorRT FP16/ONNX、垂直水平层融合，计时覆盖 ROS 帧检索到消息发布；ByteTrack 阈值 S_min=0.06、高置信 0.50，几何滤波使用归一化框、d_t>2D_{t-1} 且 S_t≤K=10 历史最大置信，T_stale=0.5s；控制为横向-垂直平面饱和 PD、死区、速度/高度钳位，OFFBOARD 经 MAVROS 接受速度命令，检测过期则零速度。局限：仅验证平面守门员策略，前向速度与偏航率置零，未展示完整三维追击、多目标或对抗机动能力，性能依赖检测器泛化与视觉条件。
