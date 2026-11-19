# Verifiably Safe Decentralized Control via Event-Triggered Topology Switching

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Amber He Wei, Shiyu Cheng, Andrew Clark, Bruno Sinopoli
- 机构：Arizona State University, Washington University in St. Louis
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23415v1) · [PDF](https://arxiv.org/pdf/2611.23415v1)

## TLDR
This paper proposes a decentralized event-triggered topology-switching protocol that lets multi-agent systems intermittently connect and disconnect based on local safety certificates while guaranteeing the estimation error stays within a certified safety bound and Zeno behavior is excluded.

## Abstract
This paper proposes a decentralized event-triggered topology-switching protocol for multi-agent systems under estimation uncertainty. We consider an intermittent communication setting in which each agent switches between connected and disconnected modes and makes communication decisions using locally computable certificates, while the closed-loop state is required to remain safe. The proposed protocol follows a safety-driven triggering principle in which agents reconnect before their certificates reach the safety boundary and disconnect only after recovering to a stricter bound below the safety limit. Our design enables intermittent connectivity while maintaining the estimation error within a certified safety bound and excluding Zeno behavior. We evaluate the proposed protocol on a quadruple-tank example, showing that it keeps all tank deviations within the safety bound while allowing agents to remain disconnected for most of the run.


## 精读解读（中文）
### 一、研究动机
多智能体系统通常依赖周期性状态交换来保证协调与安全，带来显著通信开销；已有事件触发方法虽降低传输频率，但仍需保持网络连接并持续监听，且静态拓扑易受攻击。本文关注在估计不确定性下，通过间歇式、事件触发的拓扑切换实现可验证安全，要求估计误差在包括断连期间在内的所有时刻均满足安全界。

### 二、技术方案（Method）
针对连续时间线性多智能体系统，各智能体采用基于局部估计的静态状态反馈，并运行分布式Luenberger型观测器：断连时使用基于可观测性分解的本地增益，连边时使用网络耦合增益更新全局状态估计。每个智能体维护局部可计算的估计误差上界证书，并按安全驱动触发协议切换拓扑：当证书接近安全边界前自主重连，连接受限内所有可达智能体仅在同时恢复到严格低于安全限的内层门限后才同步断连。作者进一步推导触发参数约束，以保证全连接下恢复以及安全违反前重连，并排除Zeno行为。

### 三、结果（Result）
四水箱算例表明，该协议能使所有水箱偏差始终保持在安全界内，同时智能体在大部分运行时间内处于断连状态，说明间歇连接可在不破坏安全认证的前提下显著减少通信。

### 四、结论（Conclusion）
该工作提出了一种可验证安全的分散式事件触发拓扑切换协议，将估计误差证书、安全障碍函数与间歇通信决策结合，在保持闭环安全的同时实现按需连接，并给出避免Zeno行为的理论保证。

### 五、方法论与关键技术细节
关键细节包括：过程和测量扰动由已知二次有界紧集描述；底层图连通且实际拓扑为其子图，智能体依据潜在邻居和当前连接集合确定有效邻居；观测器增益随连接度切换，安全通过多项式障碍函数定义的可认证内近似集合刻画；触发设计区分安全边界与更严格的内层恢复门限，断连需活跃链路可达智能体同步满足条件；理论保证依赖已知模型、扰动界和局部证书，实验为四水箱仿真，未给出大规模或非线性场景验证。
