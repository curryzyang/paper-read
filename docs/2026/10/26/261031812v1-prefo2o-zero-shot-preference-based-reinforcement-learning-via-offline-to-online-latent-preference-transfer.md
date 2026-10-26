# PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ruiqi Wang, Dezhong Zhao, Xuesu Xiao, Erdem Biyik, Byung-Cheol Min, Guohua Chen
- 机构：Indiana University Bloomington, Beijing University of Chemical Technology, George Mason University, University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31812v1) · [PDF](https://arxiv.org/pdf/2610.31812v1)

## TLDR
PrefO2O learns a task-invariant latent preference space from offline source-task preference data and transfers it online via confidence-weighted optimal transport alignment, enabling zero-shot preference-based reinforcement learning on unseen target tasks without human feedback.

## Abstract
Preference-based reinforcement learning (PbRL) has emerged as a promising paradigm for learning robot behaviors aligned with human intent. However, its scalability is fundamentally limited by the need to collect expensive human preference labels for every new task. In this work, we present PrefO2O, an offline-to-online latent preference transfer framework that enables zero-shot PbRL on unseen target tasks without requiring any human feedback. The core idea is to learn a task-invariant latent preference space from a small amount of offline preference data on source tasks, where transferable preference structures are disentangled from task-specific variations. This learned manifold allows PrefO2O to transfer preference structures and reward priors to new tasks under distribution shift, while confidence-weighted optimal transport alignment generates reliable pseudo-preference supervision for online reward adaptation. Extensive experiments on robotic manipulation and locomotion benchmarks demonstrate that PrefO2O substantially outperforms existing preference-transfer baselines and matches or exceeds PbRL methods trained with real human feedback, while generalizing across multi-to-one and one-to-one transfer settings as well as across different robot embodiments.


## 精读解读（中文）
### 一、研究动机
偏好强化学习能让机器人行为对齐人类意图，但每个新任务都从零收集人类偏好标签，成本高且难以扩展；现有合成反馈、元学习和零样本偏好迁移方法仍受反馈不一致、目标任务标注需求、原始轨迹空间对齐脆弱及状态动作维度共享假设等限制。本文旨在利用少量源任务离线偏好数据，实现对未见目标任务无需任何人类反馈的零样本 PbRL。

### 二、技术方案（Method）
PrefO2O 采用离线到在线两阶段框架：离线阶段聚合多个源任务偏好数据，联合训练带任务专属输入适配器和共享时序池化的轨迹编码器、以成对轨迹表征差分为输入的偏好 VAE，以及按 Bradley-Terry 偏好交叉熵训练的元奖励模型；VAE 通过重构损失和 KL 正则诱导任务不变的隐偏好流形。在线阶段在目标任务上冻结偏好 VAE，用预训练轨迹编码器和奖励模型热启动，采样目标轨迹对并在隐空间执行熵正则 Gromov-Wasserstein 最优传输，将源任务偏好标签传播为目标轨迹对的伪偏好，并以 OOD 感知置信度加权监督在线奖励适配与策略优化。

### 三、结果（Result）
在机器人操作和运动基准上，PrefO2O 显著优于现有偏好迁移基线，并能匹配或超过使用真实人类反馈训练的 PbRL 方法；方法在无目标任务人类反馈条件下实现零样本迁移，且在 multi-to-one、one-to-one 迁移以及同/跨机器人本体设置中展现泛化能力。摘要未给出具体数值指标，但可复现结论是隐空间偏好迁移与置信度加权最优传输对性能提升关键。

### 四、结论（Conclusion）
PrefO2O 表明，人类偏好中存在可跨任务复用的共享结构，将其学习为任务不变隐偏好空间后，可把源任务奖励先验和偏好监督迁移到未见目标任务，从而消除新任务的人类偏好标注瓶颈。该框架为可扩展、跨任务和跨本体的零样本偏好强化学习提供了可行路径。

### 五、方法论与关键技术细节
关键实现包括按任务适配器处理异构状态动作维度、共享步编码器与时间平均池化形成轨迹隐表征、以轨迹表征差分而非绝对轨迹作为偏好 VAE 输入、VAE 的重构与 KL 正则、元奖励模型的 Bradley-Terry 偏好损失，以及在线阶段冻结 VAE 作为稳定参考并用熵正则 Sinkhorn 近似求解 Gromov-Wasserstein 传输。伪偏好由传输矩阵传播并加 OOD 置信度权重；论文假设源与目标任务属于相关领域且偏好结构可迁移，具体源偏好预算、网络宽度、传输熵系数等超参数在摘要和预览中未完整给出，跨分布迁移时伪标签可靠性和传输计算成本仍是限制。
