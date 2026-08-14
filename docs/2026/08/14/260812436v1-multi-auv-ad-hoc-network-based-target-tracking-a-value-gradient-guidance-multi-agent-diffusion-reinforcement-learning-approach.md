# Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Jiaao Ma, Chuan Lin, Guangjie Han, Shengchao Zhu, Qian Zhu, Ying Liu, Zhenyu Wang
- 机构：Hohai University, Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12436v1) · [PDF](https://arxiv.org/pdf/2608.12436v1)

## TLDR
VGG-MADiffRL, a value-gradient-guided multi-agent diffusion reinforcement learning algorithm with a hierarchical MDCA control architecture, improves multi-AUV ad-hoc network cooperative target tracking by using diffusion policies and value-guided denoising to achieve faster convergence, higher accuracy, and more stable training under dynamic underwater conditions.

## Abstract
Multi-AUV ad-hoc network-based target tracking requires networked autonomous underwater vehicles (AUVs) to cooperatively track maneuvering targets under constrained acoustic communication, dynamic topology, and uncertain ocean disturbances. Although multi-agent reinforcement learning (MARL) enables decentralized coordination through centralized training, existing methods suffer from high-dimensional joint state-action modeling, noise-sensitive policy generation, leading to unstable training and degraded tracking. To address these issues, we propose VGG-MADiffRL, a value-gradient-guided multi-agent diffusion RL algorithm, and MDCA, a diffusion?based hierarchical control architecture. Leveraging underwater mission characteristics, we model sonar detection mechanisms and ocean current disturbances, formulating cooperative tracking for multi-AUV ad-hoc networks as an MDP. The proposed MDCA constitutes a three-tier closed-loop control framework: a global intelligent control layer, a local online training layer, and a physical action execution layer. This structure enables synergistic optimization across task allocation, local decision processes, and execution feedback. Within MDCA, the local online training layer is the policy learning framework; VGG-MADiffRL builds on diffusion policies and incorporates value gradients to guide action generation in the reverse denoising process, steering the generated actions towards higher expected returns. It employs twin value networks with joint optimization and soft target updates to mitigate overestimation and training oscillations, promoting more stable convergence. Experimental results show that VGG-MADiffRL consistently achieves faster convergence, higher tracking accuracy, and smoother training dynamics in cooperative tracking scenarios, validating its effectiveness and practical engineering value in dynamic underwater settings.


## 精读解读（中文）
### 一、研究动机
多AUV自组网协同跟踪要求网络化AUV在受限声学通信、动态拓扑和不确定海流扰动下协同跟踪机动目标，现有MARL方法虽能通过集中训练实现去中心化执行，但面临高维联合状态-动作建模困难、策略生成对噪声敏感等问题，导致训练不稳定且跟踪性能下降。

### 二、技术方案（Method）
提出VGG-MADiffRL算法和MDCA分层控制架构。首先依据主动声呐方程和海流Navier-Stokes方程建模声呐探测机制与海洋扰动，将协同跟踪问题形式化为马尔可夫决策过程。MDCA为三层闭环控制框架：全局智能控制层负责任务分配，本地在线训练层作为策略学习核心，物理动作执行层将输出转换为控制指令。VGG-MADiffRL基于扩散策略，在反向去噪过程中引入价值梯度引导动作生成，使采样动作朝向更高期望回报；采用孪生价值网络联合优化与软目标更新，以价值估计损失和策略梯度构成双目标优化，缓解过估计与训练振荡。

### 三、结果（Result）
实验结果显示，VGG-MADiffRL在协同跟踪场景中持续取得更快的收敛速度、更高的跟踪精度和更平滑的训练动态，相比现有方法具有明显优势，验证了其在动态水下环境中的有效性和实际工程价值。

### 四、结论（Conclusion）
VGG-MADiffRL通过价值梯度引导的扩散策略与分层控制架构，有效解决了多AUV自组网协同跟踪中的训练不稳定、策略表示受限和次优动作采样问题，为受限通信和动态拓扑下的水下协同决策提供了稳健可行的解决方案，具有较大的工程应用潜力。

### 五、方法论与关键技术细节
关键细节包括：声呐探测采用主动声呐方程计算余量，海流扰动通过Navier-Stokes方程建模；使用卡尔曼滤波融合预测与观测以抑制水下噪声；状态空间包含自身位姿、环境感知以及相对目标、邻居和地标的观测向量，动作空间为三维连续控制量且输出需经范围裁剪与缩放；采用孪生价值网络联合优化和软目标更新缓解过估计；扩散策略的反向去噪过程通过价值梯度引导生成高期望回报动作。由于全文预览不完整，具体超参数与数值指标未在摘要中提供，但实验中训练稳定性和跟踪精度的提升已得到验证。
