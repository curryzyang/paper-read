# Rollout-Decoded Reconstruction for Long-Horizon Prediction in Latent World Models

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Rishi Shah, Rishav Shrestha
- 机构：E3A Healthcare
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.25017v1) · [PDF](https://arxiv.org/pdf/2608.25017v1)

## TLDR
Rollout-Decoded Reconstruction (RDR) closes the train-deployment gap in latent world models by adding a single training-time loss that decodes the model's free-running rollout and penalizes reconstruction error against ground truth, improving valid prediction time on chaotic Kuramoto-Sivashinsky forecasting by 1.80× with no added parameters.

## Abstract
A latent world model trains its decoder on latents anchored to observations, then deploys it on the model's own free-running rollout, hundreds of steps past the last observation. Rollout-Decoded Reconstruction (RDR) closes this gap with a single loss term that free-runs the model during training exactly as evaluation will, decodes every rollout latent, and penalizes reconstruction error against ground truth. The term adds no parameters, costs training-time compute only, and reduces to the standard objective at weight zero, so every comparison in this paper is a one-flag A/B. On the chaotic Kuramoto-Sivashinsky equation, RDR raises valid prediction time (the time to first crossing of normalized error 0.5) from $3.87 \pm 0.23$ to $6.97 \pm 0.42$ time units at an identical 193,568 parameters, a $1.80\times$ improvement confirmed on seeds never used in selection and holding in 10 of 10 preregistered configurations at ratios of 1.71-2.50$\times$. The results come from a single system; a sweep in which the advantage grows with latent width is descriptive, and control experiments on two classic tasks are preliminary.


## 精读解读（中文）
### 一、研究动机
潜在世界模型在训练时仅用锚定到观测的隐状态训练解码器，但部署时解码器要处理模型自回归 rollout 数百步后产生的漂移隐状态，导致训练与推理分布不一致，长期预测误差提前超过阈值。现有 latent world model 都未系统研究这一 decoder 训练分布失配问题，因此提出直接让训练过程与评估过程对齐的解码目标。

### 二、技术方案（Method）
RDR 在训练时让模型从编码初始状态开始完全自由 rollout，与评估时路径一致；对 rollout 中每一步隐状态都进行解码，并将重建结果与真实场计算 L2 重建误差作为额外损失项加入总目标。总损失为 L_TF + α_e L_R + L_OBS + L_recon + λ L_RDR，其中 λ=0.3，α_e 在 epoch 2 到 5 从 0 线性升到 1，rollout 分支在 2 个 warm-up epoch 后开启；模型为 64 维 KS 场快照经 MLP 编码器映射到 32 维隐状态，S5 四层状态空间模型推进隐状态，MLP 解码器映射回场空间；训练时窗口长度为 160 快照，rollout 长度 K=128，batch size 64，Adam 学习率 3e-4，训练 320 epoch，每臂 3 个随机种子。RDR 不增加参数，推理成本不变，仅在训练时多出 K 次解码器前向与反向计算。

### 三、结果（Result）
在混沌 Kuramoto-Sivashinsky 方程上，RDR 将有效预测时间（VPT@0.5）从后验-only 基线的 3.87±0.23 时间单位提升到 6.97±0.42 时间单位，参数同为 193,568，提升 1.80 倍；在 10 个预注册配置中 RDR 全部获胜，比值 1.71–2.50 倍。长期 1300 步评估下同样从 3.77 提升到 6.90。与观测空间 pushforward 预测器（7.00±0.26）对比，RDR 与之持平，说明在完全可观测 64 维系统上隐瓶颈未带来额外优势；RDR 优势随训练 epoch 增加而继续增长，160/240/320 epoch 下 VPT 为 5.27/6.37/6.90，未见饱和。

### 四、结论（Conclusion）
RDR 通过单个训练期损失项直接消除 latent world model 解码器的训练/部署分布失配，在混沌长期预测任务上带来一致且显著的 VPT 提升，且不增加参数、不改变架构、不增加推理开销。效果在预注册的 10 个配置中全部复现，说明该目标可作为现有 latent world model 的通用即插即用改进项；但实验仅基于单一 KS 系统，latent 宽度消融为描述性结果，两个经典任务控制实验仍属初步。

### 五、方法论与关键技术细节
关键细节：RDR 损失对 rollout 中每一步隐状态解码并与真实场做 L2 重建误差，梯度同时流向解码器、预测器和编码器；λ 在 0.1–1.0 范围内结果平坦，操作权重 0.3；两臂计算同一 rollout，边际成本仅为训练期额外 K 次解码器前向/反向。共享解码器形式（193,568 参数）强于分裂解码头形式（243,296 参数，VPT 6.47），排除容量解释。VPT 定义为归一化 RMSE 首次超过 0.5 的时间，KS L=22 下最大 Lyapunov 指数约 0.043，一个 Lyapunov 时间为 23.26 时间单位；评估使用 64 条留出轨迹，3 种子平均。局限性：未测试离散隐状态、KL balancing、latent overshooting、partially observable/像素观测等场景；TD-MPC2、MuDreamer 等无解码器模型不适用；在完全可观测系统上隐瓶颈无增益。预注册协议锁定了 primary arm 门槛 5.77 tu，primary arm 实测 6.47±0.40，通过门槛。训练时长是唯一持续带来提升的杠杆，更长训练留待未来工作。
