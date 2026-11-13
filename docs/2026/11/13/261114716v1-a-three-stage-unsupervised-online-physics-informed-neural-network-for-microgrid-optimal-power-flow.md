# A Three-Stage Unsupervised Online Physics-Informed Neural Network for Microgrid Optimal Power Flow

- 区域：精读区
- 排名：3
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Abinash Giri, Yi Hu
- 机构：Michigan Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14716v1) · [PDF](https://arxiv.org/pdf/2611.14716v1)

## TLDR
The paper proposes a three-stage unsupervised online physics-informed neural network framework for microgrid optimal power flow that adapts in real time without offline retraining, satisfies system constraints, and achieves $43,665 lower operating cost than fmincon-based optimization under the same conditions.

## Abstract
Optimal allocation of generators is a key challenge in power systems to achieve economical dispatch while satisfying operational constraints. Conventional optimization techniques can be computationally expensive, limiting their applicability in real-time environments, and neural networks often require offline retraining under new operating conditions. This paper proposes a three-stage unsupervised online physics-informed neural network (PINN) framework for optimal power flow (OPF). Simulation results demonstrate that the proposed framework satisfies load demand and system constraints while achieving a $43,665 lower operating cost than fmincon-based optimization under the same operating conditions. The training process analysis further demonstrate the framework's ability to adapt its parameters online to variations in load demand and renewable generation in real time.


## 精读解读（中文）
### 一、研究动机
微电网经济调度需要实时求解AC-OPF，但AC-OPF非线性非凸，随场景反复求解计算昂贵；传统神经网络依赖代表性标注数据且不保证物理约束，现有无监督PINN又通常需要离线预训练，并在新工况下性能退化或成本高于基准。本文旨在构建无需预训练、可在线适应负荷与可再生波动的微电网OPF框架，同时兼顾经济性与AC潮流可行性。

### 二、技术方案（Method）
提出三阶段无监督在线PINN框架。Stage I用全连接网络接收顺序输入[有功负荷,无功负荷,可用光伏,可用风电,电池SOC]，输出发电机与电池有功/无功及母线电压幅值和相角；每个时间步用Adam在线反向传播K次，冷启动150次，后续迭代次数按相邻输入相对变化自适应，损失含潮流、成本、爬坡、电池SOC、线损、功率平衡和KKT边际成本项。Stage II基于等增量成本原则重分配常规机组有功，P_g*=clip((λ-b_g)/(2a_g),下限,上限)。Stage III在再调度后功率失配超过容差时，以PINN电压幅值和相角为初值执行牛顿-拉夫逊潮流校正，直至失配低于容差；电池SOC按效率和充放电功率逐步更新。

### 三、结果（Result）
在修改IEEE 14节点孤岛系统上，最大负荷85 MW，机组容量为[10,47,28,6,4.8,2.5] MW，框架满足负荷需求和系统约束，并在相同条件下比fmincon基准运行成本低43,665美元。训练分析显示冷启动150次时首样本损失最低且后续稳定，5/10/15/25/150次迭代耗时约0.05/0.09/0.13/0.23/1.23 s，在线过程能跟踪负荷与可再生变化。335天成本对比中仅PINN已低于fmincon，加入等增量成本再调度后节省约翻倍，加入NR后成本略升但保证可行运行点。

### 四、结论（Conclusion）
三阶段无监督在线PINN可在不依赖标注OPF解和离线预训练的情况下实现微电网AC-OPF在线求解，在保持物理与运行约束的同时获得优于fmincon的经济性，并具备实时自适应能力；NR校正是以轻微经济代价换取可行性的保障，整体适合变化工况下的在线经济调度。

### 五、方法论与关键技术细节
关键实现包括全连接网络4隐层128/256/512/256、ReLU、学习率1e-4、Adam、每步多次迭代并将参数保留到下一时刻；输入27维、输出50维；损失权重λ_PF、λ_cost、λ_ramp、λ_batt、λ_line、λ_bal、λ_KKT需调节，KKT项以边际成本与λ偏差惩罚。数据为顺序运行场景而非标注OPF解，约束含爬坡、电池SOC上下限、线损与功率平衡。局限是仅在修改IEEE 14节点孤岛微网验证，基线为MATLAB fmincon，未与现有需预训练的PINN方法直接对比，且NR校正会略增成本。
