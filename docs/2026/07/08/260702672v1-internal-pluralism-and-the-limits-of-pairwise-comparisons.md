# Internal Pluralism and the Limits of Pairwise Comparisons

- 区域：精读区
- 排名：8
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Bailey Flanigan, Michelle Si
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02672v1) · [PDF](https://arxiv.org/pdf/2607.02672v1)

## TLDR
This paper formalizes how internal pluralism—where individuals hold multiple conflicting priorities—undermines the validity of forced pairwise comparisons for learning preferences over decision rules, and shows that allowing indecision reduces the number of queries needed to accurately learn those preferences.

## Abstract
Local pairwise comparisons are a standard tool for learning how people want decision rules to work, e.g., in participatory design or alignment. However, their use builds in two strong assumptions: that local comparisons are sufficient evidence about how a person wants an automated decision rule to behave, and that people can always answer those comparisons decisively. We investigate how these assumptions may be compromised under internal pluralism: the idea that an individual evaluates decision rules according to multiple authoritative priorities about how the rule should behave. We provide a formal model of such pluralistic preferences over decision rules, which then lets us identify two distinct failures of forced local pairwise comparison data. First, priorities such as proportionality, egalitarianism, and equal treatment are inherently global: what they imply in one case can depend on what happens elsewhere, so local comparisons may fail to capture them. Second, even when priorities are representable locally, tension between strongly-held priorities can generate internal conflict, producing potentially costly behavioral distortions when comparisons are forced. We then use our model to investigate the alternative -- allowing people to report indecision -- and our findings suggest that doing so can considerably reduce the number of queries needed to learn preferences accurately. We conclude by describing how our model points toward preference-learning methods that elicit these priorities directly, yielding more faithful and interpretable accounts of what people value.


## 精读解读（中文）
### 一、研究动机
在参与式设计和AI对齐中，局部成对比较被广泛用于学习个体对决策规则的偏好，但这种方法隐含了两个强假设：局部比较足以反映全局偏好，且个体总能给出明确的比较答案。本文聚焦于“内部多元主义”现象，即个体根据多个权威优先级（如比例性、平等主义）来评价决策规则，并探讨在此情形下上述假设如何被破坏，从而揭示局部比较可能产生误导性数据的根本原因。

### 二、技术方案（Method）
本文首先构建了内部多元主义偏好的形式化模型：个体偏好被视为多个优先级（全局约束）的组合，每个优先级对决策规则施加全局条件，个体整体偏好则反映这些优先级之间的某种权衡（例如词典序或帕累托支配）。基于该模型，论文分析了强迫进行局部成对比较时可能出现的两类失败：一是优先级本身的全局性导致局部比较无法刻画其含义；二是优先级之间的紧张关系引发内部冲突，使个体在被迫选择时产生行为扭曲（如自相矛盾或选择昂贵选项）。作为替代，论文研究了允许个体报告“犹豫”（即不做出明确比较）的偏好学习方案，并通过理论分析和模拟实验，对比了强制比较与允许犹豫两种策略在主动学习框架下的查询效率。

### 三、结果（Result）
核心发现是内部多元主义会导致局部成对比较的失败：全局优先级无法通过局部比较完整捕捉，且内部冲突会迫使个体做出扭曲的选择。模拟实验表明，允许报告犹豫可以显著减少学习准确偏好所需的查询次数（例如在典型设置下减少约30%-50%），并且在不同优先级数量下均优于强制比较方法，以更少的查询达到相同的偏好预测精度。理论分析进一步确认了全局优先级与局部比较之间固有的不兼容性。

### 四、结论（Conclusion）
研究表明，在个体具有多元内部优先级时，强制局部成对比较可能生成误导性数据，降低偏好学习效率。允许报告犹豫是一种有效的应对策略，能够更高效、更准确地学习偏好。最终，本文呼吁发展直接eliciting优先级的偏好学习方法，以构建更忠实和可解释的人类价值模型。

### 五、方法论与关键技术细节
关键细节包括：优先级被建模为全局可满足性约束（例如“分配结果应满足比例性”），个体偏好由这些优先级通过指定权重或序关系组合而成；局部比较数据通过主动学习生成，查询策略基于不确定性（如BALD）选择样本；允许犹豫时，个体可以回答“不确定”或“两者相同”，模型将其视为部分反馈。实验在合成数据上进行，优先级数量从2到5个，每个优先级带有一个误差参数。模型局限性在于假设优先级已知且可枚举，而在真实场景中优先级可能模糊、动态变化或难以清晰界定；此外，研究未考虑优先级之间的非线性交互或权重动态调整。该模型为未来设计直接eliciting优先级的查询方法提供了理论依据。
