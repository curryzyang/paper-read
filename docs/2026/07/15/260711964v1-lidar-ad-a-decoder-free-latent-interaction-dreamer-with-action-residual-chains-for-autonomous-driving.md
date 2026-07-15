# LIDAR-AD: A Decoder-Free Latent-Interaction Dreamer with Action-Residual Chains for Autonomous Driving

- 区域：精读区
- 排名：1
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Yongzhi Liu, Yang Xiao, Zhong Cao, Zeng Kang, Sunan Zhang, Zhaozhi Dong, Guojun Yu, Weichao Zhuang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11964v1) · [PDF](https://arxiv.org/pdf/2607.11964v1)

## TLDR
LIDAR-AD introduces a decoder-free latent world model for autonomous driving that replaces observation reconstruction with risk-weighted latent alignment and models vehicle control as residual action updates with contrastive learning, achieving superior closed-loop decision-making and success rates across diverse driving scenarios.

## Abstract
Autonomous driving requires long-horizon closedloop decision making in dynamic traffic environments. Latent world models offer an effective framework for this problem by enabling imagination-based decision making in compact latent spaces. However, multi-source observations contain controlirrelevant redundancy, whereas reliable driving decisions rely on risk-relevant relations, future dynamics, and continuous action adjustments. This mismatch makes observation reconstruction and absolute action modeling suboptimal for learning decisionrelevant latent dynamics. We propose LIDAR-AD, a decoderfree Latent-Interaction Dreamer with Action-Residual Chains for autonomous driving. LIDAR-AD replaces observation reconstruction with redundancy-reduced latent alignment, encouraging compact representations of risk-relevant relations in multi-source driving inputs. It further models vehicle control as residual action updates and uses residual-action sequence contrastive learning to align multi-step residual-driven rollouts with future latent states. A deterministic analysis shows that the latent-tanh residual parameterization preserves interior action reachability while representing smooth long-horizon control as compact local updates. Together, these designs improve risk-aware state abstraction, continuous-control modeling, and long-horizon dynamics prediction. Extensive experiments across diverse simulated driving scenarios demonstrate that LIDAR-AD consistently outperforms world-model baselines, achieving the highest reward and the best success rate among learning-based methods. Evaluations on nuPlan-derived log-reconstructed scenarios further demonstrate the transferability of LIDAR-AD under real-world traffic layouts.


## 精读解读（中文）
### 一、研究动机
当前世界模型在自动驾驶中面临两大挑战：多源观测包含与控制无关的冗余信息，导致模型将容量浪费在弱决策相关的特征上；传统绝对动作建模忽略了驾驶中连续命令的高度相关性，难以捕捉微小调整对长期状态的影响。这些问题使得观测重建和独立动作预测无法有效学习决策相关的潜在动态。

### 二、技术方案（Method）
LIDAR-AD基于RSSM框架，集成三个核心模块：无解码器潜在交互表示（DLIR）将多源观测（ego状态、LiDAR距离、导航）分组编码，通过风险描述子（含距离衰减、路线误差、车辆状态）加权，用Barlow Twins损失对齐潜在状态与交互感知嵌入，避免冗余重建；残差动作世界模型（RAWM）将前一动作映射回预tanh空间并添加残差，形成联合动作嵌入作为RSSM转移输入，保持零残差时命令不变并实现单步可达性；残差动作链对比学习（ARC-CL）递归应用多步残差驱动展开，用InfoNCE损失对齐预测潜在状态与未来后验状态。训练时联合优化预测损失、RSSM正则化、DLIR损失和ARC-CL损失，再通过潜在想象进行actor-critic策略学习。

### 三、结果（Result）
在MetaDrive模拟的多样化驾驶场景（密集交通、交叉口、环岛）中，LIDAR-AD在累积奖励和成功率上全面超越规则方法和基于学习的方法（SAC、PPO、DreamerV3、R2-Dreamer），并取得最优控制平滑性（更小的转向和纵向控制差值）。在nuPlan日志重构的真实交通布局场景中，LIDAR-AD展现出良好的迁移能力，其归一化AUC@1M步骤显示样本效率显著提高。

### 四、结论（Conclusion）
LIDAR-AD通过无解码器潜在对齐、残差动作参数化和多步对比学习，有效解决了观测冗余和动作连续性问题，使世界模型聚焦于风险相关的交互变化和累积控制效果，从而改进了长时域闭环驾驶决策。该框架在模拟环境中验证了其优越的性能和泛化能力，为自动驾驶中决策相关潜在动态学习提供了新范式。

### 五、方法论与关键技术细节
数据与输入：使用MetaDrive模拟器生成包含ego状态、64线LiDAR距离和导航信息的观测，动作空间为二维连续控制（纵向加速度和转向）；基于nuPlan日志重构真实城市场景。先验假设：驾驶动作连续步骤间高度相关，残差变化范围远小于绝对动作空间，据此设计残差参数化。损失函数：世界模型包含RSSM预测损失（奖励、继续）、DLIR损失（风险加权Barlow Twins：对齐项和去冗余项）、ARC-CL损失（InfoNCE，温度参数τ=0.1）。超参数：残差范围通过tanh边界控制，风险描述子权重α=1，对比学习序列长度K=5。复杂性与约束：DLIR引入轻量级分组编码器和门控融合，总参数量低于DreamerV3解码器；ARC-CL仅增加对比投影头和计算开销。局限性：残差动作在单步内可达完整动作空间，但受限于残差范围可能导致极端机动需要多步累积；风险描述子依赖手工设计特征，可能无法覆盖所有风险模式；当前仅在模拟环境验证，物理世界需考虑传感器噪声和动力学差异。
