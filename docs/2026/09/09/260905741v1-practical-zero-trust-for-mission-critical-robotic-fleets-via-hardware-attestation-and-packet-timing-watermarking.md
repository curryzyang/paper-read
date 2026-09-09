# Practical Zero-Trust for Mission-Critical Robotic Fleets via Hardware Attestation and Packet Timing Watermarking

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Ryne Gonzales, Ethan Liesdyanto, Rex Worley, Michael Frederick, Jaewon Kim, Eman Hammad
- 机构：Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05741v1) · [PDF](https://arxiv.org/pdf/2609.05741v1)

## TLDR
TLDR: The paper proposes and empirically validates a layered Zero-Trust framework for ROS 2 robotic fleets—combining TPM 2.0 hardware attestation, SIEM telemetry, and Inter-Packet Delay timing watermarking—demonstrating that statistical kurtosis tracking of the watermark achieves complete detection of stealthy man-in-the-middle command injections without payload overhead.

## Abstract
Autonomous unmanned vehicles are vital to tactical missions, mission-critical public-safety operations like search and rescue and disaster response. However, their reliance on open wireless links and standard Robot Operating System (ROS 2) middleware exposes a broad cyber-physical attack surface. A compromise of these systems can disrupt real-time control loops, leading to mission failure or asset loss in high-stakes environments. This paper presents and empirically evaluates a layered, context-aware cybersecurity framework enforcing Zero-Trust principles for a multi-node robotic fleet over Wi-Fi. The framework integrates an active hardware root of trust (TPM 2.0), centralized in-band and out-of-band SIEM telemetry monitoring (ELK Stack and Kismet), and a non-cryptographic Inter-Packet Delay (IPD) timing watermark. Evaluated on a live ROS 2 mobile testbed under multi-layer exploits (OSI Layers 2-5), results demonstrate that while volume-based filters isolate brute denial-of-service floods, tracking the statistical sample kurtosis (K) of the embedded IPD watermark exposes stealthy Man-in-the-Middle command injections with complete detection accuracy without payload overheads.


## 精读解读（中文）
### 一、研究动机
自主无人车在战术任务和公共安全场景中高度依赖开放无线链路与ROS 2中间件，导致其面临跨OSI Layer 2至5的广泛网络物理攻击面。传统静态阈值检测无法区分环境波动与恶意干预，而现有研究多停留在理论或仿真，缺乏在真实硬件受限平台上针对多节点机器人车队的实证验证，因此需要一种实用的零信任防护框架来保障任务关键型机器人集群的实时控制闭环与运行韧性。

### 二、技术方案（Method）
提出并实测了一个分层上下文感知的零信任安全框架，面向Wi-Fi环境下的多节点ROS 2机器人车队。框架集成三项核心能力：其一，基于TPM 2.0硬件信任根，通过Endorsement Key签名和系统寄存器完整性哈希实现节点启动时的挑战-响应认证，阻止仿冒设备入网；其二，搭建集中式SIEM监控中枢，在嵌入式平台（Raspberry Pi 5）上运行ELK Stack，通过Packetbeat、Metricbeat和Heartbeat收集各机器人节点的网络流量、主机状态和连通性日志，同时由Kismet节点采样802.11频谱以检测de-authentication等无线攻击；其三，设计非加密的Inter-Packet Delay（IPD）时间水印机制：控制器发送速度指令时，在每个包间隔上叠加零均值高斯随机偏移（σ=0.02s），形成水印化的包时序；接收端在滚动窗口（N=250）内计算采样峰度K，通过判断K是否落在正常区间[2.8, 3.2]来识别中间人重放或命令注入，因为攻击者的排队和调度扰动会破坏时序水印统计特性。实验在包含TurtleBot3（树莓派4B）的实车测试床上进行，红队分别实施mdk4发起的802.11 de-authentication洪水、hping3 ICMP flood、TCP SYN flood以及ARP缓存投毒实现的MITM命令注入四类跨层攻击。

### 三、结果（Result）
实验结果表明，基于流量体积的过滤机制能够有效隔离粗暴的DoS洪水攻击；但对于隐蔽的MITM命令注入，原始网络抖动指标无法有效预警，而通过跟踪IPD水印的样本峰度K，当攻击者插入中继并篡改ROS 2速度指令时，K值会偏移至正常区间之外（K<2.0或K>4.5），实现了完全检测精度（100%检测率），且无需增加任何报文负载或计算开销。

### 四、结论（Conclusion）
该研究证实了将硬件信任根、集中式SIEM遥测与分组级时间水印相结合的实用零信任框架，能够在多节点ROS 2车队中有效应对跨OSI Layer 2至5的恶意攻击。相比单纯依赖流量阈值或应用层加密方案，所提方法不仅隔离了高带宽DoS，还以零负载开销的方式精确识别了低功率、隐遁的中间人命令注入，为资源受限的公共安全机器人系统提供了可部署的实证防御路径。

### 五、方法论与关键技术细节
关键方法论细节包括：IPD水印采用零均值高斯噪声（μ=0, σ=0.02s）调制包间延迟，窗口N=250的样本峰度K是检测指标，正常基线为2.8≤K≤3.2，异常判定为K<2.0或K>4.5；SIEM采用ELK Stack（Elasticsearch/Logstash/Kibana）部署在树莓派5上，数据采集器包括Packetbeat（解析L2/L3帧）、Metricbeat（监控socket、CPU、内存）和Heartbeat（探测连通性）；TPM 2.0在系统初始化阶段执行EK签名验证和完整性哈希度量，未注册设备被拒绝接入；攻击场景具体包括mdk4发起的802.11管理帧de-auth、hping3 ICMP echo flood、TCP SYN耗尽SSH端口连接表、以及通过ARP投毒实施ROS 2 geometry_msgs/Twist命令的主动篡改；实验平台为Wi-Fi（802.11n）连接的TurtleBot3车队，每节点搭载树莓派4B；该方案的局限性包括IPD水印依赖接收端精确的统计窗口同步，以及当前评估在单一无线测试床完成，尚未扩展到大规模异构车队或高动态移动环境。
