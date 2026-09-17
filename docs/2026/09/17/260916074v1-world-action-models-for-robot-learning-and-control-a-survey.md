# World-Action Models for Robot Learning and Control: A Survey

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Zuxing Lu, Hongjia Zhai, Guanzhi Wang, Huajian Zeng, Jiaqi Yang, Jingyu Liu, Lei Cheng, Yuantai Zhang, Yuheng Qiu, Zezhou Cheng, Ivan Laptev, Danfei Xu, Benjamin Riviere, Giuseppe Loianno, Eric Xing, Xingxing Zuo
- 机构：Georgia Tech, New York University, Amazon FAR, University of Virginia, Caltech, UC Berkeley, MBZUAI
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16074v1) · [PDF](https://arxiv.org/pdf/2609.16074v1)

## TLDR
This survey reviews World-Action Models (WAMs), which integrate predictive world modeling with executable action generation for robot learning and control, offering a unified taxonomy, cross-domain applications, evaluation protocols, and open challenges.

## Abstract
Robots operating in open environments act under partial observability, physical constraints, and dynamic task contexts. Beyond mapping observations and language instructions to actions, they must anticipate how candidate actions may affect future states and task-relevant outcomes. Recent advances in world models, video generation, and Vision-Language-Action (VLA) policies have motivated the development of World-Action Models (WAMs), which couple future world prediction with executable action generation. This survey provides a robotics-oriented review of WAMs. We clarify their scope relative to conventional world models, model-based reinforcement learning, action-conditioned video generation, and reactive VLA policies, and organize existing methods through a unified taxonomy covering representations, transition modeling, action interfaces, architectures, training pipelines, data modalities, and scaling strategies. We further review applications of WAMs in manipulation, navigation, and autonomous driving, and we summarize the datasets, benchmarks, metrics, and protocols used to evaluate WAM systems. Finally, we discuss key challenges in action alignment, world-action factorization, spatial and multi-view consistency, long-horizon memory, neural simulation for closed-loop policy learning, and efficient inference. Taken together, this survey aims to provide a concise technical foundation for integrating predictive world modeling with action generation, toward more reliable embodied robot intelligence. Project page: https://rcl-robotics.github.io/Awesome-World-Action-Models.


## 精读解读（中文）
### 一、研究动机
开放环境中的机器人需要在部分可观测、物理约束和动态任务语境下长时间行动，除了把观测与语言指令映射为动作，还必须预判候选动作会如何改变未来状态与任务相关结果。然而主流 VLA 策略基本是反应式的，缺乏对动作后果的显式建模；传统世界模型又常与规划器、策略分离训练部署，导致预测保真度与控制效用错配，视觉上合理的未来未必可执行。加之相关文献分散在视频生成、具身基础模型、VLA、基于模型的强化学习与机器人模仿学习中，命名与评测口径不一，因此急需一篇面向机器人学的综述来厘清范围、设计轴与评价标准。

### 二、技术方案（Method）
该综述以 POMDP ⟨S,A,T,R,Ω,O⟩ 为统一形式化框架，把 WAM 定义为在观测历史 o_{<t} 与语言指令 ℓ 的条件下联合预测未来状态轨迹 ô_{t:t+H} 与动作块 â_{t:t+H} 的预测式控制模型，也涵盖先预测未来再经逆动力学接口反推动作的变体。作者沿表示空间、转移建模、动作接口、架构结构、训练流程、数据模态与扩展策略等维度构建统一分类法，覆盖潜动力学模型（Dreamer、TD-MPC 类）、动作条件视频生成、扩散与流匹配策略、逆动力学系统以及统一多模态架构，并配以演进时间线。随后按操作、导航、自动驾驶与通用具身机器人四个应用域梳理代表方法，归纳数据集、基准、指标与评测协议，并讨论开放挑战。

### 三、结果（Result）
作为综述，本文不提出新模型或新实验，而是给出统一视角：相比标准 VLA，WAM 引入了推理动作后果的预测结构；相比传统基于模型的强化学习，WAM 进一步融合多模态基础模型条件、大规模离线机器人数据与摊销式动作生成。作者指出当前评测将预测质量、模仿精度、规划性能与真机鲁棒性割裂衡量，尚无法回答想象出的未来是否物理可行、时序一致并真正提升闭环控制。文章还通过时间线刻画了从 TD-MPC、Dreamer、扩散策略到 Cosmos-Policy、FastWAM、DreamZero 等里程碑的逐步收敛，并提供可复现的分类清单与项目页。

### 四、结论（Conclusion）
综述的核心主张是把世界预测与动作生成耦合进同一学习或推理过程，是通向可扩展、可靠、可部署具身智能的关键路径，WAM 可作为统一分析这一类方法的透镜，并厘清其与传统世界模型、基于模型的强化学习、动作条件视频生成和反应式 VLA 的边界。作者呼吁在动作对齐、世界-动作因子分解、空间与多视图一致性、长时程记忆、面向闭环策略学习的神经仿真以及高效推理等方向继续攻关。

### 五、方法论与关键技术细节
形式化要点包括：隐状态空间 Z 是足以预测未来动力学的交互历史低维压缩编码，隐动作空间 U 是连接高层指令与低层电机控制的紧凑行为表示，语言指令 ℓ 作为行为条件；RSSM 以确定性状态 h_t 与随机状态 s_t 建模潜动力学，世界模型可显式训练（带解码器，如 Dreamer）或隐式训练（潜空间正则化，如 TD-MPC、DINO-WM、LeWM）。方法学关键轴为表示、转移建模、动作接口（联合预测或逆动力学）、架构、训练流程、数据模态与扩展策略。局限在于本文属综述性质，未在统一基准上给定量对比，WAM 与相邻范式的边界依赖作者定义，且评测碎片化、实时推理与安全部署约束仍是未解缺口。
