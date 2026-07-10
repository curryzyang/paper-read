# Scalable and Trustworthy Earth Observation Foundation Models

- 区域：精读区
- 排名：6
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari
- 机构：Florida State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07758v1) · [PDF](https://arxiv.org/pdf/2607.07758v1)

## TLDR
This paper reviews the design principles for scalable and trustworthy Earth observation foundation models, emphasizing that next-generation models must be evaluated not only by benchmark accuracy but also by modality-aware transfer and physically plausible representations to ensure reliable and trustworthy remote sensing decisions.

## Abstract
Foundation models (FMs) have transformed machine learning from isolated task-specific model development toward general-purpose models pretrained on broad data and adapted to multiple downstream tasks. Earth observation (EO) is an important domain for this paradigm because satellite and airborne archives are large, high-revisit, and increasingly multimodal, while reliable field labels are often sparse. Remote sensing foundation models (RSFMs) cannot be transferred reliably/optimally without domain-specific adaptation. This is because EO data are governed by measurement physics and operational decision constraints. This chapter reviews the design principles arising from these domain-specific constraints. It first defines the FMs paradigm in remote sensing (RS), then synthesizes the current model landscape, pretraining objectives, architecture designs, downstream adaptation and trustworthiness requirements. The chapter also incorporates recent benchmark evidence showing that no single geospatial foundation model is universally best and that inconsistent evaluation remains a major issue to fair comparison and reliable deployment. In addition, two brief environmental monitoring case studies; physics-informed spectral targeted masking for harmful algal bloom prediction and reinforcement learning for adaptive environmental monitoring station selection to illustrate the FMs domain-guided principles in practice. This chapter posits that next-generation RSFMs should be evaluated not only by benchmark accuracy, but also by modality-aware transfer and physically plausible representations for trustworthy EO decisions.


## 精读解读（中文）
### 一、研究动机
地球观测数据具有多模态、多分辨率、光谱丰富、强时空动态和地理参考等独特属性，而传统计算机视觉模型无法直接捕捉这些物理约束和操作决策需求。同时，遥感领域标注稀疏但数据量巨大，亟需专门设计的大规模基础模型以充分挖掘无标注数据中的领域结构信息。

### 二、技术方案（Method）
本文系统综述遥感基础模型的设计原则，涵盖预训练目标（掩码图像建模、对比学习、多任务监督、视觉-生成学习）、架构设计（波段编码、传感器令牌、时空位置嵌入、多模态融合模块）、下游适应策略（线性探测、参数高效微调、提示）以及可信度评估（不确定性量化、物理一致性检查）。并通过两个案例说明：1）物理引导的掩码光谱建模，在有害藻华预测中利用诊断波长的掩码策略迫使编码器学习与生物光学过程相关的表示；2）强化学习用于自适应环境监测站点选择，在预算限制下优化采样位置以支持后续决策。

### 三、结果（Result）
综述指出，没有任何单一地理空间基础模型在所有任务上通用最优；不一致的评估标准是当前公平比较和可靠部署的主要障碍。不同模型在场景分类、语义分割、变化检测、视觉问答及环境参数回归等任务上各有优劣，且预训练数据域（如RGB vs. 多光谱）、空间分辨率和时间采样对迁移表现有显著影响。

### 四、结论（Conclusion）
下一代遥感基础模型不应仅依据基准准确率评估，而应通过模态感知的迁移能力和物理上合理的表征来实现可信的地球观测决策。模型设计必须匹配目标问题的传感器物理、光谱结构、时空动态和操作约束。

### 五、方法论与关键技术细节
关键细节包括：1）遥感数据与自然图像的差异（多模态、多分辨率、光谱连续、时间采样因卫星轨道而异）驱动了专用架构设计；2）预训练策略中，掩码建模需针对光谱诊断波段而非均匀随机，对比学习中的正样本定义需谨慎（避免掩盖真实变化）；3）评估挑战包括空间自相关导致的准确率高估、跨年份/区域泛化测试的缺失；4）案例展示了物理先验（如藻华吸收特征）如何指导掩码策略，以及强化学习如何平衡监测成本与信息增益；5）局限性在于当前模型对传感器变更、大气校正差异敏感，且生成式输出需经辐射定标验证。
