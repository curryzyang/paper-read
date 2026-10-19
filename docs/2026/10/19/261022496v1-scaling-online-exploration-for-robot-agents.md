# Scaling Online Exploration for Robot Agents

- 区域：精读区
- 排名：6
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Runhan Huang, Xiangcheng Zhang, Haoyu Chen, Yitong Li, Yen-Jen Wang, Bohan Lyu, Haotian Ye, Chuye Hong, Yixuan Wang, Chloe Su, Haoyu Xiong, Yangzhen Wu, Enze Xie, Travis Manderson, Stefano Ermon, Pieter Abbeel, Antonio Torralba, Dawn Song, Weirui Ye, Yilun Du
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22496v1) · [PDF](https://arxiv.org/pdf/2610.22496v1)

## TLDR
RAX is an open-source robot-agent framework that scales online exploration by having a coding agent synthesize executable perception-planning-control programs without demonstrations, achieving consistent generalization gains, +37.4% simulation improvement over baselines, and autonomous continual learning across diverse simulated and real robot embodiments.

## Abstract
Robot learning has advanced by scaling demonstration datasets and model capacity; however, deploying a new robot embodiment or task typically necessitates a dedicated teleoperation corpus. The resulting policies remain bounded by their imitation distributions, limiting generalization and continual self-improvement. We introduce RAX (Robot Agent eXploration), an open-source framework for robot agents centered on scaling exploration: enabling agents to improve by acquiring online experience and synthesizing executable programs. In RAX, a general-purpose coding agent generates robot control code, operating without action demonstration data, hand-engineered action primitives, or value-function guidance. Through online exploration, the agent identifies decision sequences that achieve task goals and compiles them into modular programs encapsulating the full perception-planning-control loop. Using RAX, we present a systematic multi-embodiment study on scaling online exploration across precision and long-horizon manipulation tasks using single-arm, bimanual, dexterous, mobile, and humanoid systems in simulation and on real robots. Generalization performance on unseen environments improves consistently as exploration scales. In simulation, RAX outperforms top baseline models by +37.4% on average. On real robots, RAX autonomously learns memory-dependent, articulated, high-precision, deformable, and long-horizon mobile manipulation tasks without human demonstrations, continually improving performance by composing verified skills from prior exploration sessions. As exploration scales, we observe emergent capabilities including active perception, error recovery, safety guardrails, and human-robot collaboration. We open-source RAX as a generalist robot-agent platform in which new robot embodiments are integrated through their APIs alone, without teleoperated data collection or policy training.


## 精读解读（中文）
### 一、研究动机
机器人学习依赖大规模示范数据和模型容量扩展，但部署新本体或新任务通常仍需专门遥操作数据，所得策略受模仿分布约束，难以泛化与持续自我改进。RAX 旨在把在线探索作为扩展轴，让机器人智能体通过获取在线经验和合成可执行程序来突破示范数据瓶颈。

### 二、技术方案（Method）
RAX 是以扩展在线探索为中心的开放源码机器人智能体框架：通用编码智能体直接生成机器人控制代码，不依赖动作示范数据、手工动作原语或价值函数引导；智能体通过在线探索识别可达成任务目标的决策序列，并将其编译为封装完整感知-规划-控制回路的模块化程序，再在单臂、双臂、灵巧手、移动和人形系统上于仿真与真实机器人开展多本体系统研究。新本体仅通过 API 集成，无需遥操作数据采集或策略训练。

### 三、结果（Result）
随着探索规模扩大，RAX 在未见环境上的泛化性能持续提升；仿真中平均超过最强基线模型 +37.4%。真实机器人上，RAX 无需人类示范即可自主学习依赖记忆、铰接物体、高精度、可变形和长程移动操作任务，并通过组合先前探索会话中验证过的技能持续提升性能；扩展探索还涌现出主动感知、错误恢复、安全护栏和人机协作能力。

### 四、结论（Conclusion）
RAX 表明扩展在线探索可作为替代专用遥操作语料与模仿策略训练的通路，使机器人智能体在多本体、仿真和真实环境中自主获得并复用可验证技能。其开放源码定位为通用机器人智能体平台，新本体仅需 API 集成即可接入，无需示范采集或策略训练。

### 五、方法论与关键技术细节
关键实现点包括：以通用编码智能体生成控制代码，在线探索产生决策序列并编译为模块化感知-规划-控制程序，经验证技能可跨探索会话组合复用；实验覆盖单臂、双臂、灵巧、移动和人形本体，兼顾仿真与真实机器人及精度与长程操作任务。摘要未给出具体损失函数、网络结构、超参数、探索预算与算力开销；潜在约束包括代码执行可靠性、真实机器人安全与成本、仿真到现实差距以及大规模在线探索的可复现性。
