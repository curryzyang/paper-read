# Lambda-Hold Control: Human-Like Movement Emerges from a Minimal Task Reward in Predictive Musculoskeletal Simulation

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Jun Hyuk Lee, Chihyeong Lee, Jooeun Ahn
- 机构：Seoul National University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17030v1) · [PDF](https://arxiv.org/pdf/2608.17030v1)

## TLDR
The λ-hold controller, which uses physiologically grounded equilibrium-point threshold lengths and intermittent, phase-locked control to enable efficient exploration, allows a muscle-actuated skeletal model to learn human-like sprinting from only a minimal forward-velocity reward within about an hour of training.

## Abstract
The massive overactuation in the human musculoskeletal system makes it challenging to train musculoskeletal models to generate human-like motion via reinforcement learning, primarily because exploration in the resulting high-dimensional and redundant action space is extremely inefficient. To address this problem, we propose the $λ$-hold controller, inspired by the equilibrium-point (EP) hypothesis, which has been widely supported by extensive evidence from human motor control studies. The policy's control variable is the per-muscle EP threshold length $λ$, from which a stretch-reflex recruitment law computes the muscle excitations automatically. Holding each $λ$ over an interval of the gait phase also sharply reduces the frequency at which the policy must be queried. Consequently, the controller, to our knowledge for the first time, enables a muscle-actuated skeletal model to learn human-like sprinting using only a minimal reward within an hour of training. The efficient exploration through the proposed $λ$-hold controller is not merely an engineering trick but an approach grounded in physiology, bringing together the EP hypothesis, intermittent control, and optimal feedback control. Beyond encapsulating human-like behavior in predictive simulation, this achievement contributes to developing a learnable model of the human motor controller.


## 精读解读（中文）
### 一、研究动机
人体骨骼肌肉系统存在严重的过驱动与肌肉冗余，直接以肌肉 excitation 作为强化学习动作空间时，高维且多对一映射导致探索效率极低，难以生成类人运动。受平衡点假说启发，需要一种能将协调性内建于控制变量、降低决策频率的控制器，从而仅用最小任务奖励即可学习类人奔跑。

### 二、技术方案（Method）
采用 H2190 三维肌肉骨骼模型（21自由度、90块肌肉-肌腱单元），在 SCONE/Hyfydy 中以0.01 s步长仿真；策略直接输出每块肌肉的平衡点阈值长度 λ_i（范围[0.6,1.2]），并由牵张反射募集律 e_i = clamp(G_tonic(ℓ_i-λ_i)+G_phasic[v_i]+,0,1) 自动计算肌肉 excitation，其中增益固定为 G_tonic=50、G_phasic=0.1。控制采用 λ-hold：仅在足底反作用力事件（着地/离地）及事件间的子决策点重新查询策略，并在0.05-0.15 s保持区间内由反射律持续产生 excitation；为了不绑定固定节律，子决策点由最近同类事件间隔的一半估计。策略用 SAC+gSDE 训练，观测为432维生理信号（肌长、速度、肌腱力、足底接触/GRF、关节角/角速度、前庭信号及当前 λ 的 efference copy），奖励仅为 r=exp(v_x)·exp(-(v_z/0.1)^2)，不使用参考运动、代谢代价、课程或对称辅助。

### 三、结果（Result）
在预测性肌肉骨骼仿真中首次仅用前向速度这一最小奖励，在一个小时内学会协调、类人化的冲刺运动；相比 excitation-level 控制，按仿真步而非决策步比较时，λ-hold 更早更广地覆盖联合空间状态分布，所需策略决策数大幅减少。学习速度提升显著，可在单台工作站约1小时完成训练。

### 四、结论（Conclusion）
结果表明，将控制变量从肌肉 excitation 改为具有生理基础的平衡点阈值长度 λ，并让牵张反射填补保持区间内的控制，是一种可行且高效的神经运动控制建模思路。它并非单纯工程技巧，而是融合平衡点假说、间歇控制与最优反馈控制，为可学习的、可解释的人类运动控制器模型提供了新路径。

### 五、方法论与关键技术细节
关键实现细节：模型为 H2190，90块肌肉；仿真步长0.01 s；λ 界限[0.6,1.2]，反射增益对所有肌肉共享且固定；决策点绑足底GRF事件并插入子点，保持区间0.05-0.15 s，以避免固定时钟限制步频；hold 不是 action repeat，因为区间内 excitation 仍随 ℓ、v 经反射律变化。训练使用 SAC+gSDE，超参与 SAC 基线相同，DEP-RL 基线使用 DEP+MPO；观测排除 excitation/activation，因为它们由 λ、ℓ、v 完全决定。奖励无上限地鼓励前向速度，并用窄高斯惩罚侧向速度。局限性：决策点依赖于步态的周期性事件，对于无周期结构的任务如何设置仍需研究；反射增益或需按任务调整。
