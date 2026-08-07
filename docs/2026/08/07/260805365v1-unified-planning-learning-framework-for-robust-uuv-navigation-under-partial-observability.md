# Unified Planning-Learning Framework for Robust UUV Navigation Under Partial Observability

- 区域：精读区
- 排名：1
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Md Ether Deowan, Eleni Kelasidi
- 机构：NTNU
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05365v1) · [PDF](https://arxiv.org/pdf/2608.05365v1)

## TLDR
A unified observation-only hybrid planning-learning framework for UUV navigation integrates sonar-based occupancy mapping, clearance-aware global planning, and risk-aware RL local control with behavior-tree distillation and latent uncertainty modeling to achieve robust, safe autonomy under partial observability in dynamic underwater environments.

## Abstract
This paper presents an observation-only autonomy framework for Unmanned Underwater Vehicles (UUVs) navigation in dynamic underwater environments that integrates persistent occupancy mapping, global clearance-aware planning, and risk-aware local control. The proposed pipeline constructs occupancy maps solely from onboard sonar and depth image observations, adapts a clearance-constrained global planner (GP) to provide long-horizon structure, and integrates a reinforcement learning (RL) policy to handle short-range tracking and reactive avoidance. To further support decision-making under partial observability, the system learns a compact latent state representation from onboard sensor data, encoding environmental structure, obstacle dynamics, and uncertainty. Behavior tree (BT) distillation with staged supervision is introduced to improve safety and training stability, while an uncertainty-calibrated distillation mechanism reweights teacher guidance using online latent-model uncertainty, emphasizing uncertain regimes during learning, with time-to-collision (TTC) and clearance cues remaining explicit in planning and local policy features. To demonstrate the efficacy of the framework, a reproducible multi-seed evaluation protocol is established in high-fidelity GPU-accelerated simulation using NVIDIA Isaac Sim, and performance is benchmarked against BT-only and standard RL baselines. The results obtained demonstrate improved robustness and safety under dynamic conditions, thus providing a general pipeline with a unified hybrid planning learning architecture and a reproducible methodology for robust UUV autonomy under partial observability.


## 精读解读（中文）
### 一、研究动机
水下无人潜航器（UUV）在部分可观测、动态且存在感知不确定性的环境中导航时，传统基于图搜索或采样的全局规划方法依赖已知环境和精确地图，反应式控制器缺乏长远预见，而纯深度强化学习方法样本效率低、训练早期探索不安全且常使用特权状态，现有工作多将建图、规划、控制割裂评估，缺乏端到端的观测-only自主栈，因此需要一种统一混合规划-学习框架来提升动态环境下的鲁棒性与安全性。

### 二、技术方案（Method）
提出一种观测-only的混合分层自主导航框架，输入仅包括前视声呐、深度图像、IMU、速度和路径点等机载观测，不依赖任何仿真器特权信息。首先，基于声呐命中/自由空间证据和深度一致性更新静态与动态双层占用栅格图，并计算在线清障场与风险图。其次，全局规划器在可通行且最小清障约束的单元格上使用Voronoi路径合成（失败时回退RRT），并采用事件触发重规划（包括卡死检测、TTC安全事件、路径冲突预测）。然后，局部策略采用强化学习（PPO）控制，策略输入包含路径跟踪误差、体坐标系速度、扇区化距离/TTC特征以及潜在世界模型特征；奖励函数综合进度、清障、TTC、姿态、能量和终端成败项，并在线强制执行最小距离和TTC硬安全约束。同时，训练阶段引入行为树（BT）蒸馏，通过带有阶段监督的教师策略引导RL训练，并使用基于潜在模型不确定性的校准机制动态调整蒸馏权重，突出高不确定/高风险区域。全部实验在NVIDIA Isaac Sim高保真GPU加速仿真中进行多随机种子评估，并对比BT-only和标准RL基线。

### 三、结果（Result）
在动态水下环境和部分可观测条件下，所提统一规划-学习框架相比BT-only和标准RL基线展现出更高的鲁棒性和安全性；实验表明，通过BT蒸馏和不确定性校准可显著提升样本效率和训练稳定性，降低碰撞率并提高任务完成成功率；多随机种子评估协议保证了结论的可复现性。论文未给出具体数值指标，但强调框架在动态障碍、感知噪声和地图不确定性下获得了改进的导航表现。

### 四、结论（Conclusion）
该工作验证了将基于清障的全局规划、潜在世界模型与RL局部控制以及BT蒸馏结合的混合架构，能够有效应对UUV在部分可观测动态环境下的自主导航挑战，提供了统一的观测-only端到端自主栈和可复现的评估方法，为鲁棒水下自主导航提供了一条通用技术路线。

### 五、方法论与关键技术细节
关键实现细节包括：①占用更新采用静态/动态双层记忆，动态层仅从声呐时序不一致和Doppler相对运动推断，仿真器stamp项在实验中禁用以保证纯观测约束；②全局规划使用Voronoi最大化清障而非A*，避免网格路径贴障放大声呐误差，RRT作为连接失败回退；③重规划触发条件含2.5秒常速预测的路径冲突；④局部策略特征包括潜在世界模型的一步预测残差和不确定性代理；⑤奖励系数手动挑选后固定，不做自动搜索，硬安全约束（最小距离d_coll和TTC阈值τ_coll）违反即终止；⑥BT蒸馏采用阶段式监督和不确定性校准权重λ_t^risk，教师信号按在线潜在模型不确定性重加权；⑦评估使用多随机种子、NVIDIA Isaac Sim高保真仿真，但需注意仅限于仿真环境，未涉及真实湖/海试验，且未报告具体数值指标和计算复杂度。
