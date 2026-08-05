# Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Caiwu Ding, Tao Cui, Lingyun Wang, Chengtao Wen
- 机构：Siemens Corporation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02809v1) · [PDF](https://arxiv.org/pdf/2608.02809v1)

## TLDR
The paper identifies the "fail-passive gap"—that a balancing humanoid's safe state must be actively controlled rather than de-energized, violating classical machinery safety standards—and uses a certified external safety chain as a measuring instrument to precisely localize this uncertifiable robot-side reaction chain, providing a feasibility study rather than claiming end-to-end certification.

## Abstract
Industrial humanoid robots are constrained less by locomotion or manipulation capability than by the immaturity of functional safety certification for legged platforms. The root difficulty is that the safe state of a legged robot is an actively-controlled state, which violates the fail-passive assumption underlying ISO~13849-1 / EN~60204-1: removing power from a walking biped causes an uncontrolled fall, so classical de-energization is itself a hazard. We term this the fail-passive gap and use a certified external safety chain (light curtain, emergency stop, fail-safe input, fail-safe PLC, and wireless PROFIsafe) as an instrument to locate it precisely: because the external chain is closed and quantifiable with established methods (PFHD, DC, CCF, PL/SILCL), the residual uncertifiable element is pinpointed to the robot-side reaction chain. Using a Siemens fail-safe S7-1500 emergency-stop reference, we show its certifiable Reaction subsystem is contactor-based power removal (Stop Category~0)---exactly the element a balancing humanoid cannot have. We deliberately do not claim end-to-end certified PL~e / SIL~3. We validate the approach on a Unitree G1 EDU pick-and-place cell in a 3m x 1.5m semi-enclosed workspace, and contribute a humanoid-specific analysis of the active safe state (fall-as-hazard, single-support stop bounds, balancing-policy residual risk, ISO~13855 separation) and a provenance-labeled timing budget. Hosting an industrial software-defined automation (SDA) controller on the robot, co-located with the balancing policy, moves robot-side PROFINET/PROFIsafe reception onto a standardized IEC~61131-3 interface; because the G1's onboard compute is not safety-rated hardware, this endpoint is not a certified safety runtime, which reinforces rather than resolves the fail-passive gap and localizes it to the SDA-to-balancing-policy interface.


## 精读解读（中文）
### 一、研究动机
工业人形机器人的部署瓶颈不在于运动或操作能力，而在于腿足平台的功能安全认证不成熟。根本难点在于腿足机器人的安全状态是主动受控状态，违背了ISO 13849-1 / EN 60204-1所依赖的失效被动假设：对行走中的双足机器人断电会导致失控摔倒，因此传统的断电去能本身即构成危险。本文将这一认证缺口定义为'失效被动鸿沟'，并利用一条已认证的外部安全链作为仪器精确定位该鸿沟。

### 二、技术方案（Method）
本文构建了一条由光幕、急停、fail-safe输入模块、fail-safe PLC和无线PROFIsafe组成的PL e/SIL 3级外部安全监督链，围绕Unitree G1 EDU人形机器人在约3m×1.5m半封闭传送带工位上的拾放任务展开。外部链按Detection–Evaluation–Reaction（检测–评估–反应）结构组织，安全停止命令经无线PROFIsafe从PLC传输至机器人侧。为让腿足反应链可被工业功能安全方法触及，本文将工业软件定义自动化（SDA）控制器（软PLC）直接托管在机器人板载计算上，与平衡策略共置，使PROFINET/PROFIsafe接收落到标准化的IEC 61131-3接口上，从而将问题边界收敛到SDA到平衡策略的接口。评估采用PFHD、DC、CCF、PL/SILCL等既有方法，并对照西门子fail-safe S7-1500急停参考设计，同时贡献了主动安全状态分析（摔倒即危险、单支撑停止边界、平衡策略残余风险、ISO 13855分离距离）以及带来源标注的时序预算。

### 三、结果（Result）
外部安全链是闭合且可用既有标准量化的，因此残余的不可认证元素被精确定位到机器人侧反应链。西门子S7-1500急停参考设计的可认证Reaction子系统是基于接触器断电的Stop Category 0，而这恰恰是平衡人形机器人无法具备的元素。论文明确不声称端到端认证PL e/SIL 3；由于G1板载计算并非安全级硬件，该端点也不是认证的安全运行环境，这反而强化了失效被动鸿沟的存在，并将其定位到SDA到平衡策略的接口。

### 四、结论（Conclusion）
面向工业人形机器人的功能安全认证不能直接套用传统机械的失效被动范式；主动受控的平衡停止状态目前无法通过现有标准获得认证。将认证外部链作为测量仪器可精确界定鸿沟位置，而将SDA控制器放在机器人上与平衡策略共置，是使腿足反应链可被工业功能安全方法分析的关键架构尝试，但该方案只能标准化接口，不能提供认证运行环境。真正的认证仍需要在机器人侧反应链上建立可实现主动安全停止并具备量化PFHD/PL的安全运行机制。

### 五、方法论与关键技术细节
关键细节包括：外部安全链采用SICK deTec2 Core光幕、SIPLUS ET 200SP Open Controller（CPU 1515SP PC2 F）及F-DI输入模块；与常规做法不同，设计不使用外部安全继电器或接触器，停止要求通过fail-safe PLC以安全报文经无线PROFIsafe传送，而非硬接线断电。实验在3m×1.5m半封闭工位，操作员可通过南侧开口接触，由光幕对监控。时序/延迟预算区分specified、configured、measured三类来源，给出最坏情况反应时间和距离。人形特定分析涵盖fall-as-hazard权衡、中步（单支撑）停止需求、平衡策略失效的残余风险，以及依据ISO 13855的分离距离计算。论文明确局限：外部链可认证，但机器人侧反应链无PFHD、无PL，G1板载计算非安全级硬件，因此SDA端点不构成认证PROFIsafe F-host，也无SIL/PL声明；最终鸿沟被定位到SDA到平衡策略接口，未来需在机器人侧建立可量化且可认证的主动安全停止方案。
