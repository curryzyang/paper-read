# Spectral-Target Physical Latent Structuring for JEPA-Style World Models

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Penghao Zhu, Salvatore Penachio, Kaustav Mukherjee, Aneesh Jonelagadda
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04264v1) · [PDF](https://arxiv.org/pdf/2609.04264v1)

## TLDR
The paper identifies a new "physical representation laziness" failure mode in JEPA-style latent world models where latent states fail to encode key physical properties despite avoiding collapse, and proposes a training-time Fourier auxiliary head that enforces physically-informed latent structuring, substantially improving planning success and data efficiency without added inference cost.

## Abstract
Latent world models have become increasingly popular as a method to predict and plan in latent space rather than pixel space. Recent architectures, such as LeWorldModel (LeWM), jointly train the encoder and predictor using regularization techniques like SIGReg to prevent representation collapse. Even with such regularization preventing representation collapse, we identify a new world model failure mode of \textit{physical representation laziness}, particularly noted in highly dynamic environments. For these lazy cases, the learned latent states do not collapse but nonetheless fail to represent key physical properties, causing ubiquitous downstream planning failure. To resolve this issue, we propose training-time auxiliary supervision with a lightweight "Fourier auxiliary head", which enforces physically-informed structuring of the latent space with no additional inference-time cost and can be generalized to any environment. Experimentally, we show that the auxiliary head substantially improves planning success rates in dynamic environments where the baseline LeWM exhibits physical representation laziness. It also leads to modest improvements in other environments, even when the baseline does not exhibit physical representation laziness. We further observe superior planning performance being accompanied by higher latent space correlations with key physical properties, indicating both the ability of our method to physically structure latent states and the potential planning-side benefit to the learned representation being physically structured. We also see in low-data regimes, auxiliary supervision is particularly impactful in increasing success rate. These findings support the use of our Fourier auxiliary head method to improve both overall success rate and data efficiency, while avoiding representation laziness in latent world models.


## 精读解读（中文）
### 一、研究动机
在JEPA风格潜空间世界模型中，LeWorldModel等架构利用SIGReg等正则化防止表征坍缩，但即使如此，高度动态环境中仍会出现“物理表征惰性”：隐状态并不坍缩，却未能编码决定后续动态的关键物理属性，导致规划失败。因此需要一种能在训练阶段将物理先验结构化进潜空间的方法，以支撑鲁棒规划。

### 二、技术方案（Method）
方法是在LeWorldModel的联合训练中增加一个轻量级“傅里叶辅助头”。该辅助头接收编码器输出的潜状态，将其变换到傅里叶/频谱域，并对齐环境动态关键物理量的谱目标（即使用具有物理含义的频谱作为监督信号），通过最小化谱匹配损失来迫使潜状态携带物理信息。总损失包含原有预测损失、SIGReg正则项和新的辅助谱损失，权重可调；所有模块端到端联合训练，但辅助头仅在训练时使用，推理时被移除，因此不引入额外推理成本。其输入是原始观测序列，输出为结构化的潜状态；关键操作包括傅里叶变换、物理目标定义与谱损失计算。

### 三、结果（Result）
实验显示，在LeWM基线出现物理表征惰性的强动态环境中，辅助头显著提升规划成功率；在基线无明显惰性的其他环境中也有适度提升。低数据体制下提升尤为显著。进一步分析表明，规划性能的改善伴随着潜状态与关键物理属性相关性的升高，证明该方法确实实现了物理结构化，且物理结构化对规划有正向作用。

### 四、结论（Conclusion）
提出的傅里叶辅助头谱物理潜在结构化方法能有效避免JEPA世界模型中的物理表征惰性，提高规划成功率与数据效率，同时不增加推理时计算开销，是一种通用且实用的训练正则化方案。

### 五、方法论与关键技术细节
关键实现要点包括：辅助头选择频谱域作为匹配空间，利用物理量的谱表现来引导隐状态；训练损失需与SIGReg等表示约束协同，需调节谱损失权重；高动态环境下收益最大，低数据时增益尤其明显；物理频谱目标的先验定义决定了辅助监督的有效性；方法可能受限于需要人工指定或获取物理属性，且在复杂多模态动态中谱匹配可能面临歧义。可复现的对比基线与指标包括LeWM各环境的规划成功率及隐状态-物理相关性。
