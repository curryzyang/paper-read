# ELA: End-to-End Latent Action Policy Learning from Video Demonstrations

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Cheng-Chun Hsu, Peter Stone
- 机构：The University of Texas at Austin
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05571v1) · [PDF](https://arxiv.org/pdf/2611.05571v1)

## TLDR
ELA is an end-to-end framework that jointly trains a latent action model, latent action policy, and lightweight action decoder so latent actions are optimized for both policy learning and accurate action decoding, enabling robot imitation learning from abundant video demonstrations plus only a handful of action-labeled demonstrations.

## Abstract
Robot imitation learning is limited by the scarcity of action-labeled data, while action-free demonstrations such as videos are abundant. Recent latent-action methods learn action-relevant representations from observation transitions, but they do not optimize latent actions for downstream control, leading to latent representations that are difficult for policies to model and difficult to accurately decode into continuous robot actions. This paper introduces ELA, an end-to-end framework for learning from video demonstrations via latent actions jointly optimized for policy learning and action decoding. ELA jointly trains a latent action model, latent action policy, and action decoder, enabling policies to leverage abundant video data with only a handful of action-labeled robot demonstrations. Experiments on simulated and real-world manipulation tasks show that ELA consistently outperforms prior latent action baselines. Moreover, it integrates seamlessly with existing imitation learning methods through lightweight 4M-parameter action decoders, requiring no changes to policy architectures or training objectives. Additional materials can be found on: https://end2end-latent-action.github.io/


## 精读解读（中文）
### 一、研究动机
机器人模仿学习受限于动作标注数据稀缺，而无动作视频演示（如人类视频、未标注机器人轨迹）更易大规模获取。现有 latent action 方法多采用两阶段流程，先学 latent action 再作为固定目标训练策略，未针对下游控制联合优化，导致 latent 表示难以被策略建模、也难以准确解码为连续机器人动作。

### 二、技术方案（Method）
输入为无动作视频轨迹 V={o_t} 与少量动作标注数据 R={(o_t,a_t)}；用 IDM 从 (o_t,o_{t+k}) 推断 k 步 latent action z_t，FDM 以 (o_t,z_t) 重建 o_{t+k}，并用 iFSQ 量化作信息瓶颈；latent policy π(o_t)->z_t 用 L2 监督，action decoder ψ(z_t)->a_{t:t+k} 仅在标注数据上用 L2 训练；联合训练采用 LAM-update 与 Policy-update 交替：前者冻结策略、将 alignment/action/FDM 损失回传 LAM，后者冻结 LAM、用 alignment/policy 损失更新策略，alignment 将策略编码器中层特征经 MLP 投影后与冻结 DINOv3 参考特征做余弦相似度对齐；先进行 5k 迭代 warm-up 仅优化 FDM 与 action loss，部署时策略输出 latent 再由解码器转连续动作。

### 三、结果（Result）
在 LIBERO-10 的 50 条机器人演示中仅 5/10/20 条带动作标签，并加入无动作机器人视频；真实世界任务使用人类视频加少量机器人动作数据。论文报告 ELA 在仿真与真实操作任务上稳定优于先前 latent action 基线，并与使用更大数据预算训练的 IDM 基线对比分析 decodability 与 modelability；给定预览未提供具体成功率和数值表。

### 四、结论（Conclusion）
ELA 通过学习同时面向 modelability 与 decodability 联合优化的 latent action 空间，使策略能利用大量无动作视频并只需少量动作标签即可解码为连续控制。其轻量 4M 参数 action decoder 可无缝集成现有模仿学习方法，无需修改策略架构或训练目标，在仿真和真实操作任务上优于既有 latent action 方法。

### 五、方法论与关键技术细节
关键实现包括 k 步观测转移、transformer encoder 加 register tokens 聚合、iFSQ 量化瓶颈、FDM 图像重建 L2、action 解码 L2、policy 预测 L2 以及基于 DINOv3 冻结特征的余弦 alignment；act loss 仅用于有标签样本，交替更新与共享参考表示用于防止 latent action collapse；action decoder 约 4M 参数且开销与策略规模无关。局限在于解码器依赖少量动作标签、对齐依赖冻结感知编码器，k 步、量化与对齐权重等超参及交替训练约束需调优，且给定预览未给出完整消融与数值细节。
