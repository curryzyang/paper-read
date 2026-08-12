# Physics-Informed Machine Learning in Prognostics and Health Management: A Systematic Literature Review

- 区域：精读区
- 排名：3
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Christopher Braun, Julian Raible, Marco F. Huber
- 机构：Fraunhofer Institute for Manufacturing Engineering and Automation IPA, University of Stuttgart
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10047v1) · [PDF](https://arxiv.org/pdf/2608.10047v1)

## TLDR
This systematic literature review of 212 studies examines how Physics-Informed Machine Learning is applied in Prognostics and Health Management, proposing a four-class taxonomy (observational, inductive, learning bias, and hybrid approaches) and finding that while these methods consistently improve predictive performance over conventional baselines, the field remains skewed toward batteries and bearings with insufficient evidence for broader claims of improved generalization and interpretability.

## Abstract
In modern industry, keeping complex systems reliable, safe, and efficient hinges on Prognostics and Health Management (PHM). Machine Learning (ML) has largely driven advancements in diagnostics and prognostics, yet purely data-driven models face inherent limitations, such as poor generalization, an inability to infer causal relationships, and a lack of interpretability. Physics-Informed Machine Learning (PIML) helps mitigate these limitations by incorporating prior physical knowledge directly into the ML pipeline, thereby fostering growing interest in its application to PHM. This work investigates how PIML is being leveraged in the context of PHM through a systematic literature review of 212 studies. The review introduces a four-class classification scheme, consisting of observational bias, inductive bias, learning bias, and hybrid approaches, and further categorizes studies by PHM task. Across all four classes, the reviewed studies consistently demonstrate improved predictive performance over conventional baselines across a broad range of assets, although the literature is heavily skewed toward lithium-ion batteries and bearings, and dominated by problem-specific solutions. Overall, the review indicates that physics-informed approaches already provide tangible benefits, whereas claims of improvements concerning some of the aforementioned limitations lack sufficient supporting evidence. Future research should prioritize transferable design patterns, benchmarks comparing integration strategies, and uncertainty-aware models that are lightweight and robust enough for online deployment in real-world settings.


## 精读解读（中文）
### 一、研究动机
现代工业对复杂系统的可靠性、安全性和效率要求日益提高，故障预测与健康管理（PHM）成为关键支撑。纯数据驱动的机器学习模型在泛化能力、因果推断和可解释性方面存在固有局限，难以应对工业场景中的噪声、稀疏故障数据和工况变化。物理信息机器学习（PIML）通过将先验物理知识嵌入机器学习流程，有望缓解这些局限，但该领域研究分散，缺乏统一分类和系统性证据基础，因此有必要开展系统文献综述，回答PIML如何在PHM中被利用以及关键挑战与机遇。

### 二、技术方案（Method）
本研究采用系统文献综述方法，对212项PIML在PHM中的应用研究进行全面分析。综述提出四类分类方案：观测偏差（observational bias）、归纳偏差（inductive bias）、学习偏差（learning bias）和混合方法（hybrid approaches），并按PHM任务（故障检测、诊断、健康评估、预后）进一步归类。研究流程包括明确的检索策略、筛选程序和质量评估，以系统归纳先验物理知识的类型与表示形式、知识融入机器学习的方式及实际效益，并基于对方法学趋势的分析讨论工业应用中的挑战和未来方向。

### 三、结果（Result）
综述发现，在四类方法中，PIML相比传统基线在多种资产上均一致表现出预测性能提升，尤其是在锂离子电池和轴承领域证据最集中。但文献高度偏向这两个资产类别，且以问题特定解决方案为主。关于PIML能改善泛化、因果推断和可解释性等纯数据驱动方法局限性的主张，目前缺乏充分的实证支持。

### 四、结论（Conclusion）
PIML在PHM中已展现出切实益处，能够提升预测性能，但其对数据驱动方法固有局限的改进仍需更多证据。当前研究碎片化、领域分布不均且缺乏通用设计模式，未来应优先发展可迁移的设计范式、比较不同融合策略的基准测试，以及轻量级、稳健且支持不确定性量化、适合在线部署的模型。

### 五、方法论与关键技术细节
综述涵盖212项研究，分类框架区分了四种物理知识融合方式：观测偏差（数据层面增强）、归纳偏差（模型结构约束）、学习偏差（损失函数正则化）和混合方法。分析同时考虑了PHM任务类型、资产类型和知识表示形式。当前文献以锂离子电池和轴承为主，方法多为针对特定问题的定制方案，缺乏跨场景的通用性。未来研究需要关注模型的不确定性量化、计算复杂度约束，以及在实际在线部署中的鲁棒性和轻量化要求。
