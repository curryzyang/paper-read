# See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

- 区域：精读区
- 排名：4
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jiawei Chen, Yinxi Wang, Zihan Yang, Meijun Gao, Yaowei Liu, Shuming Zhang, Zecheng Li, Xiangju Mi, Yuxuan Liu, Runzhong Huang, Tianlin Li, Xun Zhang, Zhengyang Wang, Xu Miao, Tong Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31762v1) · [PDF](https://arxiv.org/pdf/2610.31762v1)

## TLDR
RepresentNav is a navigation foundation model that learns a self-constructed representation space over multi-depth vision-foundation-model features and uses a JEPA-trained latent “dream” of the next scene to guide actions, achieving state-of-the-art navigation performance on benchmarks and real robots.

## Abstract
What visual representation should a navigation policy act on? Navigation policies built on vision foundation models largely leave representation design to the encoders' pretraining objectives. We present RepresentNav, a navigation foundation model built on a self-constructed representation space: a visual representation constructed by the policy's own objectives from vision foundation models. RepresentNav builds this space with Representation Residuals, a compact three-layer transformer that attends over features spanning the full depth of multiple complementary vision foundation models, so that the policy learns to see what it needs for navigation. In the same space it dreams what it wants: before every action a latent chain-of-thought predicts the representation of the scene a moment ahead. The dream is trained end-to-end with the policy as a joint-embedding predictive architecture (JEPA), with a next-representation prediction loss and a regularizer on its targets. RepresentNav sets a new state of the art on VLNVerse, VLN-CE R2R, EVT-Bench, and two point-goal benchmarks, and its gains carry over to a physical robot amid clutter and moving people. On VLNVerse fine-grained, RepresentNav achieves 83.80% success, outperforming the previous state of the art by 20.05 percentage points, and on EVT-Bench distracted tracking it reaches 85.5% with a single camera (+10.1). With the same encoders, the self-constructed space clearly outperforms concatenating their outputs and learns to weight their layers unevenly, and a dream in it cuts collisions by a quarter. A single dreamed latent decodes into the depth, semantics, and 3D occupancy of the scene a moment ahead, more accurately than pretrained encoders applied to the real future frame, although occupancy is never supervised, and the rollout tracks the robot's own motion over the next second: the dream emerges as a compact latent world model.


## 精读解读（中文）
### 一、研究动机
导航策略应当基于何种视觉表征来决策仍缺乏系统设计，现有方法大多把表征设计交给视觉基础模型的预训练目标，导致策略看到的不一定是导航所需。作者提出应构建由策略自身目标驱动的自构造表征空间，使策略既能“看到所需”，也能“想象所要”。

### 二、技术方案（Method）
RepresentNav 输入单相机视觉观测，并提取多个互补视觉基础模型全深度层特征；用仅三层的 Transformer 模块 Representation Residuals 对这些跨模型、跨深度特征进行注意力融合，形成自构造表征空间。在每个动作前，策略在该空间中通过 latent chain-of-thought 预测未来一刻的场景表征，并以 JEPA 方式与策略端到端联合训练，采用下一表征预测损失和对预测目标的正则化。推理时先“梦想”下一时刻表征，再结合当前表征输出导航动作。

### 三、结果（Result）
RepresentNav 在 VLNVerse、VLN-CE R2R、EVT-Bench 和两个 point-goal 基准上取得新的 SOTA，并迁移到杂物与行人环境中的实体机器人。VLNVerse fine-grained 成功率 83.80%，比此前 SOTA 高 20.05 个百分点；EVT-Bench distracted tracking 单相机达到 85.5%，提升 10.1。相同编码器下，自构造空间明显优于简单拼接多模型输出，并学会非均匀地加权各层；其“梦想”使碰撞减少约四分之一。

### 四、结论（Conclusion）
结果表明，导航表征应由策略目标自构造，而非完全继承视觉基础模型的预训练目标；将表征学习与未来表征预测结合，可同时提升导航性能和鲁棒性。 dreamed latent 还能无 occupancy 监督地解码未来深度、语义和 3D occupancy，并跟踪机器人未来一秒运动，说明其涌现为紧凑的潜在世界模型。

### 五、方法论与关键技术细节
关键实现是三层 Transformer 的 Representation Residuals 对多 VFM 全深度特征做注意力聚合，以控制复杂度并学习层间非均匀权重；JEPA 训练使用下一表征预测损失加目标正则化，latent chain-of-thought 在每个动作前预测未来表征。梦想 latent 可解码深度、语义和 3D occupancy，其中 occupancy 从未被显式监督，且单相机即可在实体机器人上验证；局限包括依赖预训练 VFM 特征、预测时域约未来一秒，具体损失权重与训练超参摘要未给出，需查原文复核。
