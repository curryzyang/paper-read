# Reinforcement learning for hardware acceleration and system-level optimization on FPGA and integrated-circuit platforms: A survey

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Hamza Kheddar
- 机构：University of Medea
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28699v1) · [PDF](https://arxiv.org/pdf/2610.28699v1)

## TLDR
This survey provides a unified, hardware-centric review of more than 100 studies on reinforcement learning implementations across FPGA and IC platforms, organizing them by RL family, hardware realization strategy, and application domain while comparing performance trade-offs and identifying architectural patterns, limitations, and open research directions.

## Abstract
Reinforcement learning (RL) enables adaptive and autonomous decision-making in embedded, edge, and heterogeneous computing systems. Field-programmable gate arrays (FPGAs) and integrated circuits (ICs) offer low latency, energy efficiency, and architectural flexibility for RL deployment, while introducing challenges in resource constraints, implementation complexity, and hardware-algorithm co-design. This review surveys more than 100 studies on RL implementations across FPGA and IC platforms, emphasizing architectures, implementation strategies, performance evaluation, and applications. The literature is organized by RL family, including model-based Markov decision processes, classical value-based methods, deep RL, actor-critic, policy-gradient, and multi-agent approaches. We further classify studies by abstraction level, hardware realization strategy, and application domain, examining how RL algorithms map onto reconfigurable and fixed hardware. Unlike surveys restricted to particular algorithms or platforms, this work provides a unified analysis of FPGA and IC implementations, covering acceleration, reconfigurable architectures, energy-aware control, and system-level optimization. Comparative assessments consider resource utilization, latency, throughput, power consumption, and reported performance gains. Finally, we identify recurring architectural patterns, practical limitations, open challenges, and research directions for efficient RL-driven hardware systems. The survey offers a consolidated reference for researchers developing and evaluating RL solutions on specialized hardware.


## 精读解读（中文）
### 一、研究动机
随着嵌入式、边缘与异构计算系统对自适应、自主决策的需求增强，传统静态控制和启发式优化难以应对动态工作负载、功耗预算与时延约束。FPGA与IC平台具有低时延、高能效和架构可定制优势，但将RL从CPU/GPU软件实现迁移到硬件面临资源受限、实现复杂和软硬件协同设计等挑战，因此需要系统梳理该交叉领域。

### 二、技术方案（Method）
该文采用系统性文献综述方法，以Scopus为主检索源，使用覆盖RL/DRL与FPGA/ASIC/IC/SoC的布尔查询，限定2015—2026年英文期刊与会议论文，并依据硬件实现细节、评估结果和相关性进行筛选，最终分析100余篇（正文称120篇）研究。文献按RL族（MDP、值方法、深度RL、Actor-Critic、策略梯度、多智能体等）、抽象层级、硬件实现策略和应用域分类，并从资源利用率、时延、吞吐、功耗和报告性能增益等维度进行比较。

### 三、结果（Result）
综述提供了FPGA与IC平台上RL实现的统一分析框架，覆盖RL作为硬件加速负载和作为硬件系统控制机制的双重角色，涉及加速器设计、可重构架构、能耗感知控制和系统级优化。文章归纳出反复出现的架构模式，汇总不同RL算法到可重构与固定硬件的映射方式，并指出现有研究报告指标不统一、实现细节不足和可复现性有限等问题。

### 四、结论（Conclusion）
RL在FPGA/IC平台上具有实现低时延、高能效和自适应智能硬件的潜力，但尚受资源约束、设计复杂度、部署灵活性和软硬件协同设计难度制约。未来需要发展可复用架构、量化与能效优化方法、统一评估基准以及面向实际部署的RL驱动硬件系统设计流程。

### 五、方法论与关键技术细节
关键方法细节包括：以Scopus为主并覆盖IEEE Xplore、Elsevier、ACM、Web of Science等来源；检索式联合RL/DRL与FPGA/ASIC/IC/SoC关键词；时间窗为2015—2026年；仅纳入英文期刊和会议论文；排除缺乏硬件实现细节、缺少有效评估或与RL-FPGA/IC弱相关的研究。综述以表格化基准对比目标应用、最佳性能/改进、局限和实现说明，但作为综述其局限在于依赖文献报告结果、指标口径不一致且难以进行统一实验复现。
