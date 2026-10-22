# Hybrid PPO-Based Multi-Objective Optimization for UAV-mounted STAR-RIS with Energy Harvesting

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Anas Hussin, Khaled M. Rabie, Mahmoud M. Salim, Ali H. Muqaibel, Louai A. Al-Awami
- 机构：King Fahd University of Petroleum and Minerals (KFUPM)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28807v1) · [PDF](https://arxiv.org/pdf/2610.28807v1)

## TLDR
This paper proposes a hybrid PPO (H-PPO) framework to solve a weighted multi-objective optimization problem in UAV-mounted STAR-RIS-assisted 6G IoT systems, jointly optimizing beamforming, STAR-RIS transmission/reflection coefficients, RF power splitting, and UAV trajectory to balance communication performance, energy efficiency, and RF energy harvesting while achieving faster and more stable convergence than PPO and TD3 baselines.

## Abstract
This paper investigates a multi-objective optimiza tion framework for UAV-mounted reconfigurable intelligent sur face (STAR-RIS)-assisted Sixth Generation (6G)-enabled Internet of Things (IoT) systems. The considered framework jointly supports communication enhancement and radio-frequency (RF) energy harvesting (EH) through adaptive STAR-RIS transmission and reflection control. A weighted multi-objective optimization problem is formulated to jointly optimize the base station (BS) beamforming vectors, STAR-RIS transmission and reflection coefficients, RF power-splitting factor, and UAV trajectory under quality-of-service (QoS), power, and mobility constraints. Due to the strong coupling among the communications, EH, and UAV mobility variables, the resulting problem is highly non convex and difficult to solve using conventional optimization methods. To address this challenge, a hybrid proximal policy optimization (H-PPO) framework is proposed. The developed hybrid actor-critic architecture combines a categorical policy for discrete UAV movement decisions with Beta-distributed policies for continuous communication-control variables. In addition, a two-stage reward mechanism is introduced to enforce QoS feasibility while balancing system sum rate, energy efficiency, and harvested energy. Simulation results demonstrate that the proposed H-PPO framework achieves faster convergence and more stable training behavior than proximal policy optimization (PPO) and twin delayed deep deterministic policy gradient (TD3) baselines. In particular, H-PPO achieves approximately 66% and 60% faster convergence than PPO and TD3, respectively, while maintaining more stable training behavior. Furthermore, the proposed framework effectively balances communication performance and EH under different QoS requirements, STAR RIS sizes, transmit power levels, and user densities.


## 精读解读（中文）
### 一、研究动机
现有UAV辅助STAR-RIS与能量收集研究多只优化系统子集：或考虑EH与UAV移动但采用单面RIS，或研究STAR-RIS但假设固定/地面部署且不含表面RF能量收集；同时多数DRL方法把动作空间视为全连续，忽略UAV移动天然离散/类别化的结构，导致高维耦合控制学习效率受限。本文因此面向6G物联网构建UAV搭载STAR-RIS、同时服务透射侧与反射侧用户并支持RF能量收集的统一多目标优化框架。

### 二、技术方案（Method）
系统由多天线基站、UAV搭载的N单元STAR-RIS及透射/反射两组用户构成，假设直连链路被遮挡，通信经BS-STAR-RIS-UT级联链路完成；在时隙化移动场景中联合优化BS波束成形向量、STAR-RIS透射与反射幅度/相位系数、RF功率分配因子和UAV轨迹。将通信增强与EH的冲突建模为加权多目标问题，在QoS、发射功率、STAR-RIS硬件和UAV移动/速度约束下最大化系统和速率、能量效率与收集能量；由于变量强耦合且非凸，提出H-PPO：状态为环境/信道与系统状态，动作为“离散UAV移动的categorical策略+Beta分布连续通信控制变量”的混合动作，采用混合actor-critic并以PPO裁剪机制训练。奖励采用两阶段机制，先以QoS违约量约束可行性，再对和速率、能量效率和收集能量进行归一化加权平衡。

### 三、结果（Result）
仿真表明H-PPO较PPO和TD3收敛更快且训练更稳定，收敛速度分别约快66%和60%；所提框架能在不同QoS要求、STAR-RIS规模、发射功率和用户密度下有效平衡通信性能与RF能量收集。

### 四、结论（Conclusion）
该工作验证了将STAR-RIS配置、UAV移动性与RF-EH纳入统一多目标DRL框架的可行性，说明显式混合动作空间设计与两阶段奖励能提升高维耦合控制问题的学习效率与稳定性，为能量受限、动态部署的6G IoT场景提供通信与供能协同优化方案。

### 五、方法论与关键技术细节
关键实现点包括：动作空间显式分为离散UAV移动与连续波束成形、STAR-RIS系数和功率分配，连续变量用Beta分布保证有界；奖励含QoS违约项及和速率、EE、EH归一化权重w_Rate、w_EE、w_EH，目标加权系数为λ1、λ2、λ3；约束覆盖QoS、BS发射功率、STAR-RIS幅度/相位硬件限制及UAV最大速度V_max。局限在于验证主要基于仿真、固定UAV高度、直连链路不可用与特定信道/EH建模假设，全文预览未给出完整超参数与复杂度分析。
