# Curriculum-Driven Deep Reinforcement Learning for Autonomous Far-Range Rocket Landing

- 区域：精读区
- 排名：2
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Atin Chowdhury, Piyush Joshi
- 机构：Indian Institute of Information Technology, Sri City
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35954v1) · [PDF](https://arxiv.org/pdf/2610.35954v1)

## TLDR
This paper proposes a curriculum-driven deep reinforcement learning framework that uses a three-stage curriculum, critic warm-up, rehearsal to prevent forgetting, rotation-matrix observations, and a redesigned bounded reward to achieve far-range autonomous rocket navigation from 1,000–1,500 units and precise soft landing with a 99.98% success rate.

## Abstract
Autonomous vertical landing of reusable launch vehicles is a critical yet formidable challenge in aerospace engineering, primarily due to highly nonlinear dynamics, stringent precision require- ments, and inherent environmental uncertainties. While reinforcement learning (RL) has emerged as a promising alternative to traditional model-based control, existing approaches frequently rely on flat training paradigms and highly simplified initial conditions, drastically limiting their real-world applicability. This paper proposes a comprehensive curriculum-driven deep reinforcement learning framework designed to master both far-range navigation and precision landing. By employing a three-stage curriculum augmented with a critic warm-up procedure and a rehearsal mechanism to prevent catastrophic forgetting, alongside a high-dimensional observation vector utilizing a full 3 X 3 rotation-matrix, the agent is trained to navigate from an initial horizontal distance of 1,000 to 1,500 units vastly farther than prior benchmarks before executing a soft touchdown. Crucially, we intro- duce a redesigned reward function that reduces unnecessary computational overhead and addresses limitations of earlier formulations, including poorly calibrated reward components and potentially conflicting optimization objectives. The redesigned function bounds the per-step reward magnitude by (O(1)), while its progress term accumulates the total distance closed over the trajectory. The available 100,000-episode results report a 99.98% success rate for the proposed policy and 68.31% for the baseline under the evaluation conditions. In the evaluation, the proposed policy retained 69.1% of its initial fuel capacity and achieved a mean final distance from the pad centre of 7.07 units, compared with 13.10 units for the baseline. Landing visualizations are available in Video 1 and Video 2.


## 精读解读（中文）
### 一、研究动机
可重复使用运载火箭垂直着陆面临强非线性动力学、严苛精度与环境不确定性；现有强化学习方法多采用平坦训练和高度简化的初始条件，横向远距离接近被弱化，难以外推到真实任务。本文因此要让智能体在1000至1500单位的初始水平距离下同时掌握远距离导航与精确软着陆。

### 二、技术方案（Method）
在继承基线常数的确定性60 Hz逐帧物理仿真器中，每3帧聚合为一次决策，状态为29维向量，含完整3×3旋转矩阵、机体坐标系位置与速度投影、高度误差、径向速度、制动余量和近台精细量；动作为推力二值、俯仰三值与滚转三值组成的18种联合离散动作。训练采用三阶段课程：远距离接近至悬停点、近台软下降、完整远距着陆，阶段间转移权重，并用critic预热和排练机制防止灾难性遗忘；奖励按阶段设计，远距阶段以距离进展、速度包络和推力对齐塑形，着陆阶段跟踪软下降参考速度并加入近地姿态、台距和水平速度惩罚。策略在仿真中通过试错优化，推理时仅用观测直接输出联合动作。

### 三、结果（Result）
在可用10万回合评估中，所提策略成功率99.98%，基线68.31%；最终距台中心平均7.07单位，基线13.10单位；保留初始燃料69.1%。这些指标表明在更远初始距离下仍能高成功率软着陆，并兼顾精度与燃料。

### 四、结论（Conclusion）
三阶段课程、critic预热与排练、旋转矩阵观测和重设计的O(1)奖励共同支撑远距自主着陆，显著优于基线；但结论基于确定性仿真与特定离散动作和奖励设定，真实环境鲁棒性与sim-to-real仍需验证。

### 五、方法论与关键技术细节
仿真常量包括重力-0.007、推力0.02、角阻尼0.985、倾斜上限80°、着陆高度13、台半径16、垂直速度不低于-0.15、水平速度不高于0.25、燃料1000（基线500）；成功需同时满足倾角不超过10°、距台中心不超过16、vz不低于-0.15、vh不高于0.25。奖励将每步幅值约束为O(1)，手工常数由15降至8，进展项累计轨迹闭合距离（阶段三约+9缩放回报），制动包络用v_cap=sqrt(2A_H d_h)+0.05，软下降参考v_des=-max(0.07,sqrt(2*0.0078*h))，阶段三关闭倾角惩罚。训练含权重转移、critic预热、排练混合；评估10万回合。局限是确定性仿真、无真实飞行与环境扰动验证、离散动作与燃料翻倍设定，奖励权重仍为人工设计。
