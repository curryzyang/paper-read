# DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models

- 区域：精读区
- 排名：1
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang, Pengfei Zhou, Wangbo Zhao, Fangyuan Kong, Pengfei Wan, Kun Gai, Yang You
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12572v1) · [PDF](https://arxiv.org/pdf/2610.12572v1)

## TLDR
DiffusionART is an efficient, stable, and scalable online reinforcement learning method for diffusion models that aggregates each prompt’s rewards into a shared reward-improving direction to eliminate hidden forward–reverse consistency and avoid EMA tuning, adding a trust-region-masked second update for drift-adaptive restoration and achieving much faster, higher-reward image and video generation than Flow-GRPO and DiffusionNFT without differentiable rewards or per-task tuning.

## Abstract
Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-moving-average (EMA) off-policy training. We show that NFT-style objectives contain a hidden forward--reverse consistency force that joint positive--negative training cancels only partially, and that EMA stabilizes training through restoration rather than off-policy rollouts. We introduce DiffusionART (Diffusion Reinforcement with Aggregation-First Reward Tilting), which aggregates each prompt's rewards into a shared reward-improving direction for reverse-process states, removing the consistency force by construction, and adds a trust-region-masked second update for drift-adaptive restoration without EMA tuning. It requires no differentiable reward model, remains effective with fewer samples per prompt, and supports pairwise reward models (DiffusionART-Pairwise). Across image and video generation, DiffusionART trains efficiently and stably without per-task tuning. In particular, on HunyuanVideo-13B with equally weighted visual and motion quality rewards, DiffusionART reaches the late-stage mean reward levels of DiffusionNFT and Flow-GRPO-Fast with 12.02 and 11.72 times fewer GPU hours, respectively, while achieving 28.8% and 53.0% higher mean training rewards.


## 精读解读（中文）
### 一、研究动机
扩散模型在线强化学习可在仅有黑盒奖励时进行微调，但反向过程方法（如 Flow-GRPO）因信用分配差而效率受限，前向过程方法（如 DiffusionNFT）虽高效却依赖精细调参的 EMA 离策略训练才稳定。作者因此要解决效率与稳定性难以兼得、且需要逐任务调参的问题，并支持不可微奖励。

### 二、技术方案（Method）
DiffusionART（Aggregation-First Reward Tilting）面向文本到图像/视频的扩散或流模型：输入为文本 prompt 与预训练生成模型，对每个 prompt 采样若干生成轨迹并仅用黑盒奖励打分，先把同一 prompt 的奖励聚合成一个共享的奖励改进方向，在反向去噪状态上直接构造 reward-tilted 更新，从结构上消除 NFT 类目标中隐藏的前向-反向一致性力。训练包含两步更新：主更新执行聚合优先的奖励倾斜；第二更新经信任域掩码筛选，在策略相对参考/行为策略漂移过大时做自适应恢复，从而替代 EMA 的稳定作用。整个流程无需可微奖励模型，也无需 EMA 离策略调参，并可通过成对奖励模型扩展为 DiffusionART-Pairwise；微调后推理仍按原扩散采样流程执行。

### 三、结果（Result）
在图像与视频生成任务上，DiffusionART 无需逐任务调参即可稳定高效训练；在 HunyuanVideo-13B 上，当视觉质量与运动质量奖励等权时，它以比 DiffusionNFT 和 Flow-GRPO-Fast 分别少 12.02 倍和 11.72 倍的 GPU 小时达到两者后期平均奖励水平，同时平均训练奖励分别高 28.8% 和 53.0%。摘要还指出该方法在每 prompt 样本更少时仍有效，并能兼容成对奖励模型。

### 四、结论（Conclusion）
DiffusionART 表明 NFT 类前向过程目标中的稳定性问题可归因于隐藏的前向-反向一致性力，而 EMA 主要起恢复而非离策略采样作用；用聚合优先奖励倾斜与信任域掩码的第二更新即可同时获得高效、稳定和可扩展的扩散模型在线 RL 微调。该方法减少了对 EMA 调参、可微奖励和大量采样的依赖，为图像与视频生成模型的黑盒奖励对齐提供了更实用的方案。

### 五、方法论与关键技术细节
关键实现点包括：以 prompt 为单位聚合奖励，构造反向过程状态上的共享改进方向，从而按构造消除一致性力；奖励只需黑盒可查询，不要求可微，且支持 pairwise 奖励；第二更新受信任域掩码约束，用于漂移自适应恢复，替代 EMA 稳定机制；训练可用较少 prompt 内样本。评估覆盖图像与视频生成，重点为 HunyuanVideo-13B 上的视觉与运动质量等权奖励，报告 GPU 小时与平均奖励对比。局限方面，摘要未展开所有任务、奖励模型噪声/偏差、聚合粒度对多样性的影响以及具体超参与复杂度，落地时仍需关注奖励质量与信任域阈值选择。
