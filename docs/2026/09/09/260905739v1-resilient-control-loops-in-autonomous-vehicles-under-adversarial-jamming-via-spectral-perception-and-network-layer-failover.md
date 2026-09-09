# Resilient Control Loops in Autonomous Vehicles Under Adversarial Jamming via Spectral Perception and Network-Layer Failover

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Luis Barajas, Colin Jeardoe, Jaewon Kim, Eman Hammad
- 机构：Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05739v1) · [PDF](https://arxiv.org/pdf/2609.05739v1)

## TLDR
This paper presents a cross-layer resilient framework for ROS 2-based autonomous vehicles that uses SDR-driven spectral perception and Random Forest classification to detect adversarial jamming, then triggers rapid network-layer failover between dual hot-standby wireless interfaces, achieving 141 ms communication recovery and a 78.9% reduction in path-tracking error on a physical robot testbed.

## Abstract
The operational integrity of autonomous mobile robots relies on the continuous availability of wireless control loops, making them highly attractive targets for adversarial intentional electromagnetic interference. This paper introduces a resilient, cross-layer framework that combines physical-layer spectral perception with network-layer routing optimization to protect middleware stability, such as ROS2, during intentional electromagnetic interference. Utilizing a software-defined radio front-end, the system extracts dynamic spectral descriptors, including spectral entropy and channel occupancy, to inform a Random Forest classifier that establishes adaptive environmental baselines. To ensure uninterrupted data flow, the architecture maintains dual pre-authenticated physical interfaces in a hot-standby configuration, enabling instantaneous failover through automated network routing table updates. Empirical validation on a physical ROS2 mobile robot testbed demonstrates that this adaptive hardware-assisted architecture optimizes communication recovery to an average of 141ms. This sub-second restoration translates directly into a 78.9% reduction in pooled root-mean-square path tracking error compared to software re-association, successfully securing system-level mission integrity.


## 精读解读（中文）
### 一、研究动机
自主移动机器人的无线控制回路持续可用是其运行完整性的关键，因此极易成为蓄意电磁干扰（IEMI）的攻击目标。现有研究多聚焦于理论链路层指标，缺乏对物理层干扰如何经由ROS 2等中间件传播并破坏物理平台闭环控制稳定性的实证评估；同时固定阈值检测在环境噪声变化下易误报漏报，亟需跨层、上下文感知的弹性通信框架。

### 二、技术方案（Method）
提出一个结合物理层频谱感知与网络层路由优化的跨层弹性框架。系统使用HackRF One作为机器人端被动感知前端，以2.5 MS/s采样率采集IQ数据，经512点FFT得到20 MHz观测窗内PSD，提取五个频谱描述符（均值PSD、PSD标准差、最大PSD、频谱熵、信道占用率）。随机森林分类器离线训练，输入这些特征区分正常Wi-Fi流量与IEMI事件，推理时输出干扰概率并与频段特定阈值（75%）比较，需连续三次检测确认并经历冷却期。缓解阶段采用双预认证物理接口热备用配置：TP-Link AC600 USB适配器永久关联2.4 GHz BSSID，板载无线接口关联5 GHz BSSID，两条链路持续认证并各配静态IP；检测到干扰后通过修改Linux默认路由和网关，瞬间将遥测与控制流量导向未受扰接口，无需解关联/重关联。实验平台为TurtleBot3 Burger（Raspberry Pi 4, Ubuntu 24.04, ROS 2 Humble, Cyclone DDS），干扰源为USRP B210发射窄带CW音（2.447 GHz或5.2 GHz，发射增益85 dB，持续5 s），对比三种架构：静态阈值软件切换、自适应ML软件切换、自适应硬件辅助切换。

### 三、结果（Result）
在物理ROS 2移动机器人测试平台上，自适应硬件辅助切换将通信恢复时间优化至平均141 ms，相比软件重关联（完整wpa_supplicant重连周期）实现了亚秒级恢复；该恢复直接带来池化均方根路径跟踪误差降低78.9%。静态阈值基线因环境噪声易误报，而自适应ML检测器在区分正常流量与IEMI方面更鲁棒。硬件辅助路由切换避免了单接口软件重关联的多秒瓶颈，显著保障了系统级任务完整性。

### 四、结论（Conclusion）
将物理层SDR频谱感知与网络层多接口路由切换相结合的跨层弹性架构，能有效抑制蓄意干扰对ROS 2闭环控制的影响，将恢复延迟压缩到毫秒级并大幅降低轨迹跟踪误差。相比纯软件重关联，维持双预认证热备用物理接口并仅修改路由表的策略是一种实用且可扩展的防御范式。

### 五、方法论与关键技术细节
关键细节包括：检测器使用随机森林分类器，特征为五个PSD衍生描述符；决策采用频段特定阈值（2.4 GHz为-30 dB静态阈值，自适应概率阈值为75%）及N_sample=75样本连续窗口抑制瞬态；每次频段切换后HackRF重调谐并施加五样本冷却期。双接口均为预认证热备用，静态IP同子网，切换只动路由表。实验局限：使用窄带CW干扰，未覆盖响应式或持续跟踪干扰机；测试仅在双频Wi-Fi（2.4/5 GHz）上进行，协议无关性仅为概念验证；6 GHz网络因Raspberry Pi 4不支持被排除；机器人路径为1m×1m方形两圈，距离2-4 m变化，干扰持续5 s，遥测本地记录以防链路中断导致数据丢失。
