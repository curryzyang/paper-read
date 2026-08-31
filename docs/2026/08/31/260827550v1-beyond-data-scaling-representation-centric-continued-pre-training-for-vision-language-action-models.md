# Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Senqiao Yang, Chengyao Wang, Yuxin Chen, Zixuan Wang, Longxiang Tang, Haokun Gui, Jinhui Ye, Changsheng Lu, Xiaoyang Wu, Mingkang Zhu, Pengguang Chen, Shu Liu, Zhuotao Tian, Hengshuang Zhao, Bei Yu, Jiaya Jia
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27550v1) · [PDF](https://arxiv.org/pdf/2608.27550v1)

## TLDR
A representation-centric continued pre-training recipe for Vision-Language-Action models (VLAct) that preserves VLM priors, uses multi-head continuous action co-supervision, and shares cross-embodiment action semantics, consistently outperforming large-scale industrial VLA systems and enabling data-efficient unseen-embodiment transfer under modest compute.

## Abstract
Scaling robot data is crucial for building generalist Vision-Language-Action (VLA) models, yet robot trajectories are harder to scale than web-scale image-text data because embodied collection is costly and sparsely covers the physical world. This makes representation quality a central bottleneck: under a fixed robot-data budget, continued pre-training must turn limited trajectories into transferable visual-action knowledge rather than merely fit actions. We propose VLAct, a VLA-oriented VLM backbone trained on broad, heterogeneous, multi-embodiment robot data before task-specific fine-tuning. VLAct preserves the broad VLM prior and encourages shared action semantics across embodiments through VLM-prior preservation, multi-head continuous action co-supervision, and a partially unified cross-embodiment action layout, while allowing task-specific action heads during fine-tuning. Across simulation, real-world, and unseen-embodiment transfer, VLAct consistently improves downstream performance under fixed fine-tuning protocols. On LIBERO-Plus and RoboTwin 2.0, VLAct surpasses industrial VLA systems including ABot-M0 and LingBot-VLA, achieving success rates of 82.6% and 92.5%. On RoboDojo, VLAct ranks sixth among all policies by success rate and outperforms all explicitly designated world-action model (WAM) entries on both metrics. Most notably, on RoboCasa-GR1, an unseen humanoid embodiment, VLAct using only 20% of downstream trajectories outperforms the full-data GR00T-N1.6 baseline. These results are obtained using fully open-source data and only a 16-GPU training setup, showing that representation-centric continued pre-training can deliver highly competitive performance under a modest compute budget and is an important independent axis of VLA progress beyond data scaling.


## 精读解读（中文）
### 一、研究动机
机器人数据难以像互联网图文数据那样规模化采集，实物遥操作成本高、覆盖稀疏，导致在固定机器人数据预算下，VLA持续预训练的效果主要受表征质量制约。已有朴素做法只是把预训练当作大规模动作拟合，容易造成VLM先验退化、动作头特异化表征坍缩以及跨本体动作语义割裂。因此需要超越数据规模本身，研究如何把有限的轨迹数据转化为可迁移的视觉-动作知识。

### 二、技术方案（Method）
VLAct以已预训练的Qwen3-VL-4B为初始化，在任务微调前使用开放获取、异构、多本体的机器人轨迹数据做持续预训练，并混合图像描述数据以锚定视觉-语言表示。训练中冻结完整视觉编码器和LLM的下半部分层，只更新LLM上半部分层与动作头，以保留VLM先验；同时采用多连续动作头并行共监督，共享骨干产生同一隐表征z，分别送入OFT、PI、GR00T三个连续动作头预测同一动作块，总动作损失为三者之和，从而避免单动作头导致的表征坍缩。为促进跨本体共享，VLAct使用部分统一的跨本体动作布局，掩蔽无效维度，并对周期性关节使用wrap-aware损失。微调阶段丢弃预训练动作头和描述流，重新初始化任务特定动作头，在固定下游协议下全模型解冻训练。

### 三、结果（Result）
在固定微调协议下，VLAct在LIBERO-Plus和RoboTwin 2.0上分别达到82.6%和92.5%的成功率，超过ABot-M0、LingBot-VLA等工业级VLA系统；在RoboDojo中按成功率排全部35个策略的第6位，并且在两个指标上都优于所有显式指定的世界动作模型（WAM）。在未见的人形本体RoboCasa-GR1上，仅用20%下游轨迹的VLAct超过使用全量数据的GR00T-N1.6基线。所有对比中只有VLM骨干权重改变，其他微调设置完全一致，7.6–21.4个百分点的提升可归因于骨干表征本身。

### 四、结论（Conclusion）
表征中心的持续预训练是VLA发展独立于数据规模之外的重要轴线：与其无限扩大机器人数据，不如在固定预算下设计能保留VLM先验、避免单头过拟合、统一跨本体动作语义的预训练方式。VLAct表明VLM骨干不应被视为固定组件，而应作为VLA首要的设计变量；基于开源数据和16卡训练也能取得强竞争力，说明该路线兼具效率和可复现性。

### 五、方法论与关键技术细节
关键细节包括：初始化采用Qwen3-VL-4B，预训练数据来自开源异构多本体轨迹并混合字幕数据；训练时冻结视觉编码器和LLM下半层，只更新上半层及动作头，微调时再全量解冻；动作监督使用OFT、PI、GR00T三种连续头对同一隐表征和同一动作块联合预测，损失为三者相加，并配合部分统一的跨本体动作布局、掩蔽无效维度及周期性关节wrap-aware损失；预训练动作头和字幕流在微调时丢弃，任务头重新初始化，下游数据、优化器、微调预算均与基线一致。整个流程仅用16张GPU和全开源数据。局限是该方法依赖既有VLM初始化而非从零预训练，且评估主要集中在固定微调预算和现有动作头组合范围内，超大规模数据或新解码形式下的边界仍需进一步探索。
