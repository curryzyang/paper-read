# Internal Pluralism and the Limits of Pairwise Comparisons

- 区域：精读区
- 排名：8
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Bailey Flanigan, Michelle Si
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02672v1) · [PDF](https://arxiv.org/pdf/2607.02672v1)

## TLDR
This paper demonstrates that internal pluralism—where individuals hold multiple authoritative priorities—undermines the assumptions of local pairwise comparisons for learning preferences, as priorities can be global and conflicting, and shows that allowing indecision can improve accuracy and reduce query cost.

## Abstract
Local pairwise comparisons are a standard tool for learning how people want decision rules to work, e.g., in participatory design or alignment. However, their use builds in two strong assumptions: that local comparisons are sufficient evidence about how a person wants an automated decision rule to behave, and that people can always answer those comparisons decisively. We investigate how these assumptions may be compromised under internal pluralism: the idea that an individual evaluates decision rules according to multiple authoritative priorities about how the rule should behave. We provide a formal model of such pluralistic preferences over decision rules, which then lets us identify two distinct failures of forced local pairwise comparison data. First, priorities such as proportionality, egalitarianism, and equal treatment are inherently global: what they imply in one case can depend on what happens elsewhere, so local comparisons may fail to capture them. Second, even when priorities are representable locally, tension between strongly-held priorities can generate internal conflict, producing potentially costly behavioral distortions when comparisons are forced. We then use our model to investigate the alternative -- allowing people to report indecision -- and our findings suggest that doing so can considerably reduce the number of queries needed to learn preferences accurately. We conclude by describing how our model points toward preference-learning methods that elicit these priorities directly, yielding more faithful and interpretable accounts of what people value.

## 精读解读（中文）

### 一、研究动机
在参与式设计和AI对齐中，常用局部成对比较来学习人们对决策规则的偏好。但这种方法隐含假设局部比较能充分反映个人偏好，且个人总能果断做出比较。然而，当个体存在内部多元主义——即根据多个权威优先级评估决策规则时，这些假设可能不成立。因此，需要研究内部多元主义如何破坏局部比较的有效性，并探索更优的偏好学习方法。

### 二、技术方案（Method）
作者构建了一个形式化模型，将个体对决策规则的偏好表示为多个权威优先级的组合。基于该模型，识别出强制局部成对比较的两种失败：第一，某些优先级（如比例性、平等主义）是全局性的，其含义取决于其他案例，局部比较无法捕捉；第二，即使优先级可局部表示，强优先级之间的冲突也会导致内部不一致，强制比较时产生行为扭曲。随后，模型用于分析允许报告不确定性的替代方案。

### 三、结果（Result）
通过模型分析发现，允许人们在比较中报告犹豫不决（即不强制选择）可以显著减少准确学习偏好所需的查询次数。这表明在存在内部多元主义时，容忍不确定性比强制比较更高效。

### 四、结论（Conclusion）
作者认为，需要转变偏好学习范式，从依赖局部成对比较转向直接引出人们的优先级。这种方法能提供更忠实和可解释的关于人们价值观的刻画，尤其适用于内部多元主义场景。

### 五、方法论与关键技术细节
该研究的形式化模型假设个体拥有多个权威优先级，每个优先级对决策规则施加约束。关键细节包括：优先级可以是全局性的（如比例性），这导致局部比较失效；优先级冲突可能引起内部冲突，强制比较会扭曲行为；通过允许不确定性的查询，可大幅降低查询次数（未给出具体数字）。局限性在于模型仍然是理论性的，未在真实数据上验证；且优先级如何被直接引出需要进一步方法开发。另外，该方法可能增加建模复杂度，因为需要同时考虑多个优先级。

