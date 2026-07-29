# Egocentric Station Holding of Robotic Fish in Unknown Turbulent Background Flow

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Xiaozhu Lin, Xu Huang, Hongru Dai, Xiaopei Liu, Junzhi Yu, Yang Wang
- 机构：Chinese Academy of Sciences, Peking University, ShanghaiTech University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24860v1) · [PDF](https://arxiv.org/pdf/2607.24860v1)

## TLDR
This paper introduces the SWiFT framework, which leverages reinforcement learning integrated with a CFD-based simulator and sim-to-real transfer to enable a robotic fish to achieve robust egocentric station-holding in unknown turbulent flows using only egocentric feedback, significantly outperforming existing methods.

## Abstract
Approaching a target position and holding station in flowing water is a fundamental and critical capability for robotic fish operating in natural aquatic environments. Despite decades of advances in enhancing swimming efficiency and maneuverability, this capability remains underdeveloped, largely owing to the insufficiently characterized, highly nonlinear fluid-structure interactions inherent to freely swimming robotic fish in flows. To bridge this gap, we propose the SWiFT framework, a Swimming With Flow Toolbox that enables the efficient exploration of an egocentric station-holding policy for a body and/or caudal fin (BCF) robotic fish in unknown and turbulent background flows via reinforcement learning (RL). Our SWiFT integrates a free-swimming flow-tank experimental setup with a highly efficient, physically consistent computational fluid dynamics (CFD)-based simulator and a systematic sim-to-real transfer pipeline. The resulting policy achieves substantial improvements over state-of-the-art methods across all metrics, most notably root-mean-square error (RMSE) of distance. Furthermore, we validated that egocentric feedback alone, without any explicit flow sensing, enables station-holding in unknown turbulent flows, closely mirroring the biological phenomenon of rheotaxis. Accordingly, the success of this egocentric station-holding policy not only advances robotic fish control toward real-world deployment, but also highlights SWiFT's promise as a foundation for tackling complex swimming tasks for underwater robots.


## 精读解读（中文）
### 一、研究动机
现有仿生鱼研究多集中于静水或受限流动环境，缺乏在未知湍流背景流中自由游动并保持位置的能力，这严重限制了实际部署。受生物鱼仅凭自我感知实现流性反应（rheotaxis）的启发，本文旨在探索是否仅依靠自我中心反馈就能实现未知湍流中的稳定station-holding。

### 二、技术方案（Method）
提出SWiFT框架，整合三大模块：自由游动水槽实验装置、基于GPU加速的格子玻尔兹曼方法（LBM）的高效CFD模拟器、以及系统化的sim-to-real迁移管道。采用软演员-评论家（SAC）强化学习算法，策略直接映射自我中心感知输入（如姿态、角速度等）到关节角度命令，无需底层周期控制器。通过域随机化和精心设计的奖励函数（结合位置误差与能量效率）增强鲁棒性，模拟器使用少量实验数据校准，实现从仿真到真实的零样本迁移。

### 三、结果（Result）
在真实水槽实验中，SWiFT策略在所有关键指标上显著优于当前最先进的模型预测控制（MPC）和数据驱动的Koopman算子等方法，特别是距离均方根误差（RMSE）降低幅度最大。验证了仅依赖自我中心反馈（无显式流感知）即可在未知湍流中实现稳定station-holding，与生物流性反应现象完全一致。

### 四、结论（Conclusion）
本研究首次系统性地解决了仿生鱼在未知湍流背景流中自我中心station-holding的问题，证明了通过强化学习与CFD模拟器的结合可以生成鲁棒的控制策略，推动了仿生鱼在自然水域中的实际部署。同时揭示了自我中心反馈足以实现类似流性反应的行为，为水下机器人复杂游泳任务提供了基础。

### 五、方法论与关键技术细节
关键细节包括：使用自由游动水槽避免了外部固定约束，模拟器采用低数值耗散的LBM并利用GPU并行性加速；RL算法为SAC，策略学习直接生成非周期性身体运动；域随机化涵盖了流速、初始姿态等变化；sim-to-real校准仅需少量实验数据；策略不依赖人工侧线系统，简化了硬件需求。局限性在于水槽尺寸有限，未来需在更复杂自然环境中验证。
