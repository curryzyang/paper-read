# Composite-Gradient Learning for Shared Control Authority Between Deep Reinforcement Learning and Model Predictive Control

- 区域：精读区
- 排名：1
- 匹配度：5.9/10
- 来源：arxiv
- 作者：Giray Önür, Azita Dabiri, Bart De Schutter
- 机构：Delft University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17697v1) · [PDF](https://arxiv.org/pdf/2609.17697v1)

## TLDR
This paper proposes composite-gradient learning (CGL), which treats the DRL agent’s action and the MPC controller’s input as a joint action during training to explicitly account for their interaction, and shows on freeway traffic networks that it provides modest benefits mainly under strong DRL-MPC coupling.

## Abstract
Integrated deep reinforcement learning (DRL) and model predictive control (MPC) methods are increasingly used to control autonomous systems by combining their complementary capabilities. DRL learns control policies through interaction with the environment. MPC uses a system model to optimize control inputs while accounting for constraints. In DRL-MPC frameworks with shared control authority, both the DRL agent and the MPC controller each determine part of the control inputs. However, common learning formulations treat MPC as part of the environment and therefore do not explicitly account for MPC's contribution to control or its interaction with the DRL agent. This paper proposes a novel composite-gradient learning (CGL) method that integrates the MPC controller into the learning process by representing the DRL and MPC control inputs as a joint action and accounting for their interaction when updating the DRL agent during training. CGL is evaluated on two multi-class freeway traffic networks with different strengths of interaction between the DRL and MPC control inputs and it is compared with alternative methods that treat MPC as part of the environment or that only partially incorporate MPC into learning. The results show that CGL offers limited benefit under weak interaction, but learns higher-performing control policies than the alternative methods in a subset of training runs under strong interaction, although the average control-performance gains remain modest.


## 精读解读（中文）
### 一、研究动机
DRL与MPC在共享控制权限的分层框架中互补，但常见学习式表述把MPC视为环境的一部分，只从环境交互中更新DRL，未显式计入MPC控制输入对性能评估和DRL更新的贡献。MPC在预测未来状态时需要DRL的未来动作，因此DRL动作会通过影响MPC预测而间接影响高层控制输入，这种双向耦合在强耦合场景下会令学习表述不完整并限制性能。

### 二、技术方案（Method）
作者将分层DRL-MPC共享控制问题建模为MDP，把低层DRL动作与高层MPC控制输入组成联合动作。训练时，高层MPC在有限预测时域内使用系统模型、扰动预测和当前DRL策略副本进行带约束优化，并通过ZOH将高层输入作用于系统；低层确定性DRL策略根据观测输出高频控制输入，同样经ZOH施加。所提复合梯度学习在更新DRL时同时计算DRL动作的直接效应和经由MPC控制律产生的间接效应，并采用层级感知的数据存储与采样方案，在两次MPC更新之间复用MPC计算以降低训练成本。

### 三、结果（Result）
在两个具有不同DRL-MPC控制输入耦合强度的多类高速公路交通网络上，CGL与将MPC视为环境或仅部分纳入MPC学习的方法进行了对比。结果表明，弱耦合下CGL带来的收益有限；强耦合下CGL在部分训练运行中学习到比对比方法性能更高的控制策略，但平均控制性能提升仍然有限。

### 四、结论（Conclusion）
该工作说明在共享控制权限的DRL-MPC框架中，显式建模DRL与MPC之间的联合作用并在更新中计入MPC的贡献，可在强耦合情形下改善部分训练结果，而非在所有情形下稳定大幅提升。CGL的有效性依赖DRL与MPC控制输入之间的耦合强度，其实际收益呈现条件性和运行间差异性。

### 五、方法论与关键技术细节
关键实现包括：将高层MPC控制输入与低层DRL动作构成联合动作空间；MPC求解有限时域约束优化，预测模型中嵌入当前固定DRL策略副本；采用ZOH处理多时间尺度控制保持；状态与输入约束、扰动预测和预测观测映射均纳入MPC；DRL更新使用复合梯度同时捕捉直接与经由MPC的间接路径；层级感知数据存储和采样复用MPC计算。局限是平均性能增益温和，强耦合下也仅在部分训练运行中优于基线，评价场景限于多类高速公路交通网络。
