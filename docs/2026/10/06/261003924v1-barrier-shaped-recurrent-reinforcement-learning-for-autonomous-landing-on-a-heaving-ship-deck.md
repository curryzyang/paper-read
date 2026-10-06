# Barrier-Shaped Recurrent Reinforcement Learning for Autonomous Landing on a Heaving Ship Deck

- 区域：精读区
- 排名：5
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Ritwik Shankar, Chiranjeev Prachand, Abhishek, Soumya Ranjan Sahoo
- 机构：Indian Institute of Technology Kanpur
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03924v1) · [PDF](https://arxiv.org/pdf/2610.03924v1)

## TLDR
This paper introduces a barrier-shaped recurrent reinforcement-learning policy—trained with an asymmetric actor-critic that gives only the critic future deck motion—combined with a control-barrier-function stopping margin as both a training reward and runtime safety filter, enabling a UAV to autonomously land reliably and softly on a physically heaving ship-deck emulator.

## Abstract
This paper addresses autonomous landing of unmanned aerial vehicle (UAV) rotorcrafts on a heaving ship deck using a recurrent policy trained via asymmetric actor-critic reinforcement learning: the critic sees 6 s of future deck height during training, while the actor sees only what the onboard sensors provide in flight, a 17-dimensional state made of the vehicle's position, velocity and attitude relative to the deck and outputs world-frame velocity and yaw-rate commands. Training is performed across 4096 parallel simulated environments, followed by fine-tuning in 16 environments with an onboard vision pipeline in the loop. A control-barrier-function (CBF) stopping margin on the deck-relative vertical state is incorporated at two stages: as a reward term during training, where it halves the median simulated contact speed relative to a policy trained without it, and as a runtime safety filter at deployment, evaluated at every control step to abort and retry the descent when the margin is violated. Because the autopilot's disarm logic cannot detect the vehicle resting on a moving deck, proximity-based thrust cutoff at touchdown is commanded directly in the landing pipeline. The proposed approach is validated using a parallel-manipulator-platform-based deck emulator that reproduces the heaving motion of the ship deck (scaled to 0.70 m peak-to-peak, 7.5 s mean period) and a quadcopter UAV with an onboard camera. Across 31 motion-capture and 20 vision-based trials, the UAV landed every time, with median times to contact of 6.5 and 7.3 s; 77% and 50% landed on the first attempt, with mean deck-relative speeds of 0.29 and 0.27 m/s, respectively, at the instant of thrust cutoff, which is the last speed under the policy's control. Supplementary video: https://youtu.be/S5hDkrSZJt4


## 精读解读（中文）
### 一、研究动机
船舶甲板升沉使自主降落从相对位姿跟踪变为时机决策问题：当前相对位姿无法确定未来接触瞬间的相对速度，下降过早或过晚会高速触地；同时运动甲板使自驾仪无法通过静止解除武装，且现有学习式海事降落缺乏运行时安全检查。

### 二、技术方案（Method）
采用非对称 actor-critic 的循环强化学习：actor 以 20 Hz 接收 17 维机载状态（甲板相对位置、速度、姿态四元数、机体系重力和上一指令），经两层 GRU[128,64] 与 32 单元 ELU MLP 输出世界系速度/偏航角速度指令；critic 仅训练时额外获得未来 6 s 甲板高度（120 维）等特权信息，经 GRU[512,256] 估计价值。训练在 4096 个 Isaac Lab 并行环境用 PPO（48 步、6 minibatch、5 epoch、clip 0.2、γ=0.99、λ=0.95）进行约 3 h，并在 16 环境、onboard vision in loop 下微调；底层用 200 Hz 的 Torch PX4-like 级联执行速度设定点。部署时将 CBF 停止裕度作为即时安全检查，每控制步评估甲板相对垂直状态，裕度耗尽则中止下降并重试，触地前 7 cm 直接触发推力切断。

### 三、结果（Result）
在复现记录船舶升沉（0.70 m 峰峰值、平均周期 7.5 s）的并联机械平台和带机载相机的四旋翼上，31 次动捕与 20 次视觉试验全部成功着陆；中位触地时间分别为 6.5 s 和 7.3 s，首次尝试成功率为 77% 和 50%，推力切断瞬间平均甲板相对速度为 0.29 m/s 和 0.27 m/s。加入 CBF 奖励项后，仿真中位接触速度相对无该奖励的策略减半。

### 四、结论（Conclusion）
结果表明，循环策略可从观测历史推断甲板升沉相位并决定下降时机，非对称特权 critic 可把未来甲板运动知识蒸馏给仅用机载观测的 actor，CBF 停止裕度既是训练塑形项也可作为部署时中止/重试安全过滤器。该方法在真实升沉甲板上实现了高成功率、低相对速度着陆，并为学习式海事降落提供了可复现的训练-部署接口。

### 五、方法论与关键技术细节
数据使用 SCONE 五段 1800 s 记录，D1/D2/D4/D5 训练、D3 验证测试，每回合重置采样记录、起点和 0.5-2.5 m 甲板高度偏置并归一化到 0.70 m 峰峰值；观测不含世界原点，动作限制 |v_x,y|≤0.8 m/s、v_z∈[-0.8,1.0] m/s、|ψdot|≤35°/s；奖励含密集居中/姿态/指令正则项、对 CBF 裕度违反的 Huber 惩罚 max(0,-h)/0.25m，以及首次接触力超过 2 N 的稀疏奖励；成功判据强调相对速度不超过 0.5 m/s。关键约束包括：actor 看不到未来甲板高度，只能靠 GRU 记忆；CBF 采用标准形式，未提出新安全学习理论；硬件试验规模 51 次且视觉首次成功率仅 50%，甲板运动为缩比/记录的升沉，未覆盖横摇、纵摇等全耦合海况。
