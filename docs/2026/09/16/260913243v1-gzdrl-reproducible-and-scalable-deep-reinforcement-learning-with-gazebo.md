# GzDRL: Reproducible and Scalable Deep Reinforcement Learning with Gazebo

- 区域：精读区
- 排名：4
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Amal Dev Haridevan, Junjie Kang, Jinjun Shan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13243v1) · [PDF](https://arxiv.org/pdf/2609.13243v1)

## TLDR
GzDRL is a single-process, middleware-free reinforcement learning framework for Gazebo that directly synchronizes agent actions with physics updates to enable deterministic, high-throughput, reproducible, and scalable robot training, validated by benchmarks and zero-shot sim-to-real transfer to a quadrotor.

## Abstract
We present GzDRL, a novel single-process reinforcement learning (RL) framework for Gazebo that overcomes longstanding bottlenecks in scalable, reproducible robotics experimentation. Unlike conventional middleware-based RL-Gazebo integrations that suffer from nondeterminism and irreproducibility, GzDRL introduces a systematic, middleware-free environment-stepping mechanism that directly synchronizes agent actions and physics updates. This design enables deterministic, high-throughput data collection, efficient vectorization, and reproducible RL training and evaluation. Comprehensive benchmarks demonstrate that GzDRL achieves the highest workstation throughput among the evaluated frameworks while remaining competitive with GPU-accelerated simulators on laptop hardware, and maintains precise agent-environment synchronization, multi-agent scalability, and experiment-level reproducibility. We further validate sim-to-real transfer by deploying learned policies directly onto a physical quadrotor, without fine-tuning. Our results establish GzDRL as an accessible and reproducible platform for advancing RL in robotics and automation.


## 精读解读（中文）
### 一、研究动机
传统基于ROS或Gazebo Transport等中间件的RL-Gazebo集成存在动作与观测配对延迟，可能引入非马尔可夫效应并损害学习稳定性、样本效率与可复现性，同时中间件通信限制并行吞吐。GPU加速仿真器虽然并行度高，但缺少Gazebo在真实机器人模型、模块化物理、传感器和ROS部署流程上的生态兼容性。因此，需要一种可直接嵌入Gazebo、确定性高吞吐、可复现且可扩展的强化学习框架。

### 二、技术方案（Method）
GzDRL是单进程框架，每个环境包含一个gz::sim::Server与一个Gazebo world，由DRLServer直接同步策略动作与物理更新；对策略动作先经Pi预处理，在K个物理步内由可选控制器Ci基于最新状态产生控制u，并通过Server::Run(1)推进仿真，PostUpdate阶段由DRLHelperSystem读取位姿、速度、加速度、传感器和接触信息，支持随机化与重置，最后由Psi输出观测、奖励和终止标志。向量化提供两条路径：Python端AsyncDRLServerPool使用任务队列、每个DRLServer一个C++工作线程、CPU绑定并释放GIL；C++端GazeboPool扩展EnvPool，维护NE个环境、NT个线程、动作队列和轮转状态缓冲，支持NB≤NE部分批处理、零拷贝NumPy观测视图，以及多机器人联合观测、团队奖励和共享终止。平台还支持多旋翼6-DoF刚体动力学、13维状态、一阶执行器滞后，以及Velocity、Jerk、Snap层级和RPM、SRT、CTBT、CTBR、Wrench、Velocity/Angular Velocity、High-Level Guidance等控制模式；训练或推理时RL策略在所选抽象层输出动作，经上述流水线批量采样并可直接部署。

### 三、结果（Result）
基准评测表明，GzDRL在评测框架中取得最高工作站吞吐，在笔记本硬件上可与GPU加速仿真器竞争，CPU吞吐达到78.6×10^3环境步/秒。它同时保持精确的智能体-环境同步、多智能体可扩展性和实验级可复现性，并对状态转移与训练可复现性进行了定量验证。学习到的策略可零样本直接部署到物理四旋翼，无需微调。

### 四、结论（Conclusion）
GzDRL通过无中间件的ECS直连与受控物理步进，解决了Gazebo强化学习在可扩展性和可复现性上的长期瓶颈，在吞吐、同步、并行与sim-to-real迁移方面表现突出。该工作为机器人强化学习实验提供了一个可访问、可复现且兼容Gazebo与ROS工作流的平台。

### 五、方法论与关键技术细节
关键实现细节包括：每个环境独立server并序列化构造以兼容全局静态变量；K步物理步进与PostUpdate保证状态观测的确定性转移契约，但渲染传感器受Gazebo渲染管线影响，该确定性保证主要适用于状态观测；重置与运行时域随机化通过缓存SDF修改质量、惯量、插件参数并重生实体，避免重建世界；支持部分批次、动态线程取任务和零拷贝观测共享；关键参数有NE、NT、NB、K和作动器时间常数tc；局限性在于基于CPU Gazebo，吞吐可能仍低于大规模GPU并行仿真，且传感器渲染确定性与多环境资源竞争需按任务评估。
