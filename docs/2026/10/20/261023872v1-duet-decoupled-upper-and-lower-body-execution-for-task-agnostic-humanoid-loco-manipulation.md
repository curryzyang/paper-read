# DUET: Decoupled Upper- and Lower-Body Execution for Task-Agnostic Humanoid Loco-Manipulation

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Kapalik Khanal, Biswash Khatiwada, Stephen Afrifa, Fan Wu, Ramesh Bahadur Bist
- 机构：North Carolina State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23872v1) · [PDF](https://arxiv.org/pdf/2610.23872v1)

## TLDR
DUET is a decoupled humanoid loco-manipulation framework in which a reinforcement-learning lower-body controller stabilizes and moves a Unitree G1 while treating the arms only as observations, allowing interchangeable manipulation policies such as vision-language-action models to control the upper body without retraining or modifying the balance controller.

## Abstract
Changing a humanoid robot's manipulation policy should not require retraining the controller that maintains the robot's balance. This study introduces DUET, a decoupled execution framework that enables locomotion and manipulation controllers to operate simultaneously by combining their commands only at the robot interface. A reinforcement-learning locomotion policy controls the 12 leg joints and a waist yaw joint, tracking planar velocity, turning rate, and pelvis height from deep crouching to upright standing on a 23-degree-of-freedom Unitree G1. The 10 arm joints are excluded from the action space, while their positions and velocities are included only as observations, so that any compatible manipulation policy that generates arm-joint targets can control the upper body, and the locomotion policy keeps the lower body stable without requiring shared training or direct coordination. This study demonstrates the modular approach on hardware by pairing the same locomotion checkpoint with two different vision-language-action models, GR00T N1.7 and pi0.5. In simulation evaluation, the locomotion controller kept the robot's lower body stable with no falls while tracking the commanded planar velocity, yaw rate, and pelvis height with errors of 0.186 m/s, 0.142 rad/s, and 0.016 m, respectively. Ablation studies identify the upper-body pose curriculum as the dominant component, and removing this training step reduces episode survival from 20.0 to 7.4 seconds and increases the fall rate to 6.06 per environment minute. Robustness tests show no falls under pushes of up to 1.0 m/s within the trained payload range, and no falls at twice the payload limit for pushes below 0.7 m/s. These results show that a manipulation policy can be exchanged without retraining, restarting, or otherwise touching the layer that keeps the robot upright.


## 精读解读（中文）
### 一、研究动机
人形机器人常把移动与操作分开开发，但现有整身策略或显式协调方案会把操作策略与维持平衡的控制器耦合，导致更换操作任务或策略时需要联合训练、适配甚至重训。作者希望把下肢稳定做成可复用的移动层，使任意兼容的操作策略都能在不触碰运动控制器的前提下驱动上身。

### 二、技术方案（Method）
DUET在23自由度Unitree G1上运行两个独立进程：RL运动策略以50 Hz控制12个腿关节和1个腰偏航关节，输出相对于标称姿态的13维关节位置偏移，由200 Hz关节PD跟踪；10个手臂关节不进入动作空间，仅以位置和速度作为71维观测的一部分。运动策略跟踪平面速度、偏航率和骨盆高度命令，高度范围0.18至0.73 m，移动时限制在0.60 m以上，并用20项奖励、上身姿态课程、镜像对称增强和域随机化在MuJoCo并行仿真中训练后导出为自描述ONNX。部署时两个进程通过DDS通信，运动进程是底层命令话题的唯一写入者，每周期从单独的手臂话题复制最近的手臂目标与增益，操作策略约15 Hz发布动作块，运动进程在间隔内保持上一目标，因此手臂策略可替换且其停顿不会阻塞腿部。

### 三、结果（Result）
仿真中运动控制器无跌倒，平面速度、偏航率和骨盆高度跟踪误差分别为0.186 m/s、0.142 rad/s和0.016 m；消融显示上身姿态课程贡献最大，移除后回合存活时间从20.0 s降至7.4 s，跌倒率升至每环境分钟6.06次。鲁棒性测试中，在训练负载范围内承受最高1.0 m/s推力无跌倒，在2倍负载上限下低于0.7 m/s推力仍无跌倒；硬件上同一运动检查点成功配对了GR00T N1.7和pi0.5两个VLA。

### 四、结论（Conclusion）
DUET证明下肢稳定层可以与上身操作策略解耦，操作策略的更换无需重训、重启或修改维持平衡的控制器，从而把人形机器人下肢变成可复用的移动能力层。该设计以放弃部分整身协调和手臂作为动量执行器的能力为代价，换取操作模型的可插拔性。

### 五、方法论与关键技术细节
关键实现包括：动作仅覆盖13个下肢关节，手臂状态仅作观测；观测含基座角速度、投影重力、速度命令、步态相位、23关节位置速度、上一动作和骨盆高度命令；奖励含速度、偏航率、高度跟踪及姿态、步态、关节限位、动作平滑和终止惩罚，终止权重为-200；训练采用上身六类锚点姿态课程、镜像数据增强与镜像一致性惩罚、域随机化。约束与局限包括手臂目标以限速方式原样透传、深蹲仅限静止命令、移动时高度不低于0.60 m，且解耦相对整身控制存在姿态代价，硬件验证主要是同一运动检查点搭配两个VLA的模块化演示。
