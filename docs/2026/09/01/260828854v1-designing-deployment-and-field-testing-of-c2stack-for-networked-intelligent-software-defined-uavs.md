# Designing, Deployment and Field Testing of C2Stack for Networked Intelligent Software-Defined UAVs

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Maxwell McManus, Zhaoxi Zhang, Sidharth Santhi Nivas, Yuqing Cui, Prem Sagar Pattanshetty Vasanth Kumar, Chenzhi Zhao, Nicholas Mastronarde, George Sklivanitis, Dimitris Pados, Elizabeth Serena Bentley, Zhangyu Guan
- 机构：University of Minnesota - Twin Cities, Virginia Tech, Florida Atlantic University, University at Buffalo, U.S. Air Force Research Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28854v1) · [PDF](https://arxiv.org/pdf/2608.28854v1)

## TLDR
C2Stack is a configurable, open-source protocol stack and experimental framework for networked software-defined UAVs, whose modular control plane and programmable data plane enable real-time data-driven network control, validated through field trials on a custom swarm platform for tasks like reinforcement learning-based utility maximization and collaborative interference localization.

## Abstract
Unmanned Aerial Vehicles (UAVs) are emerging as critical enablers of next-generation wireless networking and autonomous systems. Despite their potential, deploying and testing networked UAV systems in real-world environments remains challenging, largely due to the absence of well-developed, end-to-end, ready-to-use protocol stacks. To fill this gap, we present C2Stack, a configurable protocol stack and experimental framework designed for real-time control, evaluation, and optimization of UAV networks. C2Stack incorporates a modular control plane, referred to as the~C2Stack Network Operating System (CNOS), alongside a programmable data plane that exposes APIs for cross-layer algorithm development, digital twin integration, and autonomous swarm control.
  In this article, we share our experience with the deployment and testing of C2Stack. We implemented C2Stack on a custom UAV swarm platform that integrates multiprocessor system-on-chip (MPSoC) radios with Intel NUC computing modules, enabling interoperability with various RF front ends. Field trials were conducted in both netted environments and large-scale outdoor test ranges, focusing on two representative use cases: (i) network utility maximization through online reinforcement learning, and (ii) collaborative interference source localization. The experiments demonstrate the feasibility of real-time, data-driven optimization in dynamic aerial environments, while also revealing practical challenges in field deployments of networked UAV systems, including power constraints, sensing limitations, and deployment logistics. We have made C2Stack source code available to the community under the MIT License, with the goal of establishing it as a foundational framework for experimental research on intelligent networked aerial systems.


## 精读解读（中文）
### 一、研究动机
无人机网络的真实部署与测试仍缺乏端到端、开箱即用的协议栈。现有框架多依赖理想化网络条件或简化通信模型，难以在真实空域环境中验证AI/ML控制算法；同时公开测试平台（如AERPAW、ARA）在载荷能力、集群支持和协议灵活性上存在明显限制。为此，本文提出C2Stack，填补从理论到实验研究的鸿沟，支撑智能软件定义无人机网络的快速原型验证与现场评测。

### 二、技术方案（Method）
C2Stack采用控制平面与数据平面分离的架构。控制平面即C2Stack网络操作系统（CNOS），包含CNOS Core（进程通信服务器PCS、统一消息协议、GUI）、Autonomy Toolchain（提供X-Layer Algorithm API和Virtual Network API，支持在线强化学习等用户自定义算法）和C2-App Suite（如干扰检测与定位子模块IDLS）。数据平面为可编程协议栈（PPS），按五层架构（APP/TSPT/NET/MAC/PHY）独立对象化实现，PHY层通过软件定义协议接口（SDPI）连接FPGA基带与射频前端，支持跨层指标监控与参数动态配置。实验平台采用自研中大型无人机群，集成MPSoC无线电与Intel NUC计算模块，并支持多种RF前端。现场试验在有网环境与大型室外靶场进行，验证两个用例：基于在线强化学习的网络效用最大化，以及协同干扰源定位。

### 三、结果（Result）
现场实验证明了C2Stack在动态空中环境中支持实时数据驱动优化的可行性：在线强化学习能够根据实时网络状态调整协议参数，协同干扰源定位可有效估计干扰位置。同时，实验揭示了真实部署中的实际挑战，包括功率限制、感知局限和部署后勤问题。C2Stack已以MIT许可证开源。

### 四、结论（Conclusion）
C2Stack作为可配置、可扩展的协议栈与实验框架，能够支撑无人机网络的通信与控制实时优化，并为智能空基网络的实验研究奠定了开源基础。其模块化设计使跨层算法、数字孪生与自主集群控制可灵活集成，未来可基于现有测试平台推广协作开发。

### 五、方法论与关键技术细节
关键细节包括：PCS统一消息协议通过internal/node-level/network-level三类逻辑接口路由消息，并通过控制面与数据面子头降低复杂度；PPS各层独立对象化，用户算法可替换现有服务而无需大量修改代码；SDPI处理载荷聚合、类型转换、位掩码与符号映射，并监控符号错误率、EVM与信道分布；实验平台MPSoC+Intel NUC实现FPGA基带与上层协议间的实时双向数据流控制。局限性方面，无人机振动与风扰导致位置可靠性下降，功率与感知能力约束现场试验范围；部署后勤（如飞行许可、GPS遮挡）也影响可重复性。
