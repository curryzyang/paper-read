# Resilient Control of Switched Vehicle Platoons under False Data Injection Attacks

- 区域：精读区
- 排名：3
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Ali Eslami, Jiangbo Yu
- 机构：McGill University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28794v1) · [PDF](https://arxiv.org/pdf/2607.28794v1)

## TLDR
This paper proposes a resilient control framework for switched vehicle platoons under bounded-rate false data injection attacks on V2V channels, using per-link observers to estimate and compensate for attack signals and thereby ensuring uniform ultimate boundedness and string stability.

## Abstract
This paper investigates resilient control design for leader--follower vehicle platoons with mode-dependent powertrain dynamics subject to False Data Injection (FDI) attacks on vehicle-to-vehicle (V2V) communication channels. The longitudinal motion of each vehicle is described by a switched third-order model that captures changes in the powertrain dynamics across different operating modes. To estimate the attack signals that are injected into the communication channels, each vehicle is equipped with an auxiliary system, and a dedicated observer is implemented for each communication link. The resulting attack estimates are then used to mitigate the effects of the attacks through our proposed resilient controller. For attacks with bounded rates but potentially unbounded amplitudes, the closed-loop platoon is shown to be uniformly ultimately bounded. For a predecessor-following topology, string stability is established for the nominal switched platoon, while the effect of nonzero attack-estimation errors on acceleration propagation is shown to be bounded. Numerical case studies demonstrate the effectiveness of the proposed approach.


## 精读解读（中文）
### 一、研究动机
现有车队控制大多假定车辆纵向动力学固定不变，且网络攻击常被建模为随机或有界能量信号；对于切换动力总成动力学与V2V通信链路上幅值可能无界、仅速率有界的虚假数据注入攻击联合作用下的弹性控制问题尚无充分研究。本文同时处理物理模式切换与通信攻击，力求在不需要攻击幅值上界的前提下保证车队稳定与弦稳定。

### 二、技术方案（Method）
构建领航者-跟随者车队模型，每车纵向运动由依赖动力总成模式的切换三阶系统描述；通信拓扑固定且含以领航者为根的生成树。每个发送者运行防御者设计的切换辅助系统，接收者针对每条通信链路设计增广观测器：将被传输物理状态和辅助输出上的加性FDI攻击增广为状态，利用辅助系统模式切换构成的统一可观测性在线估计攻击信号。观测器误差仅取决于攻击变化率而非攻击幅值。随后用攻击估计值构造弹性控制器，对接收信息进行补偿；物理切换信号满足平均驻留时间条件。通过Lyapunov与平均驻留时间分析证明闭环一致最终有界，并对前车-跟随拓扑分析标称切换车队的弦稳定性及估计误差非零时加速度传播的有界性；最后用数值仿真验证。

### 三、结果（Result）
在攻击幅值可能无界、速率有界的FDI攻击下，所提弹性控制器使闭环车队一致最终有界；对前车-跟随拓扑，标称切换车队保持弦稳定，攻击估计误差非零时加速度沿车队传播的偏差也有界。数值案例验证了攻击估计与弹性控制方案的有效性，且方法不需要攻击幅值上界或攻击链路数量约束。

### 四、结论（Conclusion）
本文提出一套面向切换动力总成车队在V2V FDI攻击下的弹性控制与攻击估计方案，通过辅助系统和逐链路观测器估计并补偿攻击，在攻击幅值无界而速率有界的条件下同时实现闭环有界性和弦稳定性，为实际车队在物理模式切换与网络攻击并存场景下的安全控制提供了可行框架。

### 五、方法论与关键技术细节
关键点包括：每条V2V链路发送原始物理状态和辅助系统输出，接收端用已知公共运动参考构造moving-frame输入；辅助系统采用防御者预设的模式循环和各模式驻留时间集合，通过预共享种子与同步时钟复现切换信号，无需安全在线信道；增广状态含辅助状态及两类攻击信号，系统矩阵满足统一切换可观测性条件，观测器衰减率由可观测性格拉姆矩阵下界刻画；攻击估计误差的界由攻击速率上界决定而非攻击幅值，因此允许攻击幅值无界；控制器利用攻击估计值补偿，物理切换仅需平均驻留时间，不要求所有冻结模式共享公共Lyapunov函数；弦稳定性分析针对前车-跟随拓扑与恒定车头时距间距策略，并给出估计误差对加速度传播影响的有界性；局限是当前假设车队同步物理切换且控制器增益与模式即时同步，异步切换下的扩展留作未来工作。
