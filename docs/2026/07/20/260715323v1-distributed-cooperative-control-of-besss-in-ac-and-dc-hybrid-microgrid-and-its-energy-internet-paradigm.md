# Distributed Cooperative Control of BESSs in AC and DC Hybrid Microgrid and Its Energy Internet Paradigm

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yalin Zhang, Zhongxin Liu, Zengqiang Chen
- 机构：Nankai University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15323v1) · [PDF](https://arxiv.org/pdf/2607.15323v1)

## TLDR
This paper proposes a flexible and scalable distributed control framework for AC/DC hybrid battery energy storage systems in an Energy Internet paradigm, enabling state-of-charge balance, proportional power sharing, and frequency/voltage restoration through multi-agent systems with cloud server support.

## Abstract
An AC and DC hybrid microgrid, which inherits advantages of AC and DC microgrids and discards some disadvantages, is considered to be the most promising power network structure and gradually applied in the community. Usually, the AC subgrid and the DC subgrid are interconnected by Bidirectional Interlink Power Converters (BILPCs). Besides, in view of the different droop characteristics of AC subgrid and the DC subgrid, it is necessary to design a suitable distributed secondary controller for an AC and DC hybrid microgrid. Accordingly, this paper proposes a flexible and scalable distributed control framework for an AC and DC hybrid battery energy storage system (ADHB) with BILPCs in an Energy Internet (EI) paradigm. An ADHB governed by multi agent systems via a cloud server can reach the State-of-Charge balance, proportional power sharing, frequency and voltage restoration. The proposed control framework provides the group play-and-plug by adding or removing an inter-MASs interaction link. For a single BILPC in an ADHB, active/reactive power, frequency and voltage are adjusted by an AC BESS. For the parallel BILPCs in EI, a decentralized secondary control scheme is proposed. Communication delay issues and stability are analysed. Then, the relevant simulation results verify the correctness of the proposed scheme.


## 精读解读（中文）
### 一、研究动机
现有AC/DC混合微电网控制方案缺乏对大尺度集群的可扩展灵活解决方案，且多数二级控制器需与实体位于同一位置，无法实现远程控制。本文旨在设计一种基于云服务器的分布式远程控制框架，以实现异构BESS的SoC均衡、功率比例分配和频率电压恢复，并支持组即插即拔。

### 二、技术方案（Method）
提出一种基于多智能体系统（MAS）的分布式二级控制框架，通过云服务器远程管理AC/DC混合BESS（ADHB）。框架中，每个BESS对应一个智能体，采用有向通信图交换状态信息。将AC和DC BESS的下垂控制简化为动力学模型，并引入BILPC作为子网互联设备。控制目标包括SoC平衡、有功/无功比例分配、频率/电压恢复。对于单个BILPC，通过AC BESS调节有功/无功功率、频率和电压；对于并行BILPC，提出分散式二级控制方案，利用AC子网状态变量调节。分析了通信延迟和稳定性。

### 三、结果（Result）
仿真结果验证了所提分布式控制框架的正确性。在异构AC/DC混合BESS场景下，实现了所有电池的SoC均衡、子网内外的比例功率分配以及频率和电压恢复至参考值。该方案支持基于组的即插即拔，通过添加或移除MAS间交互链路可灵活扩展。

### 四、结论（Conclusion）
本文提出的分布式协同控制框架为AC/DC混合BESS在能源互联网范式下的远程管理提供了有效方案。该框架具有灵活性和可扩展性，能够处理异构电池组，实现多目标控制，并支持组即插即拔。未来可进一步研究通信延迟对系统稳定性的影响。

### 五、方法论与关键技术细节
数据方面，每个BESS的输入包括SoC、有功/无功功率、频率和电压测量值，控制输出为参考频率和电压。先验假设所有BESS为异构，且下垂增益与容量相关。损失函数隐含于控制目标中，通过分布式一致性协议实现。超参数包括通信拓扑、耦合增益、延迟上界。复杂度方面，框架为分布式，可扩展至大规模集群。局限性在于依赖通信网络，实际通信延迟和丢包可能影响性能，且未考虑网络攻击等安全性问题。
